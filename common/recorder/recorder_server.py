"""
录制服务器 (RecorderServer)
负责：启动 Unity 端 TouchRecorder → 实时接收操作事件 → 保存为 Python 脚本

Unity 端回传 hit_nodes 原始数据，本模块调用 node_scorer 选出最佳节点。
录制产物为 async def run(bp) 格式的 .py 文件，由 ScriptRunner 执行。
"""
from common.log import get_logger

logger = get_logger("recorder_server")

import asyncio
import datetime
import os
from pathlib import Path
from typing import Optional

from common.recorder.node_scorer import pick_best_node


class RecorderServer:
    """管理一次完整的录制会话。"""

    _3D_TRACKER_COMPONENT = "CustomUICoordinateTracker"
    _HUD_PAN_PREFIX = ""
    DEFAULT_LONG_PRESS_THRESHOLD_S = 0.5

    def __init__(self, server,
                 output_dir: str = os.path.join(os.path.dirname(__file__), "recordings"),
                 long_press_threshold_s: float = None):
        self.server = server
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.is_recording = False
        self._event_index = 0
        self.long_press_threshold_s = self._sanitize_long_press_threshold(long_press_threshold_s)

    @classmethod
    def _sanitize_long_press_threshold(cls, value) -> float:
        if value is None:
            return cls.DEFAULT_LONG_PRESS_THRESHOLD_S
        try:
            v = float(value)
        except (TypeError, ValueError):
            logger.warning(f"long_press_threshold_s 非法 {value!r}，回退默认 {cls.DEFAULT_LONG_PRESS_THRESHOLD_S}")
            return cls.DEFAULT_LONG_PRESS_THRESHOLD_S
        if v < 0:
            logger.warning(f"long_press_threshold_s 不可为负，收到 {v}，回退默认 {cls.DEFAULT_LONG_PRESS_THRESHOLD_S}")
            return cls.DEFAULT_LONG_PRESS_THRESHOLD_S
        return v

    async def start_recording(self, camera_config_list: list[dict] = None) -> bool:
        if self.is_recording:
            logger.warning("已在录制中，请先停止当前录制")
            return False

        if camera_config_list:
            for cfg in camera_config_list:
                try:
                    await self.server.call("SetCamera", cfg["path_node"], cfg["path_camera"], cfg["camera_type"])
                except Exception as e:
                    logger.warning(f"注册相机失败(非致命): {e}")

        self._event_index = 0
        self.server._on_record_event = self._on_event_received
        self.server.recording_start()
        result = await self.server.call("StartRecording")
        if not result:
            logger.error("Unity 端启动录制失败")
            self.server._on_record_event = None
            self.server.recording_stop()
            return False

        self.is_recording = True
        logger.info("录制已启动，请在游戏中操作...")
        return True

    # ======================== 实时事件回显 ========================

    def _on_event_received(self, evt: dict):
        """每收到一个录制事件实时处理并打印。"""
        self._event_index += 1
        action = evt.get("action", "?")
        if action == "ping":
            return

        idx = self._event_index

        if action == "click":
            self._log_click_event(idx, evt)
            return

        if action == "swipe":
            start = evt.get("position", [0, 0])
            end = evt.get("end_position", [0, 0])
            best_name = self._pick_best_name(evt.get("hit_nodes"), start)
            logger.info(f"  [事件#{idx}] swipe{best_name} {start} -> {end}")
            return

        if action == "input_text":
            text = evt.get("text", "")
            best_name = self._pick_best_name(evt.get("hit_nodes"), evt.get("position", [0, 0]))
            logger.info(f"  [事件#{idx}] input_text{best_name} text={text!r}")
            return

        logger.info(f"  [事件#{idx}] {action}")

    def _log_click_event(self, idx: int, evt: dict):
        hit_nodes = evt.get("hit_nodes")
        click_pos = evt.get("position", [0, 0])
        duration = evt.get("duration", 0)
        is_long = duration > self.long_press_threshold_s
        label = "long_press" if is_long else "click"
        dur_suffix = f" duration={duration}s" if is_long else ""

        if hit_nodes is None:
            logger.info(f"  [事件#{idx}] {label} pos={click_pos}{dur_suffix}")
            return
        best = pick_best_node(hit_nodes, click_pos)
        if not best:
            logger.info(f"  [事件#{idx}] {label} -> 无匹配节点, pos={click_pos}{dur_suffix}")
            return
        logger.info(
            f"  [事件#{idx}] {label} -> {best.get('name', '?')} "
            f"path={best['path']} score={best.get('score', 0)}{dur_suffix}"
        )

    @staticmethod
    def _pick_best_name(hit_nodes, position) -> str:
        """从 hit_nodes 中取最佳节点名称，返回 ' -> name' 或空串。"""
        if not hit_nodes:
            return ""
        best = pick_best_node(hit_nodes, position)
        if not best:
            return ""
        return f" -> {best.get('name', '?')}"

    # ======================== 停止录制 ========================

    async def stop_recording(self, name: Optional[str] = None) -> Optional[str]:
        if not self.is_recording:
            logger.warning("当前没有在录制")
            return None

        await self.server.call("StopRecording")
        self.server._on_record_event = None
        self.server.recording_stop()
        self.is_recording = False

        raw_events = self.server.get_recording_events()
        logger.info(f"录制结束，共捕获 {len(raw_events)} 个原始事件")

        if not raw_events:
            logger.warning("没有捕获到任何操作，跳过保存")
            return None

        steps = self._build_steps(raw_events)
        if not steps:
            logger.warning("没有有效操作步骤（仅 ping），跳过保存")
            return None

        filepath = self._save_py(steps, name)
        logger.info(f"录制文件已保存: {filepath}")
        return str(filepath)

    # ======================== 步骤构建 ========================

    _ACTION_BUILDERS = {
        "click": "_build_click_step",
        "swipe": "_build_swipe_step",
        "input_text": "_build_input_text_step",
    }

    def _build_steps(self, raw_events: list) -> list:
        """将原始录制事件转换为回放步骤序列。

        Unity 端统一发送 action='click' + duration，本方法内部按阈值分流为 click / long_press。
        合并逻辑 1：click → input_text → click 整体合并为一条 set_text_for_playback。
        合并逻辑 2：连续 swipe + click/long_press（同 ScrollRect）合并为 scroll_and_click。
        合并逻辑 3：连续 swipe + click/long_press（3D/HUD）合并为 pan_and_click_3d。
        """
        actionable = [e for e in raw_events if e.get("action") != "ping"]

        steps = []
        prev_ts = 0

        for i, evt in enumerate(actionable):
            action = evt.get("action", "click")
            prev_action = actionable[i - 1].get("action") if i > 0 else None
            next_action = actionable[i + 1].get("action") if i + 1 < len(actionable) else None

            if action == "click" and (next_action == "input_text"
                                      or prev_action == "input_text"):
                continue

            ts = evt.get("timestamp_ms", 0)
            timeout = round((ts - prev_ts) / 1000.0, 2) if prev_ts > 0 else 0

            builder_name = self._ACTION_BUILDERS.get(action)
            if builder_name:
                step = getattr(self, builder_name)(evt, timeout)
                steps.append(step)

            prev_ts = ts

        steps = self._merge_scroll_click(steps)
        steps = self._merge_pan_click_3d(steps)
        return steps

    # ======================== 单步构建 ========================

    def _build_click_step(self, evt: dict, timeout: float) -> dict:
        """构建 click / long_press 步骤。

        Unity 端统一发送 action='click' + duration，由此处根据
        long_press_threshold_s 决定最终 action。
        3D/HUD 浮动节点自动升级为 pan_and_click_3d（click 和 long_press 均适用），
        duration 会被复合合并逻辑透传。
        """
        duration = evt.get("duration", 0)
        is_long = duration > self.long_press_threshold_s
        click_position = evt.get("position", [0.5, 0.5])

        if is_long:
            step = {"action": "long_press", "timeout": timeout, "duration": duration}
        else:
            step = {"action": "click", "timeout": timeout}

        hit_nodes = evt.get("hit_nodes")
        if hit_nodes is not None:
            self._populate_from_hit_nodes(step, hit_nodes, click_position)
        elif evt.get("element"):
            self._populate_from_element(step, evt["element"], evt)

        step["fallback_position"] = click_position
        return step

    def _populate_from_hit_nodes(self, step: dict, hit_nodes, click_position):
        """用 hit_nodes 评分结果填充 step，必要时升级 action。"""
        best = pick_best_node(hit_nodes, click_position)
        if not best:
            logger.warning("  hit_nodes 为空或评分失败，仅记录坐标")
            return

        step.update({
            "element_data": {"locator": best["path"]},
            "focus": best.get("focus", [0.5, 0.5]),
            "element_name": best.get("name", ""),
            "element_components": best.get("components", []),
            "total_score": best.get("score"),
            "score_breakdown": best.get("score_breakdown"),
        })

        scroll_ancestor = self._find_scroll_ancestor(best)
        if scroll_ancestor:
            step["scroll_ancestor"] = scroll_ancestor

        if best.get("locator_camera"):
            step["locator_camera"] = best["locator_camera"]

        path = best["path"]
        upgraded = self._maybe_upgrade_to_pan_3d(step, path, best.get("is_3d", False))
        if upgraded and step.get("locator_camera") == "":
            logger.info(f"  HUD 浮动节点，升级为 pan_and_click_3d: {path} (score={best.get('score', 0)})")
        elif upgraded:
            logger.info(f"  3D 目标节点，升级为 pan_and_click_3d: {path} (score={best.get('score', 0)})")
        else:
            logger.info(
                f"  最佳节点: {path} "
                f"(score={best.get('score', 0)}, breakdown={best.get('score_breakdown')})"
            )

    def _populate_from_element(self, step: dict, element: dict, evt: dict):
        """用 element 信息填充 step（hit_nodes 不存在时的回退路径）。"""
        step.update({
            "element_data": {"locator": element["locator"]},
            "focus": element.get("focus", [0.5, 0.5]),
            "element_name": element.get("name", ""),
            "element_components": element.get("components", []),
        })
        if evt.get("total_score") is not None:
            step["total_score"] = evt["total_score"]
        if evt.get("score_breakdown"):
            step["score_breakdown"] = evt["score_breakdown"]
        self._maybe_upgrade_to_pan_3d(step, element["locator"])

    def _maybe_upgrade_to_pan_3d(self, step: dict, path: str, is_3d: bool = False) -> bool:
        """3D/HUD 节点升级 action 为 pan_and_click_3d，返回是否升级。"""
        if is_3d or self._is_3d_tracker_click(step):
            step["action"] = "pan_and_click_3d"
            return True
        if self._HUD_PAN_PREFIX and path.startswith(self._HUD_PAN_PREFIX):
            step["action"] = "pan_and_click_3d"
            step["locator_camera"] = ""
            return True
        return False

    @staticmethod
    def _is_3d_tracker_click(step: dict) -> bool:
        """判断 click 步骤的目标节点是否持有 CustomUICoordinateTracker。"""
        components = step.get("element_components", [])
        return RecorderServer._3D_TRACKER_COMPONENT in components

    def _build_swipe_step(self, evt: dict, timeout: float) -> dict:
        """构建 swipe 步骤，起始点同样通过 hit_nodes 定位元素。"""
        start_position = evt.get("position", [0.5, 0.5])
        end_position = evt.get("end_position", [0.5, 0.5])
        duration = evt.get("duration", 0.5)

        step = {
            "action": "swipe",
            "fallback_start": start_position,
            "end": end_position,
            "duration": duration,
            "timeout": timeout,
        }

        hit_nodes = evt.get("hit_nodes")
        if hit_nodes is None:
            return step
        best = pick_best_node(hit_nodes, start_position)
        if not best:
            return step

        step["element_data"] = {"locator": best["path"]}
        step["focus"] = best.get("focus", [0.5, 0.5])
        step["element_name"] = best.get("name", "")

        scroll_ancestor = self._find_scroll_ancestor(best)
        if scroll_ancestor:
            step["scroll_ancestor"] = scroll_ancestor

        logger.info(
            f"  swipe 起始节点: {best['path']} "
            f"(score={best.get('score', 0)})"
        )
        return step

    def _build_input_text_step(self, evt: dict, timeout: float) -> dict:
        """构建 input_text 步骤，包含 element_data、text、timeout。"""
        text = evt.get("text", "")
        position = evt.get("position", [0.5, 0.5])

        step = {
            "action": "input_text",
            "text": text,
            "timeout": timeout,
        }

        hit_nodes = evt.get("hit_nodes")
        if hit_nodes is None:
            return step
        best = pick_best_node(hit_nodes, position)
        if not best:
            logger.warning("  input_text hit_nodes 评分失败，仅记录文本")
            return step

        step["element_data"] = {"locator": best["path"]}
        step["element_name"] = best.get("name", "")
        step["total_score"] = best.get("score")
        logger.info(
            f"  input_text 节点: {best['path']} "
            f"(score={best.get('score', 0)}) text={text!r}"
        )
        return step

    # ======================== swipe + click → scroll_and_click 合并 ========================

    @staticmethod
    def _find_scroll_ancestor(node: dict) -> str | None:
        """从节点自身组件或 parent_chain 中查找最近的 ScrollRect 祖先路径。

        Unity 端 TouchRecorder 为每个 hit_node 提供最多 3 级 parent_chain，
        每项含 name/path/components。此方法检查 node 自身及其 parent_chain
        中是否有 ScrollRect 组件，返回最近一级的 path。

        典型 Unity ScrollRect 层级:
            ScrollRect(+ScrollRect) / Viewport(+Mask) / Content / item_5(+Button)
        item_5 的 parent_chain = [Content, Viewport, ScrollRect]
        → 返回 ScrollRect 的 path。
        """
        components = node.get("components") or []
        if "ScrollRect" in components:
            return node.get("path")

        parent_chain = node.get("parent_chain") or []
        for parent in parent_chain:
            parent_components = parent.get("components") or []
            if "ScrollRect" in parent_components:
                return parent.get("path")

        return None

    def _merge_scroll_click(self, steps: list) -> list:
        """扫描步骤列表，把 '连续 swipe + click/long_press（同 ScrollRect）' 合并为 scroll_and_click。"""
        merged: list = []
        i = 0
        while i < len(steps):
            if steps[i].get("action") != "swipe":
                merged.append(steps[i])
                i += 1
                continue

            swipe_run_start = i
            while i < len(steps) and steps[i].get("action") == "swipe":
                i += 1

            if i >= len(steps) or steps[i].get("action") not in ("click", "long_press"):
                merged.extend(steps[swipe_run_start:i])
                continue

            click_step = steps[i]
            swipe_steps = steps[swipe_run_start:i]

            scroll_merge = self._try_build_scroll_merge(swipe_steps, click_step)
            if not scroll_merge:
                merged.extend(swipe_steps)
                merged.append(click_step)
                i += 1
                continue

            merged.append(scroll_merge)
            i += 1

        return merged

    def _try_build_scroll_merge(self, swipe_steps: list, click_step: dict) -> dict | None:
        """尝试合并 swipe + click/long_press 为 scroll_and_click，条件不满足返回 None。"""
        click_locator = (click_step.get("element_data") or {}).get("locator", "")
        if not click_locator:
            return None

        click_scroll = click_step.get("scroll_ancestor")
        if not click_scroll:
            return None

        if not self._swipes_belong_to_scroll(swipe_steps, click_scroll):
            return None

        total_timeout = sum(s.get("timeout", 1) for s in swipe_steps)
        total_timeout += click_step.get("timeout", 1)
        is_long = click_step.get("action") == "long_press"
        merged_step = {
            "action": "scroll_and_click",
            "scroll_element_data": {"locator": click_scroll},
            "target_element_data": click_step.get("element_data"),
            "target_focus": click_step.get("focus"),
            "target_fallback_position": click_step.get("fallback_position"),
            "target_element_name": click_step.get("element_name", ""),
            "timeout": round(total_timeout, 2),
            "swipe_count": len(swipe_steps),
        }
        if is_long:
            merged_step["duration"] = click_step.get("duration", 1.0)
        logger.info(
            f"  合并 {len(swipe_steps)} 次 swipe + {'long_press' if is_long else 'click'}"
            f" → scroll_and_click: scroll={click_scroll}, target={click_locator}"
        )
        return merged_step

    @staticmethod
    def _swipes_belong_to_scroll(swipe_steps: list, click_scroll: str) -> bool:
        """检查所有 swipe 是否与 click 属于同一 ScrollRect 子树。

        比较方式：
        1. swipe 的 scroll_ancestor 与 click_scroll 完全相同 → 属于
        2. swipe 的 locator 是 click_scroll 的子孙路径 → 属于
        3. swipe 没有 element_data（纯坐标 swipe）→ 不阻止合并
        """
        for sw in swipe_steps:
            sw_scroll = sw.get("scroll_ancestor")
            if sw_scroll == click_scroll:
                continue
            sw_locator = (sw.get("element_data") or {}).get("locator", "")
            if not sw_locator:
                continue
            if sw_locator.startswith(click_scroll + "/"):
                continue
            return False
        return True

    # ======================== swipe + click(3D/HUD) → pan_and_click_3d 合并 ========================

    def _merge_pan_click_3d(self, steps: list) -> list:
        """扫描步骤列表，把 '连续 swipe（非 ScrollRect）+ 3D/HUD click/long_press' 合并为 pan_and_click_3d。"""
        merged: list = []
        i = 0
        while i < len(steps):
            if steps[i].get("action") != "swipe":
                merged.append(steps[i])
                i += 1
                continue

            swipe_run_start = i
            while i < len(steps) and steps[i].get("action") == "swipe":
                i += 1

            if i >= len(steps) or steps[i].get("action") not in ("click", "long_press", "pan_and_click_3d"):
                merged.extend(steps[swipe_run_start:i])
                continue

            click_step = steps[i]
            swipe_steps = steps[swipe_run_start:i]

            pan_merge = self._try_build_pan_3d_merge(swipe_steps, click_step)
            if not pan_merge:
                merged.extend(swipe_steps)
                merged.append(click_step)
                i += 1
                continue

            merged.append(pan_merge)
            i += 1

        return merged

    def _try_build_pan_3d_merge(self, swipe_steps: list, click_step: dict) -> dict | None:
        """尝试合并 swipe + 3D/HUD click/long_press 为 pan_and_click_3d，条件不满足返回 None。"""
        if not self._is_pannable_click(click_step):
            return None

        has_scroll = any(s.get("scroll_ancestor") for s in swipe_steps)
        if has_scroll:
            return None

        is_long = (click_step.get("action") == "long_press"
                   or click_step.get("duration", 0) > 0)
        total_timeout = sum(s.get("timeout", 1) for s in swipe_steps)
        total_timeout += click_step.get("timeout", 1)
        merged_step = {
            "action": "pan_and_click_3d",
            "element_data": click_step.get("element_data"),
            "focus": click_step.get("focus"),
            "fallback_position": click_step.get("fallback_position"),
            "element_name": click_step.get("element_name", ""),
            "element_components": click_step.get("element_components", []),
            "timeout": round(total_timeout, 2),
            "swipe_count": len(swipe_steps),
        }
        if is_long:
            merged_step["duration"] = click_step.get("duration", 1.0)
        if "locator_camera" in click_step:
            merged_step["locator_camera"] = click_step["locator_camera"]
        logger.info(
            f"  合并 {len(swipe_steps)} 次 swipe + {'long_press' if is_long else 'click'}"
            f" → pan_and_click_3d: target={click_step.get('element_data', {}).get('locator', '?')}"
        )
        return merged_step

    def _is_pannable_click(self, step: dict) -> bool:
        """判断 click/long_press 步骤是否可参与 pan 合并（3D Tracker 或已升级的 pan_and_click_3d）。"""
        if step.get("action") == "pan_and_click_3d":
            return True
        return self._is_3d_tracker_click(step)

    # ======================== 保存为 Python 脚本 ========================

    def _save_py(self, steps: list, name: Optional[str] = None) -> Path:
        """将步骤列表生成为 async def run(bp) 格式的 Python 脚本。"""
        now = datetime.datetime.now()
        if not name:
            name = f"recording_{now.strftime('%Y%m%d_%H%M%S')}"

        lines = [
            '"""',
            f"录制脚本: {name}",
            f"创建时间: {now.strftime('%Y-%m-%d %H:%M:%S')}",
            f"步骤数: {len(steps)}",
            '"""',
            '',
            '',
            'async def run(bp):',
        ]

        if not steps:
            lines.append('    pass')
        else:
            for i, step in enumerate(steps):
                comment = self._build_step_comment(step, i + 1)
                if comment:
                    lines.append(f"    {comment}")
                lines.append(f"    {self._step_to_code(step)}")

        lines.append('')

        filepath = self.output_dir / f"{name}.py"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write('\n'.join(lines))
        return filepath

    # ======================== 步骤注释 ========================

    def _build_step_comment(self, step: dict, step_num: int) -> str:
        """为步骤生成注释行。"""
        action = step.get("action")
        name = step.get("element_name", "")

        if action == "click":
            if not name:
                return ""
            return f"# Step {step_num}: click {name} (score={step.get('total_score', '')})"

        if action == "long_press":
            duration = step.get("duration", 0)
            if not name:
                return f"# Step {step_num}: long_press {duration}s"
            return (
                f"# Step {step_num}: long_press {name} "
                f"{duration}s (score={step.get('total_score', '')})"
            )

        if action == "swipe":
            if not name:
                return f"# Step {step_num}: swipe"
            return f"# Step {step_num}: swipe from {name}"

        if action == "input_text":
            text = step.get("text", "")
            preview = text[:20] + "..." if len(text) > 20 else text
            if name:
                return f"# Step {step_num}: input_text {preview!r} on {name}"
            return f"# Step {step_num}: input_text {preview!r}"

        if action == "scroll_and_click":
            target_name = step.get("target_element_name", "")
            n = step.get("swipe_count", 0)
            press_label = "long_press" if step.get("duration") else "click"
            dur_suffix = f" {step['duration']}s" if step.get("duration") else ""
            return f"# Step {step_num}: scroll({n} swipes) + {press_label} {target_name}{dur_suffix}"

        if action == "pan_and_click_3d":
            n = step.get("swipe_count", 0)
            is_long = bool(step.get("duration"))
            click_type = "click_hud" if step.get("locator_camera") == "" else "click_3d"
            if is_long:
                click_type = "long_press_hud" if step.get("locator_camera") == "" else "long_press_3d"
            dur_suffix = f" {step['duration']}s" if is_long else ""
            if n > 0:
                return f"# Step {step_num}: pan_camera({n} swipes) + {click_type} {name}{dur_suffix}"
            return f"# Step {step_num}: {click_type} {name}{dur_suffix}"

        return ""

    # ======================== 步骤 → Python 代码 ========================

    _CODE_GENERATORS = {
        "click": "_click_step_to_code",
        "long_press": "_long_press_step_to_code",
        "swipe": "_swipe_step_to_code",
        "input_text": "_input_text_step_to_code",
        "scroll_and_click": "_scroll_click_step_to_code",
        "pan_and_click_3d": "_pan_click_3d_step_to_code",
    }

    def _step_to_code(self, step: dict) -> str:
        """将单个步骤转换为一行 Python 代码。"""
        action = step.get("action")
        generator = self._CODE_GENERATORS.get(action)
        if not generator:
            return f"pass  # unknown action: {action}"
        return getattr(self, generator)(step)

    def _click_step_to_code(self, step: dict) -> str:
        args = []
        if step.get("element_data"):
            args.append(f"element_data={step['element_data']!r}")
        if step.get("focus"):
            args.append(f"focus={self._fmt_coords(step['focus'])}")
        if step.get("fallback_position"):
            args.append(f"fallback_position={self._fmt_coords(step['fallback_position'])}")
        args.append(f"timeout={step.get('timeout', 10)}")
        return f"await bp.click_for_playback({', '.join(args)})"

    def _long_press_step_to_code(self, step: dict) -> str:
        args = []
        if step.get("element_data"):
            args.append(f"element_data={step['element_data']!r}")
        if step.get("focus"):
            args.append(f"focus={self._fmt_coords(step['focus'])}")
        if step.get("fallback_position"):
            args.append(f"fallback_position={self._fmt_coords(step['fallback_position'])}")
        args.append(f"duration={step.get('duration', 1.0)}")
        args.append(f"timeout={step.get('timeout', 10)}")
        return f"await bp.long_press_for_playback({', '.join(args)})"

    def _swipe_step_to_code(self, step: dict) -> str:
        args = []
        if step.get("element_data"):
            args.append(f"element_data={step['element_data']!r}")
        if step.get("focus") and step.get("element_data"):
            args.append(f"focus={self._fmt_coords(step['focus'])}")
        if step.get("fallback_start"):
            args.append(f"fallback_start={self._fmt_coords(step['fallback_start'])}")
        if step.get("end"):
            args.append(f"end={self._fmt_coords(step['end'])}")
        args.append(f"duration={step.get('duration', 0.5)}")
        args.append(f"timeout={step.get('timeout', 10)}")
        return f"await bp.swipe_for_playback({', '.join(args)})"

    def _input_text_step_to_code(self, step: dict) -> str:
        args = []
        if step.get("element_data"):
            args.append(f"element_data={step['element_data']!r}")
        args.append(f"text={step.get('text', '')!r}")
        args.append(f"timeout={step.get('timeout', 10)}")
        return f"await bp.set_text_for_playback({', '.join(args)})"

    def _scroll_click_step_to_code(self, step: dict) -> str:
        args = []
        if step.get("scroll_element_data"):
            args.append(f"scroll_element_data={step['scroll_element_data']!r}")
        if step.get("target_element_data"):
            args.append(f"target_element_data={step['target_element_data']!r}")
        if step.get("target_focus"):
            args.append(f"target_focus={self._fmt_coords(step['target_focus'])}")
        if step.get("target_fallback_position"):
            args.append(f"target_fallback_position={self._fmt_coords(step['target_fallback_position'])}")
        if step.get("duration"):
            args.append(f"duration={step['duration']}")
        args.append(f"timeout={step.get('timeout', 10)}")
        return f"await bp.scroll_and_click_for_playback({', '.join(args)})"

    def _pan_click_3d_step_to_code(self, step: dict) -> str:
        args = []
        if step.get("element_data"):
            args.append(f"element_data={step['element_data']!r}")
        if step.get("focus"):
            args.append(f"focus={self._fmt_coords(step['focus'])}")
        if step.get("fallback_position"):
            args.append(f"fallback_position={self._fmt_coords(step['fallback_position'])}")
        if step.get("duration"):
            args.append(f"duration={step['duration']}")
        args.append(f"timeout={step.get('timeout', 10)}")
        locator_camera = step.get("locator_camera")
        if locator_camera is not None:
            args.append(f"locator_camera={locator_camera!r}")
        return f"await bp.click_3d_for_playback({', '.join(args)})"

    @staticmethod
    def _fmt_coords(coords: list) -> str:
        """格式化坐标列表，保留4位小数。"""
        if not coords or len(coords) < 2:
            return repr(coords)
        return f"[{round(coords[0], 4)}, {round(coords[1], 4)}]"


async def interactive_recording(server, camera_config_list: list[dict] = None,
                                output_dir: str = os.path.join(os.path.dirname(__file__), "recordings")):
    """交互式录制入口：启动录制 → 等待用户按 Enter → 停止并保存。"""
    recorder = RecorderServer(server, output_dir=output_dir)

    await recorder.start_recording(camera_config_list=camera_config_list)

    logger.info("按 Enter 键停止录制...")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, input)

    filepath = await recorder.stop_recording()
    if filepath:
        logger.info(f"录制文件: {filepath}")
    return filepath

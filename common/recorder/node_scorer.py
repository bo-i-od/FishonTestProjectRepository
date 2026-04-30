"""
节点评分器 (NodeScorer) — Unity 适配版

Unity 端 (TouchRecorder.cs) 通过 EventSystem.RaycastAll / Physics.RaycastAll
收集所有命中节点的原始数据并回传，本模块对这些原始数据执行评分并选出最佳节点。

评分公式
    total = (interactive + area + semantic + ancestor + oversize + prefer)
            * ro_mult
            + is_3d_bonus

    各项均独立可调，乘算 ro_mult 仅作用于 2D UI 候选；
    is_3d_bonus 加在乘法之后，避免 3D 命中（render_order 恒为 0）
    被乘算系数额外放大而盖过真正的 UI 按钮。

各维度含义
- interactive   : 节点上的交互组件得分 (Button=100, Image=15, ...)。
                  包含 Unity 内置 (Button/Toggle/...) 与项目自定义组件
                  (VirtualButton/CUIEventTrigger/...)。Mask/EventPenetrate
                  等组件给负分，因为它们要么裁剪显示要么穿透事件。
- area          : 面积越小分越高 (小元素更可能是按钮，大元素多为背景/容器)。
- semantic      : 节点名语义匹配 Unity 命名习惯：
                    ✓ btn_xxx / button_xxx / _btn → 按钮
                    ✓ tab_xxx / toggle_xxx / tog_xxx → 标签/切换
                    ✓ item_xxx / cell_xxx / slot_xxx / card_xxx → 列表项
                    ✗ panel_xxx / Panel_xxx / popup → 面板容器
                    ✗ bg / background / title_bg / tab_bg → 背景
                    ✗ mask / blocknode → 遮罩
                    ✗ Content / container / group / list → 布局容器
                  当 interactive >= 80 (确认强交互) 时正向语义置零，
                  避免命名差异覆盖渲染层级与组件类型的正确判断；负向惩罚保留。
- ancestor      : resolve 后继承祖先属性时的额外加分，固定 0；
                  避免间接命中 (Image 子节点) 优于直接命中 (按钮自身)。
- oversize      : 节点宽 / 高 ≥ 0.95 (近全屏) 时的高额惩罚，
                  几乎不可能是用户的真实点击目标 (背景面板 / 全屏遮罩)。
- prefer        : 调用方指定 prefer_components 时的强制偏好加分；
                  用于 click → input_text 串联场景。
- ro_mult       : 渲染层级乘算系数，越靠上 (topmost) 系数越大。
- is_3d_bonus   : Physics.RaycastAll 命中节点的固定加分，加在乘法之后。

渲染层级约定 (Unity)
TouchRecorder.cs 直接使用 EventSystem.RaycastAll 的索引：
  render_order = 0 → 最顶层 (front-most)
  render_order = N-1 → 最底层 (back-most)
所以本模块语义为 “越小越靠上”。

3D Physics.RaycastAll 命中节点 render_order 恒为 0，
不参与与 2D 节点的乘算系数比较 (使用固定 ro_mult = 1.0)。

resolve 逻辑
非交互子节点向上最多 3 级查找 STRONG_INTERACTIVE 祖先，将其属性合并代替自己评分。
合并时取较小 render_order (更靠上的视图层级)。
解析后多个 hit 落在同一祖先时去重，仅保留 render_order 最小者。
"""

from __future__ import annotations

import logging
import re
from typing import Optional

from common.log import get_logger

logger = get_logger("node_scorer")


# ────────────────────────── 渲染层级 ──────────────────────────

RENDER_ORDER_MULTIPLIER: float = 5.0
"""渲染层级乘算系数最大值。最顶层节点的基础分被乘以 (1 + 5) = 6x，最底层乘以 1.0x。
乘算（而非加算）确保上层弹窗的元素对下层面板拥有绝对优先级。"""


# ────────────────────────── 交互组件得分 ──────────────────────────

# Unity 内置 + 项目自定义组件 (类名取 Component.GetType().Name，无命名空间)。
# 当节点同时具备多个组件时取分值最大者。
INTERACTIVE_COMPONENT_SCORES: list[tuple[str, int]] = [
    # —— 标准 UGUI Selectable —— (强交互)
    ("Button",           100),
    ("Toggle",           100),
    ("Slider",           100),
    ("Dropdown",         100),
    ("InputField",       100),
    ("TMP_Dropdown",     100),
    ("TMP_InputField",   100),
    ("Scrollbar",         80),

    # —— 项目自定义强交互组件 ——
    ("VirtualButton",    100),  # UI/Component/VirtualButton.cs (IPointerClickHandler)
    ("GamePadBtn",       100),  # UI/Component/GamePadBtn.cs
    ("ToggleSwitch",      90),  # 自定义切换开关
    ("CUIEventTrigger",   90),  # Lua/UIComponent/CUIEventTrigger.cs
    ("ClickEventListener", 90), # SuperScrollView/ClickEventListener.cs
    ("TMPHyperClickHelper", 80),# UI/Utils/TMPHyperClickHelper.cs
    ("UIClickExtend",     75),  # 扩大点击区域的 wrapper
    ("CustomUICoordinateTracker", 75),  # 3D 坐标跟踪器（HUD/世界标记）
    ("ButtonSound",       60),  # UI/ButtonSound/ButtonSound.cs（点击音效，自身常依附 Button）

    # —— 容器型交互组件 ——
    ("ScrollRect",        35),  # 容器：可滚动但通常不是单击目标
    ("ToggleGroup",       30),  # 容器：仅管理 Toggle 选中互斥

    # —— 视觉组件（弱交互，仅当节点本身可点击时才作为最低候选）——
    ("RawImage",          15),
    ("Image",             15),
    ("Text",              10),
    ("TextMeshProUGUI",   10),
]

# 一旦节点拥有任一“强交互”组件，就视为可信的点击目标，
# 同时 _find_resolved_node 也以此判断祖先是否值得 resolve。
STRONG_INTERACTIVE_TYPES: frozenset[str] = frozenset({
    "Button", "Toggle", "Slider", "Dropdown", "InputField",
    "TMP_Dropdown", "TMP_InputField", "Scrollbar",
    "VirtualButton", "GamePadBtn", "ToggleSwitch",
    "CUIEventTrigger", "ClickEventListener", "TMPHyperClickHelper",
    "UIClickExtend", "CustomUICoordinateTracker",
})

# 拉低 / 排除型组件：交互得分中作为附加修正。
COMPONENT_PENALTIES: list[tuple[str, int]] = [
    ("EventPenetrate", -100),  # UI/Component/EventPenetrate.cs：事件穿透到目标，自身不是点击目标
    ("Mask",             -40),  # 仅做剪裁，几乎不会是用户意图目标
    ("RectMask2D",       -40),  # 同上
]


# ────────────────────────── 语义正则 ──────────────────────────

# 正向语义：Unity 项目使用前缀式命名 (btn_xxx / tab_xxx / item_xxx)，
# 与 Cocos 的 `_btn_` / `:but` 中缀命名完全不同，因此需要重写。

POSITIVE_PATTERNS: list[tuple[re.Pattern[str], int]] = [
    # btn_xxx / button_xxx / _btn / btn
    (re.compile(r"^btn(?:_|$)|^button(?:_|$)|_btn$|_button$"), 35),
    # tab_xxx / _tab —— 项目内大量出现 (tab_1, tab_bg, tab_license, ...)
    (re.compile(r"^tab(?:_|$)|_tab$"), 30),
    # toggle_xxx / tog_xxx
    (re.compile(r"^toggle(?:_|$)|^tog(?:_|$)"), 30),
    # input_xxx / edit / _edit
    (re.compile(r"^input(?:_|$)|^edit(?:_|$)|_edit$"), 30),
    # page_xxx / _page (page_left, page_right, page_anim ...)
    (re.compile(r"^page(?:_|$)|_page$"), 25),
    # 列表项 / 卡片 / 槽位
    (re.compile(r"^item(?:_|$)|^cell(?:_|$)|^slot(?:_|$)|^card(?:_|$)"), 20),
    # 显式 icon 按钮命名
    (re.compile(r"^icon_btn(?:_|$)|_icon_btn$"), 25),
]

# 负向语义：背景 / 容器 / 遮罩 / 装饰元素，不该作为点击目标。
NEGATIVE_PATTERNS: list[tuple[re.Pattern[str], int]] = [
    # 显式占位 / 阻挡节点
    (re.compile(r"blocknode|block_node"), -100),
    # 任意位置出现 mask
    (re.compile(r"mask"), -50),
    # 背景：bg / _bg / bg_xxx / title_bg / tab_bg / background
    (re.compile(r"(?:^|_)bg(?:_|$)|background"), -40),
    # Slider Handle —— 实际拖动靶心，但 Slider 本身才是逻辑目标
    (re.compile(r"handle"), -50),
    # 面板 / 弹窗 / 视图根
    (re.compile(r"^panel(?:_|$)|^popup(?:s)?(?:_|$)|_popup$"), -25),
    (re.compile(r"^layer(?:_|$)|^root$|^uiroot$|^canvas$"), -30),
    # 容器 / 内容
    (re.compile(r"^content(?:s)?$|^container$|_content$|^viewport$"), -20),
    # 复数命名的“一组同类节点”父级
    (re.compile(r"^group(?:s)?$|_group$|^tabs$|^buttons$|^pages$|^toggles$|^items$|^list$|^lists$"), -15),
    # 布局
    (re.compile(r"^layout(?:_|$)|_layout$|layoutgroup"), -20),
    # 纯文字 / 标签节点
    (re.compile(r"^text$|^title$|^txt$|^label$|^name$|^value$|^tip(?:s)?$|^info$|^desc(?:ription)?$"), -10),
    # 图片 / 图标 / 装饰元素
    (re.compile(r"^img(?:_|$)|^icon(?:_|$)|^sprite|^particle|^fx_|^line$|^red$|^reddot$|^arrow"), -5),
]


# ────────────────────────── 加分常数 ──────────────────────────

PREFER_COMPONENT_BONUS: int = 500
"""指定 prefer_components 命中时的加分。足够大以确保该类型节点碾压其他候选。
用于 click 后立即 input_text 等场景，强制选中 InputField 而非 Image 容器。"""

OVERSIZE_PENALTY: int = -200
"""节点尺寸 (归一化) ≥ 0.95 (近全屏) 时的惩罚分。
全屏 / 超屏节点几乎不可能是用户的真实点击目标。"""

OVERSIZE_THRESHOLD: float = 0.95
"""触发 OVERSIZE_PENALTY 的归一化尺寸阈值。"""

IS_3D_BONUS: int = 80
"""3D Physics 射线命中节点的加分（加在乘法之后）。
取值需高于非交互 UI 背景 (interactive≈15 + 负语义) 的最高值，
但低于 UI Button 在低层级时的总分 (≈100 + area ≈ 130)，
让真正交互的 UI 始终能压过同位置的 3D 命中。"""

INTERACTIVE_SUPPRESS_SEMANTIC_THRESHOLD: int = 80
"""interactive >= 该阈值时正向语义清零，避免按钮/输入框等强交互组件
再因命名“双重加分”，与命名习惯不一致的强交互目标会被错误推下。"""

MAX_AREA_SCORE: float = 40.0
"""area_score 满分（即面积最小时取的最大值）。"""

INTERACTABLE_FALSE_SCORE: int = 5
"""Selectable.interactable = false 时的兜底交互分（远低于普通可交互组件）。
保留极小正分，使得 disabled 按钮仍优于纯背景，但绝不会战胜可点击按钮。"""

ANCESTOR_RESOLVE_DEPTH: int = 3
"""向上查找强交互祖先的最大层级。"""


# ────────────────────────── 工具函数 ──────────────────────────

def _components_of(node: dict) -> list[str]:
    return node.get("components") or []


def _has_strong_interactive(components: list[str]) -> bool:
    """节点是否包含任一强交互组件。"""
    return any(c in STRONG_INTERACTIVE_TYPES for c in components)


# ────────────────────────── 各维度评分 ──────────────────────────

def _get_interactive_score(components: list[str], interactable: Optional[bool]) -> int:
    """根据节点组件列表计算交互得分，并叠加抑制型组件的负分。

    interactable == False 时强制降为低分，避免 disabled 按钮被识为目标。
    """
    if not components:
        return 0

    has_button = any(c in ("Button", "Toggle", "Slider", "Dropdown",
                           "InputField", "TMP_Dropdown", "TMP_InputField")
                     for c in components)
    if has_button and interactable is False:
        return INTERACTABLE_FALSE_SCORE

    max_score = 0
    for comp_type, score in INTERACTIVE_COMPONENT_SCORES:
        if comp_type in components and score > max_score:
            max_score = score

    penalty = 0
    for comp_type, pen in COMPONENT_PENALTIES:
        if comp_type in components:
            penalty += pen

    return max(0, max_score) + penalty


def _get_area_score(area: float, max_area: float) -> float:
    """面积越小得分越高（小元素更可能是按钮而非背景）。

    area <= 0 时返回 0：避免缺失数据 (parent_chain 中的祖先无 area 字段)
    被错误地按“最小面积”记最高分。
    """
    if area <= 0 or max_area <= 0:
        return 0.0
    ratio = area / max_area
    if ratio >= 1.0:
        return 0.0
    return (1.0 - ratio) * MAX_AREA_SCORE


def _get_semantic_score(name: str) -> int:
    """根据节点名匹配 Unity 项目命名习惯，正负各最多累加一条。"""
    if not name:
        return 0
    lower = name.lower()
    score = 0
    for pattern, pts in POSITIVE_PATTERNS:
        if pattern.search(lower):
            score += pts
            break
    for pattern, pts in NEGATIVE_PATTERNS:
        if pattern.search(lower):
            score += pts
            break
    return score


def _get_oversize_penalty(node: dict) -> int:
    """节点尺寸覆盖整个屏幕宽度或高度时给予高额惩罚。"""
    size = node.get("size") or [0.0, 0.0]
    if len(size) < 2:
        return 0
    w, h = size[0], size[1]
    if w >= OVERSIZE_THRESHOLD or h >= OVERSIZE_THRESHOLD:
        return OVERSIZE_PENALTY
    return 0


def _get_prefer_score(components: list[str], prefer_components: Optional[list[str]]) -> int:
    if not prefer_components:
        return 0
    for pc in prefer_components:
        if pc in components:
            return PREFER_COMPONENT_BONUS
    return 0


def _get_render_order_multiplier(render_order: int, max_render_order: int) -> float:
    """渲染层级乘算系数。

    Unity 端约定：render_order 来自 EventSystem.RaycastAll 的索引，
    越小越靠上 (front-most)；max_render_order 为本帧 2D 命中节点中最大的索引。

    返回 [1.0, 1.0 + RENDER_ORDER_MULTIPLIER] 的系数：
      最顶层 (render_order = 0)              → 1 + RENDER_ORDER_MULTIPLIER
      最底层 (render_order = max_render_order) → 1.0
      只有一个 2D 候选 (max == 0)            → 1.0 (无层级竞争，给中性值)
    """
    if max_render_order <= 0:
        return 1.0
    topness = (max_render_order - render_order) / max_render_order
    topness = max(0.0, min(1.0, topness))
    return 1.0 + topness * RENDER_ORDER_MULTIPLIER


# ────────────────────────── resolve 逻辑 ──────────────────────────

def _find_resolved_node(
    node: dict,
    all_nodes_by_path: dict[str, dict],
) -> tuple[dict, int]:
    """非交互节点向上最多 ANCESTOR_RESOLVE_DEPTH 级查找强交互祖先。

    返回 (resolved_node, ancestor_bonus)。
      ancestor_bonus 固定为 0，避免间接命中 (子节点) 不合理地优于
      直接命中 (强交互节点本身) —— 子节点已通过 resolve 继承祖先得分。

    resolved_node 在合并时取较小的 render_order (更靠上)，
    确保子节点的高视图层级不因 resolve 到祖先而丢失。
    """
    components = _components_of(node)
    if _has_strong_interactive(components):
        return node, 0

    parent_chain = node.get("parent_chain") or []
    for parent in parent_chain[:ANCESTOR_RESOLVE_DEPTH]:
        parent_components = parent.get("components") or []
        if not _has_strong_interactive(parent_components):
            continue

        parent_path = parent.get("path", "")
        # 优先用全量字段（all_nodes_by_path 中可能有同祖先的完整 raycast 数据）
        resolved = all_nodes_by_path.get(parent_path, parent)

        child_order = node.get("render_order", 0)
        resolved_order = resolved.get("render_order", 0)
        # Unity 约定：越小越靠上 → 取较小者继承到祖先
        if child_order < resolved_order:
            resolved = {**resolved, "render_order": child_order}
        return resolved, 0

    return node, 0


# ────────────────────────── 主入口 ──────────────────────────

def pick_best_node(
    hit_nodes: list[dict],
    click_position: list[float],
    prefer_components: Optional[list[str]] = None,
) -> Optional[dict]:
    """从 hit_nodes 列表中评分并选出最佳节点。

    每个 hit_node 的结构由 Unity 端 (TouchRecorder.cs) 提供：
        {
            "path":          str,           # LocatorPath.locatorPath 或带索引的层级路径
            "name":          str,           # GameObject.name
            "components":    list[str],     # Unity 组件类名（无命名空间）
            "area":          float,         # RectTransform.rect 面积；3D 命中为 0
            "interactable":  bool | None,   # Selectable.interactable；无 Selectable 为 None
            "position":      [float, float],# 归一化屏幕坐标 [x, y]，y 向下
            "size":          [float, float],# 归一化屏幕尺寸 [w, h]
            "render_order":  int,           # 2D：EventSystem.RaycastAll 索引（0 最顶层）
                                            # 3D：恒为 0
            "parent_chain":  list[dict],    # 最多 3 级父节点 (name/path/components)
            "is_3d":         bool | None,   # True 表示 Physics.RaycastAll 命中
            "locator_camera":str | None,    # 命中所属相机路径
        }

    :param prefer_components: 强制偏好组件，例如 click 紧跟 input_text 时
        传入 ["TMP_InputField", "InputField"]，让该类型节点直接拿下 +500 分。

    返回值在原始 hit_node dict 基础上追加 "focus" / "score" / "score_breakdown"。
    """
    if not hit_nodes:
        return None

    # 仅 2D 候选参与 render_order 比较；3D 节点 render_order 恒为 0，
    # 单独以 IS_3D_BONUS 加分，避免被乘算系数额外放大。
    max_render_order = max(
        (n.get("render_order", 0) for n in hit_nodes if not n.get("is_3d")),
        default=0,
    )
    max_area = max((n.get("area", 0) for n in hit_nodes), default=0)
    all_nodes_by_path: dict[str, dict] = {n.get("path", ""): n for n in hit_nodes}

    debug_enabled = logger.isEnabledFor(logging.DEBUG)
    if debug_enabled:
        logger.debug(
            f"┌─ 评分开始 ─ {len(hit_nodes)} hits, click={click_position}, "
            f"max_area={max_area:.0f}, max_ro_2d={max_render_order}"
        )

    scored: list[tuple[float, dict, dict]] = []
    skipped: list[str] = []
    resolved_paths_seen: set[str] = set()

    for idx, raw_node in enumerate(hit_nodes):
        resolved, ancestor_bonus = _find_resolved_node(raw_node, all_nodes_by_path)
        r_path = resolved.get("path", "")
        is_resolved = (r_path != raw_node.get("path", ""))

        # ───── 去重：多个 hit 落到同一祖先时仅保留 render_order 最小者 ─────
        if r_path in resolved_paths_seen:
            existing = next((s for s in scored if s[1].get("path") == r_path), None)
            if existing is not None:
                cur_order = resolved.get("render_order", 0)
                prev_order = existing[1].get("render_order", 0)
                if cur_order < prev_order:  # Unity: 越小越靠上 → 替换
                    scored.remove(existing)
                    resolved_paths_seen.discard(r_path)
                else:
                    skipped.append(f"[{idx}] {raw_node.get('name', '?')} → 合并到 {r_path}")
                    continue
            else:
                skipped.append(f"[{idx}] {raw_node.get('name', '?')} → 合并到 {r_path}")
                continue

        resolved_paths_seen.add(r_path)

        total, breakdown = _score_node(
            resolved, max_area, max_render_order, prefer_components, ancestor_bonus
        )
        scored.append((total, resolved, breakdown))

        if debug_enabled:
            tag = f" (← {raw_node.get('name', '?')})" if is_resolved else ""
            logger.debug(
                f"│  [{idx}] {resolved.get('name', '?')}{tag}  "
                f"total={total:.1f}  {breakdown}"
            )

    if not scored:
        logger.info("节点评分: 无有效候选节点")
        return None

    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best_node, best_breakdown = scored[0]
    focus = _compute_focus(click_position, best_node)

    _emit_decision_log(
        hit_nodes, scored, skipped, best_score, best_node, focus,
        click_position, max_area, max_render_order,
    )

    return {
        **best_node,
        "focus": focus,
        "score": round(best_score, 2),
        "score_breakdown": best_breakdown,
    }


def _score_node(
    node: dict,
    max_area: float,
    max_render_order: int,
    prefer_components: Optional[list[str]],
    ancestor_bonus: int,
) -> tuple[float, dict]:
    """为单个（已 resolve 的）节点计算总分与得分明细。"""
    components = _components_of(node)
    is_3d = bool(node.get("is_3d"))

    interactive = _get_interactive_score(components, node.get("interactable"))
    area = _get_area_score(node.get("area", 0), max_area)
    semantic = _get_semantic_score(node.get("name", ""))
    if interactive >= INTERACTIVE_SUPPRESS_SEMANTIC_THRESHOLD and semantic > 0:
        semantic = 0  # 强交互节点不再因正向命名“双重加分”
    oversize = _get_oversize_penalty(node)
    prefer = _get_prefer_score(components, prefer_components)

    base = interactive + area + semantic + ancestor_bonus + oversize + prefer

    # 3D 候选不参与 2D 渲染层级竞争，使用中性 1.0；
    # is_3d_bonus 加在乘法之后，避免被乘算放大。
    if is_3d:
        ro_mult = 1.0
        is_3d_bonus = IS_3D_BONUS
    else:
        ro_mult = _get_render_order_multiplier(node.get("render_order", 0), max_render_order)
        is_3d_bonus = 0

    total = base * ro_mult + is_3d_bonus

    breakdown = {
        "interactive":   interactive,
        "area":          round(area, 2),
        "semantic":      semantic,
        "oversize":      oversize,
        "prefer":        prefer,
        "ancestorBonus": ancestor_bonus,
        "base":          round(base, 2),
        "roMult":        round(ro_mult, 3),
        "is3dBonus":     is_3d_bonus,
    }
    return total, breakdown


def _emit_decision_log(
    hit_nodes: list[dict],
    scored: list[tuple[float, dict, dict]],
    skipped: list[str],
    best_score: float,
    best_node: dict,
    focus: list[float],
    click_position: list[float],
    max_area: float,
    max_render_order: int,
) -> None:
    """把整次评分过程拼成一段 INFO 日志，便于事后审查为何选中某节点。"""
    lines: list[str] = [
        f"┌─ 节点评分 ─ 命中 {len(hit_nodes)} 个, 候选 {len(scored)} 个, "
        f"click={click_position}, max_area={max_area:.0f}, max_ro_2d={max_render_order}"
    ]
    for i, n in enumerate(hit_nodes):
        lines.append(
            f"│ raw[{i}] {n.get('name','?')}  path={n.get('path','?')}  "
            f"comps={n.get('components', [])}  "
            f"area={n.get('area', 0):.0f}  ro={n.get('render_order', 0)}"
            f"{'  (3D)' if n.get('is_3d') else ''}"
        )
    if skipped:
        lines.append(f"│ 合并跳过: {'; '.join(skipped)}")
    lines.append("│ ── 评分排名 ──")
    for rank, (total, n, bd) in enumerate(scored, 1):
        marker = " ★" if rank == 1 else ""
        lines.append(
            f"│ #{rank} {total:.1f}{marker}  {n.get('name', '?')}  "
            f"path={n.get('path', '?')}  "
            f"base={bd['base']} ×ro={bd['roMult']} +3d={bd['is3dBonus']}  "
            f"[inter={bd['interactive']} area={bd['area']} sem={bd['semantic']} "
            f"oversize={bd['oversize']} prefer={bd['prefer']} anc={bd['ancestorBonus']}]"
        )
    lines.append(
        f"└─ 选中: {best_node.get('name', '?')} "
        f"score={best_score:.1f} focus={focus}"
    )
    logger.info("\n".join(lines))


def _compute_focus(
    click_pos: list[float],
    node: dict,
) -> list[float]:
    """根据归一化点击坐标和节点的归一化屏幕坐标 / 尺寸反算 focus。

    反推自 Locate.CorrectPosition 的公式：
        finalPos = center + size * (0.5 - focus)
    解出：
        focus = 0.5 - (click - center) / size
    click 与 center 均为归一化、y 向下，X / Y 同公式。
    """
    pos = node.get("position") or [0.5, 0.5]
    size = node.get("size") or [0.0, 0.0]

    if len(pos) < 2 or len(size) < 2:
        return [0.5, 0.5]

    sw, sh = size[0], size[1]
    if sw < 1e-3 or sh < 1e-3:
        return [0.5, 0.5]

    fx = 0.5 - (click_pos[0] - pos[0]) / sw
    fy = 0.5 - (click_pos[1] - pos[1]) / sh
    return [round(fx, 3), round(fy, 3)]

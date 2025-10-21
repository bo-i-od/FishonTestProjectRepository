import sys
import re
import random
from collections import Counter

def pct(x, denom, digits=2):
    if denom <= 0:
        return f"{0:.{digits}f}%"
    return f"{(x / denom) * 100:.{digits}f}%"

def visible_len(s):
    width = 0
    for ch in s:
        if ord(ch) < 128:
            width += 1
        else:
            width += 2
    return width

def pad_str(s, width, align="left"):
    s = "" if s is None else str(s)
    vis = visible_len(s)
    pad = max(0, width - vis)
    if align == "right":
        return " " * pad + s
    elif align == "center":
        left = pad // 2
        right = pad - left
        return " " * left + s + " " * right
    else:
        return s + " " * pad

def format_table(headers, rows, col_align=None):
    str_rows = [[("" if v is None else str(v)) for v in row] for row in rows]
    ncol = len(headers)
    for r in str_rows:
        if len(r) != ncol:
            raise ValueError("行列数不一致")
    widths = []
    for j in range(ncol):
        col_items = [headers[j]] + [r[j] for r in str_rows]
        widths.append(max(visible_len(str(x)) for x in col_items))
    if col_align is None:
        col_align = ["left"] + ["right"] * (ncol - 1)
    header_line = " | ".join(pad_str(headers[i], widths[i], "center") for i in range(ncol))
    sep_line = "-+-".join("-" * widths[i] for i in range(ncol))
    out_lines = [header_line, sep_line]
    for r in str_rows:
        out_lines.append(" | ".join(pad_str(r[i], widths[i], col_align[i]) for i in range(ncol)))
    return "\n".join(out_lines)

def simulate_spinner(
    weights_by_point,
    values_by_point,
    total_spins,
    limit_max,
    limit_min,
    special_points=(6, 12),
    adjacent_points=(1, 5, 7, 11),
    rng=None,
    emergency_reset_when_empty=True,
):
    if rng is None:
        rng = random.Random()

    all_points = list(range(1, 13))
    if set(weights_by_point.keys()) != set(all_points):
        raise ValueError("weights_by_point 必须包含1~12的所有点位")
    if set(values_by_point.keys()) != set(all_points):
        raise ValueError("values_by_point 必须包含1~12的所有点位")
    if limit_min < 0 or limit_max <= 0:
        raise ValueError("limit_min需>=0，limit_max需>0")
    if any(w < 0 for w in weights_by_point.values()):
        raise ValueError("权重必须为非负数")
    if any(v < 0 for v in values_by_point.values()):
        raise ValueError("价值必须为非负数")
    if not set(special_points).issubset(set(all_points)):
        raise ValueError("特殊点位必须在1~12内")
    if not set(adjacent_points).issubset(set(all_points)):
        raise ValueError("旁边点位必须在1~12内")
    if set(adjacent_points) & set(special_points):
        raise ValueError("旁边点位集合不应包含特殊点位")

    hits = {p: 0 for p in all_points}
    total_value = 0.0

    used_in_round = set()
    spins_in_round = 0
    value_in_round = 0.0

    special_weights = {p: weights_by_point[p] for p in special_points}
    normal_points = [p for p in all_points if p not in special_points]
    normal_weights_base = {p: weights_by_point[p] for p in normal_points}

    round_lengths = []
    round_values = []  # 每轮价值
    special_hits_in_round = []
    unique_normal_hits_per_round = []
    special_forced_count = 0
    special_natural_count = 0
    forbidden_exhausted_resets = 0

    adjacent_points = tuple(adjacent_points)
    adjacent_hits_per_round = []
    rounds_adjacent_coverage = []
    adjacent_hits_in_current_round = 0
    adjacent_points_hit_set_in_round = set()

    def pick_point(available_points, weights_dict):
        points = list(available_points)
        weights = [weights_dict[p] for p in points]
        total_w = sum(weights)
        if total_w <= 0:
            weights = None
        return rng.choices(points, weights=weights, k=1)[0]

    def close_round(last_special=None, forced=False):
        nonlocal spins_in_round, used_in_round, special_forced_count, special_natural_count
        nonlocal adjacent_hits_in_current_round, adjacent_points_hit_set_in_round, value_in_round
        if spins_in_round > 0 or forced:
            round_lengths.append(spins_in_round)
            round_values.append(value_in_round)
            unique_normal_hits_per_round.append(len(used_in_round))
            adjacent_hits_per_round.append(adjacent_hits_in_current_round)
            rounds_adjacent_coverage.append(len(adjacent_points_hit_set_in_round))
            if last_special is not None:
                special_hits_in_round.append(last_special)
                if forced:
                    special_forced_count += 1
                else:
                    special_natural_count += 1
        used_in_round.clear()
        spins_in_round = 0
        value_in_round = 0.0
        adjacent_hits_in_current_round = 0
        adjacent_points_hit_set_in_round = set()

    total_spins_done = 0
    while total_spins_done < total_spins:
        must_pick_special = (spins_in_round >= limit_max)
        special_forbidden = (spins_in_round < limit_min)

        if must_pick_special:
            available = list(special_points)
            weights_dict = special_weights
        else:
            if special_forbidden:
                available = [p for p in normal_points if p not in used_in_round]
                weights_dict = normal_weights_base
            else:
                available = [p for p in normal_points if p not in used_in_round] + list(special_points)
                weights_dict = {**normal_weights_base, **special_weights}

        if not available:
            if emergency_reset_when_empty:
                forbidden_exhausted_resets += 1
                close_round(last_special=None, forced=False)
                continue
            else:
                available = list(special_points)
                weights_dict = special_weights

        picked = pick_point(available, weights_dict)

        # 记录命中与价值
        hits[picked] += 1
        val = values_by_point[picked]
        total_value += val
        value_in_round += val

        spins_in_round += 1
        total_spins_done += 1

        if picked in adjacent_points:
            adjacent_hits_in_current_round += 1
            adjacent_points_hit_set_in_round.add(picked)

        if picked in special_points:
            forced = must_pick_special
            close_round(last_special=picked, forced=forced)
        else:
            used_in_round.add(picked)

    avg_spins_per_hit = {p: (total_spins / hits[p]) if hits[p] > 0 else None for p in all_points}
    round_length_dist = dict(Counter(round_lengths))
    special_hit_counts = {p: hits[p] for p in special_points}

    total_special_hits = sum(special_hit_counts.values())
    rounds_total = len(round_lengths)

    special_due_to_force_rate = (special_forced_count / total_special_hits) if total_special_hits > 0 else 0.0
    special_natural_rate = (special_natural_count / total_special_hits) if total_special_hits > 0 else 0.0

    adjacent_hit_counts = {p: hits[p] for p in adjacent_points}
    adjacent_hits_total = sum(adjacent_hit_counts.values())
    total_hits = sum(hits.values())
    total_normal_hits = sum(hits[p] for p in all_points if p not in special_points)

    adjacent_hit_rate = (adjacent_hits_total / total_hits) if total_hits > 0 else 0.0
    adjacent_hit_rate_among_normal = (adjacent_hits_total / total_normal_hits) if total_normal_hits > 0 else 0.0
    avg_spins_per_adjacent_hit = (total_spins / adjacent_hits_total) if adjacent_hits_total > 0 else None
    avg_adjacent_hits_per_round = (sum(adjacent_hits_per_round) / rounds_total) if rounds_total > 0 else 0.0
    rounds_with_adjacent_hits = sum(1 for x in adjacent_hits_per_round if x > 0)
    avg_rounds_adjacent_coverage = (sum(rounds_adjacent_coverage) / rounds_total) if rounds_total > 0 else 0.0

    # 价值类汇总
    avg_value_per_round = (sum(round_values) / rounds_total) if rounds_total > 0 else 0.0
    avg_value_per_spin = (total_value / total_spins) if total_spins > 0 else 0.0

    result = {
        "hits": hits,
        "avg_spins_per_hit": avg_spins_per_hit,

        "round_lengths": round_lengths,
        "round_values": round_values,
        "rounds_total": rounds_total,
        "avg_round_length": (sum(round_lengths) / rounds_total) if rounds_total else 0.0,
        "round_length_dist": round_length_dist,

        "special_hits_in_round": special_hits_in_round,
        "special_hit_counts": special_hit_counts,
        "rounds_with_forced_special": special_forced_count,
        "rounds_with_forbidden_special_exhausted": forbidden_exhausted_resets,
        "special_due_to_force_rate": special_due_to_force_rate,
        "special_natural_rate": special_natural_rate,

        "adjacent_points": list(adjacent_points),
        "adjacent_hit_counts": adjacent_hit_counts,
        "adjacent_hits_total": adjacent_hits_total,
        "adjacent_hit_rate": adjacent_hit_rate,
        "adjacent_hit_rate_among_normal": adjacent_hit_rate_among_normal,
        "avg_spins_per_adjacent_hit": avg_spins_per_adjacent_hit,
        "adjacent_hits_per_round": adjacent_hits_per_round,
        "avg_adjacent_hits_per_round": avg_adjacent_hits_per_round,
        "rounds_with_adjacent_hits": rounds_with_adjacent_hits,
        "rounds_adjacent_coverage": rounds_adjacent_coverage,
        "avg_rounds_adjacent_coverage": avg_rounds_adjacent_coverage,

        "unique_normal_hits_per_round": unique_normal_hits_per_round,
        "avg_unique_normal_hits_per_round": (sum(unique_normal_hits_per_round) / rounds_total) if rounds_total else 0.0,

        "total_spins": total_spins,
        "total_hits": total_hits,

        # 价值
        "values_by_point": values_by_point,
        "total_value": total_value,
        "avg_value_per_round": avg_value_per_round,
        "avg_value_per_spin": avg_value_per_spin,
    }
    return result

def parse_input(text, mode="weight"):
    """
    输入格式要求（字段名可包含空格/制表分隔）：
    表头需包含：号位(或点位)  价值  权重
    下面每行：点位  价值  权重
    末尾参数：总旋转次数 / 最大保底值 / 最小保底值

    mode:
      - "weight": 使用“权重”列作为抽取权重
      - "valuexweight": 使用“价值×权重”作为抽取权重
    """
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    header_idx = None
    for i, l in enumerate(lines):
        if (("号位" in l or "点位" in l) and "权重" in l and "价值" in l):
            header_idx = i
            break
    if header_idx is None:
        raise ValueError("未找到表头（需包含‘号位/点位’、‘价值’、‘权重’）")

    weights_by_point = {}
    values_by_point = {}
    i = header_idx + 1
    while i < len(lines):
        l = lines[i]
        if ("总旋转次数" in l) or ("最大保底值" in l) or ("最小保底值" in l):
            break
        parts = re.split(r"[,\t]+|\s{2,}", l)
        if len(parts) < 3:
            parts = l.split()
        if len(parts) < 3:
            i += 1
            continue
        try:
            point = int(parts[0])
            val = float(parts[1])
            w = float(parts[2])
        except Exception:
            i += 1
            continue
        if not (1 <= point <= 12):
            i += 1
            continue
        values_by_point[point] = val
        # 选择抽取权重
        weights_by_point[point] = (val * w) if mode == "valuexweight" else w
        i += 1

    total_spins = None
    limit_max = None
    limit_min = None
    for j in range(i, len(lines)):
        l = lines[j]
        if "总旋转次数" in l:
            m = re.search(r"(\d+)", l)
            if m:
                total_spins = int(m.group(1))
        elif "最大保底值" in l:
            m = re.search(r"(\d+)", l)
            if m:
                limit_max = int(m.group(1))
        elif "最小保底值" in l:
            m = re.search(r"(\d+)", l)
            if m:
                limit_min = int(m.group(1))

    if len(weights_by_point) != 12 or len(values_by_point) != 12:
        raise ValueError(f"解析到 点位={len(values_by_point)}、权重={len(weights_by_point)}，期待各12个。请检查输入格式。")
    if total_spins is None or limit_max is None or limit_min is None:
        raise ValueError("未能解析到‘总旋转次数/最大保底值/最小保底值’三个参数。")

    return weights_by_point, values_by_point, total_spins, limit_max, limit_min

def main():
    print("请选择权重模式：")
    print("1) 使用‘权重’列作为抽取权重")
    print("2) 使用‘价值×权重’作为抽取权重")
    mode = input("输入 1 或 2 回车：").strip()
    mode_key = "valuexweight" if mode == "2" else "weight"

    print("\n请粘贴你的数据（包含表头与参数），粘贴完成后按两次回车结束输入：\n")
    buffer_lines = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.strip() == "":
            next_line = sys.stdin.readline()
            if not next_line or next_line.strip() == "":
                break
            else:
                buffer_lines.append(line)
                buffer_lines.append(next_line)
                continue
        buffer_lines.append(line)
    text = "".join(buffer_lines)

    try:
        weights_by_point, values_by_point, total_spins, limit_max, limit_min = parse_input(text, mode=mode_key)
    except Exception as e:
        print(f"输入解析错误：{e}")
        return

    rng = random.Random(42)  # 如需每次不同，改为 rng = random.Random()

    result = simulate_spinner(
        weights_by_point,
        values_by_point,
        total_spins,
        limit_max,
        limit_min,
        special_points=(6, 12),
        adjacent_points=(1, 5, 7, 11),
        rng=rng,
        emergency_reset_when_empty=True
    )

    rounds_total = result["rounds_total"]
    total_hits = result["total_hits"]

    print("\n=== 结果（表格展示，含价值统计）===\n")

    # 概览
    overview_headers = ["指标", "数值"]
    overview_rows = [
        ["总轮次", rounds_total],
        ["平均每轮长度", f"{result['avg_round_length']:.4f}"],
        ["总命中次数（全部点位合计）", total_hits],
        ["总旋转次数", result["total_spins"]],
        ["总价值", f"{result['total_value']:.4f}"],
        ["每轮平均价值", f"{result['avg_value_per_round']:.4f}"],
        ["每转平均价值", f"{result['avg_value_per_spin']:.6f}"],
    ]
    print(format_table(overview_headers, overview_rows, col_align=["left", "right"]))
    print()

    # 命中次数与平均间隔与价值
    hit_headers = ["点位", "命中次数", "命中占比", "平均每次命中所需转数", "该点位价值"]
    hit_rows = []
    for p in range(1, 13):
        count = result["hits"][p]
        rate = pct(count, total_hits)
        avg_need = result["avg_spins_per_hit"][p]
        avg_str = f"{avg_need:.4f}" if isinstance(avg_need, (int, float)) else "-"
        val = result["values_by_point"][p]
        hit_rows.append([str(p), str(count), rate, avg_str, f"{val:.4f}"])
    print(format_table(hit_headers, hit_rows, col_align=["right", "right", "right", "right", "right"]))
    print()

    # 轮次相关指标
    round_headers = ["指标", "数值", "占总轮次比例"]
    round_rows = [
        ["总轮次", rounds_total, pct(rounds_total, rounds_total)],
        ["平均每轮独特普通格命中数", f"{result['avg_unique_normal_hits_per_round']:.4f}", "—"],
        ["因必中特殊的轮次数", result["rounds_with_forced_special"], pct(result["rounds_with_forced_special"], rounds_total)],
        ["禁止特殊阶段普通格耗尽的应急重启次数", result["rounds_with_forbidden_special_exhausted"], pct(result["rounds_with_forbidden_special_exhausted"], rounds_total)],
    ]
    print(format_table(round_headers, round_rows, col_align=["left", "right", "right"]))
    print()

    # 特殊命中分解
    special_headers = ["指标", "数值"]
    special_rows = [
        ["特殊命中次数（6/12）", str(result["special_hit_counts"])],
        ["特殊因强制的比例", pct(result["special_due_to_force_rate"], 1)],
        ["特殊自然命中的比例", pct(result["special_natural_rate"], 1)],
    ]
    print(format_table(special_headers, special_rows, col_align=["left", "right"]))
    print()

    # 旁边格统计
    adj_headers = ["指标", "数值"]
    adj_rows = [
        ["旁边格点位", str(result["adjacent_points"])],
        ["旁边格命中次数（各点位）", str(result["adjacent_hit_counts"])],
        ["旁边格总命中次数", result["adjacent_hits_total"]],
        ["旁边格命中占总命中的比例", pct(result["adjacent_hit_rate"], 1)],
        ["旁边格命中占普通格命中的比例", pct(result["adjacent_hit_rate_among_normal"], 1)],
        ["平均每次命中旁边格所需转数", f"{result['avg_spins_per_adjacent_hit']:.4f}" if result['avg_spins_per_adjacent_hit'] is not None else "-"],
        ["平均每轮命中旁边格次数", f"{result['avg_adjacent_hits_per_round']:.4f}"],
        ["至少命中一次旁边格的轮次数", f"{result['rounds_with_adjacent_hits']}（占比 {pct(result['rounds_with_adjacent_hits'], rounds_total)}）"],
        ["平均每轮不同旁边格覆盖数", f"{result['avg_rounds_adjacent_coverage']:.4f}"],
    ]
    print(format_table(adj_headers, adj_rows, col_align=["left", "right"]))
    print()

    # 轮长度分布
    dist_headers = ["轮长度", "次数", "占总轮次比例"]
    dist_rows = []
    for k in sorted(result["round_length_dist"].keys()):
        cnt = result["round_length_dist"][k]
        dist_rows.append([str(k), str(cnt), pct(cnt, rounds_total)])
    print(format_table(dist_headers, dist_rows, col_align=["right", "right", "right"]))
    print()

if __name__ == "__main__":
    main()
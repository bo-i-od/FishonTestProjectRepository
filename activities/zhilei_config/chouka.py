import re
from pprint import pprint
import pandas as pd


def parse_log(log_text):
    rounds = []
    current_round = None
    current_allot_stack = []

    # 正则表达式模式
    round_pattern = re.compile(r'round:(\d+):')
    allot_start_pattern = re.compile(r'$$INFO$$enter allot: \(($\d+)-(\d+)$\)')
    result_pattern = re.compile(r'do allot result:type:(\d+) id:(\d+) count:(\d+)')
    drop_result_pattern = re.compile(r'dropResult:$$type:(\d+) id:(\d+) count:(\d+)$$')
    executed_allots_pattern = re.compile(r'executedAllots:$$(.*?)$$')

    for line in log_text.split('\n'):
        # 匹配新回合开始
        if m := round_pattern.search(line):
            if current_round:
                rounds.append(current_round)
            current_round = {
                "round": int(m.group(1)),
                "drop_results": [],
                "executed_allots": [],
                "steps": []
            }
        # 匹配分配结果
        elif m := result_pattern.search(line):
            current_round["steps"].append({
                "allot_type": current_allot_stack[-1][0] if current_allot_stack else None,
                "allot_id": current_allot_stack[-1][1] if current_allot_stack else None,
                "result_type": int(m.group(1)),
                "result_id": int(m.group(2)),
                "result_count": int(m.group(3))
            })
        # 匹配分配开始
        elif m := allot_start_pattern.search(line):
            current_allot_stack.append((m.group(1), m.group(2)))  # (分配器类型, 分配器ID)
        # 匹配最终结果
        elif m := drop_result_pattern.findall(line):
            for type_, id_, count in m:
                current_round["drop_results"].append({
                    "type": int(type_),
                    "id": int(id_),
                    "count": int(count)
                })
        # 匹配执行过的分配器
        elif m := executed_allots_pattern.search(line):
            current_round["executed_allots"] = [
                tuple(map(int, a.split('-')))
                for a in m.group(1).split(', ')
            ]

    if current_round:
        rounds.append(current_round)
    return rounds


# 示例使用
log_data = read

# 解析日志
parsed_data = parse_log(log_data)

# 转换为DataFrame
df = pd.DataFrame([
    {
        "round": r["round"],
        "step_num": i,
        **step
    }
    for r in parsed_data
    for i, step in enumerate(r["steps"])
])

print("解析后的数据结构示例：")
pprint(parsed_data[0], depth=2)

print("\nDataFrame格式：")
print(df.head(3).to_markdown(index=False))
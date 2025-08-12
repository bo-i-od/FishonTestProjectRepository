from statistics.load_log import load_log_new
from collections import defaultdict

hook_log=load_log_new('../statistics/new_hook_log.txt')
num = 0

sr_card = 0
ssr_card = 0
sr_count = defaultdict(int)
ssr_count = defaultdict(int)

for i in hook_log:
    items = i.get('items', {})
    tiacs = items.get('tiacs', {})
    card = tiacs.get('1', {})
    bow_card_id = card.get('id')
    count = card.get('count', 0)
    if bow_card_id is None:
        continue
    num += count
    # 计算掉落数量
    if bow_card_id == 240164:
        sr_card += 1
        sr_count[count] += 1
    elif bow_card_id == 240165:
        ssr_card += 1
        ssr_count[count] += 1
    print(f"count: {count}, id: {bow_card_id}")

print("普通箭袋掉落次数：", sr_card)
print("普通箭袋各张数次数：", dict(sr_count))
print("高级箭袋掉落次数：", ssr_card)
print("高级箭袋各张数次数：", dict(ssr_count))
cur = len(hook_log)
print("钓鱼次数:", cur)
print("箭袋总数:", num)
print("普通箭袋掉落概率", sr_card / cur if cur else 0)
print("高级箭袋掉落概率", ssr_card / cur if cur else 0)
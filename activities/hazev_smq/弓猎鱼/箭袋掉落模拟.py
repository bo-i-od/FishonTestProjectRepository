import numpy as np

def get_bonus(accumulated, thresholds, rates):
    for i, v in enumerate(thresholds):
        if accumulated < v:
            return rates[i]
    return rates[-1]

def random_by_weights(weight_dict, size=1):
    items = np.array(list(weight_dict.keys()))
    weights = np.array(list(weight_dict.values()), dtype=np.float64)
    weights = weights / np.sum(weights)
    return np.random.choice(items, p=weights, size=size)

def simulate_one_player(global_rate, slot_cost, slot_drop_rate, bonus_thresholds, bonus_rates, drop_count_weight, stamina_limit):
    total_stamina = 0
    acc_stamina = 0
    drop_count = 0
    while total_stamina + slot_cost <= stamina_limit:
        bonus = get_bonus(acc_stamina, bonus_thresholds, bonus_rates)
        p = global_rate * slot_drop_rate * bonus
        if p >= 1:
            block_this = 0
        else:
            block_this = int(np.ceil(np.random.geometric(p) - 1))
        next_use = (block_this + 1) * slot_cost
        if total_stamina + next_use > stamina_limit:
            break
        total_stamina += next_use
        acc_stamina += next_use
        c = random_by_weights(drop_count_weight)
        drop_count += c
        acc_stamina = 0  # bonus累计清零
    if drop_count > 0:
        return total_stamina / drop_count
    else:
        return np.nan

def simulate_slot_limited_fast(global_rate, slot_cost, slot_drop_rate, bonus_thresholds, bonus_rates, drop_count_weight, stamina_limit=10000, player_count=10000):
    arr = np.empty(player_count)
    for i in range(player_count):
        arr[i] = simulate_one_player(global_rate, slot_cost, slot_drop_rate, bonus_thresholds, bonus_rates, drop_count_weight, stamina_limit)
    mask = ~np.isnan(arr)
    mean = np.nanmean(arr)
    non_drop_ratio = np.isnan(arr).sum() / player_count
    if mask.sum() > 0:
        max_v = np.nanmax(arr)
        min_v = np.nanmin(arr)
        median_v = np.nanmedian(arr)
    else:
        max_v = min_v = median_v = np.nan
    return mean, max_v, min_v, median_v, non_drop_ratio

# 配置
global_rate = 1.5
slot_costs = [1,3,10,20,30,50,100,150,200,300,500,1000,2000]
slot_drop_rates = [0.0066,0.02,0.0667,0.1333,0.1818,0.2778,0.4762,0.6667,0.7,1,1,1,1]
bonus_thresholds = [50,100,300,500,800,1000]
bonus_rates = [1,1,1,1,1,1]
drop_counts_weights = [{1:1,2:0,3:0},{1:1,2:0,3:0},{1:1,2:0,3:0},{1:1,2:0,3:0},{1:0.9,2:0.1,3:0},{1:0.8,2:0.2,3:0},{1:0.7,2:0.2,3:0.1},{1:0.6,2:0.3,3:0.1},{1:0.3,2:0.5,3:0.2},{1:0.2,2:0.6,3:0.2},{1:0,2:0.6,3:0.4},{1:0,2:0.9,3:0.1},{1:0,2:0.1,3:0.9}]



stamina_limit = 10000
player_count = 10000

for i, (cost, rate, cnt_weight) in enumerate(zip(slot_costs, slot_drop_rates, drop_counts_weights), start=1):
    mean, maxval, minval, medianval, non_drop_ratio = simulate_slot_limited_fast(
        global_rate, cost, rate, bonus_thresholds, bonus_rates, cnt_weight,
        stamina_limit, player_count
    )
    print(f"档位{i}: 每{cost}体力消耗, 玩家平均消耗 {mean:.2f} 体力获得一个掉落,"
          f" 最大值 {maxval:.2f}, 最小值 {minval:.2f}, 中位值 {medianval:.2f}, 未掉过比例 {non_drop_ratio:.1%}")
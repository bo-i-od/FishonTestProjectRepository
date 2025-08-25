import random

class DropSimulator:
    def __init__(self, global_rate, slot_costs, slot_drop_rates, bonus_thresholds,
                 bonus_rates, drop_counts_weights, slot_target_fish_rates):
        self.global_rate = global_rate
        self.slot_costs = slot_costs
        self.slot_drop_rates = slot_drop_rates
        self.bonus_thresholds = bonus_thresholds
        self.bonus_rates = bonus_rates
        self.drop_counts_weights = drop_counts_weights
        self.slot_target_fish_rates = slot_target_fish_rates

        assert len(slot_costs) == len(slot_drop_rates) == len(drop_counts_weights) == len(slot_target_fish_rates), "各档参数数量需一致"
        assert len(bonus_thresholds) == len(bonus_rates), "加成参数数量需一致"

    def get_bonus_rate(self, stamina):
        bonus = 1.0
        for thresh, rate in zip(self.bonus_thresholds, self.bonus_rates):
            if stamina >= thresh:
                bonus = rate
        return bonus

    def get_drop_count(self, slot_index):
        weight_dict = self.drop_counts_weights[slot_index]
        counts = []
        weights = []
        for k, v in weight_dict.items():
            if v > 0:
                counts.append(k)
                weights.append(v)
        total = sum(weights)
        if total == 0:
            return 1
        weights = [w / total for w in weights]
        rnd = random.random()
        s = 0
        for c, w in zip(counts, weights):
            s += w
            if rnd <= s:
                return c
        return counts[-1]

    def calc_avg(self, lst):
        return sum(lst) / len(lst) if lst else 0

    def calc_median(self, lst):
        lst = sorted(lst)
        n = len(lst)
        if n == 0:
            return 0
        if n % 2 == 1:
            return lst[n // 2]
        else:
            return (lst[n // 2 - 1] + lst[n // 2]) / 2

    def simulate_one_player(self, slot_index, total_energy):
        stamina_counter = 0
        used_energy = 0
        slot_cost = self.slot_costs[slot_index]
        base_drop_rate = self.slot_drop_rates[slot_index]
        target_fish_rate = self.slot_target_fish_rates[slot_index]
        drop_costs = []

        while used_energy + slot_cost <= total_energy:
            used_energy += slot_cost
            stamina_counter += slot_cost

            # 钓到目标鱼判定
            if random.random() > target_fish_rate:
                continue

            # 掉落判定
            bonus = self.get_bonus_rate(stamina_counter)
            real_drop_rate = base_drop_rate * self.global_rate * bonus
            if random.random() < real_drop_rate:
                drops = self.get_drop_count(slot_index)
                avg_per_drop = stamina_counter / drops
                drop_costs.extend([avg_per_drop] * drops)
                stamina_counter = 0

        return drop_costs

    def simulate_slot(self, slot_index, num_players, total_energy):
        all_drop_costs = []
        total_energy_used = num_players * total_energy
        for _ in range(num_players):
            costs = self.simulate_one_player(slot_index, total_energy)
            all_drop_costs.extend(costs)
        total_drops = len(all_drop_costs)

        # 原方式：只统计产生掉落的平均消耗
        avg = sum(all_drop_costs) / total_drops if total_drops else 0

        # 新方式：包含未出掉落玩家的总体力分摊平均体力
        avg_by_all = total_energy_used / total_drops if total_drops else 0

        if all_drop_costs:
            mn = min(all_drop_costs)
            mx = max(all_drop_costs)
            md = self.calc_median(all_drop_costs)
            drops = total_drops
        else:
            mn = mx = md = drops = 0
        return {
            "average": avg,         # 只统计有掉落体力分摊
            "avg_by_all": avg_by_all, # 所有体力分摊到掉落数
            "min": mn,
            "max": mx,
            "median": md,
            "drops": drops
        }

def main():
    global_rate = 1.25
    slot_costs = [1, 3, 10, 20, 30, 50, 100, 150, 200, 300, 500, 1000, 2000]
    slot_drop_rates = [0.002, 0.006, 0.02, 0.038, 0.06, 0.095, 0.19, 0.29, 0.4, 0.6, 1, 1, 1]
    slot_target_fish_rates = [0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145]
    bonus_thresholds = [300, 600, 3000, 6000, 9000, 10000]
    bonus_rates = [1, 1, 1.5, 6, 30, 500]
    drop_counts_weights = [{1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0},
                           {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0},
                           {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0.5, 3: 0.5},
                           {1: 0, 2: 0.1, 3: 0.9}]
    player_total_energy = 10000
    num_players = 1000
    sim = DropSimulator(global_rate, slot_costs, slot_drop_rates, bonus_thresholds,
                       bonus_rates, drop_counts_weights, slot_target_fish_rates)

    print(f"{'档位':<4}{'体力':<8}{'掉落率':<10}{'目标鱼率':<10}{'样本':<6}{'掉落数':<8}{'有掉落均':<12}{'总均':<12}{'中位数':<10}{'最小':<8}{'最大':<8}")
    print('='*105)
    for i in range(13):
        res = sim.simulate_slot(i, num_players, player_total_energy)
        print(f"{i+1:<4}{slot_costs[i]:<8}{slot_drop_rates[i]:<10.3f}{slot_target_fish_rates[i]:<10.2f}"
              f"{num_players:<6}{res['drops']:<8}{res['average']:<12.2f}{res['avg_by_all']:<12.2f}"
              f"{res['median']:<10.2f}{res['min']:<8.2f}{res['max']:<8.2f}")

if __name__ == "__main__":
    main()
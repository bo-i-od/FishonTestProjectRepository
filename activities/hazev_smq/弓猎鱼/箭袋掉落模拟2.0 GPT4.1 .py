import random
from collections import defaultdict


class DropSimulator:
    def __init__(self, global_rate, slot_costs, slot_drop_rates,
                 bonus_thresholds, bonus_rates, drop_counts_weights):
        self.global_rate = global_rate
        self.slot_costs = slot_costs
        self.slot_drop_rates = slot_drop_rates
        self.bonus_thresholds = bonus_thresholds
        self.bonus_rates = bonus_rates
        self.drop_counts_weights = drop_counts_weights

        # 验证参数
        assert len(slot_costs) == len(slot_drop_rates) == len(drop_counts_weights), "档位数据长度不匹配"
        assert len(bonus_thresholds) == len(bonus_rates), "体力累积加成数据长度不匹配"

    def get_bonus_rate(self, accumulated_stamina):
        """根据累积体力获取加成倍率"""
        bonus = 1.0
        for i, threshold in enumerate(self.bonus_thresholds):
            if accumulated_stamina >= threshold:
                bonus = self.bonus_rates[i]
            else:
                break
        return bonus

    def get_drop_count(self, slot_index):
        """根据档位和权重随机获取掉落数量"""
        weights = self.drop_counts_weights[slot_index]
        counts = list(weights.keys())
        probs = list(weights.values())

        # 归一化概率
        total_prob = sum(probs)
        if total_prob > 0:
            probs = [p / total_prob for p in probs]
            # 手动实现random.choices的功能以提高兼容性
            rand_val = random.random()
            cumulative_prob = 0
            for i, prob in enumerate(probs):
                cumulative_prob += prob
                if rand_val <= cumulative_prob:
                    return counts[i]
        return 1

    def calculate_mean(self, data):
        """计算平均值"""
        return sum(data) / len(data) if data else 0

    def calculate_median(self, data):
        """计算中位数"""
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def simulate_single_player(self, slot_index, total_energy):
        """模拟单个玩家在指定档位消耗总体力的掉落情况"""
        accumulated_stamina = 0  # 累积体力（用于计算加成）
        consumed_stamina = 0  # 已消耗的总体力
        slot_cost = self.slot_costs[slot_index]
        base_drop_rate = self.slot_drop_rates[slot_index]

        drop_results = []  # 记录每次掉落时消耗的体力

        while consumed_stamina < total_energy:
            # 检查是否还有足够体力进行一次操作
            if consumed_stamina + slot_cost > total_energy:
                break

            # 消耗体力
            accumulated_stamina += slot_cost
            consumed_stamina += slot_cost

            # 计算当前掉落率
            bonus_rate = self.get_bonus_rate(accumulated_stamina)
            current_drop_rate = min(1.0, base_drop_rate * self.global_rate * bonus_rate)

            # 判断是否掉落
            if random.random() < current_drop_rate:
                # 获得掉落
                drop_count = self.get_drop_count(slot_index)
                # 记录每个掉落所需的平均体力
                cost_per_drop = accumulated_stamina / drop_count
                for _ in range(drop_count):
                    drop_results.append(cost_per_drop)

                # 重置累积体力
                accumulated_stamina = 0

        return drop_results, consumed_stamina

    def simulate_players(self, slot_index, num_players, total_energy_per_player):
        """模拟多个玩家在指定档位的掉落情况"""
        all_drop_costs = []  # 所有玩家获得每个掉落的体力消耗
        total_drops = 0
        total_energy_consumed = 0

        for player_id in range(num_players):
            drop_costs, energy_consumed = self.simulate_single_player(slot_index, total_energy_per_player)
            all_drop_costs.extend(drop_costs)
            total_drops += len(drop_costs)
            total_energy_consumed += energy_consumed

            # 进度提示
            if (player_id + 1) % (num_players // 10) == 0:
                progress = (player_id + 1) / num_players * 100
                print(f"  进度: {progress:.0f}%")

        if not all_drop_costs:
            return {
                'slot_index': slot_index,
                'slot_cost': self.slot_costs[slot_index],
                'base_drop_rate': self.slot_drop_rates[slot_index],
                'total_drops': 0,
                'average_cost_per_drop': 0,
                'minimum': 0,
                'maximum': 0,
                'median': 0,
                'total_energy_consumed': total_energy_consumed,
                'drop_rate_actual': 0
            }

        # 计算实际掉落率
        actual_drop_rate = total_drops / (
                    total_energy_consumed / self.slot_costs[slot_index]) if total_energy_consumed > 0 else 0

        return {
            'slot_index': slot_index,
            'slot_cost': self.slot_costs[slot_index],
            'base_drop_rate': self.slot_drop_rates[slot_index],
            'total_drops': total_drops,
            'average_cost_per_drop': self.calculate_mean(all_drop_costs),
            'minimum': min(all_drop_costs),
            'maximum': max(all_drop_costs),
            'median': self.calculate_median(all_drop_costs),
            'total_energy_consumed': total_energy_consumed,
            'drop_rate_actual': actual_drop_rate
        }

    def run_full_simulation(self, num_players, total_energy_per_player):
        """运行完整的模拟，测试所有档位"""
        print("=" * 90)
        print("掉落机制模拟结果")
        print("=" * 90)
        print(f"全局倍率: {self.global_rate}")
        print(f"模拟玩家数: {num_players}")
        print(f"每个玩家总体力: {total_energy_per_player}")
        print("=" * 90)

        all_results = []

        for slot_index in range(len(self.slot_costs)):
            print(
                f"\n正在模拟档位 {slot_index + 1} (体力消耗: {self.slot_costs[slot_index]}, 基础掉落率: {self.slot_drop_rates[slot_index]:.4f})...")

            result = self.simulate_players(slot_index, num_players, total_energy_per_player)
            all_results.append(result)

            print(f"档位 {slot_index + 1} 结果:")
            print(f"  总掉落数: {result['total_drops']}")
            print(f"  获得一个掉落的平均体力消耗: {result['average_cost_per_drop']:.2f}")
            print(f"  最小值: {result['minimum']:.2f}")
            print(f"  最大值: {result['maximum']:.2f}")
            print(f"  中位数: {result['median']:.2f}")
            print(f"  实际掉落率: {result['drop_rate_actual']:.4f}")

        return all_results

    def print_configuration(self):
        """打印当前配置"""
        print("当前配置:")
        print(f"全局倍率: {self.global_rate}")
        print(f"档位体力消耗: {self.slot_costs}")
        print(f"档位掉落率: {self.slot_drop_rates}")
        print(f"累积体力阈值: {self.bonus_thresholds}")
        print(f"对应加成倍率: {self.bonus_rates}")
        print("掉落数量权重:")
        for i, weights in enumerate(self.drop_counts_weights):
            print(f"  档位{i + 1}: {weights}")
        print()


def main():
    # 配置参数
    global_rate = 1
    slot_costs = [1, 3, 10, 20, 30, 50, 100, 150, 200, 300, 500, 1000, 2000]
    slot_drop_rates = [0.0003, 0.001, 0.0033, 0.0067, 0.01, 0.0167, 0.0333, 0.05, 0.0667, 0.1, 0.1667, 0.3333, 0.6667]
    bonus_thresholds = [150, 300, 600, 1100, 2100, 4000]
    bonus_rates = [1, 1, 1, 1.8, 15, 200]
    drop_counts_weights = [{1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0},
                           {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0},
                           {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0}, {1: 1, 2: 0, 3: 0},
                           {1: 1, 2: 0, 3: 0}]
    player_total_energy = 10000
    num_players = 1000



    # 创建模拟器
    simulator = DropSimulator(
        global_rate, slot_costs, slot_drop_rates,
        bonus_thresholds, bonus_rates, drop_counts_weights
    )

    # 打印配置
    simulator.print_configuration()

    # 运行模拟
    results = simulator.run_full_simulation(num_players, player_total_energy)

    # 汇总结果表格
    print("\n" + "=" * 120)
    print("汇总结果表格")
    print("=" * 120)
    print(
        f"{'档位':<4} {'体力消耗':<8} {'基础掉落率':<12} {'实际掉落率':<12} {'总掉落数':<10} {'平均体力':<10} {'最小值':<8} {'最大值':<8} {'中位数':<8}")
    print("-" * 120)

    for result in results:
        print(f"{result['slot_index'] + 1:<4} "
              f"{result['slot_cost']:<8} "
              f"{result['base_drop_rate']:<12.4f} "
              f"{result['drop_rate_actual']:<12.4f} "
              f"{result['total_drops']:<10} "
              f"{result['average_cost_per_drop']:<10.2f} "
              f"{result['minimum']:<8.2f} "
              f"{result['maximum']:<8.2f} "
              f"{result['median']:<8.2f}")

    # 效率分析
    print("\n" + "=" * 90)
    print("效率分析 (获得一个掉落所需平均体力)")
    print("=" * 90)

    # 找出效率最高的档位
    valid_results = [r for r in results if r['total_drops'] > 0]
    if valid_results:
        best_efficiency = min(valid_results, key=lambda x: x['average_cost_per_drop'])
        print(f"最高效率档位: 档位{best_efficiency['slot_index'] + 1} "
              f"(平均{best_efficiency['average_cost_per_drop']:.2f}体力/掉落)")

        worst_efficiency = max(valid_results, key=lambda x: x['average_cost_per_drop'])
        print(f"最低效率档位: 档位{worst_efficiency['slot_index'] + 1} "
              f"(平均{worst_efficiency['average_cost_per_drop']:.2f}体力/掉落)")


if __name__ == "__main__":
    main()
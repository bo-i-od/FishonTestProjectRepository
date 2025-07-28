import random
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

"""
AI 提示词
初始有10w名玩家在初始段位，每一个周期会进行一次升降段，大约有个段位，每个段位前x名晋级，后y名降级，请给出python程序，模拟若干周期后各段位人数比例
"""


# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
class RankingSystem:
    def __init__(self, initial_players=100000, num_ranks=9,
                 promote_ratio=0.15, demote_ratio=0.15):
        """
        初始化排位系统

        Args:
            initial_players: 初始玩家数量
            num_ranks: 段位数量 (0是最低段位，num_ranks-1是最高段位)
            promote_ratio: 晋级比例 (前x%晋级)
            demote_ratio: 降级比例 (后y%降级)
        """
        self.num_ranks = num_ranks
        self.promote_ratio = promote_ratio
        self.demote_ratio = demote_ratio

        # 初始化所有玩家都在最低段位(段位0)
        self.players_per_rank = [0] * num_ranks
        self.players_per_rank[0] = initial_players

        self.total_players = initial_players
        self.history = []  # 记录每个周期的人数分布

    def simulate_one_cycle(self):
        """模拟一个升降段周期"""
        new_distribution = [0] * self.num_ranks

        for rank in range(self.num_ranks):
            current_players = self.players_per_rank[rank]

            if current_players == 0:
                continue

            # 计算晋级、降级、留级人数
            if rank < self.num_ranks - 1:  # 不是最高段位
                promote_count = int(current_players * self.promote_ratio)
            else:  # 最高段位无法晋级
                promote_count = 0

            if rank > 0:  # 不是最低段位
                demote_count = int(current_players * self.demote_ratio)
            else:  # 最低段位无法降级
                demote_count = 0

            stay_count = current_players - promote_count - demote_count

            # 分配到新的段位
            if promote_count > 0:
                new_distribution[rank + 1] += promote_count
            if demote_count > 0:
                new_distribution[rank - 1] += demote_count
            new_distribution[rank] += stay_count

        self.players_per_rank = new_distribution
        self.history.append(self.players_per_rank.copy())

    def get_distribution_percentages(self):
        """获取当前各段位人数百分比"""
        return [count / self.total_players * 100 for count in self.players_per_rank]

    def simulate_multiple_cycles(self, cycles):
        """模拟多个周期"""
        print("开始模拟...")
        print(f"初始状态: {self.get_distribution_percentages()}")

        for cycle in range(cycles):
            self.simulate_one_cycle()
            if (cycle + 1) % 10 == 0 or cycle < 10:
                percentages = self.get_distribution_percentages()
                print(f"第{cycle + 1}周期后: {[f'{p:.1f}%' for p in percentages]}")

        return self.history

    def plot_evolution(self):
        """绘制段位分布演化图"""
        if not self.history:
            print("没有历史数据可绘制")
            return

        cycles = range(len(self.history))

        plt.figure(figsize=(12, 8))

        # 绘制每个段位的人数变化
        for rank in range(self.num_ranks):
            rank_history = [period[rank] / self.total_players * 100
                            for period in self.history]
            plt.plot(cycles, rank_history, label=f'段位 {rank}', marker='o', markersize=3)

        plt.xlabel('周期')
        plt.ylabel('人数百分比 (%)')
        plt.title('各段位人数分布演化')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_final_distribution(self):
        """绘制最终分布饼图"""
        if not self.players_per_rank:
            return

        percentages = self.get_distribution_percentages()
        labels = [f'段位 {i}' for i in range(self.num_ranks)]

        plt.figure(figsize=(10, 8))
        plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('最终段位分布')
        plt.axis('equal')
        plt.show()


# 更真实的排位系统模拟
class RealisticRankingSystem(RankingSystem):
    def __init__(self, initial_players=100000, num_ranks=9):
        """
        更真实的排位系统，不同段位有不同的晋级降级比例
        """
        super().__init__(initial_players, num_ranks)

        # 不同段位的晋级降级比例 (promote_ratio, demote_ratio)
        # 低段位更容易晋级，高段位更容易降级
        self.rank_rules = {
            0: (0.6, 0),  # 青铜：25%晋级，10%降级
            1: (0.6, 0.10),  # 白银：20%晋级，15%降级
            2: (0.5, 0.20),  # 黄金：18%晋级，18%降级
            3: (0.4, 0.25),  # 铂金：15%晋级，20%降级
            4: (0.35, 0.30),  # 钻石：12%晋级，22%降级
            5: (0.25, 0.35),  # 大师：10%晋级，25%降级
            6: (0.15, 0.4),  # 宗师：8%晋级，27%降级
            7: (0.10, 0.30),  # 王者：6%晋级，30%降级
            8: (0.00, 0.20),  # 传说：0%晋级，40%降级
        }

    def simulate_one_cycle(self):
        """使用真实的晋级降级规则模拟一个周期"""
        new_distribution = [0] * self.num_ranks

        for rank in range(self.num_ranks):
            current_players = self.players_per_rank[rank]

            if current_players == 0:
                continue

            promote_ratio, demote_ratio = self.rank_rules.get(rank)

            # 计算晋级、降级、留级人数
            if rank < self.num_ranks - 1:  # 不是最高段位
                promote_count = int(current_players * promote_ratio)
            else:  # 最高段位无法晋级
                promote_count = 0

            if rank > 0:  # 不是最低段位
                demote_count = int(current_players * demote_ratio)
            else:  # 最低段位无法降级
                demote_count = 0

            stay_count = current_players - promote_count - demote_count

            # 分配到新的段位
            if promote_count > 0:
                new_distribution[rank + 1] += promote_count
            if demote_count > 0:
                new_distribution[rank - 1] += demote_count
            new_distribution[rank] += stay_count

        self.players_per_rank = new_distribution
        self.history.append(self.players_per_rank.copy())


def main():
    print("=== 真实排位系统模拟 ===")

    # 创建真实排位系统
    realistic_system = RealisticRankingSystem(
        initial_players=100000,
        num_ranks=9
    )

    # 模拟100个周期
    realistic_system.simulate_multiple_cycles(100)

    print("\n最终分布:")
    rank_names = ['青铜', '白银', '黄金', '铂金', '钻石',
                  '大师', '宗师', '王者', '传说']

    final_percentages = realistic_system.get_distribution_percentages()
    for i, percentage in enumerate(final_percentages):
        print(f"{rank_names[i]}: {percentage:.2f}%")

    # 绘制图表
    realistic_system.plot_evolution()
    realistic_system.plot_final_distribution()


if __name__ == "__main__":
    main()
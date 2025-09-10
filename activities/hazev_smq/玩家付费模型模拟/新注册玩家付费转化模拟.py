import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from dataclasses import dataclass
from typing import Dict, List
import warnings

# 忽略字体警告
warnings.filterwarnings('ignore', category=UserWarning)

# 设置matplotlib参数
plt.rcParams['font.family'] = ['DejaVu Sans', 'Arial', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False


@dataclass
class PlayerTier:
    """玩家档位配置"""
    name: str
    daily_spending_range: tuple  # 日付费额度范围 (最小值, 最大值)
    upgrade_tendency: float  # 升档倾向系数 (0-1)
    downgrade_tendency: float  # 掉档倾向系数 (0-1)
    rebate_preference: float  # 返利比偏向 (0-1)
    stability: float  # 档位稳定性 (0-1, 越高越不容易变动)


class PaymentSimulator:
    def __init__(self):
        # 定义五种付费档位
        self.tiers = {
            0: PlayerTier("游离R", (0, 10), 0.15, 0.05, 0.8, 0.6),
            1: PlayerTier("小R", (10, 50), 0.12, 0.08, 0.7, 0.65),
            2: PlayerTier("中R", (50, 200), 0.10, 0.10, 0.6, 0.7),
            3: PlayerTier("大R", (200, 1000), 0.08, 0.12, 0.5, 0.75),
            4: PlayerTier("超R", (1000, 5000), 0.02, 0.15, 0.3, 0.8)
        }

        # 初始玩家分布权重 (新注册玩家更可能是低档位)
        self.initial_distribution = [0.5, 0.3, 0.15, 0.04, 0.01]

        self.players = []
        self.daily_stats = []

    def create_player(self, tier_id: int = None) -> Dict:
        """创建新玩家"""
        if tier_id is None:
            tier_id = np.random.choice(5, p=self.initial_distribution)

        tier = self.tiers[tier_id]

        player = {
            'id': len(self.players),
            'tier': tier_id,
            'tier_name': tier.name,
            'days_in_game': 0,
            'total_spending': 0,
            'daily_spending': 0,
            'tier_stability_days': 0,  # 在当前档位的天数
            'loyalty': random.uniform(0.3, 0.9),  # 玩家忠诚度
            'spending_power': random.uniform(0.5, 1.5)  # 消费能力系数
        }

        return player

    def calculate_daily_spending(self, player: Dict) -> float:
        """计算玩家当日消费"""
        tier = self.tiers[player['tier']]
        base_min, base_max = tier.daily_spending_range

        # 考虑玩家消费能力和忠诚度
        min_spend = base_min * player['spending_power'] * player['loyalty']
        max_spend = base_max * player['spending_power'] * player['loyalty']

        # 添加随机波动
        daily_spending = random.uniform(min_spend, max_spend)

        # 考虑游戏天数的影响（新玩家可能消费更多，老玩家可能疲劳）
        if player['days_in_game'] < 7:  # 新手期
            daily_spending *= random.uniform(1.2, 1.8)
        elif player['days_in_game'] > 90:  # 疲劳期
            daily_spending *= random.uniform(0.7, 0.9)

        return max(0, daily_spending)

    def check_tier_change(self, player: Dict) -> int:
        """检查玩家档位变化"""
        current_tier = player['tier']
        tier = self.tiers[current_tier]

        # 稳定性检查：在当前档位时间越长，越不容易变动
        stability_factor = min(1.0, tier.stability + player['tier_stability_days'] * 0.01)

        if random.random() < stability_factor:
            return current_tier  # 保持当前档位

        # 基于最近7天平均消费决定档位变化
        recent_avg_spending = player.get('recent_avg_spending', player['daily_spending'])

        # 升档检查
        if current_tier < 4:  # 不是最高档位
            upper_tier = self.tiers[current_tier + 1]
            if (recent_avg_spending > upper_tier.daily_spending_range[0] * 0.8 and
                    random.random() < tier.upgrade_tendency):
                return current_tier + 1

        # 掉档检查
        if current_tier > 0:  # 不是最低档位
            lower_tier = self.tiers[current_tier - 1]
            if (recent_avg_spending < tier.daily_spending_range[0] * 0.6 and
                    random.random() < tier.downgrade_tendency):
                return current_tier - 1

        return current_tier

    def simulate_day(self, day: int):
        """模拟一天的游戏情况"""
        daily_revenue = 0
        tier_counts = {i: 0 for i in range(5)}
        tier_revenues = {i: 0 for i in range(5)}

        # 新玩家注册（模拟真实情况，每天有新玩家加入）
        if day < 30:  # 前30天模拟快速增长期
            new_players_count = random.randint(50, 100)
        else:  # 后期稳定期
            new_players_count = random.randint(10, 30)

        for _ in range(new_players_count):
            new_player = self.create_player()
            self.players.append(new_player)

        # 模拟现有玩家行为
        active_players = []
        for player in self.players:
            # 玩家流失检查
            churn_probability = 0.01 + (0.001 * player['days_in_game'])  # 随时间增加流失概率
            if random.random() < churn_probability and player['days_in_game'] > 7:
                continue  # 玩家流失

            player['days_in_game'] += 1

            # 计算当日消费
            daily_spending = self.calculate_daily_spending(player)
            player['daily_spending'] = daily_spending
            player['total_spending'] += daily_spending

            # 计算最近平均消费（用于档位判断）
            if 'spending_history' not in player:
                player['spending_history'] = []
            player['spending_history'].append(daily_spending)
            if len(player['spending_history']) > 7:
                player['spending_history'].pop(0)
            player['recent_avg_spending'] = np.mean(player['spending_history'])

            # 检查档位变化
            new_tier = self.check_tier_change(player)
            if new_tier != player['tier']:
                player['tier'] = new_tier
                player['tier_name'] = self.tiers[new_tier].name
                player['tier_stability_days'] = 0
            else:
                player['tier_stability_days'] += 1

            # 统计
            tier_counts[player['tier']] += 1
            tier_revenues[player['tier']] += daily_spending
            daily_revenue += daily_spending

            active_players.append(player)

        self.players = active_players

        # 记录当日统计
        stats = {
            'day': day,
            'total_players': len(self.players),
            'daily_revenue': daily_revenue,
            'avg_revenue_per_user': daily_revenue / max(1, len(self.players))
        }

        for i in range(5):
            stats[f'{self.tiers[i].name}_count'] = tier_counts[i]
            stats[f'{self.tiers[i].name}_revenue'] = tier_revenues[i]
            stats[f'{self.tiers[i].name}_percentage'] = (tier_counts[i] / max(1, len(self.players))) * 100

        self.daily_stats.append(stats)

    def run_simulation(self, days: int = 90):
        """运行模拟"""
        print(f"开始模拟 {days} 天的付费玩家演化过程...")

        for day in range(1, days + 1):
            self.simulate_day(day)

            if day % 10 == 0:
                print(f"第 {day} 天完成，当前玩家数: {len(self.players)}")

        print("模拟完成！")

    def analyze_results(self):
        """分析模拟结果"""
        df = pd.DataFrame(self.daily_stats)

        # 打印最终统计
        final_stats = df.iloc[-1]
        print("\n=== 最终付费群体分布 ===")
        print(f"总玩家数: {final_stats['total_players']}")
        print(f"日均收入: ${final_stats['daily_revenue']:.2f}")
        print(f"ARPU: ${final_stats['avg_revenue_per_user']:.2f}")

        print("\n各档位分布:")
        total_revenue = 0
        for i in range(5):
            tier_name = self.tiers[i].name
            count = final_stats[f'{tier_name}_count']
            percentage = final_stats[f'{tier_name}_percentage']
            revenue = final_stats[f'{tier_name}_revenue']
            total_revenue += revenue
            print(f"{tier_name}: {count}人 ({percentage:.1f}%), 收入: ${revenue:.2f}")

        print(f"\n收入贡献占比:")
        for i in range(5):
            tier_name = self.tiers[i].name
            revenue = final_stats[f'{tier_name}_revenue']
            revenue_percentage = (revenue / total_revenue * 100) if total_revenue > 0 else 0
            print(f"{tier_name}: {revenue_percentage:.1f}%")

        return df

    def plot_results(self, df: pd.DataFrame):
        """绘制结果图表"""
        # 创建图表
        fig = plt.figure(figsize=(16, 12))

        # 定义颜色
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']

        # 1. 玩家数量变化
        ax1 = plt.subplot(2, 3, 1)
        plt.plot(df['day'], df['total_players'], 'b-', linewidth=2)
        plt.title('Total Players Over Time', fontsize=12, fontweight='bold')
        plt.xlabel('Days')
        plt.ylabel('Player Count')
        plt.grid(True, alpha=0.3)

        # 2. 日收入变化
        ax2 = plt.subplot(2, 3, 2)
        plt.plot(df['day'], df['daily_revenue'], 'g-', linewidth=2)
        plt.title('Daily Revenue Over Time', fontsize=12, fontweight='bold')
        plt.xlabel('Days')
        plt.ylabel('Revenue ($)')
        plt.grid(True, alpha=0.3)

        # 3. ARPU变化
        ax3 = plt.subplot(2, 3, 3)
        plt.plot(df['day'], df['avg_revenue_per_user'], 'r-', linewidth=2)
        plt.title('ARPU Over Time', fontsize=12, fontweight='bold')
        plt.xlabel('Days')
        plt.ylabel('ARPU ($)')
        plt.grid(True, alpha=0.3)

        # 4. 各档位玩家数量变化
        ax4 = plt.subplot(2, 3, 4)
        for i in range(5):
            tier_name = self.tiers[i].name
            plt.plot(df['day'], df[f'{tier_name}_count'],
                     label=tier_name, color=colors[i], linewidth=2)
        plt.title('Player Count by Tier', fontsize=12, fontweight='bold')
        plt.xlabel('Days')
        plt.ylabel('Player Count')
        plt.legend()
        plt.grid(True, alpha=0.3)

        # 5. 各档位收入变化
        ax5 = plt.subplot(2, 3, 5)
        for i in range(5):
            tier_name = self.tiers[i].name
            plt.plot(df['day'], df[f'{tier_name}_revenue'],
                     label=tier_name, color=colors[i], linewidth=2)
        plt.title('Revenue by Tier', fontsize=12, fontweight='bold')
        plt.xlabel('Days')
        plt.ylabel('Revenue ($)')
        plt.legend()
        plt.grid(True, alpha=0.3)

        # 6. 各档位百分比变化
        ax6 = plt.subplot(2, 3, 6)
        for i in range(5):
            tier_name = self.tiers[i].name
            plt.plot(df['day'], df[f'{tier_name}_percentage'],
                     label=tier_name, color=colors[i], linewidth=2)
        plt.title('Player Percentage by Tier', fontsize=12, fontweight='bold')
        plt.xlabel('Days')
        plt.ylabel('Percentage (%)')
        plt.legend()
        plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # 最终分布饼图
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        final_stats = df.iloc[-1]

        # 玩家数量分布
        player_counts = [final_stats[f'{self.tiers[i].name}_count'] for i in range(5)]
        labels = [self.tiers[i].name for i in range(5)]

        wedges1, texts1, autotexts1 = ax1.pie(player_counts, labels=labels, autopct='%1.1f%%',
                                              colors=colors, startangle=90)
        ax1.set_title('Final Player Distribution', fontsize=14, fontweight='bold')

        # 收入分布
        revenues = [final_stats[f'{self.tiers[i].name}_revenue'] for i in range(5)]
        wedges2, texts2, autotexts2 = ax2.pie(revenues, labels=labels, autopct='%1.1f%%',
                                              colors=colors, startangle=90)
        ax2.set_title('Final Revenue Distribution', fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.show()

    def export_detailed_analysis(self, df: pd.DataFrame):
        """导出详细分析报告"""
        print("\n=== 详细分析报告 ===")

        # 计算关键指标
        final_day = df.iloc[-1]
        initial_day = df.iloc[0] if len(df) > 1 else final_day

        print(f"\n📊 总体指标:")
        print(f"模拟天数: {len(df)} 天")
        print(f"最终玩家数: {final_day['total_players']}")
        print(f"最终日收入: ${final_day['daily_revenue']:.2f}")
        print(f"最终ARPU: ${final_day['avg_revenue_per_user']:.2f}")

        # 计算增长率
        if len(df) > 1:
            revenue_growth = ((final_day['daily_revenue'] - initial_day['daily_revenue']) /
                              max(initial_day['daily_revenue'], 1)) * 100
            player_growth = ((final_day['total_players'] - initial_day['total_players']) /
                             max(initial_day['total_players'], 1)) * 100

            print(f"收入增长率: {revenue_growth:.1f}%")
            print(f"玩家增长率: {player_growth:.1f}%")

        print(f"\n💰 各档位详细分析:")
        total_revenue = final_day['daily_revenue']
        total_players = final_day['total_players']

        for i in range(5):
            tier_name = self.tiers[i].name
            count = final_day[f'{tier_name}_count']
            revenue = final_day[f'{tier_name}_revenue']

            player_percentage = (count / total_players * 100) if total_players > 0 else 0
            revenue_percentage = (revenue / total_revenue * 100) if total_revenue > 0 else 0
            arpu = revenue / count if count > 0 else 0

            print(f"\n{tier_name}:")
            print(f"  玩家数: {count} ({player_percentage:.1f}%)")
            print(f"  收入: ${revenue:.2f} ({revenue_percentage:.1f}%)")
            print(f"  ARPU: ${arpu:.2f}")

        # 计算档位转化分析
        self.analyze_tier_transitions(df)

    def analyze_tier_transitions(self, df: pd.DataFrame):
        """分析档位转化趋势"""
        print(f"\n📈 档位转化趋势分析:")

        if len(df) < 30:
            print("数据不足，无法分析转化趋势")
            return

        # 比较前30天和后30天的档位分布
        early_period = df.head(30).mean()
        late_period = df.tail(30).mean()

        print("\n前期 vs 后期档位分布变化:")
        for i in range(5):
            tier_name = self.tiers[i].name
            early_pct = early_period[f'{tier_name}_percentage']
            late_pct = late_period[f'{tier_name}_percentage']
            change = late_pct - early_pct

            trend = "↑" if change > 1 else "↓" if change < -1 else "→"
            print(f"{tier_name}: {early_pct:.1f}% → {late_pct:.1f}% ({change:+.1f}%) {trend}")

    def save_player_details(self):
        """保存玩家详细信息"""
        player_data = []
        for player in self.players:
            player_info = {
                'player_id': player['id'],
                'current_tier': player['tier_name'],
                'days_in_game': player['days_in_game'],
                'total_spending': player['total_spending'],
                'recent_avg_spending': player.get('recent_avg_spending', 0),
                'loyalty': player['loyalty'],
                'spending_power': player['spending_power'],
                'tier_stability_days': player['tier_stability_days']
            }
            player_data.append(player_info)

        player_df = pd.DataFrame(player_data)
        player_df.to_csv('player_details.csv', index=False, encoding='utf-8-sig')
        print("📋 玩家详细信息已保存到 player_details.csv")


# 使用示例
def main():
    try:
        # 创建模拟器
        simulator = PaymentSimulator()

        # 运行90天模拟
        simulator.run_simulation(days=90)

        # 分析结果
        df = simulator.analyze_results()

        # 绘制图表
        simulator.plot_results(df)

        # 导出详细分析
        simulator.export_detailed_analysis(df)

        # 保存数据
        df.to_csv('payment_simulation_results.csv', index=False, encoding='utf-8-sig')
        simulator.save_player_details()

        print("\n💾 所有数据已保存完成")

    except Exception as e:
        print(f"程序运行出错: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
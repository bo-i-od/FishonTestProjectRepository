import random
import json
from datetime import datetime, timedelta
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional


class PlayerType(Enum):
    NEW_PLAYER = "新手玩家"
    CASUAL = "休闲玩家"
    ACTIVE = "活跃玩家"
    VIP = "VIP玩家"
    WHALE = "大R玩家"


class PackageType(Enum):
    STARTER = "新手礼包"
    DAILY = "每日礼包"
    WEEKLY = "周礼包"
    MONTHLY = "月礼包"
    SPECIAL = "特殊礼包"
    HOLIDAY = "节日礼包"


@dataclass
class Player:
    id: str
    name: str
    level: int
    total_spending: float
    last_login: datetime
    registration_date: datetime
    player_type: PlayerType
    purchase_history: List[str]


@dataclass
class Package:
    id: str
    name: str
    package_type: PackageType
    base_price: float
    discount_rate: float
    content_description: str
    target_player_types: List[PlayerType]


class PricingStrategy:
    """定价策略基类"""

    def calculate_price(self, package: Package, player: Player) -> Dict:
        raise NotImplementedError


class PersonalizedPricingStrategy(PricingStrategy):
    """个性化定价策略"""

    def calculate_price(self, package: Package, player: Player) -> Dict:
        base_price = package.base_price
        final_price = base_price
        discount_reasons = []

        # 根据玩家类型调整价格
        if player.player_type == PlayerType.NEW_PLAYER:
            final_price *= 0.5  # 新手5折
            discount_reasons.append("新手特惠")
        elif player.player_type == PlayerType.CASUAL:
            final_price *= 0.8  # 休闲玩家8折
            discount_reasons.append("休闲玩家优惠")
        elif player.player_type == PlayerType.WHALE:
            final_price *= 1.2  # 大R玩家价格上浮

        # 根据消费历史调整
        if player.total_spending < 100:
            final_price *= 0.9
            discount_reasons.append("首购优惠")
        elif player.total_spending > 1000:
            final_price *= 1.1

        # 根据活跃度调整
        days_since_login = (datetime.now() - player.last_login).days
        if days_since_login > 7:
            final_price *= 0.7  # 回归玩家优惠
            discount_reasons.append("回归玩家特惠")
        elif days_since_login > 3:
            final_price *= 0.85
            discount_reasons.append("限时优惠")

        # 应用包自带的折扣
        final_price *= (1 - package.discount_rate)
        if package.discount_rate > 0:
            discount_reasons.append(f"礼包特惠{int(package.discount_rate * 100)}%")

        return {
            "original_price": base_price,
            "final_price": round(final_price, 2),
            "discount_amount": round(base_price - final_price, 2),
            "discount_rate": round((base_price - final_price) / base_price * 100, 1),
            "discount_reasons": discount_reasons
        }


class ABTestPricingStrategy(PricingStrategy):
    """A/B测试定价策略"""

    def __init__(self):
        # 预设几个测试价格档位
        self.test_groups = {
            'A': 1.0,  # 原价
            'B': 0.9,  # 9折
            'C': 0.8,  # 8折
            'D': 0.7,  # 7折
        }

    def calculate_price(self, package: Package, player: Player) -> Dict:
        # 根据玩家ID分配测试组
        group = chr(65 + (hash(player.id) % 4))  # A-D
        multiplier = self.test_groups[group]

        base_price = package.base_price
        final_price = base_price * multiplier

        return {
            "original_price": base_price,
            "final_price": round(final_price, 2),
            "test_group": group,
            "discount_amount": round(base_price - final_price, 2),
            "discount_rate": round((1 - multiplier) * 100, 1) if multiplier < 1 else 0,
            "discount_reasons": [f"测试组{group}定价"] if multiplier < 1 else []
        }


class PackagePushSystem:
    """礼包推送系统"""

    def __init__(self, pricing_strategy: PricingStrategy):
        self.pricing_strategy = pricing_strategy
        self.packages = self._init_packages()

    def _init_packages(self) -> List[Package]:
        """初始化礼包数据"""
        return [
            Package("PKG001", "新手大礼包", PackageType.STARTER, 98.0, 0.3,
                    "包含高级装备、金币、经验药水", [PlayerType.NEW_PLAYER]),
            Package("PKG002", "每日特惠", PackageType.DAILY, 18.0, 0.1,
                    "每日限购，包含必需资源", [PlayerType.CASUAL, PlayerType.ACTIVE]),
            Package("PKG003", "VIP专享礼包", PackageType.MONTHLY, 298.0, 0.2,
                    "稀有道具、专属称号、额外特权", [PlayerType.VIP, PlayerType.WHALE]),
            Package("PKG004", "周末狂欢", PackageType.WEEKLY, 68.0, 0.25,
                    "双倍经验、限定皮肤、游戏币", [PlayerType.ACTIVE, PlayerType.VIP]),
            Package("PKG005", "节日庆典", PackageType.HOLIDAY, 128.0, 0.4,
                    "节日限定内容、纪念道具", [PlayerType.ACTIVE, PlayerType.VIP, PlayerType.WHALE])
        ]

    def get_recommended_packages(self, player: Player, max_count: int = 3) -> List[Package]:
        """为玩家推荐适合的礼包"""
        suitable_packages = []

        for package in self.packages:
            if player.player_type in package.target_player_types:
                suitable_packages.append(package)

        # 如果没有特定推荐，则推荐通用礼包
        if not suitable_packages:
            suitable_packages = [pkg for pkg in self.packages
                                 if pkg.package_type in [PackageType.DAILY, PackageType.WEEKLY]]

        return suitable_packages[:max_count]

    def generate_push_offer(self, player: Player) -> Dict:
        """生成推送报价"""
        recommended_packages = self.get_recommended_packages(player)
        offers = []

        for package in recommended_packages:
            pricing_info = self.pricing_strategy.calculate_price(package, player)

            offer = {
                "package_id": package.id,
                "package_name": package.name,
                "package_type": package.package_type.value,
                "content": package.content_description,
                "pricing": pricing_info,
                "valid_until": (datetime.now() + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S"),
                "urgency_level": self._calculate_urgency(player, package)
            }
            offers.append(offer)

        return {
            "player_id": player.id,
            "player_name": player.name,
            "player_type": player.player_type.value,
            "push_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "offers": offers,
            "total_offers": len(offers)
        }

    def _calculate_urgency(self, player: Player, package: Package) -> str:
        """计算紧急程度"""
        if player.player_type == PlayerType.NEW_PLAYER:
            return "高"
        elif package.package_type == PackageType.HOLIDAY:
            return "高"
        elif (datetime.now() - player.last_login).days > 7:
            return "中"
        else:
            return "低"


def create_sample_players() -> List[Player]:
    """创建示例玩家数据"""
    players = [
        Player("P001", "新手小白", 5, 0, datetime.now() - timedelta(days=1),
               datetime.now() - timedelta(days=3), PlayerType.NEW_PLAYER, []),
        Player("P002", "休闲玩家", 25, 150, datetime.now() - timedelta(days=2),
               datetime.now() - timedelta(days=30), PlayerType.CASUAL, ["PKG002"]),
        Player("P003", "活跃玩家", 45, 500, datetime.now() - timedelta(hours=6),
               datetime.now() - timedelta(days=90), PlayerType.ACTIVE, ["PKG002", "PKG004"]),
        Player("P004", "VIP玩家", 60, 1200, datetime.now() - timedelta(hours=12),
               datetime.now() - timedelta(days=180), PlayerType.VIP, ["PKG003", "PKG004"]),
        Player("P005", "大R玩家", 80, 5000, datetime.now() - timedelta(days=8),
               datetime.now() - timedelta(days=365), PlayerType.WHALE, ["PKG003", "PKG005"])
    ]
    return players


def main():
    """主函数 - 演示礼包推送系统"""
    print("🎮 游戏礼包价格推送系统演示 🎮")
    print("=" * 50)

    # 创建示例数据
    players = create_sample_players()

    # 演示个性化定价策略
    print("\n📊 个性化定价策略:")
    print("-" * 30)
    personalized_system = PackagePushSystem(PersonalizedPricingStrategy())

    for player in players:
        push_offer = personalized_system.generate_push_offer(player)
        print(f"\n玩家: {push_offer['player_name']} ({push_offer['player_type']})")

        for offer in push_offer['offers']:
            pricing = offer['pricing']
            print(f"  📦 {offer['package_name']}")
            print(f"     原价: ¥{pricing['original_price']}")
            print(f"     现价: ¥{pricing['final_price']}")
            if pricing['discount_amount'] > 0:
                print(f"     优惠: -{pricing['discount_rate']}% (省¥{pricing['discount_amount']})")
                print(f"     理由: {', '.join(pricing['discount_reasons'])}")
            print(f"     紧急度: {offer['urgency_level']}")

    # 演示A/B测试定价策略
    print("\n\n🧪 A/B测试定价策略:")
    print("-" * 30)
    ab_test_system = PackagePushSystem(ABTestPricingStrategy())

    for player in players[:3]:  # 只显示前3个玩家
        push_offer = ab_test_system.generate_push_offer(player)
        print(f"\n玩家: {push_offer['player_name']}")

        for offer in push_offer['offers']:
            pricing = offer['pricing']
            print(f"  📦 {offer['package_name']}")
            print(f"     测试组: {pricing['test_group']}")
            print(f"     价格: ¥{pricing['final_price']}")
            if pricing['discount_rate'] > 0:
                print(f"     优惠: -{pricing['discount_rate']}%")


if __name__ == "__main__":
    main()
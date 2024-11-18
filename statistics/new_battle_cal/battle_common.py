
class BattleCommon:
    # 张力条总长度
    tension_total_max=10000
    # 张力条到极限，开始松手
    tension_max=9000
    tension_min=8000

    # 初始鱼线位置
    start_line=20
    # 初始张力条位置
    start_tension=4000

    @classmethod
    def cal_tension_atk_rate(cls,tension_now):
        """ 张力伤害计算公式 """
        rate = tension_now / cls.tension_total_max
        if rate > 0.8:
            return 1
        elif rate > 0.6:
            return 0.85
        elif rate > 0.3:
            return 0.55
        else:
            return 0.25
# 配置表路径
file_path="G:/proj/Dev_NewBattle/datapool/ElementData/BaseData/"

# 速度相关
# 鱼跑速
fish_velocityZ=4000
# 收线时的拉力速度
player_velocityZ = 2000
# 放线时的拉力速度
player_no_reel_velocityZ = 0
# ----------------张力相关-------------------
# 详细计算公式见天洋文档
GrowthTensionUnstable = 6000   # 鱼养成张力值
GrowthTensionStable = 2000   # 人养成稳定值

# 直接自定义最终张力相关参数
debug_tension=False
debug_BattleTensionUpSpeed = 10
debug_BattleTensionDownSpeed = -100
# -------------------伤害相关--------------------
player_atk = 100   # 每次收线 每200ms一次伤害

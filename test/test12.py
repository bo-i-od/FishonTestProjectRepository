from common.basePage import BasePage
from scripts import battleTest

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    bp.quick_qte = True
    bp.custom_cmd("setQuickQTE 1")
    bp.custom_cmd(f"setTension 0.9")

    # 0.初始 1.强力收线/强力爆气 2.强力回拉/强力刺鱼 3.技巧拔竿/技巧压制 4.超负荷气 5.长线绝杀 6.不动如山 7.乘胜追击 8.背水一战 9.一刺入魂
    # 力克制 1 4 7, 敏克制 2 5 8, 智克制 3 6 9
    # 90级及以下用 力1 敏2 智3
    # 90级以上用 力7 敏8 智9
    # 非克制情况， 打力鱼用敏，打敏鱼用智，打智鱼用力

    battleTest.circulate_fish(bp)


    bp.connect_close()

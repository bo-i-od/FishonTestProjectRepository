from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from configs.elementsData import ElementsData

def exp_test(bp: BasePage):
    # 得到面板经验值
    exp, lv = HomePanel.get_exp_val(bp)
    print("当前玩家面板经验是：", exp, "点")
    # 跳转到锦标赛
    HomePanel.jump_to(bp, ElementsData.Home.btn_pve)
    # 随机选一个锦标赛
    TournamentsPanel.random_tournament(bp)
    # 点击cast按钮
    BattlePreparePanel.cast(bp)
    # 进行reel in操作
    BattlePanel.reel(bp)
    # 等待结算界面
    ResultPanel.wait_for_result(bp)
    # 进行结算得到分数
    # delta_exp = ResultPanel.get_exp(bp)
    # print("钓鱼获得经验是：", delta_exp, "点")
    # # 当前经验期望结果
    # exp_cal = exp + delta_exp
    # exp_limit = HomePanel.get_exp_limit_val(bp, lv)
    # lv_exp = lv
    # if exp_cal > exp_limit:
    #     exp_cal -= exp_limit
    #     lv_exp += 1
    # print("计算得到玩家经验是：", exp_cal, "点")
    # 返回
    ResultPanel.go_home(bp)
    # 再次得到面板经验值
    exp, lv = HomePanel.get_exp_val(bp)
    print("当前玩家面板经验是：", exp, "点")
    # 钓鱼前后的经验值进行对比得出结果
    # if exp_cal == exp and lv_cal == lv:
    #     print("测试通过")
    # else:
    #     print("测试失败")

if __name__ == '__main__':
    bp = BasePage()
    exp_test(bp)

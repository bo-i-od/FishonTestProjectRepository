import random

from common import gameInit
from common.basePage import BasePage
from common.viewport import Viewport
from panelObjs.careerPanel import CareerPanel
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel


# 检查标题tips
def tips_test(bp:BasePage):
    bp.debug_log("测试页面介绍开始")
    bp.sleep(0.5)
    CareerPanel.click_btn_i(bp)
    bp.sleep(0.5)
    if not CareerPanel.is_tips_active(bp):
        bp.debug_log("error:if not CareerPanel.is_tips_active(bp)")
        return
    bp.sleep(0.5)
    CareerPanel.click_btn_i(bp)
    bp.sleep(0.5)

# 检查天赋tips
def rating_tips_test(bp:BasePage):
    bp.debug_log("测试天赋介绍开始")
    bp.sleep(0.5)
    CareerPanel.click_rating_panel(bp)
    bp.sleep(0.5)
    if not CareerPanel.is_rating_tips_active(bp):
        bp.debug_log("erro:if not CareerPanel.is_rating_tips_active(bp)")
        return
    bp.sleep(0.5)
    if not CareerPanel.compare_rating_total(bp):
        bp.debug_log("erro:if not CareerPanel.compare_rating_total(bp)")
        return
    bp.sleep(0.5)
    CareerPanel.click_btn_i(bp)
    bp.sleep(0.5)

# 检查节点突破资源不足情况
def failure_enhance_test(bp:BasePage):
    bp.debug_log("测试突破资源不足开始")
    bp.sleep(0.5)
    cash_value = CareerPanel.get_cash_value(bp)
    points_value = CareerPanel.get_points_value(bp)
    cost_qulity_list = CareerPanel.get_cost_qulity_list(bp)
    cost_cash_value = cost_qulity_list[1]
    cost_points_value = cost_qulity_list[0]
    if cash_value>=cost_cash_value & points_value>=cost_cash_value:
        bp.debug_log("erro:if cash_value>=cost_cash_value & points_value>=cost_cash_value")
        return
    bp.sleep(0.5)
    CareerPanel.click_btn_enhance(bp)
    bp.sleep(0.5)
    if not MessageBoxPanel.is_panel_active(bp):
        bp.debug_log("erro:messagebox is not exist")
        return
    MessageBoxPanel.click_btn_confirm(bp)
    bp.sleep(0.5)
    if MessageBoxPanel.is_panel_active(bp):
        bp.debug_log("erro:messagebox can not close")
        return
    bp.sleep(0.5)


# 随机突破至某天赋节点
def enhance_item(bp:BasePage):
    # page_item_middle_id_list = CareerPanel.get_page_item_id_list(bp)
    # index = random.randint(1,len(page_item_middle_id_list))
    index = 1
    CareerPanel.enhance_until_item_exist(bp, index)

def main(bp:BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "levelupto 56"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 进入天赋
    bp.go_to_panel("CareerPanel")

    tips_test(bp)

    rating_tips_test(bp)

    bp.go_home()

    bp.go_to_panel("CareerPanel")

    failure_enhance_test(bp)

    bp.go_home()

    bp.cmd_list(["add 1 100400 10000000", "add 1 100000 10000000"])

    bp.go_to_panel("CareerPanel")

    enhance_item(bp)

    bp.go_home()




# 检查未解锁节点
# 检查解锁节点
# 检查节点达到满级


if __name__ == '__main__':
    bp = BasePage("192.168.111.36:20028")
    main(bp)
    bp.connect_close()
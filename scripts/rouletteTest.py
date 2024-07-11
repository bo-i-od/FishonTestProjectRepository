from common.basePage import BasePage
from panelObjs.commonWebViewPanel import CommonWebViewPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.roulettePanel import RoulettePanel
from tools.commonTools import *
from common import resource, gameInit


def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "levelupto 21", "add 2 201001 10000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    bp.go_to_panel("RoulettePanel")
    bp.sleep(1)

    # 点击玩法说明
    RoulettePanel.click_btn_i(bp)
    bp.sleep(1)
    RoulettePanel.click_btn_i(bp)

    # 点击公示
    RoulettePanel.click_btn_announcement(bp)
    CommonWebViewPanel.wait_for_btn_close_appear(bp)
    CommonWebViewPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点击旋转
    RoulettePanel.click_btn_spin(bp)
    bp.sleep(3)

    # 按压旋转
    RoulettePanel.press_btn_spin(bp, 1)
    bp.sleep(20)

    RoulettePanel.click_btn_spin(bp)
    bp.sleep(1)

    RoulettePanel.click_btn_close(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    bp.go_home()



if __name__ == '__main__':
    bp = BasePage()
    main(bp)


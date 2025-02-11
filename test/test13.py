from common.basePage import BasePage
from netMsg import csMsgAll
from panelObjs.RogueMainStagePanel import RogueMainStagePanel
from panelObjs.RogueResultPanel import RogueResultPanel

# 升爬塔难度
if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    cur = 0
    while cur < 12:
        RogueMainStagePanel.click_btn_challenge(bp)
        bp.sleep(1)
        bp.cmd("towerPass 1 1 3 10000")
        bp.sleep(3)
        RogueResultPanel.click_btn_orange(bp)
        bp.sleep(1)
        RogueMainStagePanel.panel_tips_up.click_btn_close(bp)
        bp.sleep(1)
        cur += 1


    bp.connect_close()
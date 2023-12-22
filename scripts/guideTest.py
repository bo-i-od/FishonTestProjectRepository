import random
from common.basePage import BasePage
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.newbieGuidePanel import NewbieGuidePanel
from panelObjs.battlePanel import BattlePanel
from tools.commonTools import *


def playerEditNamePanelTest(bp: BasePage):
    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    name = PlayerEditNamePanel.get_player_name(bp)
    player_name = name[1:]
    PlayerEditNamePanel.set_player_name(player_name)
    # 得到头像个数
    head_count = PlayerEditNamePanel.get_head_count(bp)
    # 随机选一个序号
    select_index = random.randrange(0, head_count - 1)
    # 点击该序号
    head_img_object_id = PlayerEditNamePanel.select_head(bp, select_index)
    bp.sleep(1)
    # 得到head_object_id和select_object_id，它俩应该有相同的parent
    head_object_id = PlayerEditNamePanel.get_head_object_id(bp, head_img_object_id)
    select_object_id = PlayerEditNamePanel.get_select_object_id(bp)
    # 看他们parent是不是相同
    compare(bp.get_parent_id(head_object_id), bp.get_parent_id(select_object_id))
    # 点击确认按钮
    PlayerEditNamePanel.click_confirm(bp)
    bp.sleep(1)

def newbieGuidePanelTest(bp: BasePage):
    start_page = NewbieGuidePanel.get_start_page(bp)
    if start_page > 3:
        bp.cmd("autofish")
        NewbieGuidePanel.do_guide_1(bp)
        # BattlePanel.reel(bp)
        NewbieGuidePanel.do_guide_2(bp)
    if start_page > 2:
        bp.cmd("autofish")
        NewbieGuidePanel.do_guide_3(bp)
        BattlePanel.unleash_power(bp)
        # BattlePanel.reel(bp)
        NewbieGuidePanel.do_guide_4(bp)
    if start_page > 1:
        NewbieGuidePanel.do_guide_5(bp)
    if start_page > 0:
        NewbieGuidePanel.do_guide_6(bp)

if __name__ == '__main__':
    bp = BasePage()
    playerEditNamePanelTest(bp)
    newbieGuidePanelTest(bp)

import random
import time

from common import gameInit
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
    PlayerEditNamePanel.set_player_name(bp, player_name)
    # 得到头像个数
    head_id_list = PlayerEditNamePanel.get_head_id_list(bp)
    head_count = len(head_id_list)
    # 随机选一个序号
    select_index = random.randrange(0, head_count - 1)
    # 点击该序号
    head_img_object_id = PlayerEditNamePanel.select_head(bp, head_id_list,select_index)
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
        NewbieGuidePanel.do_guide_1(bp)
        NewbieGuidePanel.do_guide_2(bp)
    if start_page > 2:
        NewbieGuidePanel.do_guide_3(bp)
        NewbieGuidePanel.do_guide_4(bp)
    if start_page > 1:
        NewbieGuidePanel.do_guide_5(bp)
    if start_page > 0:
        NewbieGuidePanel.do_guide_6(bp)

def main(bp:BasePage):
    username = str(time.time()).split('.')[0]
    gameInit.login(bp, username=username)
    playerEditNamePanelTest(bp)
    newbieGuidePanelTest(bp)

if __name__ == '__main__':
    bp = BasePage()
    main(bp)
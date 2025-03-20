import random
import time

from common import gameInit
from common.basePage import BasePage
from panelObjs.AchievementWantedPanel import AchievementWantedPanel
from panelObjs.AvatarSelectPanel import AvatarSelectPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.ClubApplyPanel import ClubApplyPanel
from panelObjs.FishAlbum3DPanel import FishAlbum3DPanel
from panelObjs.FishCardPanel import FishCardPanel
from panelObjs.GearPanel import GearPanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.PlayerEditNamePanel import PlayerEditNamePanel
from panelObjs.NewbieGuidePanel import NewbieGuidePanel
from panelObjs.BattlePanel import BattlePanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from panelObjs.ResultPanel import ResultPanel
from panelObjs.TournamentsPanel import TournamentsPanel
from scripts import battleTest
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
    head_expect_object_id = bp.get_parent_id(select_object_id)
    # 看他们parent是不是相同
    if head_object_id != head_expect_object_id:
        bp.debug_log("erro_if head_object_id != head_expect_object_id")
    # 点击确认按钮
    PlayerEditNamePanel.click_confirm(bp)
    bp.sleep(1)

def newbieGuidePanelTest(bp: BasePage):
    start_page = NewbieGuidePanel.get_start_page(bp)
    if start_page > 3:
        NewbieGuidePanel.guide_rookie_1(bp)
        NewbieGuidePanel.guide_rookie_2(bp)
    if start_page > 2:
        NewbieGuidePanel.guide_rookie_3(bp)
        NewbieGuidePanel.guide_rookie_4(bp)
    if start_page > 1:
        NewbieGuidePanel.guide_rookie_5(bp)
    if start_page > 0:
        NewbieGuidePanel.guide_rookie_6(bp)

def hookTest(bp: BasePage):
    # 去卡多湖渔场抛竿
    TournamentsPanel.go_to_fishery_by_id(bp, fishery_id='400301')
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    BattlePreparePanel.click_btn_cast(bp)

    # 刺鱼引导
    BattlePanel.hook_guide(bp)

def main(bp:BasePage):
    username = str(time.time()).split('.')[0]
    gameInit.login(bp, username=username)
    bp.cmd("fishcardall 10")

    # # 姓名头像测试
    playerEditNamePanelTest(bp)
    #海外版本暂无avatar
    '''
     AvatarSelectPanel.wait_for_panel_appear(bp)

    # 随机选择性别
    r = random.randint(0, 1)
    gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    bp.click_position(gender_icon_position_list[r])
    bp.sleep(0.5)

    AvatarSelectPanel.click_btn_start(bp)
    bp.sleep(0.5)
    '''


    # 新手引导
    newbieGuidePanelTest(bp)

    # 查询水族箱的解锁等级
    unlock_lv = bp.get_unlock_lv("水族箱")
    bp.cmd(f"levelupto {unlock_lv}")

    # 鱼册引导
    bp.go_to_panel("FishAlbum3DPanel")
    FishAlbum3DPanel.guide(bp)

    # 等待升级界面弹出，避免引导过程中被卡住
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 水族馆引导
    #海外版本暂无水族箱
    '''
    bp.go_to_panel("AquariumPanel")
    AquariumPanel.guide(bp)
    bp.go_home()
    '''

    bp.go_to_panel("FishAlbum3DPanel")
    bp.go_home()

    # 鱼卡引导
    FishCardPanel.guide(bp)
    bp.go_home()

    # 俱乐部引导
    ClubApplyPanel.guide(bp)
    ClubApplyPanel.click_btn_close(bp)

    # 刺鱼引导
    bp.go_to_panel("TournamentsPanel")
    bp.cmd("mode 400301 390001")
    bp.sleep(1)
    hookTest(bp)
    BattlePanel.reel_quick(bp)
    element_btn = ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp, element_btn=element_btn)

    # 清除弹窗
    bp.sleep(3)
    bp.clear_popup()

    # 稀有鱼引导
    AchievementWantedPanel.guide(bp)
    bp.sleep(1)

    # 断线引导
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    bp.sleep(1)
    BattlePanel.release_btn_reel(bp)
    # element_btn = ResultPanel.wait_for_result(bp)
    # ResultPanel.automatic_settlement(bp, element_btn=element_btn)
    GearPanel.guide_oversea(bp)

    bp.go_home()




if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533", is_mobile_device=False)
    main(bp)
    bp.connect_close()
import random
import time

from common import gameInit
from common.basePage import BasePage
from panelObjs.achievementWantedPanel import AchievementWantedPanel
from panelObjs.aquariumPanel import AquariumPanel
from panelObjs.avatarSelectPanel import AvatarSelectPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.clubApplyPanel import ClubApplyPanel
from panelObjs.fishAlbum3DPanel import FishAlbum3DPanel
from panelObjs.fishCardPanel import FishCardPanel
from panelObjs.gearPanel import GearPanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.newbieGuidePanel import NewbieGuidePanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *



def player_edit_name_test(bp: BasePage):
    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    name = PlayerEditNamePanel.get_player_name(bp)
    player_name = name.replace("64", "000")
    PlayerEditNamePanel.set_player_name(bp, player_name)
    # 得到头像个数
    head_id_list = PlayerEditNamePanel.get_head_id_list(bp)
    head_count = len(head_id_list)
    # 随机选一个序号
    select_index = random.randrange(0, head_count - 1)
    # 点击该序号
    PlayerEditNamePanel.select_head(bp, head_id_list, select_index)
    # head_img_object_id = PlayerEditNamePanel.select_head(bp, head_id_list,select_index)
    bp.sleep(1)
    # # 得到head_object_id和select_object_id，它俩应该有相同的parent
    # head_object_id = PlayerEditNamePanel.get_head_object_id(bp, head_img_object_id)
    # select_object_id = PlayerEditNamePanel.get_select_object_id(bp)
    # head_expect_object_id = bp.get_parent_id(select_object_id)
    # # 看他们parent是不是相同
    # compare(head_object_id, head_expect_object_id)

    # 点击确认按钮
    PlayerEditNamePanel.click_confirm(bp)
    bp.sleep(1)


def guide_rookie_test(bp: BasePage):
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


def guide_common_test(bp: BasePage, guide_list, timeout=10):
    # 等待引导面板出现，如果10秒内不出现就跳过
    NewbieGuidePanel.wait_for_panel_appear(bp, timeout=timeout)
    bp.sleep(1)
    # 得到guide_list的每个引导第一步的定位元素
    first_perform_list = NewbieGuidePanel.get_first_perform_list(guide_list)
    object_id_list = bp.get_object_id_list(element_data_list=first_perform_list)

    cur = 0
    while cur < len(object_id_list):
        if object_id_list[cur]:
            break
        cur += 1

    # 没有可执行的引导就返回False
    if cur >= len(object_id_list):
        return False

    # 执行对应引导并返回True
    guide_name = guide_list.pop(cur)
    NewbieGuidePanel.guide_common(bp, guide_name=guide_name)
    return True


def guide_BattlePanel_test(bp: BasePage):
    # 不在战斗面板直接返回
    if not BattlePanel.is_panel_active(bp):
        return

    # 不在引导面板就普通提竿
    # 在引导就按引导提竿
    NewbieGuidePanel.wait_for_panel_appear(bp)
    if NewbieGuidePanel.is_panel_active(bp):
        NewbieGuidePanel.guide_common(bp, guide_name="guide_hook")
    else:
        BattlePanel.hook(bp)

    # 渔获
    BattlePanel.reel_quick(bp)
    element_btn = ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp, element_btn=element_btn)


def guide_BattlePreparePanel_test(bp: BasePage, guide_list):
    # 没有未进行的引导直接返回
    if not guide_list:
        return

    # 不在备战界面就进洪湖
    if not BattlePreparePanel.is_panel_active(bp):
        bp.go_to_panel("TournamentsPanel")
        TournamentsPanel.go_to_fishery_by_tpid(bp, fishery_tpid='400301')
        LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 有备战界面引导就进行
    did_guide = guide_common_test(bp, guide_list, timeout=5)
    if did_guide:
        bp.sleep(1)
        guide_BattlePanel_test(bp)
        guide_BattlePreparePanel_test(bp, guide_list)
        return

    # 没有备战界面引导就战斗一次之后
    # 可以设定钓鱼失败和成功
    battleTest.fish_once(bp, is_quick=True)

    # 再看有没有备战界面引导
    did_guide = guide_common_test(bp, guide_list, timeout=5)

    # 没有可进行的引导直接返回
    if not did_guide:
        return
    guide_BattlePreparePanel_test(bp, guide_list)


def guide_HomePanel_test(bp: BasePage, guide_list):
    # 没有未进行的引导直接返回
    if not guide_list:
        return
    bp.go_home()

    did_guide = guide_common_test(bp, guide_list)
    # 没有可进行的引导直接返回
    if not did_guide:
        return
    guide_HomePanel_test(bp, guide_list)

def guide_TournamentsPanel_test(bp: BasePage, guide_list):
    # 没有未进行的引导直接返回
    if not guide_list:
        return

    # 去锦标赛界面进行引导完回大厅
    bp.go_to_panel("TournamentsPanel")
    did_guide = guide_common_test(bp, guide_list, timeout=5)
    bp.go_home()

    # 没有可进行的引导直接返回
    if not did_guide:
        return
    guide_TournamentsPanel_test(bp, guide_list)

def guide_PVPHallPanel_test(bp: BasePage, guide_list):
    # 没有未进行的引导直接返回
    if not guide_list:
        return

    # 去对决界面进行引导完回大厅
    bp.go_to_panel("PVPHallPanel")
    did_guide = guide_common_test(bp, guide_list, timeout=5)
    bp.go_home()

    # 没有可进行的引导直接返回
    if not did_guide:
        return
    guide_PVPHallPanel_test(bp, guide_list)

def guide_fishing_fail_test(bp: BasePage):
    if not BattlePreparePanel.is_panel_active(bp):
        bp.go_to_panel("TournamentsPanel")
        TournamentsPanel.go_to_fishery_by_tpid(bp, fishery_tpid='400301')
        LoadingFisheryPanel.wait_until_panel_disappear(bp)
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    NewbieGuidePanel.wait_for_panel_appear(bp, timeout=30)
    guide_name = "guide_fishing_fail"
    NewbieGuidePanel.guide_common(bp, guide_name=guide_name)
    bp.go_home()

def main(bp:BasePage):
    username = str(time.time()).split('.')[0]
    gameInit.login(bp, username=username)
    gameInit.set_joystick(bp)
    bp.cmd_list(["fishcardall 10"])

    # # 姓名头像测试
    player_edit_name_test(bp)

    AvatarSelectPanel.wait_for_panel_appear(bp)
    bp.sleep(0.5)

    # 随机选择性别
    r = random.randint(0, 1)
    gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    bp.click_position(gender_icon_position_list[r])
    bp.sleep(0.5)

    AvatarSelectPanel.click_btn_start(bp)
    bp.sleep(0.5)

    # 新手引导
    guide_rookie_test(bp)
    bp.cmd_list([f"levelupto 4", "mode 400301 301001"])
    bp.go_home()

    # 钓点引导、鱼册引导
    guide_list = ["guide_fish_point", "guide_album"]
    guide_BattlePreparePanel_test(bp, guide_list)

    # 升等级
    bp.cmd(f"levelupto 99")

    # 水族箱引导、鱼卡引导、俱乐部引导
    guide_list = ["guide_club", "guide_fish_card", "guide_aquarium_1"]
    guide_HomePanel_test(bp, guide_list)

    # 好友对决引导
    guide_list = ["guide_friend_duel"]
    guide_PVPHallPanel_test(bp, guide_list)

    # 多人房引导
    bp.cmd("mode 400301 390005")
    guide_list = ["guide_multi_room"]
    guide_TournamentsPanel_test(bp, guide_list)

    # 水族箱引导、照片墙引导、体感抛竿引导、
    guide_list = ["guide_aquarium_2", "guide_fish_photo", "guide_fishing_cast"]
    guide_BattlePreparePanel_test(bp, guide_list)

    # 断线引导
    guide_fishing_fail_test(bp)





if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=True)
    main(bp)
    bp.connect_close()
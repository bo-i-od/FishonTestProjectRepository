import random

from common import gameInit
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.rankPanel import RankPanel
from tools.commonTools import *
from common.basePage import BasePage

def main(bp: BasePage):
    # 查询邮件的解锁等级
    unlock_lv = bp.excelTools.get_unlock_lv("鱼类排行榜")
    exp = bp.excelTools.get_exp_limit(unlock_lv)[1]

    # 进入大厅
    cmd_list = ["guideskip", f"add 1 100200 {exp}"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # 关闭升级弹窗
    PlayerLevelupPanel.wait_for_panel_appear(bp)

    # 进入排行榜界面
    bp.go_to_panel("RankPanel")

    # 随机选择渔场
    fisheries_viewport = RankPanel.get_fisheries_viewport(bp)
    r = random.randint(0, len(fisheries_viewport.item_id_list) - 1)
    fisheries_viewport.move_until_appear(target_id=fisheries_viewport.item_id_list[r])
    fisheries_position_list = RankPanel.get_fisheries_position_list(bp)
    bp.click_position(fisheries_position_list[r])

    # 随机选地区
    area_position_list = RankPanel.get_tab_area_position_list(bp)
    r = random.randint(0, len(area_position_list) - 1)
    bp.click_position(area_position_list[r])

    # 随机选时间
    time_position_list = RankPanel.get_tab_time_position_list(bp)
    r = random.randint(0, len(time_position_list) - 1)
    bp.click_position(time_position_list[r])

    # 随机选择鱼
    photo_viewport = RankPanel.get_photo_viewport(bp)
    r = random.randint(0, len(photo_viewport.item_id_list) - 1)
    photo_viewport.move_until_appear(target_id=photo_viewport.item_id_list[r])
    photo_position_list = RankPanel.get_photo_position_list(bp)
    bp.click_position(photo_position_list[r])

    #


if __name__ == '__main__':
    bp = BasePage()
    main(bp)
import random

from common import gameInit
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.rankFishLeaderboardPanel import RankFishLeaderboardPanel
from panelObjs.rankPanel import RankPanel
from tools.commonTools import *
from common.basePage import BasePage

def main(bp: BasePage):
    # 查询邮件的解锁等级
    unlock_lv = bp.get_unlock_lv("鱼类排行榜")

    # 进入大厅
    cmd_list = ["guideskip", f"levelupto {unlock_lv}"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # 关闭升级弹窗
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 进入排行榜界面
    bp.go_to_panel("RankPanel")

    # 随机选择渔场
    fisheries_viewport = RankPanel.get_fisheries_viewport(bp)
    r = 0
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
    is_like = False
    if r < 2:
        is_like = True

    # 随机选择有排行的鱼
    data_list, no_data_list = RankPanel.get_photo_status(bp)
    # 单鱼排行榜测试
    if data_list:
        leaderboard_test(bp, data_list, is_like)

    r = len(fisheries_viewport.item_id_list) - 1
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

    # 随机选择有排行的鱼
    data_list, no_data_list = RankPanel.get_photo_status(bp)
    #  点一个没排行的鱼
    if no_data_list:
        # 随机选没有排行的鱼
        photo_viewport = RankPanel.get_photo_viewport(bp)
        r = random.randint(0, len(no_data_list) - 1)
        photo_viewport.move_until_appear(target_id=photo_viewport.item_id_list[no_data_list[r]])
        bp.sleep(1)
        photo_position_list = RankPanel.get_photo_position_list(bp)
        bp.click_position(photo_position_list[no_data_list[r]])

    bp.go_home()

    #
# 单鱼排行榜测试
def leaderboard_test(bp: BasePage, data_list, is_like):
    photo_viewport = RankPanel.get_photo_viewport(bp)

    # 随机选择一条
    r = random.randint(0, len(data_list) - 1)
    photo_viewport.move_until_appear(target_id=photo_viewport.item_id_list[data_list[r]])
    bp.sleep(1)
    photo_position_list = RankPanel.get_photo_position_list(bp)

    # 记录信息
    rank_data = RankPanel.get_rank_data(bp, r)
    bp.click_position(photo_position_list[r])
    bp.sleep(1)
    compare(rank_data, RankFishLeaderboardPanel.get_rank_data_oversea(bp))

    # 点赞
    if not is_like:
        # 返回上级界面
        RankFishLeaderboardPanel.click_btn_close(bp)
        bp.sleep(1)
        return
    like_value = RankFishLeaderboardPanel.get_like_value(bp)
    RankFishLeaderboardPanel.click_btn_like(bp)
    bp.sleep(1)
    if RankFishLeaderboardPanel.is_btn_like_normal(bp):
        bp.debug_log("erro_RankFishLeaderboardPanel.is_btn_like_normal(bp)")
    compare(like_value + 1, RankFishLeaderboardPanel.get_like_value(bp))

    # 返回上级界面
    RankFishLeaderboardPanel.click_btn_close(bp)
    bp.sleep(1)





if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=False)
    main(bp)
    bp.connect_close()

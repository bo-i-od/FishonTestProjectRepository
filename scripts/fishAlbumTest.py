import random

from common import gameInit
from common.basePage import BasePage
from netMsg import fishingMsg
from panelObjs.fishAlbum3DPanel import FishAlbum3DPanel
from panelObjs.fishAlbumPreviewPanel import FishAlbumPreviewPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.sharePanel import SharePanel
from tools.commonTools import compare


def share_test(bp: BasePage):
    FishAlbum3DPanel.click_btn_share(bp)
    bp.sleep(1)

    SharePanel.click_btn_close(bp)
    bp.sleep(1)


def change_tab_test(bp: BasePage):
    FishAlbum3DPanel.click_btn_switch(bp)
    bp.sleep(1)

    tab_id_list = FishAlbum3DPanel.get_tab_id_list(bp)

    unlock_tab_list, lock_tab_list = FishAlbum3DPanel.get_tab_status(bp, tab_id_list)

    # 切换已解锁页签
    r = random.randint(0, len(unlock_tab_list) - 1)

    tab_index = unlock_tab_list[r]
    tab_name = FishAlbum3DPanel.get_tab_name_list(bp, tab_id_list)[tab_index]

    FishAlbum3DPanel.switch_tab(bp, tab_index)

    bp.sleep(3)
    if FishAlbum3DPanel.is_panel_fisheries_active(bp):
        bp.click_position([0.5, 0.1])
        bp.sleep(0.5)

    photo_name = FishAlbum3DPanel.get_photo_name(bp)
    compare(tab_name, photo_name)

    FishAlbum3DPanel.click_btn_switch(bp)
    bp.sleep(1)

    # 点击锁定页签，但锁定页签无法切换
    r = random.randint(0, len(lock_tab_list) - 1)

    tab_index = lock_tab_list[r]
    FishAlbum3DPanel.switch_tab(bp, tab_index)

    bp.sleep(3)

    compare(FishAlbum3DPanel.get_photo_name(bp), photo_name)

    bp.click_position([0.5, 0.5])
    bp.sleep(0.5)


def photo_test(bp: BasePage):
    photo_bg_position = FishAlbum3DPanel.get_photo_bg_position(bp)

    # 点击i
    FishAlbum3DPanel.click_btn_i(bp)
    bp.sleep(0.5)
    if not FishAlbum3DPanel.is_panel_rewards_tip_active(bp):
        bp.debug_log("error:if not FishAlbum3DPanel.is_panel_rewards_tip_active(bp):")
    FishAlbum3DPanel.click_btn_i(bp)
    bp.sleep(0.5)

    # 点击鱼卡奖励
    reward_icon_position = FishAlbum3DPanel.get_reward_icon_position(bp)
    bp.click_position(reward_icon_position)
    # 如果鱼卡弹窗打开就先关闭
    if not FishCardPackTipsPanel.is_panel_active(bp):
        bp.debug_log("erro_if not FishCardPackTipsPanel.is_panel_active(bp):")
    bp.click_position(photo_bg_position)
    bp.sleep(0.5)

    # 点击星星
    star_position_list = FishAlbum3DPanel.get_star_position_list(bp)
    cur = 0
    while cur < len(star_position_list):
        bp.click_position(star_position_list[cur])
        bp.sleep(0.1)
        cur += 1
    bp.click_position(photo_bg_position)
    bp.sleep(0.5)

    FishAlbum3DPanel.click_btn_preview(bp)
    bp.sleep(1)

    FishAlbumPreviewPanel.click_btn_close(bp)


def anime_test(bp: BasePage):
    # 去主界面调用接口钓鱼
    bp.go_home()
    table_data = bp.excelTools.get_table_data("FISHERIES.xlsm")
    tpId = 400301
    index = table_data["tpId"].index(tpId)
    fish_list = table_data["fish"]
    fish_count = 0
    cur = 0
    while cur < len(fish_list):
        fish_id = fish_list[cur][index]
        if fish_id in [0, "0", ""]:
            cur += 1
            continue
        bp.cmd(f"mode {tpId} {fish_id}")
        bp.sleep(0.1)
        fishingMsg.fish(bp, [{"spot_id": f"{tpId}03", "energy_cost": 30, "times": 1, "is_activity_spot": False}])
        fish_count += 1
        cur += 1


    bp.go_to_panel("FishAlbum3DPanel")
    # 等待动画播放完
    progress = -1
    while True:
        progress_cur = FishAlbum3DPanel.get_progress_cur(bp)
        if progress == progress_cur:
            break
        progress = progress_cur
        bp.sleep(2)
    compare(fish_count, progress)

    reward_icon_position = FishAlbum3DPanel.get_reward_icon_position(bp)
    bp.click_position(reward_icon_position)

    bp.go_home()




def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip","levelupto 36"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    bp.go_to_panel("FishAlbum3DPanel")

    share_test(bp)

    change_tab_test(bp)

    photo_test(bp)

    anime_test(bp)


if __name__ == '__main__':
    # 连接设备号为127.0.0.1:21533的设备
    bp = BasePage(serial_number="127.0.0.1:21523", is_mobile_device=True)
    main(bp)
    bp.connect_close()

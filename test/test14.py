from common.basePage import BasePage
from netMsg import csMsgAll, fishingMsg
from panelObjs import LoginPanel, LoadingPanel, PlayerEditNamePanel, AvatarSelectPanel
from scripts.createUsers import logout, connect
from tools import fastCommand
from tools.commonTools import lua_dict_to_python_dict, sort_dict_recursively


def login(bp: BasePage, name):
    LoginPanel.wait_for_panel_appear(bp)
    connect(bp, name)
    LoadingPanel.wait_until_panel_disappear(bp)


def get_flash_card(bp:BasePage, flash_card_list, name):
    fastCommand.guide_skip(bp)
    bp.sleep(1)
    bp.cmd_list(["setQuest 80000031"])
    bp.sleep(1)
    res = {}
    msg = get_FlashCardBatchDataMsg(bp, name=name)
    python_dict = lua_dict_to_python_dict(msg)
    if 'flashCardList' not in python_dict:
        return res
    flash_card_dict = python_dict['flashCardList']
    flash_card_len = len(flash_card_dict)
    star = 2
    cur = 1
    while cur <= len(flash_card_dict):
        tpid = flash_card_dict[cur]['flashCardTpId']
        count = flash_card_dict[cur]['count']
        res[tpid] = count
        if tpid in flash_card_list:
            if count < 5 and star > 1:
                star = 1
            if count < 3 and star > 0:
                star = 0
        else:
            flash_card_len -= 1
        cur += 1
    if flash_card_len < len(flash_card_list):
        star = -1
    return res, star

def get_FlashCardBatchDataMsg(bp: BasePage, name):
    logout(bp)

    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    # 登录
    login(bp, name)

    msg = bp.receive_until_get_msg(msg_name="FlashCardBatchDataMsg")
    return msg

def fish(bp: BasePage, spot_id, times, energy_cost):
    bp.custom_cmd("setSceneType 4")
    bp.set_item_count(target_count=times * energy_cost * 2, item_tpid="100500")
    # 掉藏宝图
    bp.cmd("mode 500301 399002")
    fishingMsg.fish(bp, [
        # {"spot_id": "40032014", "times": 1000, "target_id_list": ["340003"], "ignore_id_list":["340003"],  "energy_cost":100},
        {"spot_id": f"{spot_id}", "times": 1, "is_limited_spot": False}
        # {"spot_id": f"40030214", "times": 1000, "energy_cost": 50},
    ])

    bp.cmd("mode 0 0")
    fishingMsg.fish(bp, [
        # {"spot_id": "40032014", "times": 1000, "target_id_list": ["340003"], "ignore_id_list":["340003"],  "energy_cost":100},
        {"spot_id": f"{spot_id}", "times": times, "is_limited_spot": True, "energy_cost": energy_cost}
        # {"spot_id": f"40030214", "times": 1000, "energy_cost": 50},
    ])
    bp.sleep(times * 0.1)

def create_account(bp: BasePage, name):
    login(bp, name)
    if not PlayerEditNamePanel.is_panel_active(bp):
        return
        # bp.cmd_list(["guideskip"])
    bp.sleep(2)
    fastCommand.guide_skip(bp)
    bp.sleep(2)
    fastCommand.level_up_to_new_plot(bp, 99)
    bp.sleep(2)
    bp.cmd_list(["setQuest 80000031", "levelupto 21"])
    bp.sleep(2)
    while True:
        # PlayerEditNamePanel.set_player_name(bp, name)
        PlayerEditNamePanel.click_confirm(bp, is_ray_input=True)
        bp.sleep(1)
        if not PlayerEditNamePanel.is_panel_active(bp):
            break
        # name = name.replace("64", "000")
        # name = "t" + str(time.time()).split('.')[0]

    bp.sleep(1)
    if not AvatarSelectPanel.is_panel_active(bp):
        return
    # # 随机选择性别
    # r = 0
    # gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    # bp.click_position(gender_icon_position_list[0])
    # bp.sleep(0.5)
    AvatarSelectPanel.click_gender_icon(bp, is_ray_input=True)
    bp.sleep(0.5)
    AvatarSelectPanel.click_btn_start(bp, is_ray_input=True)

def get_max_flash_card_weight_spot(flash_card, every_spot_flash_card, quality_dict):
    max_flash_card_weight_spot = None
    max_flash_card_weight = 0
    # p = ""
    for spot in every_spot_flash_card:
        spot_flash_card = every_spot_flash_card[spot]
        weight_total = 0

        for count_dict in spot_flash_card:
            count = spot_flash_card[count_dict]
            if count_dict in flash_card:
                count -= flash_card[count_dict]
            if count < 0:
                count = 0
            factor = 0
            if quality_dict[count_dict] == 1:
                factor = 3
            elif quality_dict[count_dict] == 2:
                factor = 4
            elif quality_dict[count_dict] == 3:
                factor = 5
            if count > 4:
                factor *= 5
            elif count > 3:
                factor *= 4
            elif count > 2:
                factor *= 3
            elif count > 1:
                factor *= 2

            weight_total += factor * count
        weight_ave = weight_total / len(spot_flash_card)
        # p += f"钓点{spot}: {weight_ave}   "
        if weight_ave > max_flash_card_weight:

            max_flash_card_weight = weight_ave
            max_flash_card_weight_spot = spot

    return max_flash_card_weight_spot

def get_quality_dict(bp: BasePage, fishery_id):
    quality_dict = {}
    table_data_object_list = bp.excelTools.get_table_data_object_list_by_key_value(key="fishSceneTpId", value=fishery_id, book_name="COLLECTION_BASE.xlsm")
    for table_data_object in table_data_object_list:
        flash_card_id = table_data_object["collectionId"]
        quality = table_data_object["collectionLevel"]
        quality_dict[flash_card_id] = quality
    return quality_dict


def get_every_spot_flash_card(bp: BasePage, fishery_id):
    every_spot_flash_card = {}
    table_data_object_list = bp.excelTools.get_table_data_object_list_by_key_value(key="newPlotFisheriesId", value=fishery_id, book_name="NEW_PLOT_FISH_SPOT.xlsm")
    table_data_detail = bp.excelTools.get_table_data_detail(book_name="COLLECTION_BASE.xlsm")

    for table_data_object in table_data_object_list:
        if "enabled" not in table_data_object:
            continue
        spot_id = table_data_object["tpId"]
        fish_id_list = bp.get_drop_fish_id_list(spot_id=spot_id)
        count_dict = {}
        for fish_id in fish_id_list:
            flash_card_id = bp.fish_id_to_flash_card_id(fish_id=fish_id, table_data_detail=table_data_detail)
            count_dict[flash_card_id] = 5
        every_spot_flash_card[spot_id] = count_dict
    return every_spot_flash_card


def test_once(bp: BasePage, name):
    # 获取每个钓点的闪卡
    every_spot_flash_card = get_every_spot_flash_card(bp, fishery_id=500301)

    # 获取闪卡对应的品质
    quality_dict = get_quality_dict(bp, fishery_id=500301)

    # 获取闪卡列表
    flash_card_list = list(quality_dict)


    cost_total = 0
    times = 50
    energy_cost = 200
    create_account(bp, name)
    cur = 0
    spot_id_list = list(every_spot_flash_card)
    while cur < len(spot_id_list):
        spot_id = spot_id_list[cur]
        fish(bp, spot_id=spot_id, times=times, energy_cost=energy_cost)
        cost_total += times * energy_cost
        cur += 1

    star_pre = -1
    cur = 0
    while True:
        flash_card, star = get_flash_card(bp, flash_card_list, name)
        spot_id = get_max_flash_card_weight_spot(flash_card, every_spot_flash_card, quality_dict)
        # print("最缺闪卡钓点:", spot_id, "  消耗体力:", cost_total, "当前星级:", star)
        # print(sort_dict_recursively(flash_card))
        # print(bp.get_drop_fish_id_list(spot_id=spot_id))

        if star > star_pre:
            print(f"达成{star}星共消耗{cost_total}体力")
            star_pre = star
        if star == 2:
            break
        cost_total += times * energy_cost
        fish(bp, spot_id=spot_id, times=times, energy_cost=energy_cost)
        cur += 1
    logout(bp)

def main(bp: BasePage):
    cur = 110
    while cur < 120:
        name = f"test{cur}"
        test_once(bp, name)
        cur += 1

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    main(bp)
    bp.connect_close()


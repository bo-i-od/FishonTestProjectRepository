from common.basePage import BasePageMain, BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData
from netMsg import fishingMsg
from netMsg.luaLog import get_value
from panelObjs import AvatarSelectPanel, PlayerEditNamePanel, LoginPanel, LoadingPanel
from scripts.createUsers import disconnect, connect
from collections import defaultdict


def auto_fish_all_type(bp: BasePage, fishery_id: str):
    """
    根据渔场id列出该渔场所有REM鱼

    返回：
        fish_type_map:{2: [...], 3: [...], 4: [...]}, 记录每一类型鱼的鱼ID列表
        fished_dict:{2: set(), 3: set(), 4: set()}, 初始化每种类型已钓鱼的set

    """
    fish_id_list = get_fish_id_list(bp, fishery_id)
    fish_type_map = defaultdict(list)

    table_data_detail = bp.excelTools.get_table_data_detail("FISH.xlsm")
    for fid in fish_id_list:
        fclass = get_fish_type(bp, fid, table_data_detail)
        # 2,3,4对应R,E,M
        if str(fclass) in ('2','3','4'):
            fish_type_map[int(fclass)].append(fid)
    fished_dict = {2: set(), 3: set(), 4: set()}
    return fish_type_map, fished_dict

def fish_finish(fished_dict, fish_type_map):
    """
    判断是否钓完所有REM鱼
    """
    for t in (2,3,4):
        if len(fished_dict[t]) < len(fish_type_map[t]):
            return False
    return True

def fish(bp: BasePage, fish_id):
    """
    接口钓鱼，钓黄金鱼
    """
    log_list = bp.log_list
    bp.set_item_count(item_tpid="100500", target_count=100000000000)

    if fish_id:
        spot_id = bp.fish_id_to_spot_id(fish_id = fish_id)[0]
        fishery_id = bp.fish_id_to_fishery_id(fish_id = fish_id)

    bp.cmd(f"mode {fishery_id} 399002")
    bp.sleep(0.1)
    fishingMsg.fish(bp, [
        # {"spot_id": f"{fishery_id}03", "times": 1, "is_limited_spot": False},
        {"spot_id": spot_id, "times": 1},
        #
    ])
    bp.sleep(0.1)
    c = f"mode {fishery_id} {fish_id}"
    bp.cmd(c)
    bp.sleep(0.1)

    while True:
        bp.log_list.clear()

        fishingMsg.fish(bp, [
            # {"spot_id": f"{fishery_id}04", "times": 1, "is_limited_spot":True, "energy_cost":50},
            {"spot_id": spot_id, "times": 1, "is_limited_spot":True},
            #
        ])
        bp.sleep(1)
        target_log = bp.get_target_log(msg_key="SCFishingHookMsg")
        color = get_value(msg=target_log,key="color",is_str=False)
        # print(target_log)
        if str(color) == "11":
            print(f"黄金鱼{fish_id}")
            break
        bp.sleep(0.5)

def get_fish_id_list(bp: BasePage, fishery_id, fisheries_detail=None):
    """函数功能简述
        根据fishery_id获取该渔场的鱼id列表

    参数:
        fishery_id: 渔场id
    """
    if fisheries_detail is None:
        fisheries_detail = bp.excelTools.get_table_data_detail(book_name="FISHERIES.xlsm")
    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_detail)
    fish_list = table_data_object["fish"]
    activity_fish_list = []
    if "activityFishNotShow" in table_data_object:
        activity_fish_list = table_data_object["activityFishNotShow"]
    res_list = []
    for fish in fish_list:
        if not fish:
            continue
        if activity_fish_list and fish in activity_fish_list:
            continue
        res_list.append(fish)
    return res_list

def get_fish_type(bp:BasePage, fish_tpid, table_data_detail=None):
    """函数功能简述
        从FISH.xlsm中获取鱼的体型

    参数:
        fish_tpid: 鱼id

    输出:
        str
        "小"，"中"，"大"，"特大"，"超巨"，"奇珍"，"超奇珍"，"典藏"，"其它"
    """
    fish_tpid = str(fish_tpid)
    if table_data_detail is None:
        table_data_detail = bp.excelTools.get_table_data_detail("FISH.xlsm")
    if fish_tpid == '':
        return "钓鱼失败"
    if fish_tpid in ["399001", "399002"]:
        return "藏宝图"

    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=fish_tpid,
                                                                           table_data_detail=table_data_detail)

    fishClass = 0
    fishType = 0
    if "fishClass" in table_data_object:
        fishClass = table_data_object["fishClass"]
    if "fishType" in table_data_object:
        fishType = table_data_object["fishType"]
    # index = table_data_object_list["tpId"].index(int(fish_tpid))

    if fishClass == 2:
        return 2
    if fishClass == 3:
        return 3
    if fishClass == 4:
        return 4

    fish_id = bp.fish_bone_id_to_fish_id(fish_bone_id=fish_tpid)
    if not fish_id:
        return None
    fish_type = bp.get_fish_type(fish_tpid=fish_id)
    if not fish_type:
        return None
    if fish_tpid[0:2] in ["37"]:
        fish_type = fish_type + "黄金"
    if fish_tpid[0:3] in ["385"]:
        fish_type = fish_type + "黄金"
    return fish_type + "鱼骨"

def click_golden_tab(bp: BasePage):
    """
    进入金色传说-金色鱼王TAB
    """
    bp.go_to_panel("ActivityCenterPanel")
    text_list = bp.get_text_list(element_data=ElementsData.ActivityCenterPanel.eventsname)
    print(f"当前tab文本列表: {text_list}")

    try:
        target_index = text_list.index('金色传说')
    except ValueError:
        raise RuntimeError("未找到'金色传说'tab")

    tab_id_list = bp.get_object_id_list(element_data=ElementsData.ActivityCenterPanel.eventsname)
    if not tab_id_list or len(tab_id_list) <= target_index:
        raise RuntimeError("tab的object_id列表有误")
    target_obj_id = tab_id_list[target_index]

    viewport = Viewport(
        bp,
        element_viewport=ElementsData.ActivityCenterPanel.viewport,
        element_item_list=ElementsData.ActivityCenterPanel.eventsname,
        item_id_list=tab_id_list,
        delta_len=0.5
    )
    viewport.move_until_appear(target_obj_id)
    bp.click_element_safe(object_id=target_obj_id)

    bp.sleep(1)
    bp.go_to_panel("EventCenterGoldenLegendPanel")
    bp.click_element_safe(element_data=ElementsData.EventCenterGoldenLegendPanel.tab_4)
    bp.sleep(0.1)
    bp.click_element_safe(element_data=ElementsData.EventCenterGoldenLegendPanel.name)
    bp.sleep(0.1)
    bp.click_element_safe(element_data=ElementsData.RewardsPanel.tap_to_claim)
    bp.sleep(0.1)
    bp.clear_popup_until_appear(element_data=ElementsData.EventCenterGoldenLegendPanel.name)

# def fish_golden(bp: BasePage, fishery_id: int):
#     fish_detail = bp.excelTools.get_table_data_detail(book_name="FISH.xlsm")
#     fish_detail, _, _ = fish_detail
#     fish_tpId_list = get_fish_id_list(fishery_id)

def login(bp: BasePage, name):
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    LoginPanel.wait_for_panel_appear(bp)
    connect(bp, name)
    LoadingPanel.wait_until_panel_disappear(bp)
    # bp.log_list_flag = False

    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    # bp.cmd_list(["guideskip"])
    # gameInit.guide_skip(bp)
    bp.sleep(1)
    # while True:
    #     # PlayerEditNamePanel.set_player_name(bp, name)
    #     PlayerEditNamePanel.click_confirm(bp, is_ray_input=True)
    #     bp.sleep(1)
    #     if not PlayerEditNamePanel.is_panel_active(bp):
    #         break
        # name = name.replace("64", "000")
        # name = "t" + str(time.time()).split('.')[0]

    # bp.sleep(1)
    # if not AvatarSelectPanel.is_panel_active(bp):
    #     return
    # # 随机选择性别
    # r = 0
    # gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    # bp.click_position(gender_icon_position_list[0])
    # bp.sleep(0.5)
    # AvatarSelectPanel.click_gender_icon(bp, is_ray_input=True)
    # bp.sleep(0.5)
    # AvatarSelectPanel.click_btn_start(bp, is_ray_input=True)

def relogin(bp:BasePage,name,uid=None):
    """
    clone账号重新登录
    """
    if uid:
        bp.cmd(f"clone {uid}")
        logout(bp)
        login(bp,name)
        bp.cmd(f"open_chapter_all")

def logout(bp: BasePage):
    bp.sleep(1)
    disconnect(bp)

def init(bp: BasePage):
    if LoginPanel.is_panel_active(bp):
        return
    logout(bp)

def clone(bp:BasePage, uid):
    bp.sleep(2)
    bp.clear_popup()
    cmd = f"clone {uid}"
    print(cmd)
    bp.cmd(cmd)

def photo_shot(bp:BasePage):
    """
    截图保存到report文件夹下
    """
    click_golden_tab(bp)
    bp.sleep(1)
    img = bp.get_full_screen_shot()
    bp.save_img(img)

def main(bp:BasePage, fish_type_map, fished_dict, uid=None):
    """
    主体流程：
        按用户循环自动登录、钓全部目标类型鱼，每完成后截图并登出。
        直至每个类型鱼全部钓完。

    参数:
        fish_type_map: {2:[...],3:[],4:[]} 类型鱼id列表
        fished_dict: {2:set,3:set,4:set} 已钓鱼id集合
        uid (optional): clone账号的uid
    """
    prefix = "611_"
    cur = 0
    init(bp)
    while not fish_finish(fished_dict,fish_type_map):
        name = prefix + str(cur)
        bp.sleep(1)
        login(bp,name)
        relogin(bp,name,uid)
        for t in (2,3,4):
            untapped = [fish_id for fish_id in fish_type_map[t] if fish_id not in fished_dict[t]]
            if not untapped:
                continue
            fish_id = untapped[0]
            try:
                print(f"用户[{name}]钓类型为{t}的鱼{fish_id}")
                fish(bp,fish_id)
                fished_dict[t].add(fish_id)
            except Exception as e:
                print("钓鱼失败,pass")
        photo_shot(bp)
        logout(bp)
        cur+=1
    print("全部钓完")

if __name__ == '__main__':
    with open("../statistics/hook_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容
    with open("../statistics/cast_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容

    bp = BasePage()
    fish_type_map, fished_dict = auto_fish_all_type(bp,"500305")

    # setSceneType x (x=1是pve，x=2是pvp, x=3是钓者挑战, x=4是新主线, x=5是爬塔)
    bp.custom_cmd("setSceneType 4")

    # 主函数，可以修改登录名称前缀：prefix
    # 若clone账号需要填写uid
    main(bp,fish_type_map,fished_dict,uid=1074242127)
    # photo_shot(bp)
    bp.connect_close()


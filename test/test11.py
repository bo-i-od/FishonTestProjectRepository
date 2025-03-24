import os
import time

from matplotlib.lines import Line2D

from common.basePage import BasePage
from common import gameInit
from configs.elementsData import ElementsData
from netMsg import csMsgAll
from panelObjs import BattlePreparePanel, BattlePanel, ResultPanel
from panelObjs.BattleDebugPanel import BattleDebugPanel
import matplotlib.pyplot as plt
from matplotlib import rcParams

from panelObjs.HomePanelNew import HomePanelNew
from panelObjs.MainStageFishSpotPanel import MainStageFishSpotPanel
from scripts.createUsers import logout, login
from tools.videoCompression import record_start, record_end


class Personality:
    qte_rate = 0
    tension = 0


class PersonalityNB(Personality):
    qte_rate = 1
    tension = 0.85


class PersonalityLJ(Personality):
    qte_rate = 0.66
    tension = 0.6


def deal_with_hold_status(hold_status):
    if not hold_status:
        return 0, 0
    hold = hold_status.split("收")[1].split("/")[0]
    if not hold:
        hold = '0'
    release = hold_status.split("放:")[1].split("/")[0]
    if not release:
        release = '0'
    return int(hold), int(release)


def parse_key_value(text):
    """
    扁平化解析所有键值对（最后出现的同名键会覆盖之前的值）
    输入示例文本返回格式：{ 'HOOK_DAMAGE': '15000', 'ULT_MODIFIER': '250', ... }
    """
    data = {}
    for line in text.split('\n'):
        # 清理行首尾空白并跳过空行
        cleaned_line = line.strip()
        if not cleaned_line:
            continue

        # 提取键值对（兼容包含多个冒号的情况）
        if ':' in cleaned_line and not cleaned_line.startswith(('------', 'Skill')):
            # 找到第一个冒号的位置
            colon_pos = cleaned_line.find(':')
            key = cleaned_line[:colon_pos].strip()
            value = cleaned_line[colon_pos + 1:].strip()

            # 特殊处理包含管道的行（如BUFF/SKILL中的复杂结构）
            if '|' in key:
                continue  # 跳过非简单键值对的行

            data[key] = value
    return data


def get_value(data_dict, key):
    """支持带类型的值获取（自动转换数字类型）"""
    value = data_dict.get(key)
    if value is None:
        return None
    # 类型转换逻辑
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    elif value == 'table':  # 特殊值处理
        return None
    return value


def get_m_max(content: str):
    try:
        m_max = content.split("LINE_LENGTH:")[1].split("STAR")[0].strip()
    except IndexError:
        m_max = None
    # save_text(content=content, filename=res)
    return m_max


def get_base_hp(content: str):
    try:
        base_hp = content.split("BaseHP:")[1].split("DamageReduceRate")[0].strip()
    except IndexError:
        base_hp = None
    return base_hp


def get_current_hp(content: str):
    try:
        current_hp = content.split("CURRENT_HP:")[1].split("VELOCITY_Z")[0].strip()
    except IndexError:
        current_hp = None
    return current_hp


def qte(bp, personality: Personality = None):
    element_data_list = [ElementsData.BattlePanel.qte_left, ElementsData.BattlePanel.qte_right,
                         ElementsData.BattlePanel.qte_dance_left, ElementsData.BattlePanel.qte_dance_right,
                         ElementsData.BattlePanel.qte_up, ElementsData.BattlePanel.qte_jump_left,
                         ElementsData.BattlePanel.qte_jump_right, ElementsData.BattlePanel.hud_power_list,
                         ElementsData.BattlePanel.hud_power_list_old, ElementsData.ResultPanel.btn_claim_pve,
                         ElementsData.ResultPanel.btn_claim_pvp, ElementsData.ResultPanel.btn_claim_token_fish,
                         ElementsData.MainStageBattleFailedPanel.btn_again,
                         ElementsData.BattleFailedPanel.btn_again,
                         ElementsData.FlashCardReceivePanel.FlashCardReceivePanel,
                         ElementsData.BattlePanel.warning,
                         ElementsData.MainlineFlashCardReceivePanel.MainlineFlashCardReceivePanel,
                         ElementsData.BattlePanel.BattlePanel,
                         ElementsData.BattlePanel.crt,
                         ElementsData.BattlePanel.crt2,
                         ElementsData.BattlePanel.progress
                         ]

    btn_claim_pve_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_pve)
    btn_claim_pvp_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_pvp)
    btn_claim_token_fish_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_token_fish)
    btn_again_index = element_data_list.index(ElementsData.BattleFailedPanel.btn_again)
    btn_again_2_index = element_data_list.index(ElementsData.MainStageBattleFailedPanel.btn_again)
    FlashCardReceivePanel_index = element_data_list.index(ElementsData.FlashCardReceivePanel.FlashCardReceivePanel)
    warning_index = element_data_list.index(ElementsData.BattlePanel.warning)
    MainlineFlashCardReceivePanel_index = element_data_list.index(ElementsData.MainlineFlashCardReceivePanel.MainlineFlashCardReceivePanel)
    crt_index = element_data_list.index(ElementsData.BattlePanel.crt)
    crt2_index = element_data_list.index(ElementsData.BattlePanel.crt2)
    progress_index = element_data_list.index(ElementsData.BattlePanel.progress)
    size_tension = None
    is_in_crt_pre = False

    m_cur = 0
    current_hp = 0
    m_max = 0
    base_hp = 0
    battle_damage = 0
    reel_velocity_z = 0
    start_time = None
    end_time = None
    t_one = 10
    hold_status_start = 0, 0
    data_list = []
    battle_time = 0
    time_remain = 0
    line_data = ""
    t = None
    while True:
        if start_time:
            t = time.time() - start_time
            t_ten = int(t) // 10
            t_one = t - t_ten * 10

        text_list = bp.get_text_list(element_data_list=[ElementsData.BattlePanel.m_value, ElementsData.BattleDebugPanel.content, ElementsData.BattleChallengeTimerHUD.time])
        if text_list[0]:
            m_cur = float(text_list[0][0].split("米")[0])
        if text_list[1]:
            content = text_list[1][0]
            content_dict = parse_key_value(content)
            # current_hp = get_current_hp(content)
            current_hp =get_value(content_dict,"CURRENT_HP")
            # m_max_temp = get_m_max(content)
            m_max_temp = get_value(content_dict, "LINE_LENGTH")
            if m_max_temp:
                m_max = float(m_max_temp)
            # base_hp_temp = get_base_hp(content)
            base_hp_temp = get_value(content_dict, "BaseHP")
            if base_hp_temp:
                base_hp = float(base_hp_temp)
            battle_damage_temp = get_value(content_dict, "STAMINA_DECREASE")
            if battle_damage_temp:
                battle_damage = float(battle_damage_temp)
            reel_velocity_z_temp = get_value(content_dict, "REEL_VELOCITY_Z")
            if reel_velocity_z_temp:
                reel_velocity_z = float(reel_velocity_z_temp)
        if text_list[2]:
            time_remain = float(text_list[2][0])

        if t and m_cur and current_hp:
            data_list.append((t, float(m_cur), float(current_hp)))
        object_id_list = bp.get_object_id_list(element_data_list=element_data_list)

        if object_id_list[progress_index]:
            bp.set_time_scale(1)
            bp.sleep(1)
            continue

        if object_id_list[crt_index] or object_id_list[crt2_index]:
            if size_tension is None:
                size_tension = bp.get_size(element_data=ElementsData.BattlePanel.hud_tension)
            if not is_in_crt_pre:
                is_in_crt_pre = True
            crt_center = BattlePanel.get_crt_center(bp, size_tension=size_tension)
            bp.custom_cmd(f"setTension {crt_center}")
        else:
            if is_in_crt_pre:
                is_in_crt_pre = False
                bp.custom_cmd(f"setTension {bp.tension_default}")

        if object_id_list[warning_index] and not start_time:
            show_data(bp)
            start_time = time.time()
            bp.sleep(0.1)
            hold_status = BattleDebugPanel.get_hold_status(bp)
            hold_status_start = deal_with_hold_status(hold_status)
        if (not object_id_list[warning_index]) and (start_time is not None):
            if end_time is None:
                end_time = time.time()
                battle_time = f"{(end_time - start_time):.1f}s"
                hold_status = BattleDebugPanel.get_hold_status(bp)
                hold_status_end = deal_with_hold_status(hold_status)
                time_hold = (hold_status_end[0] - hold_status_start[0])
                time_release = (hold_status_end[1] - hold_status_start[1])
                line_data = f"收线占比{100 * time_hold // (time_release + time_hold)}%"
            bp.set_time_scale(time_scale=time_scale)

        if object_id_list[btn_claim_pve_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_pve)
            bp.res = "成功"
            break
        if object_id_list[btn_claim_pvp_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_pvp)
            break
        if object_id_list[btn_claim_token_fish_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_token_fish)
            break
        if object_id_list[btn_again_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.BattleFailedPanel.btn_again)
            bp.res = "失败"
            break
        if object_id_list[btn_again_2_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.MainStageBattleFailedPanel.btn_again)
            bp.res = "失败"
            break
        if object_id_list[FlashCardReceivePanel_index]:
            bp.clear_popup()
            continue
        if object_id_list[MainlineFlashCardReceivePanel_index]:
            bp.clear_popup()
            continue
        # if t_one > personality.qte_rate * 10:
        #     bp.custom_cmd("setQuickQTE 0")
        # else:
        #     bp.custom_cmd("setQuickQTE 1")
        bp.sleep(0.1)
    return data_list, m_max, base_hp, battle_time, line_data, battle_damage, reel_velocity_z, time_remain

def show_data(bp: BasePage):
    text_list = bp.get_text(element_data=ElementsData.BattleDebugPanel.content)
    content_dict = parse_key_value(text_list)
    m_max_temp = get_value(content_dict, "LINE_LENGTH")
    base_hp_temp = get_value(content_dict, "BaseHP")
    battle_damage_temp = get_value(content_dict, "STAMINA_DECREASE")
    reel_velocity_z_temp = get_value(content_dict, "REEL_VELOCITY_Z")
    bp.set_text(element_data={"locator": "UICanvas>star(Clone)"},
                text=f"{bp.rod_lv}级{bp.rod_star}星装备 {bp.fish_kind}鱼 {bp.star}星渔场 {bp.name_line} {bp.name_lure} 第{bp.index}场  伤害:{battle_damage_temp} 线长:{m_max_temp} 收线:{reel_velocity_z_temp} 鱼血量上限:{base_hp_temp}")



def fish_once(bp: BasePage, fish_id="", personality=None):
    if fish_id != "":
        fishery_id = bp.fish_id_to_fishery_id(fish_id=fish_id)
        c = f"mode {fishery_id} {fish_id}"
        # print(c)
        bp.cmd(c)
    bp.custom_cmd(f"setTension {personality.tension}")
    BattlePreparePanel.click_btn_cast(bp)

    bp.custom_cmd("autofish")

    data_list, m_max, base_hp, battle_time, line_data, battle_damage, reel_velocity_z, time_remain = qte(bp, personality)
    plt_name = f"{bp.rod_lv}级{bp.rod_star}星装备_{bp.fish_kind}鱼_{bp.star}星渔场_{bp.name_line}{bp.name_lure}_{bp.index}_{bp.res}"
    write_log(plt_name)
    save_plt(data_list, m_max, base_hp, name=plt_name)
    write_log(f"鱼血量上限：{base_hp} 伤害：{battle_damage} 线长：{m_max} 跑线：{reel_velocity_z}")
    # print(f"剩余时间：{time_remain}s, 战斗时间：{battle_time}")
    write_log(f"战斗时间：{battle_time}")
    write_log("")
    write_log(line_data)
    if fish_id != "":
        bp.cmd("mode 0 0")

def get_gear(kind, rod_quality):
    if kind == 1:
        part_id_line = 1700001
        part_id_lure = 1700002
    elif kind == 2:
        part_id_line = 1700027
        part_id_lure = 1700028
    elif kind == 3:
        part_id_line = 1700029
        part_id_lure = 1700030
    elif kind == 4:
        part_id_line = 1700003
        part_id_lure = 1700006
    elif kind == 5:
        part_id_line = 1700004
        part_id_lure = 1700007
    elif kind == 6:
        part_id_line = 1700005
        part_id_lure = 1700008
    elif kind == 7:
        part_id_line = 1700031
        part_id_lure = 1700032
    elif kind == 8:
        part_id_line = 1700033
        part_id_lure = 1700034
    elif kind == 9:
        part_id_line = 1700035
        part_id_lure = 1700036
    elif kind == 10:
        part_id_line = 1700009
        part_id_lure = 1700010
    elif kind == 11:
        part_id_line = 1700011
        part_id_lure = 1700012
    elif kind == 12:
        part_id_line = 1700013
        part_id_lure = 1700014
    elif kind == 13:
        part_id_line = 1700015
        part_id_lure = 1700016
    elif kind == 14:
        part_id_line = 1700017
        part_id_lure = 1700018
    else:
        part_id_line = 1700019
        part_id_lure = 1700020

    if rod_quality == "紫":
        part_id_rod = 1901004
        return part_id_line, part_id_lure, part_id_rod
    if kind % 3 == 1:
        part_id_rod = 1901001
    elif kind % 3 == 2:
        part_id_rod = 1901002
    else:
        part_id_rod = 1901003

    return part_id_line, part_id_lure, part_id_rod

def change_gear(bp: BasePage, kind, rod_quality):
    # part_id_line = 0
    part_id_line, part_id_lure, part_id_rod = get_gear(kind, rod_quality)
    lua_code_line = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_line)
    lua_code_lure = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_lure)
    lua_code_rod = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_rod)
    bp.lua_console_list([lua_code_line, lua_code_lure, lua_code_rod])
    table_data_detail = bp.excelTools.get_table_data_detail(book_name="ADV_GEAR_LANGUAGE.xlsm")
    name_line = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=part_id_line, table_data_detail=table_data_detail)["name"]
    name_lure = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=part_id_lure, table_data_detail=table_data_detail)["name"]
    bp.name_line = name_line
    bp.name_lure = name_lure


def save_plt(data_list, m_max, base_hp, name):
    # 设置全局字体
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['SimHei']
    rcParams['axes.unicode_minus'] = False

    # 数据预处理
    t_values = [item[0] for item in data_list]
    d_normalized = [item[1] / m_max for item in data_list]
    hp_normalized = [item[2] / base_hp for item in data_list]

    # 创建可视化画布
    plt.figure(figsize=(12, 6), dpi=100)
    ax = plt.gca()

    # 绘制纯折线（修改点1：移除所有marker相关参数）
    line1, = ax.plot(t_values, d_normalized,
                     linewidth=1.5,
                     color='#2c7bb6',
                     label='线长')  # 移除marker参数

    line2, = ax.plot(t_values, hp_normalized,
                     linewidth=1.5,
                     color='#d7191c',
                     linestyle='--',  # 保留线型区分
                     label='鱼血量')  # 移除marker参数

    # 图表元数据
    plt.title('钓鱼状态监控', fontsize=14, pad=15)
    plt.xlabel('时间 (秒)', fontsize=12, labelpad=10)
    plt.ylabel('归一化值', fontsize=12, labelpad=10)

    # 坐标轴设置
    plt.xticks(fontsize=10)
    plt.yticks([i / 10 for i in range(11)],
               [f'{i * 10}%' for i in range(11)],
               fontsize=10)

    # 辅助线
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, color='#636363')
    ax.axhline(y=1, color='#d7191c', linestyle=':', linewidth=1.5)

    # 简化图例（修改点2：移除图例中的marker元素）
    legend_elements = [
        Line2D([0], [0],
               color='#2c7bb6',
               lw=1.5,
               label='线长'),
        Line2D([0], [0],
               color='#d7191c',
               lw=1.5,
               linestyle='--',
               label='鱼血量'),
        Line2D([0], [0],
               color='#d7191c',
               linestyle=':',
               lw=1.5,
               label='极限阈值')
    ]

    plt.legend(handles=legend_elements,
               loc='upper left',
               frameon=True,
               framealpha=0.8)

    # 显示范围
    plt.xlim(0, max(t_values) * 1.05)
    plt.ylim(0, 1.1)

    # 输出
    plt.tight_layout()
    savefig_autoname(f"{name}.png")


def savefig_autoname(base_name):
    """
    自动编号保存图片函数
    参数：
    base_name : 期望的文件名 (如 "plot.png")
    """
    # 分离文件名和扩展名
    name_part, ext = os.path.splitext(base_name)

    # 优先尝试原始文件名
    if not os.path.exists(base_name):
        plt.savefig(base_name)
        plt.close()
        # print(f"保存成功: {base_name}")
        return

    # 查找可用编号
    counter = 1
    while True:
        new_name = f"{name_part}_{counter}{ext}"
        if os.path.exists(new_name):
            counter += 1
            continue
        plt.savefig(new_name)
        plt.close()
        write_log(f"检测到重名文件，已保存为: {new_name}")
        return



def save_text(content, filename, mode='w', encoding='utf-8'):
    """
    智能保存文本内容到文件

    参数：
    - content : 要保存的内容（支持字符串/列表/字典）
    - filename : 目标文件名（如 "data.txt"）
    - mode : 写入模式，'w'覆盖 / 'a'追加
    - encoding : 文件编码
    """
    # 创建文件目录（如果不存在）
    dir_path = os.path.dirname(filename)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    # 处理不同数据类型
    if isinstance(content, (list, tuple)):
        content = '\n'.join(map(str, content))
    elif isinstance(content, dict):
        content = '\n'.join(f"{k}: {v}" for k, v in content.items())
    else:
        content = str(content)

    # 生成唯一文件名
    base, ext = os.path.splitext(filename)
    counter = 0
    while True:
        target_file = f"{base}_{counter}{ext}" if counter else filename
        if not os.path.exists(target_file) or mode == 'a':
            break
        counter += 1

    # 写入文件
    with open(target_file, mode, encoding=encoding) as f:
        f.write(content)

    # print(f"文件已保存到：{os.path.abspath(target_file)}")
    return target_file


def increase_star(bp: BasePage, fishery_star_range):

    write_log(f"{bp.rod_lv}级{bp.rod_star}星装备_{bp.fish_kind}鱼_{fishery_star_range[0]}至{fishery_star_range[1]}星渔场_{bp.name_line}{bp.name_lure}")
    star = fishery_star_range[0]
    while star <= fishery_star_range[1]:
        bp.star = star
        bp.cmd(f"fishscenestarset 500301 {star}")
        bp.star = star
        bp.index = 1
        fish_once(bp, fish_id=bp.fish_id, personality=personality)
        bp.index = 2
        bp.cmd(f"fishscenestarset 500301 {star}")
        fish_once(bp, fish_id=bp.fish_id, personality=personality)
        bp.set_text(element_data={"locator": "UICanvas>star(Clone)"}, text=f"")
        star += 2


def increase_gear(bp: BasePage, fishery_star_range, gear_kind_list, rod_quality):
    cur = 0
    while cur < len(gear_kind_list):
        change_gear(bp, kind=gear_kind_list[cur], rod_quality=rod_quality)
        bp.lua_console('PanelMgr:OpenPanel("GearMainPanel")')
        bp.sleep(0.5)
        bp.lua_console('PanelMgr:ClosePanel("GearMainPanel")')
        increase_star(bp, fishery_star_range)
        cur += 1

def increase_rod(bp: BasePage):
    cur = 0
    while cur < len(test_list):
        try:
            test = test_list[cur]
            bp.rod_lv = test["rod_lv"]
            bp.rod_star = test["rod_star"]
            bp.rod_quality = test["rod_quality"]
            bp.gear_quality = test["gear_quality"]
            file_name = f'{bp.rod_lv}级{bp.rod_star}星装备_{bp.fish_kind}鱼_{test["fishery_star_range"][0]}至{test["fishery_star_range"][1]}星渔场'
            bp.video = record_start(file_name=f"{file_name}.mp4")
            bp.sleep(1)
            write_log(file_name)
            login(bp, name=test["name"])
            # gameInit.guide_skip(bp)
            # bp.clear_popup()
            # bp.lua_console('PanelMgr:OpenPanel("HomePanelNew")')

            lua_code = """local battleController = ControllerMgr:Get("BattleController")
    battleController:GoToDaily(10101, true)
    """
            bp.lua_console(lua_code)

            if bp.fish_kind == "力":
                if bp.gear_quality == "紫":
                    gear_kind_list = [1]
                elif bp.gear_quality == "金":
                    gear_kind_list = [4, 7]
                else:
                    gear_kind_list = [10, 13]
            elif bp.fish_kind == "敏":
                if bp.gear_quality == "紫":
                    gear_kind_list = [2]
                elif bp.gear_quality == "金":
                    gear_kind_list = [5, 8]
                else:
                    gear_kind_list = [11, 14]
            else:
                if bp.gear_quality == "紫":
                    gear_kind_list = [3]
                elif bp.gear_quality == "金":
                    gear_kind_list = [6, 9]
                else:
                    gear_kind_list = [12, 15]

            increase_gear(bp, fishery_star_range=test["fishery_star_range"], gear_kind_list=gear_kind_list, rod_quality=bp.rod_quality)
        except Exception as e:
            print(e)
            record_end(bp.video)
            write_log("------------------------------")
            write_log("上方一个区间作废")
            write_log("------------------------------")
            logout(bp)
            bp.sleep(5)
            continue
        record_end(bp.video)
        write_log("------------------------------")
        write_log("")
        logout(bp)
        bp.sleep(5)
        cur += 1

def increase_fish_kind(bp: BasePage):
    fish_kind_list = ["力", "敏", "智"]
    cur = 0
    while cur < len(fish_kind_list):
        bp.fish_kind = fish_kind_list[cur]
        if bp.fish_kind == "力":
            bp.fish_id = "360113"
        elif bp.fish_kind == "敏":
            bp.fish_id = "360115"

        elif bp.fish_kind == "智":
            bp.fish_id = "360107"
        increase_rod(bp)
        cur += 1



def write_log(*msg):
    f = open("../test/log.txt", "a", encoding="utf-8")
    print(*msg)
    f.write(str(*msg) + '\n')
    f.close()

def main(bp: BasePage):
    # gameInit.guide_skip(bp)
    bp.is_time_scale = True
    bp.set_time_scale(time_scale=time_scale)
    bp.set_is_quick_qte(is_quick_qte=True)
    bp.set_hook_progress(hook_progress=0.85)
    bp.custom_cmd("setQTECD 0.45")
    increase_fish_kind(bp)
    bp.connect_close()


if __name__ == '__main__':
    bp1 = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")

    test_list = [
                 {"name": "y_30_0_0", "rod_lv": 30, "rod_star": 0,"gear_star": 0,"rod_quality":"紫", "gear_quality":"紫", "fishery_star_range": [3, 7]},
                 {"name": "y_60_0_0", "rod_lv": 60, "rod_star": 0, "gear_star": 0,"rod_quality":"紫", "gear_quality":"紫", "fishery_star_range": [7, 15]},
                 {"name": "y_90_0_0", "rod_lv": 90, "rod_star": 0, "gear_star": 0,"rod_quality":"紫", "gear_quality":"紫",  "fishery_star_range": [11, 19]},
                 {"name": "y_120_0_0", "rod_lv": 120, "rod_star": 0, "gear_star": 0,"rod_quality":"紫", "gear_quality":"紫",  "fishery_star_range": [17,25]},
                 {"name": "y_150_0_0", "rod_lv": 150, "rod_star": 0, "gear_star": 0,"rod_quality":"紫", "gear_quality":"紫",  "fishery_star_range": [21, 31]},
                 {"name": "y_215_0_0", "rod_lv": 215, "rod_star": 0, "gear_star": 0,"rod_quality":"紫", "gear_quality":"紫",  "fishery_star_range": [29, 39]},
                 {"name": "y_30_0_3", "rod_lv": 30, "rod_star": 0, "gear_star": 3,"rod_quality":"金", "gear_quality":"紫",  "fishery_star_range": [5, 13]},
                 {"name": "y_60_0_3", "rod_lv": 60, "rod_star": 0, "gear_star": 3,"rod_quality":"金", "gear_quality":"紫",  "fishery_star_range": [11, 19]},
                 {"name": "y_90_0_3", "rod_lv": 90, "rod_star": 0, "gear_star": 3,"rod_quality":"金", "gear_quality":"紫",  "fishery_star_range": [17, 25]},
                 {"name": "y_120_0_3", "rod_lv": 120, "rod_star": 0, "gear_star": 3,"rod_quality":"金", "gear_quality":"紫",  "fishery_star_range": [21, 31]},
                 {"name": "y_150_0_3", "rod_lv": 150, "rod_star": 0, "gear_star": 3,"rod_quality":"金", "gear_quality":"紫",  "fishery_star_range": [27, 35]},
                 {"name": "y_215_0_3", "rod_lv": 215, "rod_star": 0, "gear_star": 3, "rod_quality":"金", "gear_quality":"紫", "fishery_star_range": [37, 47]},
                 {"name": "y_30_0_0", "rod_lv": 30, "rod_star": 0, "gear_star": 0,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [3, 11]},
                 {"name": "y_60_0_0", "rod_lv": 60, "rod_star": 0, "gear_star": 0,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [9, 19]},
                 {"name": "y_90_0_0", "rod_lv": 90, "rod_star": 0, "gear_star": 0,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [15, 23]},
                 {"name": "y_120_0_0", "rod_lv": 120, "rod_star": 0, "gear_star": 0,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [21, 29]},
                 {"name": "y_150_0_0", "rod_lv": 150, "rod_star": 0, "gear_star": 0,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [25, 33]},
                 {"name": "y_215_0_0", "rod_lv": 215, "rod_star": 0, "gear_star": 0,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [35, 43]},
                 {"name": "y_30_2_2", "rod_lv": 30, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [5, 15]},
                 {"name": "y_60_2_2", "rod_lv": 60, "rod_star": 2, "gear_star": 2, "rod_quality":"金", "gear_quality":"金", "fishery_star_range": [12, 21]},
                 {"name": "y_90_2_2", "rod_lv": 90, "rod_star": 2, "gear_star": 2, "rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [19, 29]},
                 {"name": "y_120_2_2", "rod_lv": 120, "rod_star": 2, "gear_star": 2, "rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [25, 35]},
                 {"name": "y_150_2_2", "rod_lv": 150, "rod_star": 2, "gear_star": 2, "rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [31, 39]},
                 {"name": "y_215_2_2", "rod_lv": 215, "rod_star": 2, "gear_star": 2, "rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [41, 49]},
    #              {"name": "y_30_4_4", "rod_lv": 30, "rod_star": 4, "gear_star": 4,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [9, 19]},
    #              {"name": "y_60_4_4", "rod_lv": 60, "rod_star": 4, "gear_star": 4,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [17, 25]},
    #              {"name": "y_90_4_4", "rod_lv": 90, "rod_star": 4, "gear_star": 4,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [25, 33]},
    #              {"name": "y_120_4_4", "rod_lv": 120, "rod_star": 4, "gear_star": 4, "rod_quality":"金", "gear_quality":"金", "fishery_star_range": [31, 39]},
    #              {"name": "y_150_4_4", "rod_lv": 150, "rod_star": 4, "gear_star": 4,"rod_quality":"金", "gear_quality":"金",  "fishery_star_range": [37, 45]},
    #              {"name": "y_215_4_4", "rod_lv": 215, "rod_star": 4, "gear_star": 4, "rod_quality":"金", "gear_quality":"金", "fishery_star_range": [45, 55]},
    #              {"name": "y_30_2_0", "rod_lv": 30, "rod_star": 2, "gear_star": 0,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [7, 17]},
    #              {"name": "y_60_2_0", "rod_lv": 60, "rod_star": 2, "gear_star": 0,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [15, 23]},
    #              {"name": "y_90_2_0", "rod_lv": 90, "rod_star": 2, "gear_star": 0,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [21, 29]},
    #              {"name": "y_120_2_0", "rod_lv": 120, "rod_star": 2, "gear_star": 0,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [29, 37]},
    #              {"name": "y_150_2_0", "rod_lv": 150, "rod_star": 2, "gear_star": 0,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [33, 41]},
    #              {"name": "y_215_2_0", "rod_lv": 215, "rod_star": 2, "gear_star": 0,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [43, 51]},
    #              {"name": "y_30_2_2", "rod_lv": 30, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [9, 19]},
    #              {"name": "y_60_2_2", "rod_lv": 60, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [17, 25]},
    #              {"name": "y_90_2_2", "rod_lv": 90, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [25, 33]},
    #              {"name": "y_120_2_2", "rod_lv": 120, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [31, 39]},
    #              {"name": "y_150_2_2", "rod_lv": 150, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [37, 45]},
    #              {"name": "y_215_2_2", "rod_lv": 215, "rod_star": 2, "gear_star": 2,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [45, 53]},
    #              {"name": "y_30_2_5", "rod_lv": 30, "rod_star": 2, "gear_star": 5,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [13, 23]},
    #              {"name": "y_60_2_5", "rod_lv": 60, "rod_star": 2, "gear_star": 5,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [23, 31]},
    #              {"name": "y_90_2_5", "rod_lv": 90, "rod_star": 2, "gear_star": 5,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [31, 39]},
    #              {"name": "y_120_2_5", "rod_lv": 120, "rod_star": 2, "gear_star": 5,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [37, 45]},
    #              {"name": "y_150_2_5", "rod_lv": 150, "rod_star": 2, "gear_star": 5,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [43, 51]},
    #              {"name": "y_215_2_5", "rod_lv": 215, "rod_star": 2, "gear_star": 5,"rod_quality":"金", "gear_quality":"红",  "fishery_star_range": [51, 59]},

                 ]
    time_scale = 4
    # bp2 = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")

    # 装备等级


    # 套装0-9
    # 0.初始 1.强力收线/强力爆气 2.强力回拉/强力刺鱼 3.技巧拔竿/技巧压制 4.远交近攻/鱼跃反制 5.绝佳时机/暴力挥杆 6.越挫越勇/贴身肉搏 7.超负荷气 8.长线绝杀 9.不动如山 10.乘胜追击 11.背水一战 12.一刺入魂




    # is_restrain = False

    # PersonalityNB是挂机高手
    # PersonalityLJ是挂机菜鸡
    personality = PersonalityNB()

    # res = f"{rod_lv}级_{star}星"




    # if is_restrain:
    #     res += "_克制"
    # else:
    #     res += "_非克制"
    #     fish_kind += 1
    # if fish_kind > 3:
    #     fish_kind = 1

    # if personality.__class__ is PersonalityLJ:
    #     res += "_菜鸡"
    # else:
    #     res += "_高手"
    main(bp1)


    # main(bp2)

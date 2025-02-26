import os
import time

from common.basePage import BasePage
from configs.elementsData import ElementsData
from netMsg import csMsgAll
from panelObjs import BattlePreparePanel, BattlePanel, ResultPanel
from panelObjs.BattleDebugPanel import BattleDebugPanel
import matplotlib.pyplot as plt
from matplotlib import rcParams

class Personality:
    qte_rate = 0
    tension = 0


class PersonalityNB(Personality):
    qte_rate = 0.75
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

def get_m_max(content: str):
    m_max = content.split("LINE_LENGTH:")[1].split("STAR")[0].strip()
    save_text(content=content, filename=res)
    return float(m_max)

def qte(bp, personality: Personality = None):
    element_data_list = [ElementsData.BattlePanel.qte_left, ElementsData.BattlePanel.qte_right,
                         ElementsData.BattlePanel.qte_dance_left, ElementsData.BattlePanel.qte_dance_right,
                         ElementsData.BattlePanel.qte_up, ElementsData.BattlePanel.qte_jump_left,
                         ElementsData.BattlePanel.qte_jump_right, ElementsData.BattlePanel.hud_power_list,
                         ElementsData.BattlePanel.hud_power_list_old, ElementsData.ResultPanel.btn_claim_pve,
                         ElementsData.ResultPanel.btn_claim_pvp, ElementsData.ResultPanel.btn_claim_token_fish,
                         ElementsData.BattleFailedPanel.btn_again,
                         ElementsData.FlashCardReceivePanel.FlashCardReceivePanel,
                         ElementsData.BattlePanel.warning,
                         ElementsData.MainlineFlashCardReceivePanel.MainlineFlashCardReceivePanel,
                         ElementsData.BattlePanel.BattlePanel,
                         ElementsData.BattlePanel.crt,
                         ]
    qte_left_index = element_data_list.index(ElementsData.BattlePanel.qte_left)
    qte_right_index = element_data_list.index(ElementsData.BattlePanel.qte_right)
    qte_up_index = element_data_list.index(ElementsData.BattlePanel.qte_up)
    qte_dance_right_index = element_data_list.index(ElementsData.BattlePanel.qte_dance_right)
    qte_dance_left_index = element_data_list.index(ElementsData.BattlePanel.qte_dance_left)
    qte_jump_left_index = element_data_list.index(ElementsData.BattlePanel.qte_jump_left)
    qte_jump_right_index = element_data_list.index(ElementsData.BattlePanel.qte_jump_right)
    hud_power_list_index = element_data_list.index(ElementsData.BattlePanel.hud_power_list)
    hud_power_list_old_index = element_data_list.index(ElementsData.BattlePanel.hud_power_list_old)
    btn_claim_pve_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_pve)
    btn_claim_pvp_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_pvp)
    btn_claim_token_fish_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_token_fish)
    btn_again_index = element_data_list.index(ElementsData.BattleFailedPanel.btn_again)
    FlashCardReceivePanel_index = element_data_list.index(ElementsData.FlashCardReceivePanel.FlashCardReceivePanel)
    warning_index = element_data_list.index(ElementsData.BattlePanel.warning)
    MainlineFlashCardReceivePanel_index = element_data_list.index(ElementsData.MainlineFlashCardReceivePanel.MainlineFlashCardReceivePanel)
    BattlePanel_index = element_data_list.index(ElementsData.BattlePanel.BattlePanel)
    crt_index = element_data_list.index(ElementsData.BattlePanel.crt)
    size_tension = None
    is_in_crt_pre = False

    m_cur = ""
    content = bp.get_text(element_data=ElementsData.BattleDebugPanel.content)
    m_max = get_m_max(content)
    start_time = None
    end_time = None
    t_one = 10
    hold_status_start = 0, 0
    m_list = []
    battle_time = 0
    line_data = ""
    t = None
    while True:
        if start_time:
            t = time.time() - start_time
            t_ten = int(t) // 10
            t_one = t - t_ten * 10

        text_list = bp.get_text_list(element_data=ElementsData.BattlePanel.m_value)
        if text_list:
            m_cur = text_list[0].split("米")[0]
        if t:
            m_list.append((t, float(m_cur)))
        object_id_list = bp.get_object_id_list(element_data_list=element_data_list)

        if object_id_list[crt_index]:
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
            start_time = time.time()
            bp.sleep(0.1)
            hold_status = BattleDebugPanel.get_hold_status(bp)
            hold_status_start = deal_with_hold_status(hold_status)
        # if len(object_id_list[hud_power_list_index]) > 2:
        #     BattlePanel.unleash_power(bp)
        #     continue
        # if len(object_id_list[hud_power_list_old_index]) > 2:
        #     BattlePanel.unleash_power(bp)
        #     continue
        # if object_id_list[qte_up_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "up")
        #     continue
        # if object_id_list[qte_jump_left_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "left")
        #     continue
        # if object_id_list[qte_jump_right_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "right")
        #     continue
        # if object_id_list[qte_dance_left_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "left")
        #     continue
        # if object_id_list[qte_dance_right_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "right")
        #     continue
        # if object_id_list[qte_left_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "left")
        #     continue
        # if object_id_list[qte_right_index]:
        #     if t_one > personality.qte_rate * 10:
        #         continue
        #     BattlePanel.slide(bp, "right")
        #     continue
        if (not object_id_list[warning_index]) and (end_time is None) and (start_time is not None):
            end_time = time.time()
            battle_time = f"{(end_time - start_time):.1f}s"
            hold_status = BattleDebugPanel.get_hold_status(bp)
            hold_status_end = deal_with_hold_status(hold_status)
            time_hold = (hold_status_end[0] - hold_status_start[0])
            time_release = (hold_status_end[1] - hold_status_start[1])
            line_data = f"收线占比{100 * time_hold // (time_release + time_hold)}%"
            # print(time_hold, time_release)

        if object_id_list[btn_claim_pve_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_pve)
            break
        if object_id_list[btn_claim_pvp_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_pvp)
            break
        if object_id_list[btn_claim_token_fish_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_token_fish)
            break
        if object_id_list[btn_again_index]:
            ResultPanel.automatic_settlement(bp, element_btn=ElementsData.BattleFailedPanel.btn_again)
            break
        if object_id_list[FlashCardReceivePanel_index]:
            bp.clear_popup()
            continue
        if object_id_list[MainlineFlashCardReceivePanel_index]:
            bp.clear_popup()
            continue
        if t_one > personality.qte_rate * 10:
            bp.custom_cmd("setQuickQTE 0")
        else:
            bp.custom_cmd("setQuickQTE 1")
        bp.sleep(0.1)
    return m_list, m_max, battle_time, line_data

    

def fish_once(bp: BasePage, fish_id="", personality=None):
    if fish_id != "":
        fishery_id = bp.fish_id_to_fishery_id(fish_id=fish_id)
        c = f"mode {fishery_id} {fish_id}"
        # print(c)
        bp.cmd(c)
    bp.custom_cmd(f"setTension {personality.tension}")
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    if BattlePanel.is_reel_active(bp):
        bp.custom_cmd("autofish")

    m_list, m_max, battle_time, line_data = qte(bp, personality)
    print(bp.serial_number)
    print(res)
    print(battle_time)
    print(line_data)
    save_plt(m_list, m_max)
    if fish_id != "":
        bp.cmd("mode 0 0")


def change_gear(bp: BasePage, kind):
    # part_id_line = 0
    if kind == 1:
        part_id_line = 1700003
        part_id_lure = 1700006
    elif kind == 2:
        part_id_line = 1700004
        part_id_lure = 1700007
    elif kind == 3:
        part_id_line = 1700005
        part_id_lure = 1700008
    elif kind == 4:
        part_id_line = 1700009
        part_id_lure = 1700010
    elif kind == 5:
        part_id_line = 1700011
        part_id_lure = 1700012
    elif kind == 6:
        part_id_line = 1700013
        part_id_lure = 1700014
    elif kind == 7:
        part_id_line = 1700015
        part_id_lure = 1700016
    elif kind == 8:
        part_id_line = 1700017
        part_id_lure = 1700018
    elif kind == 9:
        part_id_line = 1700019
        part_id_lure = 1700020
    else:
        part_id_line = 1700001
        part_id_lure = 1700002
    # if level < 15:
    #     if kind == 1:
    #         part_id_line = 1700001
    #     elif kind == 2:
    #         part_id_line = 1700027
    #     elif kind == 3:
    #         part_id_line = 1700029
    #
    # elif level < 120:
    #     if kind == 1:
    #         part_id_line = 1700031
    #     elif kind == 2:
    #         part_id_line = 1700033
    #     elif kind == 3:
    #         part_id_line = 1700035
    #
    # elif level < 210:
    #     if kind == 1:
    #         part_id_line = 1700015
    #     elif kind == 2:
    #         part_id_line = 1700017
    #     elif kind == 3:
    #         part_id_line = 1700019
    #
    # else:
    #     if kind == 1:
    #         part_id_line = 1700021
    #     elif kind == 2:
    #         part_id_line = 1700023
    #     elif kind == 3:
    #         part_id_line = 1700025
    # part_id_lure = part_id_line + 1
    lua_code_line = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_line)
    lua_code_lure = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_lure)
    bp.lua_console_list([lua_code_line, lua_code_lure])

def save_plt(m_list, m_max):
    # 设置全局字体
    rcParams['font.family'] = 'sans-serif'  # 通用字体族
    rcParams['font.sans-serif'] = ['SimHei']  # Windows系统中文黑体
    rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    # 后续绘图代码保持原样...

    # 数据预处理
    t_values = [item[0] for item in m_list]  # 提取时间序列
    d_normalized = [item[1] / m_max for item in m_list]  # 计算归一化距离

    # 创建可视化画布
    plt.figure(figsize=(12, 6), dpi=100)

    # 绘制归一化距离曲线
    plt.plot(t_values, d_normalized,
             linewidth=1.5,
             color='#2c7bb6',
             marker='o',
             markersize=4,
             markerfacecolor='#fdae61',
             markeredgewidth=0,
             label='归一化距离')

    # 图表装饰
    plt.title('归一化距离随时间变化趋势', fontsize=14, pad=15)
    plt.xlabel('时间 (秒)', fontsize=12, labelpad=10)
    plt.ylabel('归一化距离', fontsize=12, labelpad=10)

    # 坐标轴设置
    plt.xticks(fontsize=10)
    plt.yticks([i / 10 for i in range(11)],
               [f'{i * 10}%' for i in range(11)],  # 百分比格式显示
               fontsize=10)

    # 辅助元素
    plt.grid(True,
             linestyle='--',
             linewidth=0.5,
             alpha=0.7,
             color='#636363')
    plt.axhline(y=1,
                color='#d7191c',
                linestyle=':',
                linewidth=1.5,
                label='鱼线极限')

    # 显示图例
    plt.legend(loc='upper left',
               frameon=True,
               framealpha=0.8)

    # 优化显示范围
    plt.xlim(0, max(t_values) * 1.05)
    plt.ylim(0, 1.05)

    # 显示图表
    plt.tight_layout()
    savefig_autoname(f"{res}.png")  # 默认格式为PNG


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
        # print(f"保存成功: {base_name}")
        return

    # 查找可用编号
    counter = 1
    while True:
        new_name = f"{name_part}_{counter}{ext}"
        if not os.path.exists(new_name):
            plt.savefig(new_name)
            print(f"检测到重名文件，已保存为: {new_name}")
            return
        counter += 1


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


def main(bp: BasePage):
    bp.is_time_scale = True
    bp.set_time_scale(time_scale=5)
    change_gear(bp, kind=gear_kind)
    bp.lua_console('PanelMgr:OpenPanel("GearPanelNew")')
    bp.sleep(0.5)
    bp.lua_console('PanelMgr:ClosePanel("GearPanelNew")')
    bp.cmd(f"fishscenestarset 500301 {star}")
    fish_once(bp, fish_id=fish_id, personality=personality)
    bp.connect_close()


if __name__ == '__main__':
    bp1 = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    # bp2 = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")

    # # 装备等级
    # lv = 30

    # 1力 2敏 3智
    fish_kind = 3

    # 套装0-9
    # 0.初始 1.强力收线/强力爆气 2.强力回拉/强力刺鱼 3.技巧拔竿/技巧压制 4.超负荷气 5.长线绝杀 6.不动如山 7.乘胜追击 8.背水一战 9.一刺入魂
    gear_kind = 1

    # 渔场难度
    star = 61

    # is_restrain = False

    # PersonalityNB是挂机高手
    # PersonalityLJ是挂机菜鸡
    personality = PersonalityNB()

    # res = f"{lv}级_{star}星"
    res = f"套装{gear_kind}"
    res += f"_{star}星"
    if fish_kind == 1:
        fish_id = "360113"
        res += "力"
    elif fish_kind == 2:
        fish_id = "360115"
        res += "敏"
    elif fish_kind == 3:
        fish_id = "360107"
        res += "智"

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

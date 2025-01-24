import time

from common.basePage import BasePage
from configs.elementsData import ElementsData
from netMsg import csMsgAll
from panelObjs import BattlePreparePanel, BattlePanel, ResultPanel
from panelObjs.BattleDebugPanel import BattleDebugPanel


class Personality:
    qte_rate = 0
    tension = 0


class PersonalityNB(Personality):
    qte_rate = 1
    tension = 0.9


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

def qte(bp, personality: Personality = None):
    element_data_list = [ElementsData.BattlePanel.qte_left, ElementsData.BattlePanel.qte_right,
                         ElementsData.BattlePanel.qte_dance_left, ElementsData.BattlePanel.qte_dance_right,
                         ElementsData.BattlePanel.qte_up, ElementsData.BattlePanel.qte_jump_left,
                         ElementsData.BattlePanel.qte_jump_right, ElementsData.BattlePanel.hud_power_list,
                         ElementsData.BattlePanel.hud_power_list_old, ElementsData.ResultPanel.btn_claim_pve,
                         ElementsData.ResultPanel.btn_claim_pvp, ElementsData.ResultPanel.btn_claim_token_fish,
                         ElementsData.BattleFailedPanel.btn_again,
                         ElementsData.FlashCardReceivePanel.FlashCardReceivePanel,
                         ElementsData.BattlePanel.warning
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

    m_cur = ""
    m_max = ""
    start_time = None
    end_time = None
    t_one = 10
    hold_status_start = 0, 0
    while True:
        if start_time:
            t = time.time() - start_time
            t_ten = int(t) // 10
            t_one = t - t_ten * 10

        text_list = bp.get_text_list(element_data_list=[ElementsData.BattlePanel.m_value, ElementsData.BattlePanel.hud_escaping])
        if text_list[0]:
            m_cur = text_list[0][0]
        if text_list[1]:
            m_max = text_list[1][0]
        object_id_list = bp.get_object_id_list(element_data_list=element_data_list)
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
        #     if t_one > personality.qte_up_rate * 10:
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
            print(f"{(end_time - start_time):.1f}s")
            print(f"{m_cur}/{m_max}")
            hold_status = BattleDebugPanel.get_hold_status(bp)
            hold_status_end = deal_with_hold_status(hold_status)
            time_hold = (hold_status_end[0] - hold_status_start[0])
            time_release = (hold_status_end[1] - hold_status_start[1])
            print(f"收线占比{100 * time_hold // (time_release + time_hold)}%")
            print(time_hold, time_release)

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
        if t_one > personality.qte_rate * 10:
            bp.custom_cmd("setQuickQTE 0")
        else:
            bp.custom_cmd("setQuickQTE 1")
        bp.sleep(0.1)

    

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

    qte(bp, personality)
    if fish_id != "":
        bp.cmd("mode 0 0")

def change_gear(bp: BasePage, level, kind):
    part_id_line = 0
    if level < 15:
        if kind == 1:
            part_id_line = 1700001
        elif kind == 2:
            part_id_line = 1700027
        elif kind == 3:
            part_id_line = 1700029


    elif level < 120:
        if kind == 1:
            part_id_line = 1700031
        elif kind == 2:
            part_id_line = 1700033
        elif kind == 3:
            part_id_line = 1700035

    elif level < 210:
        if kind == 1:
            part_id_line = 1700015
        elif kind == 2:
            part_id_line = 1700017
        elif kind == 3:
            part_id_line = 1700019

    else:
        if kind == 1:
            part_id_line = 1700021
        elif kind == 2:
            part_id_line = 1700023
        elif kind == 3:
            part_id_line = 1700025
    part_id_lure = part_id_line + 1
    lua_code_line = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_line)
    lua_code_lure = csMsgAll.get_CSEquipPrepareReplaceMsg(prepareIndex=1, dlc=1, partId=part_id_lure)
    bp.lua_console_list([lua_code_line, lua_code_lure])


def main(bp: BasePage):
    bp.cmd(f"fishscenestarset 500301 {star}")
    fish_once(bp, fish_id=fish_id, personality=personality)

# 7 8 12 13 14 15

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    bp.custom_cmd("setQuickQTE 1")
    # 360107智 360113速 360115力
    fish_id = "360115"
    star = 11
    lv = 45
    is_restrain = False
    personality = PersonalityLJ()
    res = f"{lv}级_{star}星"
    fish_kind = ""
    if fish_id == "360113":
        fish_kind = 1
        res += "力"
    elif fish_id == "360115":
        fish_kind = 2
        res += "敏"
    elif fish_id == "360107":
        fish_kind = 3
        res += "智"
    elif fish_id == "360101":
        fish_kind = 1
        res += "力"
    elif fish_id == "360104":
        fish_kind = 2
        res += "敏"
    elif fish_id == "360102":
        fish_kind = 3
        res += "智"
    if is_restrain:
        res += "_克制"
    else:
        res += "_非克制"
        fish_kind += 1
    if fish_kind > 3:
        fish_kind = 1

    if personality.__class__ is PersonalityLJ:
        res += "_菜鸡"
    else:
        res += "_高手"
    change_gear(bp, level=lv, kind=fish_kind)
    print(res)
    bp.lua_console('PanelMgr:OpenPanel("GearPanelNew")')
    bp.sleep(0.5)
    bp.lua_console('PanelMgr:ClosePanel("GearPanelNew")')

    main(bp)
    bp.connect_close()
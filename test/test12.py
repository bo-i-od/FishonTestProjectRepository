from common.basePage import BasePage
from netMsg import csMsgAll
from panelObjs.ChallengeMainStagePanel import ChallengeMainStagePanel
from panelObjs.MainStageSettlePanel import MainStageSettlePanel
from test import test11



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

def main(bp: BasePage):
    cur = start
    while cur <= end:
        index = str(cur)
        if cur < 10:
            index = "0" + index
        bp.cmd(f"setChallenge 1 10000{index}")
        ChallengeMainStagePanel.click_btn_orange(bp)
        data_list, m_max, base_hp = test11.fish_once(bp, personality=personality)

        status = MainStageSettlePanel.get_status(bp)
        name = f"关卡{cur}" + status
        print(name)
        test11.save_plt(data_list, m_max, base_hp, name=name)

        MainStageSettlePanel.click_btn_blue(bp)
        cur += 1

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    bp.quick_qte = True
    bp.custom_cmd("setQuickQTE 1")
    bp.custom_cmd("setQTECD 1")
    bp.custom_cmd("setQTECD 1")

    personality = test11.PersonalityNB()
    bp.custom_cmd(f"setTensionEscape {personality.tension}")
    # 0.初始 1.强力收线/强力爆气 2.强力回拉/强力刺鱼 3.技巧拔竿/技巧压制 4.超负荷气 5.长线绝杀 6.不动如山 7.乘胜追击 8.背水一战 9.一刺入魂
    # 力克制 1 4 7, 敏克制 2 5 8, 智克制 3 6 9
    # 90级及以下用 力1 敏2 智3
    # 90级以上用 力7 敏8 智9
    # 非克制情况， 打力鱼用敏，打敏鱼用智，打智鱼用力

    # battleTest.circulate_fish(bp)
    start = 30
    end = 50
    gear_kind = 3
    change_gear(bp, kind=gear_kind)
    print(f"装备{gear_kind}")
    # bp.lua_console('PanelMgr:OpenPanel("GearPanelNew")')
    # bp.sleep(0.5)
    # bp.lua_console('PanelMgr:ClosePanel("GearPanelNew")')

    main(bp)


    bp.connect_close()

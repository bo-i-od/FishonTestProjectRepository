from common.basePage import BasePage

from panelObjs.buyEnergyPanel import BuyEnergyPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.champoinshipTournamentsPanel import ChampoinshipTournamentsPanel


def circulate_chest(bp: BasePage):
    res_dict = {}
    cur = 0
    count_gold = 0
    count_silver = 0
    count_normal = 0
    while True:
        BattlePreparePanel.click_btn_cast(bp)
        while BuyEnergyPanel.is_panel_active(bp):
            BuyEnergyPanel.get_energy(bp)
            bp.sleep(0.5)
            BuyEnergyPanel.click_tap_to_close(bp)
            bp.sleep(0.5)
            BattlePreparePanel.click_btn_cast(bp)
        BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        chest_icon, temp_dict = ResultPanel.automatic_settlement(bp)
        res_dict = update_dict(chest_icon,temp_dict, res_dict)
        cur += 1
        if "ChestNormal" == chest_icon:
            count_normal+=1
        elif "ChestSilver" == chest_icon:
            count_silver+=1
        elif "ChestGold" == chest_icon:
            count_gold += 1
        rate_normal = format(count_normal/float(cur),".3f")
        rate_silver = format(count_silver / float(cur), ".3f")
        rate_gold = format(count_gold / float(cur), ".3f")
        print(f"共计钓了{cur}次,金箱子:{rate_gold},银箱子:{rate_silver},木箱子:{rate_normal}")
        print(res_dict)

def circulate_sundries(bp: BasePage):
    BattlePanel.reel_without_sleep(bp)
    # cur = 0
    # while True:
    #     BattlePreparePanel.cast(bp)


def robot_test(bp: BasePage):
    res_dict = {}
    cur = 0
    rank_list, name_list, points_list = ChampoinshipTournamentsPanel.get_rank_data(bp)
    ChampoinshipTournamentsPanel.save_rank_data(bp, rank_list, name_list, points_list, cur)
    while cur < 50:
        BattlePreparePanel.cast(bp)
        while BuyEnergyPanel.is_panel_active(bp):
            BuyEnergyPanel.get_energy(bp)
            bp.sleep(0.5)
            BuyEnergyPanel.click_tap_to_close(bp)
            bp.sleep(0.5)
            BattlePreparePanel.cast(bp)
        BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        chest_icon, temp_dict = ResultPanel.automatic_settlement(bp)
        res_dict = update_dict(chest_icon,temp_dict, res_dict)
        cur += 1
        if cur % 1 == 0:
            rank_list, name_list, points_list = ChampoinshipTournamentsPanel.get_rank_data(bp)
            ChampoinshipTournamentsPanel.save_rank_data(bp, rank_list, name_list, points_list, cur)

def circulate_fish(bp: BasePage):
    cur = 0
    fish = 0
    while True:
        bp.cmd(f"mode 400308 30801{int(cur / 3)}")
        BattlePreparePanel.click_btn_cast(bp)
        while BuyEnergyPanel.is_panel_active(bp):
            BuyEnergyPanel.get_energy(bp)
            bp.sleep(0.5)
            BuyEnergyPanel.click_tap_to_close(bp)
            bp.sleep(0.5)
            BattlePreparePanel.click_btn_cast(bp)
        BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        img = bp.get_full_screen_shot()
        bp.save_img(img)
        if ResultPanel.automatic_settlement(bp, is_return=False) == 1:
            fish += 1
        cur += 1
        # print(f"第{cur}次钓鱼,鱼的概率为{fish/float(cur)}")


def update_dict(chest_icon: str, temp_dict: dict, res_dict: dict):
    if temp_dict == {}:
        return res_dict
    for temp in temp_dict:
        key = chest_icon + "-" + temp + "-" + str(temp_dict[temp])
        if key in res_dict:
            res_dict[key] += 1
            continue
        res_dict[key] = 1
    return res_dict

# def update_dict(temp_dict, res_dict):
#     if temp_dict == {}:
#         return {}
#     for temp in temp_dict:
#         if temp in res_dict:
#             res_dict[temp] += temp_dict[temp]
#         res_dict[temp] = temp_dict[temp]


if __name__ == '__main__':
    bp = BasePage()
    circulate_fish(bp)





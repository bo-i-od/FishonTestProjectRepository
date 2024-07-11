import random
from common.basePage import BasePage
from netMsg import csMsgAll
from panelObjs.commonItemGetPanel import CommonItemGetPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from tools.commonTools import *
from common import resource, gameInit
from panelObjs.gearPanel import GearPanel
from panelObjs.gearLevelupPanel import GearLevelupPanel
from panelObjs.gearEnhancePanel import GearEnhancePanel
from panelObjs.storePanel import StorePanel
from panelObjs.gearSkillTipsPanel import GearSkillTipsPanel
from panelObjs.gearEnhanceSuccesPanel import GearEnhanceSuccesPanel
from panelObjs.flashTipsPanel import FlashTipsPanel


def lock_test(bp: BasePage):
    # 随机选取未解锁鱼竿
    GearPanel.select_lock_rod(bp)

    # 点击升级按钮
    rod_info_gear = GearPanel.get_rod_info(bp)
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(1)

    rod_info_gear_levelup = GearLevelupPanel.get_rod_info(bp)
    compare(rod_info_gear, rod_info_gear_levelup)
    GearLevelupPanel.click_btn_upgrade(bp)
    bp.sleep(1)

    # 无法升级 所以数值应该不变
    rod_info_gear_levelup_cur = GearLevelupPanel.get_rod_info(bp)
    compare(rod_info_gear_levelup, rod_info_gear_levelup_cur)
    GearLevelupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点击升星按钮
    GearPanel.click_btn_enhance(bp)
    bp.sleep(1)
    rod_info_gear_enhance = GearEnhancePanel.get_rod_info(bp)
    compare(rod_info_gear, rod_info_gear_enhance)
    GearEnhancePanel.click_btn_enhance(bp)
    bp.sleep(1)

    # 无法升级 所以数值应该不变
    rod_info_gear_enhance_cur = GearEnhancePanel.get_rod_info(bp)
    compare(rod_info_gear_enhance, rod_info_gear_enhance_cur)

    # 点击技能
    skill_icon = GearEnhancePanel.get_skill_icon(bp)
    GearEnhancePanel.click_skill_icon(bp)
    bp.sleep(1)
    tips_skill_icon = GearSkillTipsPanel.get_skill_icon(bp)
    compare(skill_icon, tips_skill_icon)
    bp.click_position([0.5, 0.9])
    bp.sleep(1)

    GearEnhancePanel.click_btn_close(bp)

def unlock_test(bp: BasePage):
    # 随机选取已解锁鱼竿
    GearPanel.select_unlock_rod(bp)

    # 点击升级按钮
    rod_info_gear = GearPanel.get_rod_info(bp)
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    rod_info_gear_levelup = GearLevelupPanel.get_rod_info(bp)
    compare(rod_info_gear, rod_info_gear_levelup)

    # 点击next切换鱼竿 对照信息
    GearLevelupPanel.click_btn_next(bp)
    bp.sleep(1)
    rod_info_gear_next = GearLevelupPanel.get_rod_info(bp)
    if rod_info_gear_levelup == rod_info_gear_next:
        bp.debug_log("erro_", "rod_info_gear_levelup == rod_info_gear_next", rod_info_gear_levelup, rod_info_gear_next)

    # 再点击previous切回来 对照信息
    GearLevelupPanel.click_btn_previous(bp)
    bp.sleep(1)
    rod_info_gear_previous = GearLevelupPanel.get_rod_info(bp)
    compare(rod_info_gear_levelup, rod_info_gear_previous)

    # 无法升级弹出
    GearLevelupPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    CommonItemGetPanel.click_btn_close(bp)
    bp.sleep(1)

    # 再对照信息
    rod_info_gear_cur = GearLevelupPanel.get_rod_info(bp)
    compare(rod_info_gear_levelup, rod_info_gear_cur)

    GearLevelupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点击升星按钮
    rod_info_gear = GearPanel.get_rod_info(bp)
    GearPanel.click_btn_enhance(bp)
    bp.sleep(1)
    rod_info_gear_enhance = GearEnhancePanel.get_rod_info(bp)
    compare(rod_info_gear, rod_info_gear_enhance)

    # 点击next切换鱼竿 对照信息
    GearEnhancePanel.click_btn_next(bp)
    bp.sleep(1)
    rod_info_gear_next = GearEnhancePanel.get_rod_info(bp)
    if rod_info_gear_enhance == rod_info_gear_next:
        bp.debug_log("erro_", "rod_info_gear_enhance == rod_info_gear_next", rod_info_gear_enhance, rod_info_gear_next)
    # 再点击previous切回来 对照信息
    GearEnhancePanel.click_btn_previous(bp)
    bp.sleep(1)
    rod_info_gear_previous = GearEnhancePanel.get_rod_info(bp)
    compare(rod_info_gear_enhance, rod_info_gear_previous)

    # 升星直到碎片不足
    GearEnhancePanel.click_btn_enhance(bp)
    # 等待动画
    bp.sleep(3)
    # 关闭升星成功面板
    while not CommonItemGetPanel.is_panel_active(bp):
        GearEnhanceSuccesPanel.click_btn_close(bp)
        bp.sleep(1)
        # 点击升星按钮
        GearEnhancePanel.click_btn_enhance(bp)
        # 等待动画
        bp.sleep(3)
    CommonItemGetPanel.click_btn_close(bp)
    bp.sleep(1)

    # 再对照信息
    rod_info_gear_cur = GearEnhancePanel.get_rod_info(bp)
    compare(rod_info_gear_enhance, rod_info_gear_cur)

    # 点击技能
    skill_icon = GearEnhancePanel.get_skill_icon(bp)
    GearEnhancePanel.click_skill_icon(bp)
    bp.sleep(1)
    tips_skill_icon = GearSkillTipsPanel.get_skill_icon(bp)
    compare(skill_icon, tips_skill_icon)
    bp.click_position([0.5, 0.9])
    bp.sleep(1)

    # 关闭升星界面
    GearEnhancePanel.click_btn_close(bp)



# 解锁所有鱼竿可以升到满星
def unlock_allrod(bp: BasePage):
    bp.cmd("allrod 1000")
    GearPanel.click_btn_close(bp)
    bp.sleep(1)
    bp.go_to_panel("GearPanel")

def level_up_test(bp: BasePage):
    # 随机选取已解锁鱼竿
    GearPanel.select_unlock_rod(bp)
    bp.sleep(1)
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(1)


    # 商店未解锁跳转商店测试
    GearLevelupPanel.click_btn_add_100000(bp)
    bp.sleep(1)
    if not FlashTipsPanel.is_panel_active(bp):
        raise FindNoElementError

    GearLevelupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 随机选取已解锁鱼竿
    GearPanel.select_unlock_rod(bp)

    # 资源充足情况下的升级
    bp.set_item_count_list(target_count_list=[1234567890, 123456, 1234567], item_tpid_list=["100000", "200300","100200"])
    bp.sleep(1)
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    while not GearLevelupPanel.is_max_active(bp):
        if not level_up_once_test(bp):
            break
        bp.sleep(0.5)

    # 商店解锁跳转商店测试
    GearLevelupPanel.click_btn_add_100000(bp)
    bp.sleep(1)
    StorePanel.click_btn_close(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_close(bp)

    # 应该切到了最大值
    if not GearPanel.is_upgrade_max_active(bp):
        raise FindNoElementError


def level_up_once_test(bp: BasePage):
    res = True
    cost_dict = GearLevelupPanel.get_cost_dict(bp)
    cost_icon_list = list(cost_dict)
    item_count_list = bp.get_item_count_list(item_icon_name_list=cost_icon_list)
    stock_expect_list = item_count_list.copy()
    cur = 0
    while cur < len(cost_icon_list):
        if cost_dict[cost_icon_list[cur]] > item_count_list[cur]:
            res = False
            break
        # 计算期望库存
        stock_expect_list[cur] -= cost_dict[cost_icon_list[cur]]
        cur += 1

    # 计算期望数值
    lv_expect = GearLevelupPanel.get_level_next(bp)
    skill_value_list_expect = GearLevelupPanel.get_skill_value_next_list(bp)
    if not res:
        stock_expect_list = item_count_list.copy()
        lv_expect = GearLevelupPanel.get_level(bp)
        skill_value_list_expect = GearLevelupPanel.get_skill_value_list(bp)

    # 点击升级按钮
    GearLevelupPanel.click_btn_upgrade(bp)

    if GearLevelupPanel.is_max_active(bp):
        return res

    # 当前数值
    item_count_list = bp.get_item_count_list(item_icon_name_list=cost_icon_list)
    lv = GearLevelupPanel.get_level(bp)
    skill = GearLevelupPanel.get_skill_value_list(bp)

    compare(stock_expect_list, item_count_list)
    compare(lv_expect, lv)
    compare(skill_value_list_expect, skill)
    return res

def enhance_test(bp: BasePage):
    # # 随机选取已解锁鱼竿
    # GearPanel.select_unlock_rod(bp)
    #
    # GearPanel.click_btn_enhance(bp)
    # bp.sleep(1)
    # while not GearEnhancePanel.is_max_active(bp):
    #     if not enhance_once_test(bp):
    #         break
    # GearEnhancePanel.click_btn_close(bp)
    # bp.sleep(1)

    # 解锁全部鱼竿可以升满的碎片
    unlock_allrod(bp)

    # 随机选取已解锁鱼竿
    GearPanel.select_unlock_rod(bp)

    GearPanel.click_btn_enhance(bp)
    bp.sleep(1)
    while not GearEnhancePanel.is_max_active(bp):
        if not enhance_once_test(bp):
            break

    # 关闭升星界面
    GearEnhancePanel.click_btn_close(bp)

    # 应该切到了最大值
    if not GearPanel.is_enhance_max_active(bp):
        raise FindNoElementError


def enhance_once_test(bp: BasePage):
    res = True
    # 计算碎片期望数量
    shard_numerator, shard_denominator = GearEnhancePanel.get_shard(bp)
    shard_expect = shard_numerator - shard_denominator
    if shard_expect < 0:
        res = False

    # 计算星数期望
    stars = GearEnhancePanel.get_stars(bp)
    stars_now = GearEnhancePanel.get_stars_now(bp)
    stars_next = GearEnhancePanel.get_stars_next(bp)
    compare(stars, stars_now)
    compare(stars_now + 1, stars_next)
    stars_expect = stars_next

    # 计算技能期望数值
    skill_value_list_expect = GearEnhancePanel.get_skill_value_next_list(bp)

    if not res:
        shard_expect = shard_numerator
        stars_expect = stars_now
        skill_value_list_expect = GearEnhancePanel.get_skill_value_list(bp)

    # 点击升级按钮
    GearEnhancePanel.click_btn_enhance(bp)

    # 等待动画
    bp.sleep(3)

    # 关闭升星成功面板
    if GearEnhanceSuccesPanel.is_panel_active(bp):
        GearEnhanceSuccesPanel.click_btn_close(bp)

    if GearEnhancePanel.is_max_active(bp):
        return res

    # 当前数值
    stars = GearEnhancePanel.get_stars(bp)
    stars_now = GearEnhancePanel.get_stars_now(bp)
    stars_next = GearEnhancePanel.get_stars_next(bp)
    compare(stars, stars_now)
    compare(stars_now + 1, stars_next)
    skill_value_list = GearEnhancePanel.get_skill_value_list(bp)
    shard, _ = GearEnhancePanel.get_shard(bp)

    # 对比数值
    compare(stars_expect, stars)
    compare(skill_value_list_expect, skill_value_list)
    compare(shard_expect, shard)

    return res



def GearPanel_test(bp: BasePage):
    # 随机选取已解锁鱼竿
    GearPanel.select_unlock_rod(bp)
    # 点击技能图标测试
    skill_icon_list = GearPanel.get_skill_icon_list(bp)
    skill_position_list = GearPanel.get_skill_position_list(bp)
    r = random.randint(0, len(skill_position_list) - 1)
    bp.click_position(skill_position_list[r])
    skill_icon = GearSkillTipsPanel.get_skill_icon(bp)
    compare(skill_icon_list[r], skill_icon)
    bp.click_position([0.5, 0.9])

    # 点击筛选
    GearPanel.click_btn_filter(bp)
    if not GearPanel.is_tip_filter_rod_active(bp):
        raise FindNoElementError
    GearPanel.click_btn_reset(bp)
    GearPanel.click_btn_apply(bp)

    GearPanel.click_btn_close(bp)

def hide_unowned_test(bp: BasePage):
    GearPanel.click_btn_filter(bp)


def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)
    bp.set_item_count(target_count=0, item_tpid="100000")
    # 进入装备界面
    bp.go_to_panel("GearPanel")
    lock_test(bp)
    unlock_test(bp)
    enhance_test(bp)
    level_up_test(bp)
    GearPanel_test(bp)

def full_level(bp: BasePage, tpId=None, table_data=None):
    if table_data is None:
        table_data = GearPanel.get_fishing_rod_table_data(bp)
    tpId_list = table_data["tpId"]

    if tpId is not None:
        maxLevel_list = table_data["maxLevel"]
        index = tpId_list.index(tpId)
        specify_level(bp, maxLevel_list[index], tpId=tpId, table_data=table_data)
        return

    cur = 0
    while cur < len(tpId_list):
        full_level(bp, tpId=tpId_list[cur], table_data=table_data)
        bp.sleep(0.1)
        cur += 1


def specify_level(bp: BasePage, target_level, tpId=None, table_data=None):
    if table_data is None:
        table_data = GearPanel.get_fishing_rod_table_data(bp)
    tpId_list = table_data["tpId"]

    if tpId is not None:
        lua_code = csMsgAll.get_CSBaitAndRodLevelUpToMsg(ioIdType=5, tpId=tpId, targetLevel=target_level)
        bp.lua_console(lua_code)
        return

    cur = 0
    while cur < len(tpId_list):
        specify_level(bp, target_level, tpId=tpId_list[cur], table_data=table_data)
        bp.sleep(0.1)
        cur += 1

def full_star(bp: BasePage, tpId=None, table_data=None):
    if table_data is None:
        table_data = GearPanel.get_fishing_rod_table_data(bp)
    tpId_list = table_data["tpId"]
    maxStarLv_list = table_data["maxStarLv"]

    if tpId is not None:
        index = tpId_list.index(tpId)
        maxStarLv = maxStarLv_list[index]
        cur = 0
        while cur < maxStarLv:
            one_star(bp, tpId=tpId, table_data=table_data)
            bp.sleep(0.1)
            cur += 1
        return
    cur = 0
    while cur < len(tpId_list):
        full_star(bp, tpId=tpId_list[cur], table_data=table_data)
        cur += 1

def one_star(bp: BasePage, tpId=None, table_data=None):
    if tpId is not None:
        lua_code = csMsgAll.get_CSBaitAndRodStarLevelUpMsg(ioIdType=5, tpId=tpId)
        bp.lua_console(lua_code)
        return
    if table_data is None:
        table_data = GearPanel.get_fishing_rod_table_data(bp)
    tpId_list = table_data["tpId"]
    cur = 0
    while cur < len(tpId_list):
        one_star(bp, tpId=tpId_list[cur])
        bp.sleep(0.1)
        cur += 1



if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21503")
    # full_star(bp)
    bp.cmd("allrod 1")
    bp.cmd("allrod 1000")
    bp.set_item_count(target_count=100000000000, item_tpid="100000")
    bp.set_item_count(target_count=100000000, item_tpid="200300")
    bp.sleep(1)
    full_level(bp)
    # specify_level(bp, target_level=80, tpId=500028)
    bp.connect_close()

import random
from common.basePage import BasePage
from panelObjs.storePanel import StorePanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from tools.commonTools import *
from common import resource


def gift_pack_test(bp:BasePage):
    # 切换到 gift pack
    StorePanel.change_tab(bp, 0)

    # 点击图标
    gift_pack_click_icon_test(bp)

    # 购买测试
    gift_pack_buy_test(bp)


def gift_pack_click_icon_test(bp:BasePage):
    # 得到图标及位置
    gift_pack_position_list = StorePanel.get_gift_pack_position_list(bp)
    gift_pack_icon_list = StorePanel.get_gift_pack_icon_list(bp)

    # 随机点击图标
    r = random.randint(0, len(gift_pack_position_list) - 1)
    bp.click_position(gift_pack_position_list[r])

    # 得到弹出的图标
    item_icon = ItemTipsPanel.get_item_icon(bp)

    # 对比点击的图标和弹出的图标
    compare(item_icon, gift_pack_icon_list[r])

    # 消去弹出的浮窗
    bp.click_position([0.5, 0.1])


def gift_pack_buy_test(bp:BasePage):


    # 得到购买按钮位置的列表
    gift_pack_id_list = StorePanel.get_gift_pack_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, gift_pack_id_list)

    # 依次进行购买
    cur = 0
    while cur < len(gift_pack_id_list):
        # 得到商品图标数量的列表
        gift_pack_dict_list = StorePanel.get_gift_pack_dict_list(bp)
        gift_pack_buy_once_test(bp,gift_pack_dict_list[cur], btn_position_list[cur])
        cur += 1

def gift_pack_buy_once_test(bp:BasePage, gift_pack_dict, btn_position):
    # 得到图标和数量
    gift_pack_icon_list = list(gift_pack_dict)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=gift_pack_icon_list)

    # 点击购买
    bp.click_position(btn_position)
    bp.sleep(0.5)

    # 对比售卖的物品和实际获得的物品
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(reward_dict, gift_pack_dict)


    # 计算期望库存
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += gift_pack_dict[gift_pack_icon_list[cur]]
        cur += 1

    # 实际库存
    item_count_list = bp.get_item_count_list(item_icon_name_list=gift_pack_icon_list)

    # 对比期望库存和实际库存
    compare_list(item_count_expect_list, item_count_list)

    # 关闭恭喜获得
    RewardsPanel.click_tap_to_claim(bp)


def cash_test(bp:BasePage):
    # 切换到cash
    StorePanel.change_tab(bp, 3)

    # 点击图标测试
    cash_click_icon_test(bp)

    # 购买测试
    cash_buy_test(bp)


def cash_click_icon_test(bp:BasePage):
    # 有浮窗先消去浮窗
    if ItemTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])

    # 得到图标及其位置
    cash_icon_list = StorePanel.get_cash_icon_list(bp)
    cash_position_list = StorePanel.get_cash_position_list(bp)

    # 随机点击一个图标
    r = random.randint(0, len(cash_position_list) - 1)
    bp.click_position(cash_position_list[r])

    # 得到浮窗图标
    item_icon = ItemTipsPanel.get_item_icon(bp)

    # 对比浮窗图标和物品图标
    compare(item_icon, cash_icon_list[r])

    # 关闭浮窗
    bp.click_position([0.5, 0.1])

def cash_buy_test(bp:BasePage):
    # 得到图标、数量、首次x2、按钮位置
    cash_icon_list = StorePanel.get_cash_icon_list(bp)
    cash_id_list = StorePanel.get_cash_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, cash_id_list)

    # 依次购买
    cur = 0
    while cur < len(cash_id_list):
        cash_quantity_list = StorePanel.get_cash_quantity_list(bp)
        cash_first_time_list = StorePanel.get_cash_first_time_list(bp)
        # 计算首次翻倍后的实际数量
        if cash_first_time_list[cur]:
            cash_quantity_list[cur] *= 2

        # 购买
        cash_buy_once_test(bp, cash_icon_list[cur], cash_quantity_list[cur], btn_position_list[cur])
        cur += 1

def cash_buy_once_test(bp:BasePage, cash_icon, cash_quantity, btn_position):
    # 得到钞票库存
    item_count_expect = bp.get_item_count(item_icon_name=cash_icon)

    # 点击购买
    bp.click_position(btn_position)
    bp.sleep(0.5)

    # 对比商品数量和实际获取物品数量
    reward_quantity_list = RewardsPanel.get_reward_quantity_list(bp)
    compare(cash_quantity, reward_quantity_list[0])

    # 期望库存
    item_count_expect += cash_quantity

    # 实际库存
    item_count = bp.get_item_count(item_icon_name=cash_icon)

    # 对比期望库存和实际库存
    compare(item_count_expect, item_count)

    # 关闭恭喜获得
    RewardsPanel.click_tap_to_claim(bp)

def gear_test(bp:BasePage):
    StorePanel.change_tab(bp, 1)
    bp.sleep(0.5)
    StorePanel.change_resource_tab(bp, 0)
    item_tpid_list = ["100000", "100100"]
    target_count_list = [1500000, 10000]
    bp.set_item_count_list(target_count_list=target_count_list, item_tpid_list=item_tpid_list)

    # 展示测试
    gear_show_test(bp)

    # 购买测试
    gear_buy_test(bp)

def gear_show_test(bp:BasePage):
    # 获得鱼竿信息
    gear_position_list = StorePanel.get_gear_position_list(bp)
    gear_name_list = StorePanel.get_gear_name_list(bp)

    # 随机选一个鱼竿
    r = random.randint(0, len(gear_position_list) - 1)
    bp.click_position(gear_position_list[r])

    # 点击放大镜
    StorePanel.click_btn_info(bp)
    bp.sleep(0.5)

    # 对比鱼竿名是否正确
    gear_name = BaitAndRodShowPanel.get_gear_name(bp)
    compare(gear_name_list[r], gear_name)

    # 关闭展示界面
    BaitAndRodShowPanel.click_tap_to_continue(bp)

def gear_buy_test(bp:BasePage):
    # 得到图标和购买按钮位置
    gear_icon_list = StorePanel.get_gear_icon_list(bp)
    gear_position_list = StorePanel.get_gear_position_list(bp)
    item_id_list = StorePanel.get_item_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=item_id_list)

    # 依次购买
    cur = 0
    while cur < len(gear_icon_list):
        # 点击指定鱼竿
        bp.click_position(gear_position_list[cur])
        bp.sleep(0.5)

        # 获取价格
        price_list = StorePanel.get_price_list(bp, item_id_list=item_id_list)
        btn_icon_list = StorePanel.get_btn_icon_list(bp, item_id_list=item_id_list)
        # 购买
        gear_buy_once_test(bp, gear_icon_list[cur],price_list[0], btn_icon_list[0], btn_position_list[0])

        cur += 1

def gear_buy_once_test(bp:BasePage, gear_icon, price,btn_icon, btn_position):
    stock_expect = 0
    item_tpid = ""
    if price >= 0:
        # 当前库存
        item_tpid = bp.get_tpid(item_icon_name=btn_icon)
        stock_expect = bp.get_item_count(bp, item_tpid=item_tpid)

    # 判断是否可以购买
    is_clickable = StorePanel.is_clickable(bp, cost=price, icon=btn_icon)

    # 点击购买
    bp.click_position(btn_position)

    # 不能购买就返回
    if not is_clickable:
        if price >= 0:
            stock = bp.get_item_count(bp, item_tpid=item_tpid)
            compare(stock_expect, stock)
        return

    # 关闭鱼竿展示界面
    bp.sleep(0.5)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.sleep(0.5)

    # 计算库存与实际库存，然后对比
    stock_expect -= price
    stock = bp.get_item_count(bp, item_tpid=item_tpid)
    compare(stock_expect, stock)

    # 看购买的图标与商品图标是否一致
    reward_item_icon_list, reward_gear_icon_list = RewardsPanel.get_reward_icon_list(bp, is_divide=True)
    compare(reward_gear_icon_list[0], gear_icon)

    # 关闭恭喜获得
    RewardsPanel.click_tap_to_claim(bp)


def fish_card_test(bp:BasePage):
    StorePanel.change_tab(bp, 1)
    bp.sleep(0.5)
    StorePanel.change_resource_tab(bp, 1)
    # 得到第一根鱼卡包的价格，差一块钱
    item_id_list = StorePanel.get_item_id_list(bp)
    price_list = StorePanel.get_price_list(bp, item_id_list=item_id_list)
    bp.set_item_count(target_count=price_list[0] - 1, item_tpid="100000")
    fish_card_click_icon_test(bp)
    fish_card_buy_test(bp)

def fish_card_buy_test(bp:BasePage):
    # 获取鱼卡位置列表
    fish_card_position_list = StorePanel.get_fish_card_position_list(bp)

    # 获取购买按钮位置列表
    item_id_list = StorePanel.get_item_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=item_id_list)


    # 依次购买
    cur = 0
    while cur < len(fish_card_position_list):
        # 点击购买
        bp.click_position(fish_card_position_list[cur])
        bp.sleep(0.5)

        # 获取价格
        price_list = StorePanel.get_price_list(bp, item_id_list=item_id_list)
        btn_icon_list = StorePanel.get_btn_icon_list(bp, item_id_list=item_id_list)

        # 购买
        fish_card_buy_once_test(bp, price_list[0], btn_icon_list[0],btn_position_list[0])
        cur += 1


def fish_card_buy_once_test(bp:BasePage, price, btn_icon, btn_position):
    # 库存
    stock_expect = 0
    item_tpid = ""
    if price >= 0:
        # 当前库存
        item_tpid = bp.get_tpid(item_icon_name=btn_icon)
        stock_expect = bp.get_item_count(bp, item_tpid=item_tpid)

    # 是否可购买
    is_clickable = StorePanel.is_clickable(bp, cost=price, icon=btn_icon)

    # 点击购买
    bp.click_position(btn_position)

    # 不可购买就返回
    if not is_clickable:
        stock = bp.get_item_count(bp, item_tpid=item_tpid)
        compare(stock_expect, stock)
        return

    # 关闭鱼卡弹窗
    bp.clear_popup_until_appear(StorePanel.get_StorePanel_element_data())

    # 对比预期库存和实际库存
    stock_expect -= price
    stock = bp.get_item_count(bp, item_tpid=item_tpid)
    compare(stock_expect, stock)


def fish_card_click_icon_test(bp:BasePage):
    # 如果鱼卡弹窗打开就先关闭
    if FishCardPackTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])

    # 随机选择一个鱼卡包进行切换
    fish_card_position_list = StorePanel.get_fish_card_position_list(bp)
    fish_card_name_list = StorePanel.get_fish_card_name_list(bp)

    r = random.randint(0, len(fish_card_position_list) - 1)
    bp.click_position(fish_card_position_list[r])

    # 点击放大镜
    StorePanel.click_btn_info(bp)

    # 名称对比
    fish_card_main_name = StorePanel.get_fish_card_main_name(bp)  # 主展示卡包名
    fish_card_name = FishCardPackTipsPanel.get_fish_card_name(bp)
    fish_card_name = fish_card_name.replace(" Pack", "")  # 浮窗上卡包名
    compare(fish_card_main_name, fish_card_name_list[r])
    compare(fish_card_name_list[r], fish_card_name)

    # 关闭浮窗
    bp.click_position([0.5, 0.1])


def booster_click_icon_test(bp:BasePage):
    if ItemTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])
    booster_icon_list = StorePanel.get_booster_icon_list(bp)
    booster_position_list = StorePanel.get_booster_position_list(bp)
    r = random.randint(0, len(booster_position_list) - 1)
    bp.click_position(booster_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, booster_icon_list[r])
    bp.click_position([0.5, 0.1])


def booster1_buy_test(bp:BasePage):
    booster_id_list = StorePanel.get_item_id_list(bp)
    price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
    booster_dict_list = StorePanel.get_booster_dict_list(bp)
    # 买每日免费booster礼包
    r = 0
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=booster_id_list)
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    if price_list[r] != -1:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
        price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
        compare(price_list[r], -1)
    # 买每日lager booster礼包
    r = 1
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    if price_list[r] != -1 and is_clickable:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
        price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
        compare(price_list[r], -1)
    else:
        bp.click_position(btn_position_list[r])
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
    # 随机选一个
    r = random.randint(2, 5)
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    if is_clickable:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
    else:
        bp.click_position(btn_position_list[r])
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)


def booster2_buy_test(bp:BasePage):
    booster_id_list = StorePanel.get_item_id_list(bp)
    price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
    booster_dict_list = StorePanel.get_booster_dict_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=booster_id_list)
    # 随机选一个
    r = random.randint(0, 5)
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    if is_clickable:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
    else:
        bp.click_position(btn_position_list[r])
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)

def materials_test(bp: BasePage):
    StorePanel.change_tab(bp, 1)
    bp.sleep(0.5)
    StorePanel.change_resource_tab(bp, 2)
    materials_click_icon_test(bp)
    materials_slider_test(bp)
    materials_buy_test(bp)


def materials_click_icon_test(bp:BasePage):
    # 如果信息弹窗打开就先关闭
    if ItemTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])

    # 随机点一种材料
    materials_position_list = StorePanel.get_materials_position_list(bp)
    materials_icon_list = StorePanel.get_materials_icon_list(bp)
    r = random.randint(0, len(materials_icon_list) - 1)
    bp.click_position(materials_position_list[r])

    StorePanel.click_btn_info(bp)
    # 对比弹窗物品和商品是否一致
    materials_icon = ItemTipsPanel.get_item_icon(bp)
    compare(materials_icon_list[r], materials_icon)

    # 关闭信息弹窗
    bp.click_position([0.5, 0.1])

def materials_slider_test(bp:BasePage):
    # 得到最小单位和单位价格的数量
    item_min = StorePanel.get_item_quantity(bp)
    cost_min = StorePanel.get_cost_quantity(bp)
    k = int(item_min / cost_min)

    # 测btn_max
    StorePanel.click_btn_max(bp)
    item_max = StorePanel.get_item_quantity(bp)
    cost_max = StorePanel.get_cost_quantity(bp)
    compare(k, int(item_max/cost_max))

    # 测上限时的btn_add
    StorePanel.click_btn_add(bp)
    item_cur = StorePanel.get_item_quantity(bp)
    cost_cur = StorePanel.get_cost_quantity(bp)
    compare(item_max, item_cur)
    compare(cost_max, cost_cur)
    compare(k, int(item_cur / cost_cur))

    # 测btn_sub
    StorePanel.click_btn_sub(bp)
    item_cur = StorePanel.get_item_quantity(bp)
    cost_cur = StorePanel.get_cost_quantity(bp)
    compare(item_max - item_min, item_cur)
    compare(cost_max - cost_min, cost_cur)
    compare(k, int(item_cur / cost_cur))

    # 测滑条滑到下限
    slider_position = StorePanel.get_slider_position(bp)
    slider_size = StorePanel.get_slider_size(bp)
    bp.swipe(point_start=[slider_position[0] - 0.4 * slider_size[0], slider_position[1]], point_end=[slider_position[0] - 0.6 * slider_size[0], slider_position[1]])
    item_cur = StorePanel.get_item_quantity(bp)
    cost_cur = StorePanel.get_cost_quantity(bp)
    compare(item_min, item_cur)
    compare(cost_min, cost_cur)
    compare(k, int(item_cur / cost_cur))

    # 测下限时的btn_sub
    StorePanel.click_btn_sub(bp)
    item_cur = StorePanel.get_item_quantity(bp)
    cost_cur = StorePanel.get_cost_quantity(bp)
    compare(item_min, item_cur)
    compare(cost_min, cost_cur)
    compare(k, int(item_cur / cost_cur))

    # 测btn_add
    StorePanel.click_btn_add(bp)
    item_cur = StorePanel.get_item_quantity(bp)
    cost_cur = StorePanel.get_cost_quantity(bp)
    compare(item_min + item_min, item_cur)
    compare(cost_min + cost_min, cost_cur)
    compare(k, int(item_cur / cost_cur))

    # 测滑条滑到上限
    bp.swipe(point_start=[slider_position[0] + 0.4 * slider_size[0], slider_position[1]], point_end=[slider_position[0] + 0.6 * slider_size[0], slider_position[1]])
    item_cur = StorePanel.get_item_quantity(bp)
    cost_cur = StorePanel.get_cost_quantity(bp)
    compare(item_max, item_cur)
    compare(cost_max, cost_cur)
    compare(k, int(item_cur / cost_cur))

def materials_buy_test(bp: BasePage):
    # 获取材料位置列表
    materials_position_list = StorePanel.get_materials_position_list(bp)
    cur = 0
    while cur < len(materials_position_list):
        bp.click_position(materials_position_list[cur])
        materials_buy_once_test(bp)
        cur += 1


def materials_buy_once_test(bp: BasePage):
    # 随机设一个数量
    slider_position = StorePanel.get_slider_position(bp)
    slider_size = StorePanel.get_slider_size(bp)
    r = random.randint(-49, 49)
    bp.click_position([slider_size[0] * r / 100 + slider_position[0], slider_position[1]])
    r = random.randint(0, 2)
    if r == 0:
        StorePanel.click_btn_add(bp)
    if r == 1:
        StorePanel.click_btn_sub(bp)

    item_quantity = StorePanel.get_item_quantity(bp)
    item_icon = StorePanel.get_item_icon(bp)
    item_stock_expect = bp.get_item_count(item_icon_name=item_icon)

    # 不足情况下购买
    cost_quantity = StorePanel.get_cost_quantity(bp)
    bp.set_item_count(target_count=cost_quantity - 1, item_tpid="100100")
    StorePanel.click_btn_purchase(bp)

    # 确保钞票没变 物品库存没变
    cash = StorePanel.get_cash(bp)
    compare(cost_quantity - 1, cash)
    compare(item_stock_expect, bp.get_item_count(item_icon_name=item_icon))

    # 充足的情况下购买
    bp.set_item_count(target_count=cost_quantity, item_tpid="100100")
    StorePanel.click_btn_purchase(bp)
    bp.sleep(0.5)
    # 对比钞票
    cash_expect = 0
    cash = StorePanel.get_cash(bp)
    compare(cash_expect, cash)

    # 对比物品和恭喜获得的图标和数量
    reward_icon = RewardsPanel.get_reward_icon_list(bp, is_divide=False)[0]
    compare(reward_icon, item_icon)
    reward_quantity = RewardsPanel.get_reward_quantity_list(bp)[0]
    compare(reward_quantity, item_quantity)

    # 对比期望库存和实际物品库存
    item_stock_expect += item_quantity
    item_stock = bp.get_item_count(item_icon_name=item_icon)
    compare(item_stock_expect, item_stock)

    # 关闭恭喜获得
    RewardsPanel.click_tap_to_claim(bp)

def box_test(bp: BasePage):
    StorePanel.change_tab(bp, 2)
    bp.sleep(0.5)
    box_id_list = StorePanel.get_box_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, box_id_list)
    box_price_test(bp, box_id_list)

    # 免费项点两次
    box_buy_once_test(bp, btn_position_list, box_id_list, 0)
    box_price_test(bp, box_id_list)
    box_buy_once_test(bp, btn_position_list, box_id_list, 0)

    # 点一个绿钞项
    r = random.randint(1, 5)
    box_buy_once_test(bp, btn_position_list, box_id_list, r)
    box_price_test(bp, box_id_list)

    # 点击刷新
    refresh_cost = StorePanel.get_refresh_cost(bp)
    while refresh_cost >= 0:
        # StorePanel.click_btn_refresh(bp)
        box_refresh_test(bp, box_id_list)
        refresh_cost = StorePanel.get_refresh_cost(bp)
        if refresh_cost > StorePanel.get_cash(bp):
            box_refresh_test(bp, box_id_list)
            # StorePanel.click_btn_refresh(bp)
            StorePanel.change_tab(bp, 3)
            bp.set_item_count(target_count=20000, item_tpid="100100")
            StorePanel.change_tab(bp, 2)

    # 全买一遍
    cur = 0
    while cur < len(box_id_list):
        box_buy_once_test(bp, btn_position_list, box_id_list, cur)
        cur += 1


def box_price_test(bp: BasePage, box_id_list:list):
    # 获取图标、数量、折扣信息计算期望价格列表
    icon_list, quantity_list, off_list = StorePanel.get_box_details(bp)
    expect_price_list = StorePanel.get_expect_price_list(bp, icon_list, quantity_list, off_list)

    # 获取实际价格列表
    price_list = StorePanel.get_price_list(bp, box_id_list)

    # 去掉已购买项
    cur = 0
    while cur < len(expect_price_list):
        if price_list[cur] == -1:
            expect_price_list[cur] = -1
        cur += 1

    # 进行对比
    compare(price_list, expect_price_list)

def box_buy_once_test(bp:BasePage, btn_position_list, box_id_list, index: int):
    # 获取信息
    price_list = StorePanel.get_price_list(bp, item_id_list=box_id_list)
    cash_expect = StorePanel.get_cash(bp)
    box_icon_list, box_quantity_list, box_off_list = StorePanel.get_box_details(bp)
    quantity_expect = bp.get_item_count(item_icon_name=box_icon_list[index])

    # 计算期望箱子数量和绿钞
    if StorePanel.is_clickable(bp, cost=price_list[index], icon="coin_gem"):
        quantity_expect += box_quantity_list[index]
        cash_expect -= price_list[index]

    # 点击购买
    bp.click_position(btn_position_list[index])

    # 对比箱子数量
    item_count = bp.get_item_count(item_icon_name=box_icon_list[index])
    compare(quantity_expect, item_count)

    # 对比绿钞数量
    cash = StorePanel.get_cash(bp)
    compare(cash, cash_expect)

def box_refresh_test(bp: BasePage, box_id_list: list):
    # 刷新次数
    times_refresh_numerator, times_refresh_denominator = StorePanel.get_times_refresh(bp)
    times_refresh_expect = times_refresh_numerator

    # 绿钞和刷新费用
    cash = StorePanel.get_cash(bp)
    refresh_cost = StorePanel.get_refresh_cost(bp)
    cash_expect = cash - refresh_cost

    # 刷新次数用光或费用不足
    if refresh_cost < 0 or cash_expect < 0:
        price_list_expect = StorePanel.get_price_list(bp, box_id_list)
        cash_expect = cash

        # 不管按钮是否可点击都点击
        StorePanel.click_btn_refresh(bp)

        # 对比期望和实际
        cash = StorePanel.get_cash(bp)
        price_list = StorePanel.get_price_list(bp, box_id_list)
        times_refresh_numerator, times_refresh_denominator = StorePanel.get_times_refresh(bp)
        compare(cash, cash_expect)
        compare(price_list, price_list_expect)
        compare(times_refresh_numerator, times_refresh_expect)
        return

    # 刷新前的价格列表
    price_list_pre = StorePanel.get_price_list(bp, box_id_list)

    # 刷新
    StorePanel.click_btn_refresh(bp)

    # 看刷新是否成功
    price_list = StorePanel.get_price_list(bp, box_id_list)
    cash = StorePanel.get_cash(bp)
    times_refresh_expect -= 1
    times_refresh_numerator, times_refresh_denominator = StorePanel.get_times_refresh(bp)
    compare(cash, cash_expect)
    compare(times_refresh_numerator, times_refresh_expect)
    if price_list_pre == price_list:
        print("未刷新成功")
        raise SameError

def store_test(bp: BasePage):
    bp.go_to_panel("StorePanel")
    gift_pack_test(bp)
    cash_test(bp)
    gear_test(bp)
    fish_card_test(bp)
    materials_test(bp)
    box_test(bp)
    bp.go_home()

if __name__ == '__main__':
    bp = BasePage()
    # bp.set_item_count(target_count=1000000, item_tpid="100200")
    store_test(bp)
    # box_test(bp)
import random

from common.basePage import BasePage
from panelObjs.treasureChestPanel import TreasureChestPanel
from panelObjs.storePanel import StorePanel
from panelObjs.treasureChestRewardsPanel import TreasureChestRewardsPanel
from panelObjs.treasureChestGearsShardsPanel import TreasureChestGearsShardsPanel
from panelObjs.homePanel import HomePanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from tools.commonTools import *
from configs.elementsData import ElementsData
from items import resource



def TreasureChestPanel_test(bp: BasePage):
    HomePanel.go_to(bp, element=ElementsData.Home.btn_chest)
    print("正在获取箱子图标和数量列表")
    box_icon_list, box_quantity_list =TreasureChestPanel.get_box_icon_and_quantity_list(bp)
    print("图标列表：", box_icon_list, "\n数量列表：", box_quantity_list)
    cur = 0
    while cur < len(box_icon_list):
        print(f"正在选择第{cur + 1}个箱子")
        TreasureChestPanel.select_box(bp, cur)
        # 得到当前展示箱子的icon名，与第cur个箱子的icon名对比
        print("正在获取当前展示箱子图标名称")
        box_mian_icon = TreasureChestPanel.get_box_main_icon(bp)
        print(f"当前展示箱子图标名称为：{box_mian_icon}，选中的箱子图标名称为：{box_icon_list[cur]}")
        compare(box_icon_list[cur], box_mian_icon)
        print("图标一致")
        # 得到open x后的可打开数量，与第cur个箱子的数量对比
        n = TreasureChestPanel.get_open_x_n(bp)
        expect_n = box_quantity_list[cur]
        if box_quantity_list[cur] > 10:
            expect_n = 10
        print(f"按钮应该显示OPEN X {expect_n},实际显示为OPEN X {n}")
        compare(expect_n, n)
        print("数量显示无误")
        open_box_test(bp, box_mian_icon, n)
        cur += 1
    get_box_point_box_test(bp)
    click_tips_test(bp)
    print("测试通过")

def TreasureChestMerchant_price_test(bp: BasePage, box_id_list:list):
    print("正在获取图标和质量列表")
    icon_list, quantity_list, off_list = StorePanel.get_box_icon_and_quantity_and_box_off_list(bp)
    print("图标列表：",icon_list, "\n数量列表：",quantity_list, "\n折扣列表：", off_list)
    print("正在获取折扣和价格列表")
    price_list = StorePanel.get_price_list(bp, box_id_list)
    print("价格列表：", price_list)
    print("正在计算期望价格列表")
    expect_price_list = StorePanel.get_expect_price_list(bp, icon_list, quantity_list, off_list)
    cur = 0
    while cur < len(expect_price_list):
        if price_list[cur] == -1:
            expect_price_list[cur] = -1
        cur += 1
    print("期望价格列表：", expect_price_list)
    print("正在比较期望价格和实际标注价格")
    compare(price_list, expect_price_list)
    print("价格一致，测试通过")


def get_box_point_box_test(bp: BasePage):
    cur = 0
    while cur < 5:
        print(f"进行第{cur + 1}次进度条箱子点击测试")
        if click_progressbar_box_test(bp) is False:
            break
        cur += 1
    print("测试通过")

def click_progressbar_box_test(bp: BasePage):
    if TreasureChestPanel.is_box_points_enough(bp) is False:
        box_points_expect = TreasureChestPanel.get_box_points(bp)
        TreasureChestPanel.click_progressbar_box(bp)
        bp.sleep(0.5)
        box_points = TreasureChestPanel.get_box_points(bp)
        compare(box_points, box_points_expect)
        print("箱子点不足下的点击，测试通过")
        return False
    box_icon_list, quantity_list = TreasureChestPanel.get_box_icon_and_quantity_list(bp)
    progressbar_box = TreasureChestPanel.get_progressbar_box(bp)
    cur = 0
    while cur < len(box_icon_list):
        if progressbar_box == box_icon_list[cur]:
            quantity_list[cur] += 1
            break
        cur += 1
    quantity_list_except = quantity_list
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    box_points_numerator_expect = box_points_numerator - box_points_denominator
    TreasureChestPanel.click_progressbar_box(bp)
    bp.sleep(0.5)
    box_points_numerator_new, box_points_denominator_new = TreasureChestPanel.get_box_points(bp)
    box_points_numerator = box_points_numerator_new
    box_icon_list, quantity_list = TreasureChestPanel.get_box_icon_and_quantity_list(bp)
    compare(quantity_list, quantity_list_except)
    compare(box_points_numerator_expect, box_points_numerator)
    print("箱子点充足下的点击，测试通过")
    return True

def open_box_test(bp: BasePage, icon, quantity):
    print("正在获取开箱前的箱子点")
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    print(f"箱子点为{box_points_numerator}")
    chest_point = TreasureChestPanel.get_chest_point(bp, icon)
    box_points_numerator_expect = box_points_numerator + chest_point * quantity
    print(f"开箱后箱子点期望为{box_points_numerator_expect}")
    TreasureChestPanel.click_open_x(bp)
    if quantity > 0:
        TreasureChestRewardsPanel.click_btn_close(bp)
        if TreasureChestGearsShardsPanel.is_panel_active(bp):
            print("点击tap to continue")
            TreasureChestGearsShardsPanel.click_tap_to_continue(bp)
    print("等待加分动画")
    bp.sleep(2)
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    print(f"开箱后箱子点实际为{box_points_numerator}")
    compare(box_points_numerator, box_points_numerator_expect)
    print("箱子点一致")

def click_tips_test(bp: BasePage):
    TreasureChestPanel.click_btn_magnifier(bp)
    TreasureChestPanel.click_btn_magnifier(bp)
    preview_icon_list, preview_position_list = TreasureChestPanel.get_preview_icon_and_position_list(bp)
    index_random = random.randint(0, len(preview_icon_list) - 1)
    bp.click_position(preview_position_list[index_random])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(preview_icon_list[index_random], item_icon)
    bp.click_position([0.5, 0.1])
    if ItemTipsPanel.is_panel_active(bp):
        raise FindElementError

def refresh_test(bp: BasePage, box_id_list:list):
    times_refresh_numerator, times_refresh_denominator = StorePanel.get_times_refresh(bp)
    times_refresh_expect = times_refresh_numerator
    cash = StorePanel.get_cash(bp)
    refresh_cost = StorePanel.get_refresh_cost(bp)
    cash_expect = cash - refresh_cost
    if refresh_cost < 0 or cash_expect < 0:
        price_list_expect = StorePanel.get_price_list(bp)
        cash_expect = cash
        # 不管按钮是否可点击都点击
        StorePanel.click_btn_refresh(bp)
        cash = StorePanel.get_cash(bp)
        price_list = StorePanel.get_price_list(bp, box_id_list)
        times_refresh_numerator, times_refresh_denominator = StorePanel.get_times_refresh(bp)
        print("无法刷新")
        compare(cash, cash_expect)
        compare(price_list, price_list_expect)
        compare(times_refresh_numerator, times_refresh_expect)
        return
    price_list_pre = StorePanel.get_price_list(bp, box_id_list)
    StorePanel.click_btn_refresh(bp)
    price_list = StorePanel.get_price_list(bp, box_id_list)
    cash = StorePanel.get_cash(bp)
    times_refresh_expect -= 1
    times_refresh_numerator, times_refresh_denominator = StorePanel.get_times_refresh(bp)
    compare(cash, cash_expect)
    compare(times_refresh_numerator, times_refresh_expect)
    if price_list_pre == price_list:
        print("未刷新成功")
        raise SameError

def TreasureChestMerchant_test(bp: BasePage):
    TreasureChestPanel.click_btn_box_store(bp)
    box_id_list = StorePanel.get_box_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, box_id_list)
    TreasureChestMerchant_price_test(bp, box_id_list)
    # 免费项点两次
    buy_test(bp, btn_position_list,box_id_list,0)
    TreasureChestMerchant_price_test(bp, box_id_list)
    buy_test(bp, btn_position_list,box_id_list, 0)
    # 点一个绿钞项
    r = random.randint(1, 5)
    buy_test(bp, btn_position_list, box_id_list,r)
    TreasureChestMerchant_price_test(bp, box_id_list)
    refresh_cost = StorePanel.get_refresh_cost(bp)
    while refresh_cost >= 0:
        # StorePanel.click_btn_refresh(bp)
        refresh_test(bp, box_id_list)
        refresh_cost = StorePanel.get_refresh_cost(bp)
        if refresh_cost > StorePanel.get_cash(bp):
            refresh_test(bp)
            # StorePanel.click_btn_refresh(bp)
            print("刷新费用不足")
            break
    StorePanel.click_btn_close(bp)
    # 检查箱子数量是否与库存一致
    box_icon_list, box_quantity_list = TreasureChestPanel.get_box_icon_and_quantity_list(bp)
    cur = 0
    while cur < len(box_quantity_list):
        item_count = bp.get_item_count(item_icon_name=box_icon_list[cur])
        compare(item_count, box_quantity_list[cur])
        cur += 1
    print("TreasureChestMerchant_test购买箱子测试通过")

def buy_test(bp:BasePage,btn_position_list, box_id_list,index: int):
    price_list = StorePanel.get_price_list(bp, item_id_list=box_id_list)
    print(price_list)
    cash_expect = StorePanel.get_cash(bp)
    print("点击购买")
    res = StorePanel.get_box_icon_and_quantity_and_box_off_list(bp)
    box_icon_TreasureChestMerchant_list, quantity_TreasureChestMerchant_list, box_off_list = res
    quantity_expect = bp.get_item_count(item_icon_name=box_icon_TreasureChestMerchant_list[index])
    if StorePanel.is_clickable(bp, price_list[index]):
        print("可以点击")
        quantity_expect += quantity_TreasureChestMerchant_list[index]
        cash_expect -= price_list[index]
    bp.click_position(btn_position_list[index])
    item_count = bp.get_item_count(item_icon_name=box_icon_TreasureChestMerchant_list[index])
    compare(quantity_expect, item_count)
    cash = StorePanel.get_cash(bp)
    print(f"点击后的期望绿钞数为{cash_expect}，实际绿钞数为{cash}")
    compare(cash, cash_expect)



if __name__ == '__main__':
    bp = BasePage()
    TreasureChestPanel_test(bp)
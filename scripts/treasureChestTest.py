import random

from common.basePage import BasePage
from panelObjs.treasureChestPanel import TreasureChestPanel
from panelObjs.treasureChestMerchantPanel import TreasureChestMerchantPanel
from panelObjs.rechargeStorePanel import RechargeStorePanel
from panelObjs.treasureChestRewardsPanel import TreasureChestRewardsPanel
from panelObjs.homePanel import HomePanel
from tools.commonTools import *
from configs.elementsData import ElementsData

def box_quantity_init(bp: BasePage):
    bp.set_item_count(target_count=1,item_tpid="207001")
    bp.set_item_count(target_count=9, item_tpid="207002")
    bp.set_item_count(target_count=19, item_tpid="207003")
    bp.set_item_count(target_count=20, item_tpid="207004")
    bp.set_item_count(target_count=10000, item_tpid="207005")

def change_box_test(bp: BasePage):
    HomePanel.jump_to(bp, element=ElementsData.Home.btn_chest)
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
        if n > 0:
            open_box_test(bp,box_mian_icon, n)
        cur += 1
    print("测试通过")

def TreasureChestMerchant_price_test(bp: BasePage):
    print("正在获取图标和质量列表")
    icon_list, quantity_list, off_list = TreasureChestMerchantPanel.get_box_icon_and_quantity_and_box_off_list(bp)
    print("图标列表：",icon_list, "\n数量列表：",quantity_list, "\n折扣列表：", off_list)
    print("正在获取折扣和价格列表")
    price_list = TreasureChestMerchantPanel.get_price_list(bp)
    print("价格列表：", price_list)
    print("正在计算期望价格列表")
    expect_price_list = TreasureChestMerchantPanel.get_expect_price_list(bp, icon_list, quantity_list, off_list)
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
        click_progressbar_box_test(bp)
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
        return
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


def open_box_test(bp: BasePage, icon, quantity):
    print("正在获取开箱前的箱子点")
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    print(f"箱子点为{box_points_numerator}")
    chest_point = TreasureChestPanel.get_chest_point(bp, icon)
    box_points_numerator_expect = box_points_numerator + chest_point * quantity
    print(f"开箱后箱子点期望为{box_points_numerator_expect}")
    TreasureChestPanel.click_open_x(bp)
    TreasureChestRewardsPanel.close_TreasureChestRewardsPanel(bp)
    print("等待加分动画")
    bp.sleep(1)
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    print(f"开箱后箱子点实际为{box_points_numerator}")
    compare(box_points_numerator, box_points_numerator_expect)
    print("箱子点一致")

def TreasureChestMerchant_test(bp: BasePage):
    print(f"将绿钞设为{500}")
    bp.set_item_count(500, item_tpid="100100")
    TreasureChestPanel.goto_TreasureChestMerchantPanel(bp)
    buy_test(bp)
    refresh_cost = TreasureChestMerchantPanel.get_refresh_cost(bp)
    while refresh_cost >= 0:
        TreasureChestMerchantPanel.click_btn_refresh(bp)
        refresh_cost = TreasureChestMerchantPanel.get_refresh_cost(bp)
        if refresh_cost > TreasureChestMerchantPanel.get_resource(bp):
            bp.set_item_count(1000, item_tpid="100100")
            TreasureChestMerchantPanel.close_TreasureChestMerchantPanel(bp)
            TreasureChestPanel.goto_TreasureChestMerchantPanel(bp)
    # 刷新次数用尽再点击
    TreasureChestMerchantPanel.click_btn_refresh(bp)
    print(f"将绿钞设为{5000}")
    bp.set_item_count(5000, item_tpid="100100")
    TreasureChestMerchantPanel.close_TreasureChestMerchantPanel(bp)
    TreasureChestPanel.goto_TreasureChestMerchantPanel(bp)
    buy_test(bp)

def buy_test(bp: BasePage):
    cur = 0
    while cur < 10:
        index = random.randint(0,5)
        TreasureChestMerchantPanel.click_btn_buy(bp, index)
        cur += 1
# 跳转测试
def jump_test(bp: BasePage):
    print("正在打开付费商城界面")
    TreasureChestMerchantPanel.goto_RechargeStorePanel(bp)
    print("正在关闭付费商城界面")
    RechargeStorePanel.close_RechargeStorePanel(bp)
    print("正在关闭鱼箱商人界面")
    TreasureChestMerchantPanel.close_TreasureChestMerchantPanel(bp)
    print("正在关闭鱼箱界面")
    TreasureChestPanel.close_TreasureChestPanel(bp)
    print("测试通过")


if __name__ == '__main__':
    bp = BasePage()
    TreasureChestMerchant_test(bp)
import random

from common import gameInit
from common.basePage import BasePage
from panelObjs.gearPanel import GearPanel
from panelObjs.treasureChestPanel import TreasureChestPanel
from panelObjs.storePanel import StorePanel
from panelObjs.treasureChestRewardsPanel import TreasureChestRewardsPanel
from panelObjs.treasureChestGearsShardsPanel import TreasureChestGearsShardsPanel
from panelObjs.homePanel import HomePanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.baitAndRodAlbumPanel import BaitAndRodAlbumPanel
from tools.commonTools import *

# 随机生成0，1~10，11~20 数量的箱子
def random_box_count():
    r = random.randint(0, 2)
    if r == 0:
        return 0
    if r == 1:
        return random.randint(1, 10)
    return random.randint(11, 20)


def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)
    # 初始化箱子数量
    cur = 1
    while cur < 6:
        box_count = random_box_count()
        bp.set_item_count(target_count=box_count, item_tpid=f"20700{cur}")
        cur += 1
    bp.sleep(1)

    # 进入鱼箱界面
    bp.go_to_panel("TreasureChestPanel")
    bp.sleep(1)


    # 获取箱子信息
    box_icon_list, box_quantity_list =TreasureChestPanel.get_box_icon_and_quantity_list(bp)
    bp.debug_log(f"图标列表：{box_icon_list} , 数量列表： {box_quantity_list}")

    # 挨个选中进行打开
    cur = 0
    while cur < len(box_icon_list):
        # 选中
        bp.debug_log(f"正在选择第{cur + 1}个箱子")
        TreasureChestPanel.select_box(bp, cur)
        bp.sleep(1)
        # 得到当前展示箱子的icon名，与第cur个箱子的icon名对比
        box_mian_icon = TreasureChestPanel.get_box_main_icon(bp)
        bp.debug_log(f"当前展示箱子图标名称为：{box_mian_icon}，选中的箱子图标名称为：{box_icon_list[cur]}")
        compare(box_icon_list[cur], box_mian_icon)

        # 得到open x后的可打开数量，与第cur个箱子的数量对比
        n = TreasureChestPanel.get_open_x_n(bp)
        expect_n = box_quantity_list[cur]
        if box_quantity_list[cur] > 10:
            expect_n = 10
        bp.debug_log(f"按钮应该显示OPEN X {expect_n},实际显示为OPEN X {n}")
        compare(expect_n, n)

        # 进行开箱测试
        open_box_test(bp, box_mian_icon, n)
        cur += 1

    # 进行点击箱子点测试
    get_box_point_box_test(bp)

    # 进行tips点击测试
    click_tips_test(bp)

    TreasureChestPanel.click_btn_close(bp)
    print("测试通过")




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
        bp.sleep(1)
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
    bp.sleep(1)
    box_points_numerator_new, box_points_denominator_new = TreasureChestPanel.get_box_points(bp)
    box_points_numerator = box_points_numerator_new
    box_icon_list, quantity_list = TreasureChestPanel.get_box_icon_and_quantity_list(bp)
    compare(quantity_list, quantity_list_except)
    compare(box_points_numerator_expect, box_points_numerator)
    print("箱子点充足下的点击，测试通过")
    return True

def open_box_test(bp: BasePage, icon, quantity):
    # 得到箱子点和期望的箱子点
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    bp.debug_log(f"箱子点为{box_points_numerator}")
    chest_point = TreasureChestPanel.get_chest_point(bp, icon)
    box_points_numerator_expect = box_points_numerator + chest_point * quantity
    bp.debug_log(f"开箱后箱子点期望为{box_points_numerator_expect}")

    # 点击开箱
    TreasureChestPanel.click_open_x(bp)


    # 无法开箱就直接返回
    if quantity == 0:
        box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
        compare(box_points_numerator, box_points_numerator_expect)
        return

    # 得到open x后的可打开数量, 再次计算期望箱子点
    n = TreasureChestRewardsPanel.get_open_x_n(bp)
    box_points_numerator_expect = box_points_numerator_expect + chest_point * n

    # 可以打开就继续开
    if n > 0:
        TreasureChestRewardsPanel.skip_anime(bp)
        bp.sleep(1)
        TreasureChestRewardsPanel.click_open_x(bp)
        bp.debug_log(f"开箱后箱子点期望为{box_points_numerator_expect}")

    # 返回
    TreasureChestRewardsPanel.skip_anime(bp)
    bp.sleep(1)
    bp.clear_popup()
    box_fragment_test(bp)

    # 对比箱子点和期望箱子点
    bp.debug_log("等待加分动画")
    bp.sleep(2)
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    bp.debug_log(f"开箱后箱子点实际为{box_points_numerator}")
    compare(box_points_numerator, box_points_numerator_expect)
    bp.debug_log("箱子点一致")

def box_fragment_test(bp:BasePage):
    box_fragment_position = TreasureChestRewardsPanel.get_box_fragment_position(bp)
    print(box_fragment_position)
    # 没有就不进行测试
    if not box_fragment_position:
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        return
    r = random.randint(0, 3)

    if r == 0:
        bp.click_position(box_fragment_position)
        bp.sleep(1)
        TreasureChestGearsShardsPanel.click_tap_to_continue(bp)
        bp.sleep(1)
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        TreasureChestGearsShardsPanel.click_tap_to_continue(bp)
    elif r == 1:
        bp.click_position(box_fragment_position)
        bp.sleep(1)
        btn_enhance_position_list = TreasureChestGearsShardsPanel.get_btn_enhance_position_list(bp)
        s = random.randint(0, len(btn_enhance_position_list) - 1)
        bp.click_position(btn_enhance_position_list[s])
        bp.sleep(1)
        if not BaitAndRodAlbumPanel.is_panel_active(bp):
            raise FindNoElementError
        BaitAndRodAlbumPanel.click_btn_close(bp)
        return
    elif r == 2:
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        TreasureChestGearsShardsPanel.click_tap_to_continue(bp)
        return
    elif r == 3:
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        btn_enhance_position_list = TreasureChestGearsShardsPanel.get_btn_enhance_position_list(bp)
        s = random.randint(0, len(btn_enhance_position_list) - 1)
        bp.click_position(btn_enhance_position_list[s])
        bp.sleep(1)
        if not GearPanel.is_panel_active(bp):
            raise FindNoElementError
        GearPanel.click_btn_close(bp)
        return

def click_tips_test(bp: BasePage):
    TreasureChestPanel.click_btn_magnifier(bp)
    TreasureChestPanel.click_btn_magnifier(bp)
    preview_icon_list, preview_position_list = TreasureChestPanel.get_preview_icon_and_position_list(bp)
    index_random = random.randint(0, len(preview_icon_list) - 1)
    bp.click_position(preview_position_list[index_random])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(preview_icon_list[index_random], item_icon)
    bp.click_position([0.5, 0.9])
    if ItemTipsPanel.is_panel_active(bp):
        raise FindElementError




if __name__ == '__main__':
    bp = BasePage()
    main(bp)
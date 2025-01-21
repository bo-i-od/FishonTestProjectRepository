import random
from common import gameInit
from common.basePage import BasePage
from panelObjs.GearPanel import GearPanel
from panelObjs.TreasureChestPanel import TreasureChestPanel
from panelObjs.StorePanel import StorePanel
from panelObjs.TreasureChestRewardsPanel import TreasureChestRewardsPanel
from panelObjs.TreasureChestGearsShardsPanel import TreasureChestGearsShardsPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from tools.commonTools import *


# 随机生成0，1~10，11~20 数量的箱子
def random_box_count():
    r = random.randint(0, 2)
    if r == 0:
        return 0
    if r == 1:
        return random.randint(1, 10)
    return random.randint(11, 20)


def get_box_point_box_test(bp: BasePage):
    cur = 0
    while cur < 5:
        if click_progressbar_box_test(bp) is False:
            break
        cur += 1


def click_progressbar_box_test(bp: BasePage):
    # 箱子点不足下的点击
    if TreasureChestPanel.is_box_points_enough(bp) is False:
        box_points_expect = TreasureChestPanel.get_box_points(bp)
        TreasureChestPanel.click_progressbar_box(bp)
        bp.sleep(1)
        box_points = TreasureChestPanel.get_box_points(bp)
        compare(box_points, box_points_expect)
        return False

    # 箱子点充足下的点击
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
    return True


def open_box_test(bp: BasePage, icon, quantity):
    # 得到箱子点和期望的箱子点
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    chest_point = TreasureChestPanel.get_chest_point(bp, icon)
    box_points_numerator_expect = box_points_numerator + chest_point * quantity

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

    # 返回
    TreasureChestRewardsPanel.skip_anime(bp)
    bp.sleep(1)
    bp.clear_popup()
    box_fragment_test(bp)

    # 对比箱子点和期望箱子点
    # 等待加分动画
    bp.sleep(2)
    box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(bp)
    compare(box_points_numerator, box_points_numerator_expect)


def box_fragment_test(bp:BasePage):
    box_fragment_position = TreasureChestRewardsPanel.get_box_fragment_position(bp)
    # 没有就不进行测试
    if not box_fragment_position:
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        return
    r = random.randint(0, 3)

    if r == 0:
        bp.click_position(box_fragment_position)
        bp.sleep(1)
        TreasureChestGearsShardsPanel.click_btn_close(bp)
        bp.sleep(1)
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        TreasureChestGearsShardsPanel.click_btn_close(bp)
    elif r == 1:
        bp.click_position(box_fragment_position)
        bp.sleep(1)
        btn_enhance_position_list = TreasureChestGearsShardsPanel.get_btn_enhance_position_list(bp)
        s = random.randint(0, len(btn_enhance_position_list) - 1)
        bp.click_position(btn_enhance_position_list[s])
        bp.sleep(1)
        # if not BaitAndRodAlbumPanel.is_panel_active(bp):
        #     raise FindNoElementError
        GearPanel.click_btn_close(bp)
        return
    elif r == 2:
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        TreasureChestGearsShardsPanel.click_btn_close(bp)
        return
    elif r == 3:
        TreasureChestRewardsPanel.click_btn_close(bp)
        bp.sleep(1)
        btn_enhance_position_list = TreasureChestGearsShardsPanel.get_btn_enhance_position_list(bp)
        s = random.randint(0, len(btn_enhance_position_list) - 1)
        bp.click_position(btn_enhance_position_list[s])
        bp.sleep(1)
        # if not GearPanel.is_panel_active(bp):
        #     raise FindNoElementError
        GearPanel.click_btn_close(bp)
        return

def click_tips_test(bp: BasePage):
    TreasureChestPanel.click_btn_magnifier(bp)
    bp.sleep(1)
    preview_icon_list, preview_position_list = TreasureChestPanel.get_preview_icon_and_position_list(bp)
    index_random = random.randint(0, len(preview_icon_list) - 1)
    bp.click_position(preview_position_list[index_random])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(preview_icon_list[index_random], item_icon)
    bp.click_position([0.5, 0.9])


def box_store_test(bp: BasePage):
    # 未解锁情况点击商店
    TreasureChestPanel.click_btn_box_store(bp)
    bp.sleep(1)
    if StorePanel.is_panel_active(bp):
        raise FindElementError

    # 查询商城的解锁等级
    unlock_lv = bp.get_unlock_lv("商店")
    bp.cmd(f"levelupto {unlock_lv}")

    # 返回大厅
    bp.go_home()

    # 再次进入尝试点击商店
    bp.go_to_panel("TreasureChestPanel")
    bp.sleep(1)
    TreasureChestPanel.click_btn_box_store(bp)
    bp.sleep(1)
    StorePanel.click_btn_close(bp)
    bp.sleep(1)


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
    box_icon_list, box_quantity_list = TreasureChestPanel.get_box_icon_and_quantity_list(bp)

    # 挨个选中进行打开
    cur = 0
    while cur < len(box_icon_list):
        # 选中
        TreasureChestPanel.select_box(bp, cur)
        bp.sleep(1)
        # 得到当前展示箱子的icon名，与第cur个箱子的icon名对比
        box_mian_icon = TreasureChestPanel.get_box_main_icon(bp)
        compare(box_icon_list[cur], box_mian_icon)

        # 得到open x后的可打开数量，与第cur个箱子的数量对比
        n = TreasureChestPanel.get_open_x_n(bp)
        expect_n = box_quantity_list[cur]
        if box_quantity_list[cur] > 10:
            expect_n = 10
        compare(expect_n, n)

        # 进行开箱测试
        open_box_test(bp, box_mian_icon, n)
        cur += 1

    # 进行点击箱子点测试
    get_box_point_box_test(bp)

    # 进行tips点击测试
    click_tips_test(bp)

    box_store_test(bp)

    # 返回大厅
    bp.go_home()



if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=False)
    main(bp)
    bp.connect_close()
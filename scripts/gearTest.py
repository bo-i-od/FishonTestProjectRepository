import random
from common.basePage import BasePage
from tools.commonTools import *
from common import resource
from panelObjs.gearPanel import GearPanel
from panelObjs.gearLevelupPanel import GearLevelupPanel
from panelObjs.gearEnhancePanel import GearEnhancePanel
from panelObjs.baitAndRodAlbumPanel import BaitAndRodAlbumPanel


def lock_test(bp: BasePage):
    # 获取鱼竿列表
    rod_id_list = GearPanel.get_rod_id_list(bp)
    lock_list, unlock_list = GearPanel.get_rod_status(bp, rod_id_list)

    # 获取viewport
    rodlist_viewport = GearPanel.get_rodlist_viewport(bp)

    # 随机选取未解锁鱼竿
    r = random.randint(0, len(lock_list) - 1)
    rod_index = lock_list[r]

    # 移动到鱼竿出现，点击鱼竿
    rod_id_list = GearPanel.get_rod_id_list(bp)
    rodlist_viewport.move_until_appear(target_id=rod_id_list[rod_index])
    rod_position_list = GearPanel.get_rod_position_list(bp)
    bp.click_position(rod_position_list[rod_index])

    # 点击升级按钮
    rod_info_gear = GearPanel.get_rod_info(bp)
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(0.2)
    rod_info_gear_levelup = GearLevelupPanel.get_rod_info(bp)
    compare(rod_info_gear, rod_info_gear_levelup)
    GearLevelupPanel.click_btn_close(bp)
    bp.sleep(0.2)
    GearPanel.click_btn_enhance(bp)



if __name__ == "__main__":
    bp = BasePage()
    lock_test(bp)
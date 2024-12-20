from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *
from common.viewport import Viewport
import random

from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.gearLevelupPanel import GearLevelupPanel


class GearPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Gear.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Gear.GearPanel)

    def is_upgrade_max_active(self):
        return self.exist(element_data=ElementsData.Gear.upgrade_max)

    def is_enhance_max_active(self):
        return self.exist(element_data=ElementsData.Gear.enhance_max)

    def click_btn_upgrade(self):
        self.click_element(element_data=ElementsData.Gear.btn_upgrade)

    def click_btn_enhance(self):
        self.click_element(element_data=ElementsData.Gear.btn_enhence)

    def get_level(self):
        level = self.get_text(element_data=ElementsData.Gear.level)
        progress_now = self.get_text(element_data=ElementsData.Gear.progress_now)
        compare(level, progress_now)
        progress_max = self.get_text(element_data=ElementsData.Gear.progress_max).split("/")[1]
        return int(level), int(progress_max)


    def get_stars(self):
        stars_list = self.get_icon_list(element_data=ElementsData.Gear.stars)
        stars = 0
        cur = 0
        while cur < len(stars_list):
            if stars_list[cur] == "fish_star":
                stars += 1
                cur += 1
                continue
            stars += 2
            cur += 1
        return stars

    def get_rod_info(self):
        name = self.get_text(element_data=ElementsData.Gear.name)
        t = self.get_icon(element_data=ElementsData.Gear.t)
        kind = self.get_icon(element_data=ElementsData.Gear.kind)
        stars = GearPanel.get_stars(self)
        dps = int(self.get_text(element_data=ElementsData.Gear.dps))
        rod_info = {"name": name, "t": t, "kind": kind, "stars": stars, "dps": dps}
        return rod_info

    def get_skill_position_list(self):
        return self.get_position_list(element_data=ElementsData.Gear.skill_list)

    def get_skill_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.Gear.skill_list)

    def get_rod_id_list(self):
        rod_id_list = self.get_object_id_list(element_data=ElementsData.Gear.rod_list)
        return rod_id_list

    def get_rod_status(self, rod_id_list):
        cur = 0
        lock_list = []
        unlock_list = []
        while cur < len(rod_id_list):
            if self.get_offspring_id_list(offspring_path="lock", object_id=rod_id_list[cur]):
                lock_list.append(cur)
                cur += 1
                continue
            unlock_list.append(cur)
            cur += 1
        return lock_list, unlock_list

    def get_rodlist_viewport(self):
        rodlist_viewport = Viewport(self, element_viewport=ElementsData.Gear.rodlist_viewport, element_item_list=ElementsData.Gear.rod_bg_list)
        return rodlist_viewport

    def get_rod_position_list(self):
        return self.get_position_list(element_data=ElementsData.Gear.rod_bg_list)

    def select_unlock_rod(self):
        # 获取鱼竿列表
        rod_id_list = GearPanel.get_rod_id_list(self)
        lock_list, unlock_list = GearPanel.get_rod_status(self, rod_id_list)

        # 获取viewport
        rodlist_viewport = GearPanel.get_rodlist_viewport(self)

        # 随机选取未解锁鱼竿
        r = random.randint(0, len(unlock_list) - 1)
        rod_index = unlock_list[r]

        # 移动到鱼竿出现，点击鱼竿
        rodlist_viewport.move_until_appear(target_id=rod_id_list[rod_index])
        rod_position_list = GearPanel.get_rod_position_list(self)
        self.click_position(rod_position_list[rod_index])

    def select_lock_rod(self):
        # 获取鱼竿列表
        rod_id_list = GearPanel.get_rod_id_list(self)
        lock_list, unlock_list = GearPanel.get_rod_status(self, rod_id_list)

        # 获取viewport
        rodlist_viewport = GearPanel.get_rodlist_viewport(self)

        # 随机选取未解锁鱼竿
        r = random.randint(0, len(lock_list) - 1)
        rod_index = lock_list[r]

        # 移动到鱼竿出现，点击鱼竿
        rodlist_viewport.move_until_appear(target_id=rod_id_list[rod_index])
        rod_position_list = GearPanel.get_rod_position_list(self)
        self.click_position(rod_position_list[rod_index])

    def click_btn_filter(self):
        self.click_element(element_data=ElementsData.Gear.btn_filter)

    def is_tip_filter_rod_active(self):
        return self.exist(element_data=ElementsData.Gear.tip_filter_rod)

    def click_btn_apply(self):
        self.click_element(element_data=ElementsData.Gear.btn_apply)

    def click_btn_reset(self):
        self.click_element(element_data=ElementsData.Gear.btn_reset)

    def get_hide_unowned_toggle(self):
        return self.get_toggle_is_on(element_data=ElementsData.Gear.hide_unowned)

    def get_rarity_toggle_list(self):
        return self.get_toggle_is_on_list(element_data=ElementsData.Gear.rarity_list)

    def get_rarity_position_list(self):
        return self.get_position_list(element_data=ElementsData.Gear.rarity_list)

    def get_available_location_toggle_list(self):
        return self.get_toggle_is_on_list(element_data=ElementsData.Gear.available_location_list)

    def get_available_location_position_list(self):
        return self.get_position_list(element_data=ElementsData.Gear.available_location_list)


    def guide_oversea(self):
        perform_list = [ElementsData.NewbieGuide_oversea.NBG_fishing_fail_1,
                        ElementsData.NewbieGuide_oversea.NBG_fishing_fail_2, ElementsData.NewbieGuide_oversea.NBG_fishing_fail_3,
                        ElementsData.NewbieGuide_oversea.NBG_fishing_fail_4, ElementsData.NewbieGuide_oversea.NBG_fishing_fail_5,
                        ElementsData.NewbieGuide_oversea.NBG_fishing_fail_6, ElementsData.NewbieGuide_oversea.NBG_fishing_fail_7]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide_oversea.NBG_fishing_fail_7)
        self.sleep(1)
        GearLevelupPanel.click_btn_close(self)
        self.sleep(1)
        GearPanel.click_btn_close(self)
        self.sleep(1)
        BattlePreparePanel.click_btn_apply(self)

    def get_fishing_rod_table_data_detail(self):
        table_data_object_list = self.excelTools.get_table_data_detail(book_name="FISHING_ROD.xlsm")
        return table_data_object_list

    def click_btn_equip(self):
        self.click_element(element_data=ElementsData.Gear.btn_equip)





if __name__ == "__main__":
    bp = GearPanel()
    a = bp.click_btn_reset()
    print(a)
    # rod_id_list = GearPanel.get_rod_id_list(bp)
    # a = GearPanel.get_rod_status(bp, rod_id_list)
    # print(rod_id_list)
    # a = BaitAndRodAlbumPanel.get_all_rod_list(bp)
    # b = BaitAndRodAlbumPanel.get_all_bait_list(bp)




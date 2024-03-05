from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *
from common.viewport import Viewport


class GearPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Gear.btn_close)
        if GearPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Gear.GearPanel):
            return True
        return False

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





if __name__ == "__main__":
    bp = GearPanel()
    rod_id_list = GearPanel.get_rod_id_list(bp)
    a = GearPanel.get_rod_status(bp, rod_id_list)
    print(rod_id_list)
    # a = BaitAndRodAlbumPanel.get_all_rod_list(bp)
    # b = BaitAndRodAlbumPanel.get_all_bait_list(bp)




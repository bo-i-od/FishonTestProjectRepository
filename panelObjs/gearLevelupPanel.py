from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearLevelupPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearLevelup.btn_close)
        if GearLevelupPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.GearLevelup.GearLevelupPanel):
            return True
        return False

    def is_max_active(self):
        if self.exist(element_data=ElementsData.GearLevelup.max):
            return True
        return False

    def get_level(self):
        lv_str = self.get_text(element_data=ElementsData.GearLevelup.lv)
        if "LV." in lv_str:
            return int(lv_str.split('LV.')[1])
        if "等级" in lv_str:
            return int(lv_str.split('等级')[1])
        return -1

    def get_level_next(self):
        lv_str = self.get_text(element_data=ElementsData.GearLevelup.lv_next)
        if "LV." in lv_str:
            return int(lv_str.split('LV.')[1])
        if "等级" in lv_str:
            return int(lv_str.split('等级')[1])
        return -1

    def get_skill_value_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearLevelup.skill_value_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_skill_value_next_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearLevelup.skill_value_next_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_stars(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearLevelup.stars)
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
        name = self.get_text(element_data=ElementsData.GearLevelup.name)
        t = self.get_icon(element_data=ElementsData.GearLevelup.t)
        kind = self.get_icon(element_data=ElementsData.GearLevelup.kind)
        dps = int(self.get_text(element_data=ElementsData.GearLevelup.dps))
        stars = GearLevelupPanel.get_stars(self)
        rod_info = {"name": name, "t": t, "kind": kind, "stars": stars, "dps": dps}
        return rod_info

    def click_btn_upgrade(self):
        self.click_element(element_data=ElementsData.GearLevelup.btn_upgrade)

    def get_cost_dict(self):
        cost_icon_list = self.get_icon_list(element_data=ElementsData.GearLevelup.cost_icon_list)
        cost_quantity_list = self.get_text_list(element_data=ElementsData.GearLevelup.cost_quantity_list)
        cost_dict = make_item_dict(item_icon_list=cost_icon_list, item_quantity_list=cost_quantity_list)
        return cost_dict

    def click_btn_next(self):
        self.click_element(element_data=ElementsData.GearLevelup.btn_next)

    def click_btn_previous(self):
        self.click_element(element_data=ElementsData.GearLevelup.btn_previous)

    def click_btn_add_100000(self):
        self.click_element(element_data=ElementsData.GearLevelup.btn_add_100000)

if __name__ == '__main__':
    bp = BasePage()
    GearLevelupPanel.click_btn_next(bp)
    GearLevelupPanel.click_btn_previous(bp)


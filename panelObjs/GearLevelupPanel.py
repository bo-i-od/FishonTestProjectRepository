from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearLevelupPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearLevelupPanel.btn_close)


    def is_panel_active(self):
        return self.exist(element_data=ElementsData.GearLevelupPanel.GearLevelupPanel)

    def is_max_active(self):
        return self.exist(element_data=ElementsData.GearLevelupPanel.max)

    def get_level(self):
        lv_str = self.get_text(element_data=ElementsData.GearLevelupPanel.lv)
        if "LV." in lv_str:
            return int(lv_str.split('LV.')[1])
        if "等级" in lv_str:
            return int(lv_str.split('等级')[1])
        return -1

    def get_level_next(self):
        lv_str = self.get_text(element_data=ElementsData.GearLevelupPanel.lv_next)
        if "LV." in lv_str:
            return int(lv_str.split('LV.')[1])
        if "等级" in lv_str:
            return int(lv_str.split('等级')[1])
        return -1

    def get_skill_value_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearLevelupPanel.skill_value_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_skill_value_next_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearLevelupPanel.skill_value_next_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_stars(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearLevelupPanel.stars)
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
        name = self.get_text(element_data=ElementsData.GearLevelupPanel.name)
        t = self.get_icon(element_data=ElementsData.GearLevelupPanel.t)
        kind = self.get_icon(element_data=ElementsData.GearLevelupPanel.kind)
        dps = int(self.get_text(element_data=ElementsData.GearLevelupPanel.dps))
        stars = GearLevelupPanel.get_stars(self)
        rod_info = {"name": name, "t": t, "kind": kind, "stars": stars, "dps": dps}
        return rod_info

    def click_btn_upgrade(self):
        self.click_element(element_data=ElementsData.GearLevelupPanel.btn_upgrade)

    def get_cost_dict(self):
        cost_icon_list = self.get_icon_list(element_data=ElementsData.GearLevelupPanel.cost_icon_list)
        cost_quantity_list = self.get_text_list(element_data=ElementsData.GearLevelupPanel.cost_quantity_list)
        cost_dict = make_item_dict(item_icon_list=cost_icon_list, item_quantity_list=cost_quantity_list)
        return cost_dict

    def click_btn_next(self):
        self.click_element(element_data=ElementsData.GearLevelupPanel.btn_next)

    def click_btn_previous(self):
        self.click_element(element_data=ElementsData.GearLevelupPanel.btn_previous)

    def click_btn_add_100000(self):
        self.click_element(element_data=ElementsData.GearLevelupPanel.btn_add_100000)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.GearLevelupPanel.top_res_btns, index=index)

    operation_pool = [
        {"element_data": ElementsData.GearLevelupPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.GearLevelupPanel.btn_next, "func": click_btn_next, "weight": 1},
        {"element_data": ElementsData.GearLevelupPanel.btn_previous, "func": click_btn_previous, "weight": 1},
        {"element_data": ElementsData.GearLevelupPanel.btn_upgrade, "func": click_btn_upgrade, "weight": 1},
        {"element_data": ElementsData.GearLevelupPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    GearLevelupPanel.click_btn_close(bp)
    GearLevelupPanel.click_btn_next(bp)
    GearLevelupPanel.click_btn_previous(bp)
    GearLevelupPanel.click_btn_upgrade(bp)
    GearLevelupPanel.click_top_res_btn(bp)
    bp.connect_close()


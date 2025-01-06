from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearEnhancePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearEnhancePanel.btn_close)


    def is_panel_active(self):
        return self.exist(element_data=ElementsData.GearEnhancePanel.GearEnhancePanel)

    def is_max_active(self):
        return self.exist(element_data=ElementsData.GearEnhancePanel.max)

    def get_stars_now(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearEnhancePanel.stars_now)
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

    def get_stars_next(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearEnhancePanel.stars_next)
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

    def get_skill_value_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearEnhancePanel.skill_value_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_skill_value_next_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearEnhancePanel.skill_value_next_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_stars(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearEnhancePanel.stars)
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
        name = self.get_text(element_data=ElementsData.GearEnhancePanel.name)
        t = self.get_icon(element_data=ElementsData.GearEnhancePanel.t)
        kind = self.get_icon(element_data=ElementsData.GearEnhancePanel.kind)
        dps = int(self.get_text(element_data=ElementsData.GearEnhancePanel.dps))
        stars = GearEnhancePanel.get_stars(self)
        rod_info = {"name": name, "t": t, "kind": kind, "stars": stars, "dps": dps}
        return rod_info

    def click_btn_enhance(self):
        self.click_element(element_data=ElementsData.GearEnhancePanel.btn_enhance)

    def get_shard(self):
        shard_numerator = self.get_text(element_data=ElementsData.GearEnhancePanel.cost_numerator)
        shard_numerator = int(shard_numerator)
        shard_denominator = self.get_text(element_data=ElementsData.GearEnhancePanel.cost_denominator)
        shard_denominator = int(shard_denominator.split('/')[1])
        return shard_numerator, shard_denominator

    def click_btn_next(self):
        self.click_element(element_data=ElementsData.GearEnhancePanel.btn_next)

    def click_btn_previous(self):
        self.click_element(element_data=ElementsData.GearEnhancePanel.btn_previous)

    def get_skill_icon(self):
        return self.get_icon(element_data=ElementsData.GearEnhancePanel.skill_icon)

    def click_skill_icon(self):
        self.click_element(element_data=ElementsData.GearEnhancePanel.skill_icon)


    operation_pool = [
        {"element_data": ElementsData.GearEnhancePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.GearEnhancePanel.btn_enhance, "func": click_btn_enhance, "weight": 1},
        {"element_data": ElementsData.GearEnhancePanel.btn_next, "func": click_btn_next, "weight": 1},
        {"element_data": ElementsData.GearEnhancePanel.btn_previous, "func": click_btn_previous, "weight": 1},
        {"element_data": ElementsData.GearEnhancePanel.skill_icon, "func": click_skill_icon, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    GearEnhancePanel.click_btn_close(bp)
    GearEnhancePanel.click_btn_enhance(bp)
    GearEnhancePanel.click_btn_next(bp)
    GearEnhancePanel.click_btn_previous(bp)
    GearEnhancePanel.click_skill_icon(bp)
    bp.connect_close()
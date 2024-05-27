from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearEnhancePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearEnhance.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.GearEnhance.GearEnhancePanel):
            return True
        return False

    def is_max_active(self):
        if self.exist(element_data=ElementsData.GearEnhance.max):
            return True
        return False

    def get_stars_now(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearEnhance.stars_now)
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
        stars_list = self.get_icon_list(element_data=ElementsData.GearEnhance.stars_next)
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
        skill_value_list = self.get_text_list(element_data=ElementsData.GearEnhance.skill_value_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_skill_value_next_list(self):
        skill_value_list = self.get_text_list(element_data=ElementsData.GearEnhance.skill_value_next_list)
        str_to_int_list(skill_value_list)
        return skill_value_list

    def get_stars(self):
        stars_list = self.get_icon_list(element_data=ElementsData.GearEnhance.stars)
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
        name = self.get_text(element_data=ElementsData.GearEnhance.name)
        t = self.get_icon(element_data=ElementsData.GearEnhance.t)
        kind = self.get_icon(element_data=ElementsData.GearEnhance.kind)
        dps = int(self.get_text(element_data=ElementsData.GearEnhance.dps))
        stars = GearEnhancePanel.get_stars(self)
        rod_info = {"name": name, "t": t, "kind": kind, "stars": stars, "dps": dps}
        return rod_info

    def click_btn_enhance(self):
        self.click_element(element_data=ElementsData.GearEnhance.btn_enhance)

    def get_shard(self):
        shard_numerator = self.get_text(element_data=ElementsData.GearEnhance.cost_numerator)
        shard_numerator = int(shard_numerator)
        shard_denominator = self.get_text(element_data=ElementsData.GearEnhance.cost_denominator)
        shard_denominator = int(shard_denominator.split('/')[1])
        return shard_numerator, shard_denominator

    def click_btn_next(self):
        self.click_element(element_data=ElementsData.GearEnhance.btn_next)

    def click_btn_previous(self):
        self.click_element(element_data=ElementsData.GearEnhance.btn_previous)

    def get_skill_icon(self):
        return self.get_icon(element_data=ElementsData.GearEnhance.skill_icon)

    def click_skill_icon(self):
        self.click_element(element_data=ElementsData.GearEnhance.skill_icon)

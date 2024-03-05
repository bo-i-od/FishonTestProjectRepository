import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport
from tools.commonTools import *

class FishCardPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCard.btn_close)
        if FishCardPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FishCard.FishCardPanel):
            return True
        return False

    def click_btn_upgrade(self):
        self.click_element(element_data=ElementsData.FishCard.btn_upgrade)

    def switch_tab(self, index):
        target_id = self.get_object_id_list(element_data=ElementsData.FishCard.tab_list)[index]
        viewport = Viewport(self, element_viewport=ElementsData.FishCard.fisheries_viewport, element_item_list=ElementsData.FishCard.tab_list)
        viewport.move_until_appear(target_id)
        position_list = self.get_position_list(element_data=ElementsData.FishCard.tab_list)
        self.click_position(position_list[index])

    def get_fisheries_list(self):
        fisheries_title_list = self.get_text_list(element_data=ElementsData.FishCard.fisheries_title_list)
        return fisheries_title_list


    def select_card(self, index):
        card_id_list = FishCardPanel.get_card_id_list(self)

        target_id = card_id_list[index]
        viewport = Viewport(self, element_viewport=ElementsData.FishCard.fish_card_viewport, item_id_list=card_id_list, viewport_direction="column")
        viewport.move_until_appear(target_id)
        # position_list = self.get_position_list(element_data=ElementsData.FishCard.fisheries_title_list)
        self.click_element(object_id=card_id_list[index])

    # 得到卡模型id列表
    # 选中的卡记作selected_index 如果没有选中selected_index = -1
    def get_card_id_list(self):
        fish_card_model_id_list = self.get_object_id_list(element_data=ElementsData.FishCard.fish_card_model_list)
        return fish_card_model_id_list

    def get_card_information(self):
        fish_name = self.get_text(element_data=ElementsData.FishCard.fish_name_selected)
        fisheries_name = self.get_text(element_data=ElementsData.FishCard.fisheries_name_selected)
        progress = self.get_text(element_data=ElementsData.FishCard.progress_selected)
        progress_split = progress.split('/')
        progress_numerator = int(progress_split[0])
        progress_denominator = int(progress_split[1])
        level = int(self.get_text(element_data=ElementsData.FishCard.level_selected))
        talent = self.get_text(element_data=ElementsData.FishCard.talent_selected)
        talent = positive_percentage_to_float(talent)
        title_bg = self.get_icon(element_data=ElementsData.FishCard.title_bg_selected)
        card_information = {"fish_name": fish_name,
                            "fisheries_name": fisheries_name,
                            "progress_numerator": progress_numerator,
                            "progress_denominator": progress_denominator,
                            "level": level,
                            "talent": talent,
                            "title_bg": title_bg}
        return card_information

    def get_main_name_and_size(self):
        main_name = self.get_text(element_data=ElementsData.FishCard.main_name)
        main_size = self.get_icon(element_data=ElementsData.FishCard.main_size)
        return main_name, main_size

    def get_talent_dict(self):
        upgrade_talent_now_list = self.get_text_list(element_data=ElementsData.FishCard.talent_now_list)
        talent_dict = {}
        cur = 0
        while cur < len(upgrade_talent_now_list):
            str_split = upgrade_talent_now_list[cur].split('+')
            talent_dict[str_split[0]] = positive_percentage_to_float(str_split[1])
            cur += 1
        return talent_dict

    def get_progress_list(self, fish_card_model_id_list):
        progress_list = []
        cur = 0
        while cur < len(fish_card_model_id_list):
            progress = self.get_text_list(offspring_path="progress>text", object_id=fish_card_model_id_list[cur])
            numerator, denominator = progress[0].split("/")
            progress_list.append([int(numerator), int(denominator)])
            cur += 1
        return progress_list


    def get_card_status(self):
        fish_card_model_id_list = FishCardPanel.get_card_id_list(self)
        unlock_list = []
        unlevelable_list = []
        levelable_list = []
        progress_list = FishCardPanel.get_progress_list(self, fish_card_model_id_list)
        cur = 0
        while cur < len(progress_list):
            if progress_list[cur][0] >= progress_list[cur][1]:
                levelable_list.append(cur)
                cur += 1
                continue
            lock_id_list = self.get_offspring_id_list(offspring_path="lock", object_id=fish_card_model_id_list[cur])
            if lock_id_list:
                unlock_list.append(cur)
                cur += 1
                continue
            unlevelable_list.append(cur)
            cur += 1
        return unlock_list, unlevelable_list, levelable_list

    def get_tab_status(self):
        tab_id_list = self.get_object_id_list(element_data=ElementsData.FishCard.tab_list)
        unlock_tab_list = []
        lock_tab_list = []

        cur = 0
        while cur < len(tab_id_list):
            if self.get_offspring_id_list(object_id=tab_id_list[cur], offspring_path="lock"):
                lock_tab_list.append(cur)
                cur += 1
                continue
            unlock_tab_list.append(cur)
            cur += 1
        return unlock_tab_list, lock_tab_list


    def click_btn_events(self):
        self.click_element(element_data=ElementsData.FishCard.btn_events)

    def switch_sub_tab(self, index):
        position_list = self.get_position_list(element_data=ElementsData.FishCard.sub_tab_list)
        self.click_position(position_list[index])

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.FishCard.btn_i)

    def is_tips_cardbonus_active(self):
        if self.exist(element_data=ElementsData.FishCard.tips_cardbonus):
            return True
        return False

    @staticmethod
    def bg_to_tier(bg:str):
        if bg == "FishCard_namebg01":
            return "result_tier_small"
        if bg == "FishCard_namebg02":
            return "result_tier_medium"
        if bg == "FishCard_namebg03":
            return "result_tier_large"
        if bg == "FishCard_namebg04":
            return "result_tier_hidden"
        if bg == "FishCard_namebg05":
            return "result_tier_boss"



if __name__ == '__main__':
    bp = BasePage()
    progress_list = FishCardPanel.switch_tab(bp, 11)
    print(progress_list)


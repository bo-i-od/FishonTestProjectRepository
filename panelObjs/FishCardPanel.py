import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport
from tools.commonTools import *

class FishCardPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardPanel.btn_close)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.FishCardPanel.btn_close_tips)

    def click_btn_close_rating(self):
        self.click_element(element_data=ElementsData.FishCardPanel.btn_close_rating)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardPanel.FishCardPanel)

    def click_btn_upgrade(self):
        self.click_element(element_data=ElementsData.FishCardPanel.btn_upgrade)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FishCardPanel.tab_list, element_viewport=ElementsData.FishCardPanel.fisheries_viewport, index=index)

    def get_fisheries_list(self):
        fisheries_title_list = self.get_text_list(element_data=ElementsData.FishCardPanel.fisheries_title_list)
        return fisheries_title_list

    def select_card(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FishCardPanel.fish_card_model_list, element_viewport=ElementsData.FishCardPanel.fish_card_viewport, viewport_direction="column", index=index)

    # 得到卡模型id列表
    # 选中的卡记作selected_index 如果没有选中selected_index = -1
    def get_card_id_list(self):
        fish_card_model_id_list = self.get_object_id_list(element_data=ElementsData.FishCardPanel.fish_card_model_list)
        return fish_card_model_id_list

    def get_card_information(self):
        fish_name = self.get_text(element_data=ElementsData.FishCardPanel.fish_name_selected)
        fisheries_name = self.get_text(element_data=ElementsData.FishCardPanel.fisheries_name_selected)
        progress = self.get_text(element_data=ElementsData.FishCardPanel.progress_selected)
        progress_split = progress.split('/')
        progress_numerator = int(progress_split[0])
        progress_denominator = int(progress_split[1])
        level = int(self.get_text(element_data=ElementsData.FishCardPanel.level_selected))
        talent = self.get_text(element_data=ElementsData.FishCardPanel.talent_selected)
        talent = positive_percentage_to_float(talent)
        title_bg = self.get_icon(element_data=ElementsData.FishCardPanel.title_bg_selected)
        card_information = {"fish_name": fish_name,
                            "fisheries_name": fisheries_name,
                            "progress_numerator": progress_numerator,
                            "progress_denominator": progress_denominator,
                            "level": level,
                            "talent": talent,
                            "title_bg": title_bg}
        return card_information

    def get_main_name_and_size(self):
        main_name = self.get_text(element_data=ElementsData.FishCardPanel.main_name)
        main_size = self.get_icon(element_data=ElementsData.FishCardPanel.main_size)
        return main_name, main_size

    def get_talent_dict(self):
        upgrade_talent_now_list = self.get_text_list(element_data=ElementsData.FishCardPanel.talent_now_list)
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
        tab_id_list = self.get_object_id_list(element_data=ElementsData.FishCardPanel.tab_list)
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
        self.click_element(element_data=ElementsData.FishCardPanel.btn_events)

    def switch_sub_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FishCardPanel.sub_tab_list, index=index)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.FishCardPanel.btn_i)

    def is_tips_cardbonus_active(self):
        return self.exist(element_data=ElementsData.FishCardPanel.tips_cardbonus)

    def get_rating(self):
        rating = int(self.get_text(element_data=ElementsData.FishCardPanel.rating))
        return rating
    
    def click_rating(self):
        self.click_element(element_data=ElementsData.FishCardPanel.rating)

    def get_rating_fisheries(self):
        rating = int(self.get_text(element_data=ElementsData.FishCardPanel.rating_fisheries))
        return rating



    operation_pool = [
        {"element_data": ElementsData.FishCardPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 10},
        {"element_data": ElementsData.FishCardPanel.btn_close_rating, "func": click_btn_close_rating , "weight": 10},
        {"element_data": ElementsData.FishCardPanel.btn_events, "func": click_btn_events, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.btn_upgrade, "func": click_btn_upgrade, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.rating, "func": click_rating, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.fish_card_model_list, "func": select_card, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.sub_tab_list, "func": switch_sub_tab, "weight": 1},
        {"element_data": ElementsData.FishCardPanel.tab_list, "func": switch_tab, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # FishCardPanel.click_btn_close(bp)
    # FishCardPanel.click_btn_events(bp)
    # FishCardPanel.click_btn_i(bp)
    # FishCardPanel.click_btn_upgrade(bp)
    # FishCardPanel.click_rating(bp)
    # FishCardPanel.select_card(bp)
    # FishCardPanel.switch_sub_tab(bp)
    # FishCardPanel.switch_tab(bp)
    # FishCardPanel.click_btn_close_i(bp)
    # FishCardPanel.click_btn_close_rating(bp)
    bp.connect_close()

import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.viewport import Viewport
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
        target_id = self.get_object_id_list(element_data=ElementsData.FishCard.fisheries_bg_list)[index]
        viewport = Viewport(self, element_viewport=ElementsData.FishCard.fisheries_viewport, element_item_list=ElementsData.FishCard.fisheries_bg_list)
        viewport.move_until_appear(target_id)
        position_list = self.get_position_list(element_data=ElementsData.FishCard.fisheries_title_list)
        self.click_position(position_list[index])

    def get_fisheries_list(self):
        fisheries_title_list = self.get_text_list(element_data=ElementsData.FishCard.fisheries_title_list)
        return fisheries_title_list


    def select_card(self, index):
        card_id_list, selected_index = FishCardPanel.get_card_id_list(self)
        if selected_index == index:
            return
        target_id = card_id_list[index]
        viewport = Viewport(self, element_viewport=ElementsData.FishCard.fish_card_viewport, item_id_list=card_id_list)
        viewport.move_until_appear(target_id)
        # position_list = self.get_position_list(element_data=ElementsData.FishCard.fisheries_title_list)
        self.click_element(object_id=card_id_list[index])

    # 得到卡模型id列表
    # 选中的卡记作selected_index 如果没有选中selected_index = -1
    def get_card_id_list(self):
        fish_card_model_id_list = self.get_object_id_list(element_data=ElementsData.FishCard.fish_card_model_list)
        name_list = self.get_name_list(element_data=ElementsData.FishCard.fish_card_model_list)
        selected_index = -1
        cur = 0
        while cur < len(fish_card_model_id_list):
            if name_list[cur] == "FishCard_on":
                fish_card_model_id_list[cur] = self.get_offspring_id(offspring_path="FishCard_on>", object_id=fish_card_model_id_list[cur])
                selected_index = cur
                break
            cur += 1
        return fish_card_model_id_list, selected_index

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

    def get_arrow_index_list(self):
        fish_card_model_id_list, selected_index = FishCardPanel.get_card_id_list(self)
        arrow_index_list = []
        cur = 0
        while cur < len(fish_card_model_id_list):
            if self.get_offspring_id_list(offspring_path="kind_02>arrow", object_id=fish_card_model_id_list[cur]):
                arrow_index_list.append(cur)
            cur += 1
        return arrow_index_list

    def select_arrow_card(self):
        fisheries_title_list = self.get_text_list(element_data=ElementsData.FishCard.fisheries_title_list)
        cur = 0
        while cur < len(fisheries_title_list):
            FishCardPanel.switch_tab(self, cur)
            fisheries_name_list = self.get_text_list(element_data=ElementsData.FishCard.fisheries_name_list)
            for fisheries_name in fisheries_name_list:
                compare(fisheries_title_list[cur], fisheries_name)
            arrow_index_list = FishCardPanel.get_arrow_index_list(self)
            if not arrow_index_list:
                cur += 1
                continue
            r = random.randint(0, len(arrow_index_list) - 1)
            FishCardPanel.select_card(self, arrow_index_list[r])
            break

    def click_btn_events(self):
        self.click_element(element_data=ElementsData.FishCard.btn_events)

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
    FishCardPanel.select_arrow_card(bp)
from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common import resource


class FishCardUpgradePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardUpgrade.btn_close)
        if FishCardUpgradePanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FishCardUpgrade.FishCardUpgradePanel):
            return True
        return False

    def click_btn_level_up(self):
        self.click_element(element_data=ElementsData.FishCardUpgrade.btn_level_up)

    def level_up_check(self):
        stock = FishCardUpgradePanel.get_stock(self)
        cost = self.get_text(element_data=ElementsData.FishCardUpgrade.cost_value_list)
        cost = str_to_int(cost)
        # if not FishCardUpgradePanel.is_btn_level_up_abled(self):
        #     if stock >= cost and progress_numerator >= progress_denominator :
        #         raise CompareError
        #     return False
        if cost > stock:
            raise CompareError
        # return True

    def is_btn_level_up_abled(self):
        if self.exist(element_data=ElementsData.FishCardUpgrade.max_text):
            return False
        progress = self.get_text(element_data=ElementsData.FishCardUpgrade.progress)
        progress_split = progress.split('/')
        progress_numerator = int(progress_split[0])
        progress_denominator = int(progress_split[1])
        if progress_numerator < progress_denominator:
            return False
        return True



    def get_stock(self):
        stock = self.get_item_count(item_tpid="100000")
        # stock = resource.get_resource(self, "100000", element_data=ElementsData.FishCardUpgrade.text_100000)
        return stock

    def get_card_information(self):
        fish_name = self.get_text(element_data=ElementsData.FishCardUpgrade.fish_name_selected)
        # fisheries_name = self.get_text(element_data=ElementsData.FishCardUpgrade.fisheries_name_selected)
        # progress = self.get_text(element_data=ElementsData.FishCardUpgrade.progress_selected)
        # progress_split = progress.split('/')
        # progress_numerator = int(progress_split[0])
        # progress_denominator = int(progress_split[1])
        level = int(self.get_text(element_data=ElementsData.FishCardUpgrade.level_selected))
        rating_card = int(self.get_text(element_data=ElementsData.FishCardUpgrade.rating_card))

        # title_bg = self.get_icon(element_data=ElementsData.FishCardUpgrade.title_bg_selected)
        card_information = {"fish_name": fish_name,
                            # "fisheries_name": fisheries_name,
                            # "progress_numerator": progress_numerator,
                            # "progress_denominator": progress_denominator,
                            "level": level,
                            "rating_card": rating_card}
                            # "title_bg": title_bg
        return card_information

    def get_rating(self):
        rating = int(self.get_text(element_data=ElementsData.FishCardUpgrade.rating))
        return rating

    def get_rating_fisheries(self):
        rating = int(self.get_text(element_data=ElementsData.FishCardUpgrade.rating_fisheries))
        return rating

    def get_level_up_information(self):
        level_up_information = {}
        talent_now_list = self.get_text_list(element_data=ElementsData.FishCardUpgrade.talent_now_list)
        talent_val_now_list = []
        cur = 0
        while cur < len(talent_now_list):
            str_split = talent_now_list[cur].split('+')
            talent_val_now_list.append(positive_percentage_to_float(text=str_split[1]))
            cur += 1
        talent_val_next_list = self.get_text_list(element_data=ElementsData.FishCardUpgrade.talent_next_list)
        positive_percentage_to_float(text_list=talent_val_next_list)
        progress = self.get_text(element_data=ElementsData.FishCardUpgrade.progress)
        progress_split = progress.split('/')
        progress_numerator = int(progress_split[0])
        progress_denominator = int(progress_split[1])
        level_now = self.get_text(element_data=ElementsData.FishCardUpgrade.level_now)
        level_now = int(level_now.split('.')[1])
        level_next = self.get_text(element_data=ElementsData.FishCardUpgrade.level_next)
        level_next = int(level_next.split('.')[1])
        cost_icon_list = self.get_icon_list(element_data=ElementsData.FishCardUpgrade.cost_icon_list)
        cost_value_list = self.get_text_list(element_data=ElementsData.FishCardUpgrade.cost_value_list)
        str_to_int_list(cost_value_list)
        level_up_information["talent_val_now_list"] = talent_val_now_list
        level_up_information["talent_val_next_list"] = talent_val_next_list
        level_up_information["progress_numerator"] = progress_numerator
        level_up_information["progress_denominator"] = progress_denominator
        level_up_information["level_now"] = level_now
        level_up_information["level_next"] = level_next
        level_up_information["cost_icon_list"] = cost_icon_list
        level_up_information["cost_value_list"] = cost_value_list
        return level_up_information

    def click_btn_add_100000(self):
        self.click_element(element_data=ElementsData.FishCardUpgrade.btn_add_100000)
        if not self.exist(element_data=ElementsData.Store.panel_resource):
            raise FindNoElementError

    def click_btn_next(self):
        self.click_element(element_data=ElementsData.FishCardUpgrade.btn_next)

    def click_btn_previous(self):
        self.click_element(element_data=ElementsData.FishCardUpgrade.btn_previous)

    def get_talent_dict(self):
        upgrade_talent_now_list = self.get_text_list(element_data=ElementsData.FishCardUpgrade.talent_now_list)
        talent_dict = {}
        cur = 0
        while cur < len(upgrade_talent_now_list):
            str_split = upgrade_talent_now_list[cur].split('+')
            talent_dict[str_split[0]] = positive_percentage_to_float(str_split[1])
            cur += 1
        return talent_dict

    def click_fishcard(self):
        self.click_element(element_data=ElementsData.FishCardUpgrade.cotent_fishcard)


if __name__ == "__main__":
    bp = BasePage()
    img = bp.get_element_shot(element_data=ElementsData.FishCardUpgrade.cotent_fishcard)
    bp.save_img(img)
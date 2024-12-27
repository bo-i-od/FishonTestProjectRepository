from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishingTipsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishingTipsPanel.FishingTipsPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishingTipsPanel.btn_close)

    def switch_tab_main(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FishingTipsPanel.tab_main_list, index=index)

    def switch_tab_sub(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FishingTipsPanel.tab_sub_list, index=index)

    def click_btn_arrow(self):
        self.click_element(element_data=ElementsData.FishingTipsPanel.btn_arrow)

    operation_pool = [
        {"element_data": ElementsData.FishingTipsPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FishingTipsPanel.tab_main_list, "func": switch_tab_main, "weight": 2},
        {"element_data": ElementsData.FishingTipsPanel.tab_sub_list, "func": switch_tab_sub, "weight": 2},
        {"element_data": ElementsData.FishingTipsPanel.btn_arrow, "func": click_btn_arrow, "weight": 6},

    ]


if __name__ == '__main__':
    bp = BasePage()
    # FishingTipsPanel.click_btn_close(bp)

    # FishingTipsPanel.switch_tab_main(bp)

    # FishingTipsPanel.switch_tab_sub(bp)
    #
    FishingTipsPanel.click_btn_arrow(bp)

    bp.connect_close()

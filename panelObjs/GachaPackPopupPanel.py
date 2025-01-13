from common.basePage import BasePage
from configs.elementsData import ElementsData

class GachaPackPopupPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.GachaPackPopupPanel.GachaPackPopupPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GachaPackPopupPanel.btn_close, ignore_set={"GachaPackPopupPanel"})

    def click_btn_enter(self):
        self.click_element(element_data=ElementsData.GachaPackPopupPanel.btn_enter, ignore_set={"GachaPackPopupPanel"})

    def click_btn_form(self):
        self.click_element(element_data=ElementsData.GachaPackPopupPanel.btn_form, ignore_set={"GachaPackPopupPanel"})

    operation_pool = [
        {"element_data": ElementsData.GachaPackPopupPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.GachaPackPopupPanel.btn_enter, "func": click_btn_enter, "weight": 1},
        {"element_data": ElementsData.GachaPackPopupPanel.btn_form, "func": click_btn_form, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    # GachaPackPopupPanel.click_btn_close(bp)
    GachaPackPopupPanel.click_btn_enter(bp)
    # GachaPackPopupPanel.click_btn_form(bp)
    bp.connect_close()
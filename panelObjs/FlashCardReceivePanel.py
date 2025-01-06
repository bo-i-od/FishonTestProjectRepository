from common.basePage import BasePage
from configs.elementsData import ElementsData


class FlashCardReceivePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FlashCardReceivePanel.FlashCardReceivePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FlashCardReceivePanel.btn_close, ignore_set={"FlashCardReceivePanel"})

    operation_pool = [
        {"element_data": ElementsData.FlashCardReceivePanel.btn_close, "func": click_btn_close, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    FlashCardReceivePanel.click_btn_close(bp)
    bp.connect_close()
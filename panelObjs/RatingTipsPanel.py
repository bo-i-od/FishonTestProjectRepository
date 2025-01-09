from common.basePage import BasePage
from configs.elementsData import ElementsData


class RatingTipsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RatingTipsPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RatingTipsPanel.RatingTipsPanel)


    operation_pool = [
        {"element_data": ElementsData.RatingTipsPanel.btn_close, "func": click_btn_close, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    RatingTipsPanel.click_btn_close(bp)
    # RatingTipsPanel.is_panel_active(bp)
    bp.connect_close()
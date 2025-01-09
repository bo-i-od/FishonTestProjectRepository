from common.basePage import BasePage
from configs.elementsData import ElementsData


class NumberKeyboardPanel(BasePage):
    # 面板是否存在
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.NumberKeyboardPanel.NumberKeyboardPanel)

    # 点击关闭按钮
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.NumberKeyboardPanel.btn_close)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.NumberKeyboardPanel.btn_confirm)


    def click_btn(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NumberKeyboardPanel.btns)


    operation_pool = [
        {"element_data": ElementsData.NumberKeyboardPanel.btns, "func": click_btn, "weight": 1},
        {"element_data": ElementsData.NumberKeyboardPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.NumberKeyboardPanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    NumberKeyboardPanel.click_btn(bp)
    NumberKeyboardPanel.click_btn_confirm(bp)
    NumberKeyboardPanel.click_btn_close(bp)
    bp.connect_close()

from common.basePage import BasePage
from configs.elementsData import ElementsData

class MessageBoxPanel(BasePage):
    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.MessageBoxPanel.btn_cancel, ignore_set={"MessageBoxPanel"})

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.MessageBoxPanel.btn_confirm, ignore_set={"MessageBoxPanel"})

    def click_toggle(self):
        self.click_element(ElementsData.MessageBoxPanel.toggle, ignore_set={"MessageBoxPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MessageBoxPanel.MessageBoxPanel)


    operation_pool = [
        {"element_data": ElementsData.MessageBoxPanel.btn_cancel, "func": click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.MessageBoxPanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.MessageBoxPanel.toggle, "func": click_toggle, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    MessageBoxPanel.click_btn_cancel(bp)
    MessageBoxPanel.click_btn_confirm(bp)
    MessageBoxPanel.click_toggle(bp)
    MessageBoxPanel.is_panel_active(bp)
    bp.connect_close()
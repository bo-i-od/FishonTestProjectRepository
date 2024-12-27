from common.basePage import BasePage
from configs.elementsData import ElementsData

class MessageBoxPanel(BasePage):
    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.MessageBoxPanel.btn_cancel, ignore_set={"MessageBoxPanel"})

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.MessageBoxPanel.btn_confirm, ignore_set={"MessageBoxPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MessageBoxPanel.MessageBoxPanel)
from common.basePage import BasePage
from configs.elementsData import ElementsData



class CommonItemGetPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.CommonItemGet.btn_close)
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.CommonItemGet.CommonItemGetPanel)
from common.basePage import BasePage
from configs.elementsData import ElementsData



class HomePanelNew(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.HomePanelNew.HomePanelNew)

    def click_btn_spot(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.HomePanelNew.btn_spot, index=index)

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    HomePanelNew.click_btn_spot(bp, index=1)
    bp.connect_close()
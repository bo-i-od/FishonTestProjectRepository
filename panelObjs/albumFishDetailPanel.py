from common.basePage import BasePage
from configs.elementsData import ElementsData


class AlbumFishDetailPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AlbumFishDetail.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AlbumFishDetail.AlbumFishDetailPanel)

    def click_btn_share(self):
        self.click_element(element_data=ElementsData.AlbumFishDetail.btn_share)
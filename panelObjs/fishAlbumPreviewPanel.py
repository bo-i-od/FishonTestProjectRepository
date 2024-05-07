from common.basePage import BasePage
from configs.elementsData import ElementsData

from tools.commonTools import *


class FishAlbumPreviewPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishAlbumPreview.btn_close)
        if FishAlbumPreviewPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FishAlbumPreview.FishAlbumPreviewPanel):
            return True
        return False
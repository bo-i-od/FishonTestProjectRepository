from common.basePage import BasePage
from configs.elementsData import ElementsData

from tools.commonTools import *


class FishAlbumPreviewPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishAlbumPreview.btn_close, ignore_set={"FishAlbumPreviewPanel"})


    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishAlbumPreview.FishAlbumPreviewPanel)
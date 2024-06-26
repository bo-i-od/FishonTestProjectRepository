from common.basePage import BasePage
from configs.elementsData import ElementsData

from tools.commonTools import *


class FishAlbum3DPanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.FishAlbum3D.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FishAlbum3D.FishAlbum3DPanel):
            return True
        return False

    def guide(self):
        perform_list = [ElementsData.NewbieGuide.NBG_album_01, ElementsData.NewbieGuide.NBG_album_02, ElementsData.NewbieGuide.NBG_album_03,ElementsData.Home.HomePanel]
        self.click_a_until_b_appear_list(perform_list=perform_list)

    def click_btn_share(self):
        self.click_until_disappear(element_data=ElementsData.FishAlbum3D.btn_share)

    def click_btn_switch(self):
        self.click_element(element_data=ElementsData.FishAlbum3D.btn_switch)

if __name__ == "__main__":
    bp = BasePage()
    FishAlbum3DPanel.guide(bp)
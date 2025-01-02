from common.basePage import BasePage
from configs.elementsData import ElementsData


class AlbumFishDetailPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AlbumFishDetailPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AlbumFishDetailPanel.AlbumFishDetailPanel)

    def click_btn_share(self):
        self.click_element(element_data=ElementsData.AlbumFishDetailPanel.btn_share)

    def click_btn_share_chat(self):
        self.click_element(element_data=ElementsData.AlbumFishDetailPanel.btn_share_chat)

    def click_btn_close_share_chat(self):
        self.click_element(element_data=ElementsData.AlbumFishDetailPanel.btn_close_share_chat)

    def click_btn_confirm(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AlbumFishDetailPanel.btn_confirm_list, index=index)

    operation_pool = [
        {"element_data": ElementsData.AlbumFishDetailPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AlbumFishDetailPanel.btn_share, "func": click_btn_share, "weight": 4},
        {"element_data": ElementsData.AlbumFishDetailPanel.btn_share_chat, "func": click_btn_share, "weight": 4},
        {"element_data": ElementsData.AlbumFishDetailPanel.btn_close_share_chat, "func": click_btn_close_share_chat, "weight": 2},
        {"element_data": ElementsData.AlbumFishDetailPanel.btn_confirm_list, "func": click_btn_confirm, "weight": 4},
        ]

if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    # AlbumFishDetailPanel.click_btn_share(bp)

    # AlbumFishDetailPanel.click_btn_share_chat(bp)

    # AlbumFishDetailPanel.click_btn_close_share_chat(bp)

    AlbumFishDetailPanel.click_btn_confirm(bp)
    bp.connect_close()
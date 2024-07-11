from common.basePage import BasePage
from common.viewport import Viewport
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

    def get_reward_icon_position(self):
        return self.get_position(element_data=ElementsData.FishAlbum3D.reward_icon)

    def click_btn_preview(self):
        self.click_element(element_data=ElementsData.FishAlbum3D.btn_preview)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.FishAlbum3D.btn_i)

    def is_panel_rewards_tip_active(self):
        if self.exist(element_data=ElementsData.FishAlbum3D.panel_rewards_tip):
            return True
        return False

    def is_panel_fisheries_active(self):
        if self.exist(element_data=ElementsData.FishAlbum3D.panel_fisheries):
            return True
        return False

    def switch_tab(self, index):
        target_id = self.get_object_id_list(element_data=ElementsData.FishAlbum3D.fisheries_list)[index]
        viewport = Viewport(self, element_viewport=ElementsData.FishAlbum3D.fisheries_list_viewport,
                            element_item_list=ElementsData.FishAlbum3D.fisheries_list)
        viewport.move_until_appear(target_id)
        position_list = self.get_position_list(element_data=ElementsData.FishAlbum3D.fisheries_list)
        self.click_position(position_list[index])

    def get_tab_status(self, tab_id_list):
        unlock_tab_list = []
        lock_tab_list = []

        cur = 0
        while cur < len(tab_id_list):
            if self.get_offspring_id_list(object_id=tab_id_list[cur], offspring_path="lock"):
                lock_tab_list.append(cur)
                cur += 1
                continue
            unlock_tab_list.append(cur)
            cur += 1
        return unlock_tab_list, lock_tab_list

    def get_tab_name_list(self, tab_id_list):
        tab_name_list = self.get_text_list(object_id_list=tab_id_list, offspring_path="title")
        return tab_name_list

    def get_progress_cur(self):
        progress_cur_list = self.get_text_list(element_data=ElementsData.FishAlbum3D.progress_cur_list)
        str_to_int_list(progress_cur_list)
        progress_cur = progress_cur_list[0] + progress_cur_list[1]
        return progress_cur

    def get_tab_id_list(self):
        tab_id_list = self.get_object_id_list(element_data=ElementsData.FishAlbum3D.fisheries_list)
        return tab_id_list

    def get_select_index(self, tab_id_list):
        cur = 0
        while cur < len(tab_id_list):
            if self.get_offspring_id_list(object_id_list=tab_id_list[cur], offspring_path="select"):
                break
            cur += 1
        return cur

    def get_photo_name(self):
        return self.get_text(element_data=ElementsData.FishAlbum3D.photo_name)

    def get_photo_bg(self):
        return self.get_icon(element_data=ElementsData.FishAlbum3D.photo_bg)

    def get_photo_bg_position(self):
        return self.get_position(element_data=ElementsData.FishAlbum3D.photo_bg)

    def get_star_position_list(self):
        return self.get_position_list(element_data=ElementsData.FishAlbum3D.star_list)




if __name__ == "__main__":
    bp = BasePage()
    FishAlbum3DPanel.guide(bp)
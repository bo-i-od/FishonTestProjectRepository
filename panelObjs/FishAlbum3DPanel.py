from common.basePage import BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData

from tools.commonTools import *


class FishAlbum3DPanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.FishAlbum3DPanel.btn_close, ignore_set={"FishAlbum3DPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishAlbum3DPanel.FishAlbum3DPanel)

    def click_btn_share(self):
        self.click_until_disappear(element_data=ElementsData.FishAlbum3DPanel.btn_share, ignore_set={"FishAlbum3DPanel"})

    def click_btn_switch(self):
        self.click_element(element_data=ElementsData.FishAlbum3DPanel.btn_switch)

    def get_reward_icon_position(self):
        return self.get_position(element_data=ElementsData.FishAlbum3DPanel.reward_icon)

    def click_btn_preview(self):
        self.click_element(element_data=ElementsData.FishAlbum3DPanel.btn_preview)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.FishAlbum3DPanel.btn_i)

    def is_panel_rewards_tip_active(self):
        return self.exist(element_data=ElementsData.FishAlbum3DPanel.panel_rewards_tip)

    def is_panel_fisheries_active(self):
        return self.exist(element_data=ElementsData.FishAlbum3DPanel.panel_fisheries)

    def switch_tab(self, index):
        target_id = self.get_object_id_list(element_data=ElementsData.FishAlbum3DPanel.fisheries_list)[index]
        viewport = Viewport(self, element_viewport=ElementsData.FishAlbum3DPanel.fisheries_list_viewport,
                            element_item_list=ElementsData.FishAlbum3DPanel.fisheries_list)
        viewport.move_until_appear(target_id)
        position_list = self.get_position_list(element_data=ElementsData.FishAlbum3DPanel.fisheries_list)
        self.click_position(position_list[index])

    def get_tab_status(self, tab_id_list):
        unlock_tab_list = []
        lock_tab_list = []

        cur = 0
        while cur < len(tab_id_list):
            lock_id_list = self.get_offspring_id_list(object_id=tab_id_list[cur], offspring_path="lock")
            if lock_id_list:
                lock_tab_list.append(cur)
                cur += 1
                continue
            unlock_tab_list.append(cur)
            cur += 1
        return unlock_tab_list, lock_tab_list

    def get_tab_name_list(self, tab_id_list):
        tab_name_list = self.get_text_list(object_id_list=tab_id_list, offspring_path="title")
        tab_name_list = merge_list(tab_name_list)
        return tab_name_list

    def get_progress_cur(self):
        progress_cur_list = self.get_text_list(element_data=ElementsData.FishAlbum3DPanel.progress_cur_list)
        str_to_int_list(progress_cur_list)
        progress_cur = progress_cur_list[0] + progress_cur_list[1]
        return progress_cur

    def get_tab_id_list(self):
        tab_id_list = self.get_object_id_list(element_data=ElementsData.FishAlbum3DPanel.fisheries_list)
        return tab_id_list

    def get_select_index(self, tab_id_list):
        cur = 0
        while cur < len(tab_id_list):
            select_id_list = self.get_offspring_id_list(object_id_list=tab_id_list[cur], offspring_path="select")
            select_id_list = merge_list(select_id_list)
            if select_id_list:
                break
            cur += 1
        return cur

    def get_photo_name(self):
        return self.get_text(element_data=ElementsData.FishAlbum3DPanel.photo_name)

    def get_photo_bg(self):
        return self.get_icon(element_data=ElementsData.FishAlbum3DPanel.photo_bg)

    def get_photo_bg_position(self):
        return self.get_position(element_data=ElementsData.FishAlbum3DPanel.photo_bg)

    def get_star_position_list(self):
        return self.get_position_list(element_data=ElementsData.FishAlbum3DPanel.star_list)




if __name__ == "__main__":
    bp = BasePage()
    FishAlbum3DPanel.guide(bp)
import random

import tools.commonTools
from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport


class PlayerEditNamePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerEditNamePanel.PlayerEditNamePanel)

    def is_panel_active_oversea(self):
        return self.exist(element_data=ElementsData.PlayerEditNamePanel_oversea.PlayerEditNamePanel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.PlayerEditNamePanel.PlayerEditNamePanel, is_click=False)

    def wait_for_panel_appear_oversea(self):
        self.wait_for_appear(element_data=ElementsData.PlayerEditNamePanel_oversea.PlayerEditNamePanel, is_click=False)

    def get_player_name(self):
        return self.get_text(element_data=ElementsData.PlayerEditNamePanel.Input_PlayerName)

    def get_player_name_oversea(self):
        return self.get_text(element_data=ElementsData.PlayerEditNamePanel_oversea.Input_PlayerName)

    # 编辑名称
    def set_player_name(self, name: str=None):
        if name is None:
            name = tools.commonTools.generate_random_string(random.randint(0, 30))
        object_id_list = self.get_object_id_list(element_data_list=[ElementsData.PlayerEditNamePanel.Input_PlayerName, ElementsData.PlayerEditNamePanel.Input_PlayerName_oversea])
        if object_id_list[0]:
            self.set_text(element_data=ElementsData.PlayerEditNamePanel.Input_PlayerName, text=name)
            return
        if object_id_list[1]:
            self.set_text(element_data=ElementsData.PlayerEditNamePanel.Input_PlayerName, text=name)
            return

    def set_player_name_oversea(self, name: str):
        object_id_list = self.get_object_id_list(
            element_data_list=[ElementsData.PlayerEditNamePanel_oversea.Input_PlayerName,
                               ElementsData.PlayerEditNamePanel_oversea.Input_PlayerName])
        if object_id_list[0]:
            self.set_text(element_data=ElementsData.PlayerEditNamePanel_oversea.Input_PlayerName, text=name)
            return
        if object_id_list[1]:
            self.set_text(element_data=ElementsData.PlayerEditNamePanel_oversea.Input_PlayerName, text=name)
            return

    def get_head_viewport(self, head_id_list):
        head_viewport = Viewport(self, element_viewport=ElementsData.PlayerEditNamePanel.head_viewport, item_id_list=head_id_list, viewport_direction="column")
        return head_viewport

    def get_head_viewport_oversea(self, head_id_list):
        head_viewport = Viewport(self, element_viewport=ElementsData.PlayerEditNamePanel_oversea.head_viewport, item_id_list=head_id_list, viewport_direction="column")
        return head_viewport

    # 根据序号选择头像,并返回选择头像的object_id
    def select_head(self, head_id_list, index: int):
        head_id = head_id_list[index]
        head_viewport = PlayerEditNamePanel.get_head_viewport(self, head_id_list=head_id_list)
        head_viewport.move_until_appear(target_id=head_id)
        self.click_element(object_id=head_id)
        return head_id

    # 得到有多少个头像可以选
    def get_head_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerEditNamePanel.head_list)

    # 得到选择特效框的object_id
    def get_select_object_id(self):
        return self.get_object_id(element_data=ElementsData.PlayerEditNamePanel.select)

    # 得到有多少个头像可以选

    def get_head_id_list_oversea(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerEditNamePanel_oversea.head_list)

    # 得到选择特效框的object_id

    def get_select_object_id_oversea(self):
        return self.get_object_id(element_data=ElementsData.PlayerEditNamePanel_oversea.select)

    def get_head_object_id(self, head_img_object_id: int):
        head_mask_object_id = self.get_parent_id(head_img_object_id)
        head_object_id = self.get_parent_id(head_mask_object_id)
        return head_object_id

    # 点击确认按钮
    def click_confirm(self, is_ray_input=False):
        position_list = self.get_position_list(element_data_list=[ElementsData.PlayerEditNamePanel.btn_confirm, ElementsData.PlayerEditNamePanel_oversea.btn_confirm])
        if position_list[0]:
            if is_ray_input:
                self.ray_input(kind="click", element_data=ElementsData.PlayerEditNamePanel.btn_confirm)
                return
            self.click_position(position_list[0][0])
            return
        if position_list[1]:
            if is_ray_input:
                self.ray_input(kind="click", element_data=ElementsData.PlayerEditNamePanel_oversea.btn_confirm)
                return
            self.click_position(position_list[1][0])
            return

    def click_head(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerEditNamePanel.head_list, element_viewport=ElementsData.PlayerEditNamePanel.head_viewport, viewport_direction="column", index=index)

    operation_pool = [
        {"element_data": ElementsData.PlayerEditNamePanel.btn_confirm, "func": click_confirm, "weight": 1},
        {"element_data": ElementsData.PlayerEditNamePanel.head_list, "func": click_head, "weight": 1},
        {"element_data": ElementsData.PlayerEditNamePanel.Input_PlayerName, "func": set_player_name, "weight": 1},

    ]


if __name__ == "__main__":
    bp = BasePage()
    PlayerEditNamePanel.click_head(bp)
    PlayerEditNamePanel.set_player_name(bp)
    PlayerEditNamePanel.click_confirm(bp)

    bp.connect_close()
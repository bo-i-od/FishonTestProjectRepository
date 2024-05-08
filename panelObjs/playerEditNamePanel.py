from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport


class PlayerEditNamePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PlayerEditName.PlayerEditNamePanel):
            return True
        return False

    def get_player_name(self):
        return self.get_text(element_data=ElementsData.PlayerEditName.Input_PlayerName)

    # 编辑名称
    def set_player_name(self, name: str):
        self.set_text(element_data=ElementsData.PlayerEditName.Input_PlayerName, text=name)

    def get_head_viewport(self, head_id_list):
        head_viewport = Viewport(self, element_viewport=ElementsData.PlayerEditName.head_viewport, item_id_list=head_id_list, viewport_direction="column")
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
        return self.get_object_id_list(element_data=ElementsData.PlayerEditName.head_list)

    # 得到选择特效框的object_id
    def get_select_object_id(self):
        return self.get_object_id(element_data=ElementsData.PlayerEditName.select)

    def get_head_object_id(self, head_img_object_id: int):
        head_mask_object_id = self.get_parent_id(head_img_object_id)
        head_object_id = self.get_parent_id(head_mask_object_id)
        return head_object_id

    # 点击确认按钮
    def click_confirm(self):
        self.click_until_disappear(element_data=ElementsData.PlayerEditName.btn_confirm)

if __name__ == "__main__":
    bp = BasePage()
    head_id_list = PlayerEditNamePanel.get_head_id_list(bp)
    PlayerEditNamePanel.select_head(bp, head_id_list=head_id_list, index=24)
from common.basePage import BasePage
from configs.elementsData import ElementsData


class PlayerEditNamePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PlayerEditName.PlayerEditNamePanel):
            return True
        return False
    def get_name(self):
        return self.get_text(element_data=ElementsData.PlayerEditName.Input_PlayerName)

    # 编辑名称
    def set_name(self, name: str):
        self.set_text(element_data=ElementsData.PlayerEditName.Input_PlayerName, text=name)

    # 根据序号选择头像,并返回选择头像的object_id
    def select_head(self, index: int):
        head_id_list = self.get_object_id_list(element_data=ElementsData.PlayerEditName.head_list)
        object_id = head_id_list[index]
        self.click_element(object_id=object_id)
        return object_id

    # 得到有多少个头像可以选
    def get_head_count(self):
        return len(self.get_object_id_list(element_data=ElementsData.PlayerEditName.head_list))

    # 得到选择特效框的object_id
    def get_select_object_id(self):
        return self.get_object_id(element_data=ElementsData.PlayerEditName.select)

    def get_head_object_id(self, head_img_object_id: int):
        head_mask_object_id = self.get_parent_id(head_img_object_id)
        head_object_id = self.get_parent_id(head_mask_object_id)
        return head_object_id

    # 点击确认按钮
    def click_confirm(self):
        self.click_element(element_data=ElementsData.PlayerEditName.btn_confirm)

if __name__ == "__main__":
    bp = PlayerEditNamePanel()
    n = bp.get_name()
    print(n)
    bp.set_name(n[1:])
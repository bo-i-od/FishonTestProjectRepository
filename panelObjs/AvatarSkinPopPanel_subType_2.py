from common.basePage import BasePage
from configs.elementsData import ElementsData


class AvatarSkinPopPanel_subType_2(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarSkinPopPanel_subType_2.AvatarSkinPopPanel_subType_2)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AvatarSkinPopPanel_subType_2.btn_close, ignore_set={"AvatarSkinPopPanel_subType_2"})

    def click_btn_enter(self):
        self.click_element(element_data=ElementsData.AvatarSkinPopPanel_subType_2.btn_enter, ignore_set={"AvatarSkinPopPanel_subType_2"})

    operation_pool = [
        {"element_data": ElementsData.AvatarSkinPopPanel_subType_2.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AvatarSkinPopPanel_subType_2.btn_enter, "func": click_btn_enter, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    AvatarSkinPopPanel_subType_2.click_btn_close(bp)
    # AvatarSkinPopPanel_subType_2.click_btn_enter(bp)

    bp.connect_close()
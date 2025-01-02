from common.basePage import BasePage
from configs.elementsData import ElementsData


class AvatarTipsView(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarTipsView.AvatarTipsView)

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.AvatarTipsView.tap_to_continue)

    def click_btn_changesex(self):
        self.click_element(element_data=ElementsData.AvatarTipsView.btn_changesex)

    def click_btn_changecamera(self):
        self.click_element(element_data=ElementsData.AvatarTipsView.btn_changecamera)

    operation_pool = [
        {"element_data": ElementsData.AvatarTipsView.tap_to_continue, "func": click_tap_to_continue, "weight": 1},
        {"element_data": ElementsData.AvatarTipsView.btn_changesex, "func": click_btn_changesex, "weight": 2},
        {"element_data": ElementsData.AvatarTipsView.btn_changecamera, "func": click_btn_changecamera, "weight": 2},
        ]

if __name__ == '__main__':
    bp = BasePage()

    # AvatarTipsView.click_tap_to_continue(bp)

    # AvatarTipsView.click_btn_changesex(bp)
    #
    AvatarTipsView.click_btn_changecamera(bp)

    bp.connect_close()
from common.basePage import BasePage
from common.error import FindNoElementError
from configs.elementsData import ElementsData


class FishCardSelectPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardSelectPanel.FishCardSelectPanel)
    def wait_for_panel_appear(self,ignore_set=None):
        if ignore_set is None:
            ignore_set = {"FishCardSelectPanel"}
        try:
            self.wait_for_appear(element_data=ElementsData.FishCardSelectPanel.FishCardSelectPanel, is_click=False, ignore_set=ignore_set)
            return True
        except Exception:
            return False

    def click_btn_fishery(self):
        position_list = self.get_position_list(element_data=ElementsData.FishCardSelectPanel.fishery_select_list)
        if position_list:
            self.click_position(position_list[0])
        else:
            raise FindNoElementError("No fishery select button found")
    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.FishCardSelectPanel.btn_select_confirm)



if __name__ == '__main__':
    bp = BasePage()
    FishCardSelectPanel.click_btn_confirm(bp)
    bp.connect_close()



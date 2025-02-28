from common.basePage import BasePage
from configs.elementsData import ElementsData


class MainStageSettlePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MainStageSettlePanel.MainStageSettlePanel)

    def click_btn_blue(self):
        self.click_until_disappear(element_data=ElementsData.MainStageSettlePanel.btn_blue)

    def click_btn_orange(self):
        self.click_element(element_data=ElementsData.MainStageSettlePanel.btn_orange)

    def get_status(self):
        object_id_list = self.get_object_id_list(element_data=ElementsData.MainStageSettlePanel.MainStageSettlePanel, offspring_path="panel_lost")
        if object_id_list:
            return "失败"
        object_id_list = self.get_object_id_list(element_data=ElementsData.MainStageSettlePanel.MainStageSettlePanel,
                                                 offspring_path="panel_succeed")
        if object_id_list:
            return "成功"
        return "未知"


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    MainStageSettlePanel.get_status(bp)

    bp.connect_close()


from common.basePage import BasePage
from configs.elementsData import ElementsData


class MainStageBattleFailedPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MainStageBattleFailedPanel.MainStageBattleFailedPanel)

    def click_btn_again(self):
        self.click_element(element_data=ElementsData.MainStageBattleFailedPanel.btn_again)


if __name__ == '__main__':
    bp = BasePage("192.168.111.34:20089", is_mobile_device=False)
    MainStageBattleFailedPanel.click_btn_again(bp)
    bp.connect_close()
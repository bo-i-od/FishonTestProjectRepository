from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattlePassIntroPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassIntroPanel.BattlePassIntroPanel)

    def close_battlePassIntroPanel(self, is_test=True):
        if is_test:
            # 点next按钮 从1到2
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.next1to2)
            # 点←箭头 从2到1
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.panel2to1Btn)
            # 点→箭头 从1到2
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.panel1to2Btn)
            # 点→箭头 从2到3
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.panel2to3Btn)
            # 点←箭头 从3到2
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.panel3to2Btn)
            # 点next按钮 从2到3
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.next2to3)
            # 点next按钮 关闭
            self.click_element(element_data=ElementsData.BattlePassIntroPanel.btn_go)
            return
        self.click_element(element_data=ElementsData.BattlePassIntroPanel.panel1to2Btn)
        self.click_element(element_data=ElementsData.BattlePassIntroPanel.panel2to3Btn)
        self.click_element(element_data=ElementsData.BattlePassIntroPanel.btn_go)


if __name__ == "__main__":
    bp = BattlePassIntroPanel()
    bp.close_battlePassIntroPanel(is_test=False)


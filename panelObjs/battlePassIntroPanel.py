from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattlePassIntroPanel(BasePage):
    def close_battlePassIntroPanel(self, is_test=True):
        if is_test:
            # 点next按钮 从1到2
            self.click_element(element_data=ElementsData.BattlePassIntro.next1to2)
            # 点←箭头 从2到1
            self.click_element(element_data=ElementsData.BattlePassIntro.panel2to1Btn)
            # 点→箭头 从1到2
            self.click_element(element_data=ElementsData.BattlePassIntro.panel1to2Btn)
            # 点→箭头 从2到3
            self.click_element(element_data=ElementsData.BattlePassIntro.panel2to3Btn)
            # 点←箭头 从3到2
            self.click_element(element_data=ElementsData.BattlePassIntro.panel3to2Btn)
            # 点next按钮 从2到3
            self.click_element(element_data=ElementsData.BattlePassIntro.next2to3)
            # 点next按钮 关闭
            self.click_element(element_data=ElementsData.BattlePassIntro.go)
            return
        self.click_element(element_data=ElementsData.BattlePassIntro.panel1to2Btn)
        self.click_element(element_data=ElementsData.BattlePassIntro.panel2to3Btn)
        self.click_element(element_data=ElementsData.BattlePassIntro.go)

if __name__ == "__main__":
    bp = BattlePassIntroPanel()
    bp.close_battlePassIntroPanel(is_test=False)


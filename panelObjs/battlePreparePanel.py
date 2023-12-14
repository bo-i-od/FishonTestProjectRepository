from common.basePage import BasePage
from configs.elementsData import ElementsData

class BattlePreparePanel(BasePage):
    def cast(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.btn_cast, is_click=False)
        position = self.get_position(element_data=ElementsData.BattlePrepare.btn_cast)
        while position and (not self.exist(element_data=ElementsData.BuyEnergy.BuyEnergyPanel)):
            self.click_position(position)
            self.sleep(0.2)

    def click_btn_cast(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.btn_cast, is_click=True)

    def click_btn_quick_switch(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.quick_switch, is_click=True)



if __name__ == '__main__':
    bp = BasePage()
    BattlePreparePanel.click_btn_cast(bp)




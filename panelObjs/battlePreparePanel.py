from common.basePage import BasePage
from configs.elementsData import ElementsData

class BattlePreparePanel(BasePage):
    def cast(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.pve_prepare.btn_cast, is_click=False)
        position = self.get_position(element_data=ElementsData.BattlePrepare.pve_prepare.btn_cast)
        while self.exist(element_data=ElementsData.BattlePrepare.pve_prepare.btn_cast) and self.exist(element_data=ElementsData.BuyEnergy.BuyEnergyPanel) is False:
            self.click_position(position)
            self.sleep(0.2)


from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from items import resource

class BuyEnergyPanel(BasePage):
    def click_tap_to_close(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_close)
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuyEnergy.BuyEnergyPanel)

    def click_btn_drink(self):
        remaining_drink_value = self.get_text(element_data=ElementsData.BuyEnergy.remaining_drink_value)
        if int(remaining_drink_value) <= 0:
            print("没有能量饮料了")
            return False
        self.click_element(element_data=ElementsData.BuyEnergy.btn_drink)
        return True

    def click_btn_cash(self):
        cost_cash = self.get_text(element_data=ElementsData.BuyEnergy.btn_cash)
        resource.get_resource(self, item_tpid="100100", element_data=ElementsData.BuyEnergy.text_100100)
        cash_value = self.get_text(element_data=ElementsData.BuyEnergy.text_100100)
        if int(cost_cash) > int(cash_value):
            print("没钱买体力了")
            return False
        self.click_element(element_data=ElementsData.BuyEnergy.btn_cash)
        return True

    def get_energy(self):
        if BuyEnergyPanel.click_btn_drink(self) is True:
            RewardsPanel.click_tap_to_continue(self)
            return
        BuyEnergyPanel.click_btn_cash(self)
        RewardsPanel.click_tap_to_continue(self)

    def click_btn_add_100100(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_add_100100)



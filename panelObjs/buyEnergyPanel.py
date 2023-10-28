from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel

class BuyEnergyPanel(BasePage):
    def drink_energy(self):
        remaining_drink_value = self.get_text(element_data=ElementsData.BuyEnergy.remaining_drink_value)
        if int(remaining_drink_value) <= 0:
            print("没有能量饮料了")
            return False
        self.click_element(element_data=ElementsData.BuyEnergy.btn_drink)
        return True

    def buy_energy(self):
        cost_cash = self.get_text(element_data=ElementsData.BuyEnergy.btn_cash)
        cash_value = self.get_text(element_data=ElementsData.BuyEnergy.cash_value)
        if int(cost_cash) > int(cash_value):
            print("没钱买体力了")
            return False
        self.click_element(element_data=ElementsData.BuyEnergy.btn_cash)
        return True

    def tap_to_close(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_close)

    def get_energy(self):
        if BuyEnergyPanel.drink_energy(self) is True:
            RewardsPanel.click_tap_to_continue(self)
            return
        BuyEnergyPanel.buy_energy(self)
        RewardsPanel.click_tap_to_continue(self)

    def buy_energy_panel_is_opened(self):
        return self.exist(element_data=ElementsData.BuyEnergy.BuyEnergyPanel)
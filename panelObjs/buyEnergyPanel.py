from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *


class BuyEnergyPanel(BasePage):
    def click_tap_to_close(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_close)
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuyEnergy.BuyEnergyPanel)

    def click_btn_drink(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_drink)
        return True

    def click_btn_cash(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_cash)
        return True

    def click_btn_cash_usd(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_cash_usd)

    def get_drink_count(self):
        remaining_drink_value = self.get_text(element_data=ElementsData.BuyEnergy.remaining_drink_value)
        drink_count = resource.str_to_int(remaining_drink_value)
        item_count = self.get_item_count(item_tpid="200600")
        compare(drink_count, item_count)
        return drink_count

    def get_drink_recovery_value(self):
        drink_recovery_value = self.get_text(element_data=ElementsData.BuyEnergy.drink_recovery_value)
        return str_to_int(drink_recovery_value)

    def get_cash_recovery_value(self):
        cash_recovery_value = self.get_text(element_data=ElementsData.BuyEnergy.cash_recovery_value)
        return str_to_int(cash_recovery_value)

    def get_cash_usd_recovery_value(self):
        cash_usd_recovery_value = self.get_text(element_data=ElementsData.BuyEnergy.cash_usd_recovery_value)
        return str_to_int(cash_usd_recovery_value)


    def buy_energy(self):
        if BuyEnergyPanel.click_btn_drink(self) is True:
            RewardsPanel.wait_for_panel_appear(self)
            self.sleep(1)
            RewardsPanel.click_tap_to_claim(self)
            return
        BuyEnergyPanel.click_btn_cash(self)
        RewardsPanel.wait_for_panel_appear(self)
        self.sleep(1)
        RewardsPanel.click_tap_to_claim(self)


    def get_energy_value(self):
        energy_text = self.get_text(element_data=ElementsData.BuyEnergy.text_100500)
        energy_value = str_to_int(energy_text.split('/')[0])
        item_count = self.get_item_count(item_tpid="100500")
        compare(energy_value, item_count)
        return energy_value

    def get_cash_value(self):
        cash_value = resource.get_resource(self, item_tpid="100100", element_data=ElementsData.BuyEnergy.text_100100)
        return cash_value

    def get_cash_cost(self):
        cash_cost = self.get_text(element_data=ElementsData.BuyEnergy.btn_cash, offspring_path='text')
        return str_to_int(cash_cost)

    def click_btn_add_100100(self):
        self.click_element(element_data=ElementsData.BuyEnergy.btn_add_100100)

    def get_btn_drink_status(self):
        if self.get_object_id_list(element_data=ElementsData.BuyEnergy.btn_drink, offspring_path="btn_disabled"):
            return 0
        return 1

    def get_btn_cash_status(self):
        btn_cash_id_list = self.get_object_id_list(element_data=ElementsData.BuyEnergy.btn_cash)
        if not btn_cash_id_list:
            return 2
        if self.get_object_id_list(element_data=ElementsData.BuyEnergy.btn_cash, offspring_path="btn_disabled"):
            return 0
        return 1

    def get_btn_cash_usd_status(self):
        btn_cash_usd_id_list = self.get_object_id_list(element_data=ElementsData.BuyEnergy.btn_cash_usd)
        if not btn_cash_usd_id_list:
            return 2
        if self.get_object_id_list(element_data=ElementsData.BuyEnergy.btn_cash_usd, offspring_path="btn_disabled"):
            return 0
        return 1



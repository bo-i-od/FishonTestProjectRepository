from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.basePage import BasePage
from tools.commonTools import *

class BattlePassPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_close)
        if BattlePassPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePass.BattlePassPanel):
            return True
        return False

    # 点击鱼竿进入预览
    def click_btn_detail(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_detail)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_i)

    def click_btn_i_gold_band(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_i_goldbank)

    def is_Tip_goldbank_active(self):
        if self.exist(element_data=ElementsData.BattlePass.Tip_goldbank):
            return True
        return False

    def click_btn_task(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_task)

    def click_btn_buy_levels(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_buy)

    def click_btn_get_premium(self):
        if not self.exist(element_data=ElementsData.BattlePass.btn_premium):
            return False
        self.click_element(element_data=ElementsData.BattlePass.btn_premium)
        return True

    def click_btn_unlock_premium(self):
        if not self.exist(element_data=ElementsData.BattlePass.btn_unlock):
            return False
        self.click_element(element_data=ElementsData.BattlePass.btn_unlock)
        return True

    def click_btn_collect_all(self):
        if not self.exist(element_data=ElementsData.BattlePass.btn_collect):
            return False
        self.click_element(element_data=ElementsData.BattlePass.btn_collect)
        return True


    def get_premium_collectable_icon_quantity_and_position_list(self):
        return BattlePassPanel.get_collectable_icon_quantity_and_position_list(self, ElementsData.BattlePass.particle_claim_premium_list)

    def get_free_collectable_icon_quantity_and_position_list(self):
        return BattlePassPanel.get_collectable_icon_quantity_and_position_list(self, ElementsData.BattlePass.particle_claim_free_list)


    def get_collectable_icon_quantity_and_position_list(self, element_particle_claim):
        # 获得付费的可点击
        particle_claim_id_list = self.get_parent_id_list(element_data=element_particle_claim)
        icon_id_list = self.get_offspring_id_list(offspring_path="item>item_model_new(Clone)>icon", object_id_list=particle_claim_id_list)
        icon_list = self.get_icon_list(object_id_list=icon_id_list)
        # check_icon_list(icon_list)
        quantity_id_list = self.get_offspring_id_list(offspring_path="item>item_model_new(Clone)>quantity>value", object_id_list=particle_claim_id_list)
        quantity_list = self.get_text_list(object_id_list=quantity_id_list)
        str_to_int_list(quantity_list)
        position_list = self.get_position_list(object_id_list=icon_id_list)
        return icon_list, quantity_list, position_list

    def get_viewport(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePass.Viewport, element_item_list=ElementsData.BattlePass.reward_icon_list)
        return viewport

    def get_preview_icon_and_position_list(self):
        preview_item_icon_list = self.get_icon_list(element_data=ElementsData.BattlePass.preview_item_icon_list)
        preview_item_position_list = self.get_position_list(element_data=ElementsData.BattlePass.preview_item_icon_list)
        preview_gear_icon_list = self.get_icon_list(element_data=ElementsData.BattlePass.preview_gear_icon_list)
        preview_gear_position_list = self.get_position_list(element_data=ElementsData.BattlePass.preview_gear_icon_list)
        return preview_item_icon_list, preview_item_position_list, preview_gear_icon_list, preview_gear_position_list

if __name__ == '__main__':
    bp = BasePage()
    a = BattlePassPanel.get_free_collectable_icon_quantity_and_position_list(bp)
    print(a)


    



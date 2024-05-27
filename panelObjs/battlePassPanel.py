from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.basePage import BasePage
from tools.commonTools import *

class BattlePassPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_close)

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

    def get_premium_position_list(self):
        return self.get_position_list(element_data=ElementsData.BattlePass.premium_icon_list)

    def get_free_position_list(self):
        return self.get_position_list(element_data=ElementsData.BattlePass.free_icon_list)

    def get_premium_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.BattlePass.premium_icon_list)

    def get_free_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.BattlePass.free_icon_list)

    def get_premium_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.BattlePass.premium_quantity_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_free_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.BattlePass.free_quantity_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_gear_data(self):
        gear_id = self.get_object_id(element_data=ElementsData.BattlePass.reward_gear_list)
        position = self.get_position(object_id = gear_id)
        return gear_id, position

    def get_premium_id_list(self):
        object_id_list = self.get_object_id_list(element_data=ElementsData.BattlePass.premium_list)
        return object_id_list

    def get_free_id_list(self):
        object_id_list = self.get_object_id_list(element_data=ElementsData.BattlePass.free_list)
        return object_id_list

    def get_free_status(self):
        free_id_list = BattlePassPanel.get_free_id_list(self)
        uncollectable_list = []
        collectable_list = []
        collected_list = []
        cur = 0
        while cur < len(free_id_list):
            particle_claim_id_list = self.get_offspring_id_list(offspring_path="particle_claim",object_id=free_id_list[cur])
            if particle_claim_id_list:
                collectable_list.append(cur)
                cur += 1
                continue
            collected_id_list = self.get_offspring_id_list(offspring_path="item>item_model_new(Clone)>collected",object_id=free_id_list[cur])
            if collected_id_list:
                collected_list.append(cur)
                cur += 1
                continue
            uncollectable_list.append(cur)
            cur += 1
            continue
        return uncollectable_list, collectable_list, collected_list

    def get_premium_status(self):
        premium_id_list = BattlePassPanel.get_premium_id_list(self)
        status_list = []
        premium_id_list_len = len(premium_id_list)
        cur = 0
        while cur < premium_id_list_len:
            gear_model_id_list = self.get_offspring_id_list(offspring_path="item>gear_model_new(Clone)",object_id=premium_id_list[cur])
            if gear_model_id_list:
                cur += 1
                continue
            particle_claim_id_list = self.get_offspring_id_list(offspring_path="particle_claim",object_id=premium_id_list[cur])
            if particle_claim_id_list:
                status_list.append(1)
                cur += 1
                continue
            collected_id_list = self.get_offspring_id_list(offspring_path="item>item_model_new(Clone)>collected",object_id=premium_id_list[cur])
            if collected_id_list:
                status_list.append(2)
                cur += 1
                continue
            status_list.append(0)
            cur += 1
            continue
        return BattlePassPanel.get_status(status_list)

    @staticmethod
    def get_status(status_list):
        uncollectable_list = []
        collectable_list = []
        collected_list = []
        cur = 0
        while cur < len(status_list):
            if status_list[cur] == 0:
                uncollectable_list.append(cur)
                cur += 1
                continue
            if status_list[cur] == 1:
                collectable_list.append(cur)
                cur += 1
                continue
            if status_list[cur] == 2:
                collected_list.append(cur)
                cur += 1
                continue
        return uncollectable_list, collectable_list, collected_list

    # def get_premium_collectable_data(self):
    #     return BattlePassPanel.get_collectable_data(self, ElementsData.BattlePass.particle_claim_premium_list)
    #
    # def get_free_collectable_data(self):
    #     return BattlePassPanel.get_collectable_data(self, ElementsData.BattlePass.particle_claim_free_list)


    # def get_collectable_data(self, element_particle_claim):
    #     # 获得付费的可点击
    #     particle_claim_id_list = self.get_parent_id_list(element_data=element_particle_claim)
    #     icon_id_list = self.get_offspring_id_list(offspring_path="item>item_model_new(Clone)>icon", object_id_list=particle_claim_id_list)
    #     icon_list = self.get_icon_list(object_id_list=icon_id_list)
    #     # check_icon_list(icon_list)
    #     quantity_id_list = self.get_offspring_id_list(offspring_path="item>item_model_new(Clone)>quantity>value", object_id_list=particle_claim_id_list)
    #     quantity_list = self.get_text_list(object_id_list=quantity_id_list)
    #     str_to_int_list(quantity_list)
    #     print(icon_list, quantity_list, icon_id_list)
    #     return icon_list, quantity_list, icon_id_list

    def get_collectable_icon_position(self, icon_id):
        return self.get_position(object_id=icon_id)


    def get_viewport(self):
        right_size = self.get_size_list(element_data=ElementsData.BattlePass.free_icon_list)[0][0] + 0.05
        viewport_free = Viewport(self, element_viewport=ElementsData.BattlePass.Viewport, element_item_list=ElementsData.BattlePass.free_icon_list, viewport_edge=[0, right_size])
        viewport_premium = Viewport(self, element_viewport=ElementsData.BattlePass.Viewport, element_item_list=ElementsData.BattlePass.premium_icon_list, viewport_edge=[0, right_size])
        return viewport_free, viewport_premium

    def get_preview_icon_and_position_list(self):
        preview_item_icon_list = self.get_icon_list(element_data=ElementsData.BattlePass.preview_item_icon_list)
        preview_item_position_list = self.get_position_list(element_data=ElementsData.BattlePass.preview_item_icon_list)
        preview_gear_icon_list = self.get_icon_list(element_data=ElementsData.BattlePass.preview_gear_icon_list)
        preview_gear_position_list = self.get_position_list(element_data=ElementsData.BattlePass.preview_gear_icon_list)
        return preview_item_icon_list, preview_item_position_list, preview_gear_icon_list, preview_gear_position_list

if __name__ == '__main__':
    bp = BasePage()
    bp.click_element(element_data=ElementsData.DailyTips.btn_close)



    



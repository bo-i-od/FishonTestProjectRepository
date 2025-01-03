from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.basePage import BasePage
from tools.commonTools import *

class BattlePassPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassPanel.BattlePassPanel)

    # 点击鱼竿进入预览
    def click_btn_detail(self):
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_detail)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_i)

    def click_btn_i_gold_band(self):
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_i_goldbank)

    def is_Tip_goldbank_active(self):
        return self.exist(element_data=ElementsData.BattlePassPanel.Tip_goldbank)

    def click_btn_task(self):
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_task)

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_buy)

    def click_btn_premium(self):
        if not self.exist(element_data=ElementsData.BattlePassPanel.btn_premium):
            return False
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_premium)
        return True

    def click_btn_unlock_premium(self):
        if not self.exist(element_data=ElementsData.BattlePassPanel.btn_unlock):
            return False
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_unlock)
        return True

    def click_btn_collect_all(self):
        if not self.exist(element_data=ElementsData.BattlePassPanel.btn_collect):
            return False
        self.click_element(element_data=ElementsData.BattlePassPanel.btn_collect)
        return True

    def get_premium_position_list(self):
        return self.get_position_list(element_data=ElementsData.BattlePassPanel.premium_icon_list)

    def get_free_position_list(self):
        return self.get_position_list(element_data=ElementsData.BattlePassPanel.free_icon_list)

    def get_premium_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.BattlePassPanel.premium_icon_list)

    def get_free_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.BattlePassPanel.free_icon_list)

    def get_premium_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.BattlePassPanel.premium_quantity_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_free_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.BattlePassPanel.free_quantity_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_gear_data(self):
        gear_id = self.get_object_id(element_data=ElementsData.BattlePassPanel.reward_gear_list)
        position = self.get_position(object_id = gear_id)
        return gear_id, position

    def get_premium_id_list(self):
        object_id_list = self.get_object_id_list(element_data=ElementsData.BattlePassPanel.premium_list)
        return object_id_list

    def get_free_id_list(self):
        object_id_list = self.get_object_id_list(element_data=ElementsData.BattlePassPanel.free_list)
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
        right_size = self.get_size_list(element_data=ElementsData.BattlePassPanel.free_icon_list)[0][0] + 0.05
        viewport_free = Viewport(self, element_viewport=ElementsData.BattlePassPanel.Viewport, element_item_list=ElementsData.BattlePassPanel.free_icon_list, viewport_edge=[0, right_size])
        viewport_premium = Viewport(self, element_viewport=ElementsData.BattlePassPanel.Viewport, element_item_list=ElementsData.BattlePassPanel.premium_icon_list, viewport_edge=[0, right_size])
        return viewport_free, viewport_premium

    def get_preview_icon_and_position_list(self):
        preview_item_icon_list = self.get_icon_list(element_data=ElementsData.BattlePassPanel.preview_item_icon_list)
        preview_item_position_list = self.get_position_list(element_data=ElementsData.BattlePassPanel.preview_item_icon_list)
        preview_gear_icon_list = self.get_icon_list(element_data=ElementsData.BattlePassPanel.preview_gear_icon_list)
        preview_gear_position_list = self.get_position_list(element_data=ElementsData.BattlePassPanel.preview_gear_icon_list)
        return preview_item_icon_list, preview_item_position_list, preview_gear_icon_list, preview_gear_position_list

    def click_item(self, index=-1):
        right_size = self.get_size_list(element_data=ElementsData.BattlePassPanel.item_icon_list)[0][0] + 0.05
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassPanel.Viewport, element_item_list=ElementsData.BattlePassPanel.item_icon_list, viewport_edge=[0, right_size])
        self.click_object_of_plural_objects(element_data=ElementsData.BattlePassPanel.item_icon_list, viewport=viewport, index=index)

    def click_preview(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BattlePassPanel.preview_item_list, index=index)

    operation_pool = [
        {"element_data": ElementsData.BattlePassPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_buy, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_task, "func": click_btn_task, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_collect, "func": click_btn_collect_all, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_unlock, "func": click_btn_unlock_premium, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_i_goldbank, "func": click_btn_i_gold_band, "weight": 2},
        {"element_data": ElementsData.BattlePassPanel.btn_detail, "func": click_btn_detail, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.btn_premium, "func": click_btn_premium, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.item_icon_list, "func": click_item, "weight": 1},
        {"element_data": ElementsData.BattlePassPanel.preview_item_list, "func": click_preview, "weight": 1},
        ]

if __name__ == '__main__':
    bp = BasePage()
    # BattlePassPanel.click_preview(bp)
    #
    # BattlePassPanel.click_item(bp)

    # BattlePassPanel.click_btn_detail(bp)

    # BattlePassPanel.click_btn_premium(bp)
    #
    BattlePassPanel.click_btn_unlock_premium(bp)

    bp.connect_close()



    



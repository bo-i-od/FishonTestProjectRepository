from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *
from common import resource

class DLCDownloadPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DLCDownloadPanel.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DLCDownloadPanel.DLCDownloadPanel):
            return True
        return False

    def get_item_dict_list(self):
        item_dict_list = []
        group_id_list = self.get_object_id_list(element_data=ElementsData.DLCDownloadPanel.group_list)
        cur = 0
        while cur < len(group_id_list):
            icon_list = self.get_icon_list(object_id=group_id_list[cur], offspring_path="item>>icon")
            quantity_list = self.get_text_list(object_id=group_id_list[cur], offspring_path="item>>quantity>value")
            str_to_int_list(quantity_list)
            item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
            item_dict_list.append(item_dict)
            cur += 1
        return item_dict_list

    def get_reward_icon_position_list(self):
        return self.get_position_list(element_data=ElementsData.DLCDownloadPanel.icon_list)

    def get_reward_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.DLCDownloadPanel.icon_list)


    def get_btn_claim_position_list(self):
        position_list = []
        group_id_list = self.get_object_id_list(element_data=ElementsData.DLCDownloadPanel.group_list)
        cur = 0
        while cur < len(group_id_list):
            btn_claim_position = self.get_position_list(object_id=group_id_list[cur], offspring_path="btn_orange>btn_normal")
            if not btn_claim_position:
                completed_list = self.get_position_list(object_id=group_id_list[cur],offspring_path="completed_bg")
                if not completed_list:
                    raise FindNoElementError
                position_list.append([])
                cur += 1
                continue
            position_list.append(btn_claim_position[0])
            cur += 1
        return position_list

class DLCDownloadPanel_oversea(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DLCDownloadPanel_oversea.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DLCDownloadPanel_oversea.DLCDownloadPanel):
            return True
        return False

    def get_item_dict_list(self):
        item_dict_list = []
        group_id_list = self.get_object_id_list(element_data=ElementsData.DLCDownloadPanel_oversea.group_list)
        cur = 0
        while cur < len(group_id_list):
            icon_list = self.get_icon_list(object_id=group_id_list[cur], offspring_path="item>>icon")
            quantity_list = self.get_text_list(object_id=group_id_list[cur], offspring_path="item>>quantity>value")
            str_to_int_list(quantity_list)
            item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
            item_dict_list.append(item_dict)
            cur += 1
        return item_dict_list

    def get_reward_icon_position_list(self):
        return self.get_position_list(element_data=ElementsData.DLCDownloadPanel_oversea.icon_list)

    def get_reward_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.DLCDownloadPanel_oversea.icon_list)


    def get_btn_claim_position_list(self):
        position_list = []
        group_id_list = self.get_object_id_list(element_data=ElementsData.DLCDownloadPanel_oversea.group_list)
        cur = 0
        while cur < len(group_id_list):
            btn_claim_position = self.get_position_list(object_id=group_id_list[cur], offspring_path="btn_orange>btn_normal")
            if not btn_claim_position:
                completed_list = self.get_position_list(object_id=group_id_list[cur],offspring_path="completed_bg")
                if not completed_list:
                    raise FindNoElementError
                position_list.append([])
                cur += 1
                continue
            position_list.append(btn_claim_position[0])
            cur += 1
        return position_list
if __name__ == '__main__':
    bp = BasePage()
    a = DLCDownloadPanel.get_item_dict_list(bp)
    print(a)
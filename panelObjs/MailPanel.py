from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport
class MailPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.MailPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MailPanel.MailPanel)

    def get_tab_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.MailPanel.tab_list)
        return position_list

    def switch_tab(self, position_list: list, index: int):
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.MailPanel.tab_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def is_mail_empty(self):
        return self.exist(element_data=ElementsData.MailPanel.EmptyMailTip)

    def get_mail_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.MailPanel.mail_list)
        return position_list

    def get_mail_viewport(self):
        size_list = self.get_size_list(element_data=ElementsData.MailPanel.mail_list)
        bottom = 0
        if size_list:
            bottom = 0.5 * size_list[0][1]
        mail_viewport = Viewport(self, element_viewport=ElementsData.MailPanel.mail_viewport, element_item_list=ElementsData.MailPanel.mail_list, viewport_edge=[0, bottom])
        return mail_viewport

    def get_mail_detail_viewport(self,item_id_list):
        mail_detail_viewport = Viewport(self, element_viewport=ElementsData.MailPanel.mail_detail_viewport, item_id_list=item_id_list)
        mail_detail_viewport.viewport_direction = "column"
        return mail_detail_viewport

    def get_mail_is_on_list(self):
        return self.get_toggle_is_on_list(element_data=ElementsData.MailPanel.mail_list)

    def get_mail_is_on_index(self, mail_is_on_list):
        return get_toggle_is_on_index(mail_is_on_list)


    def is_claimable(self):
        return self.exist(element_data=ElementsData.MailPanel.btn_claim)

    def is_claimed(self):
        return self.exist(element_data=ElementsData.MailPanel.text_claimed)

    def click_btn_claim(self):
        self.click_element(element_data=ElementsData.MailPanel.btn_claim)

    def get_reward_icon_id_list(self):
        reward_icon_id_list = self.get_object_id_list(element_data=ElementsData.MailPanel.reward_icon_list)
        return reward_icon_id_list

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.MailPanel.reward_icon_list)
        return reward_icon_list

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.MailPanel.reward_icon_list)
        return reward_position_list

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.MailPanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    def get_btn_claim_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.MailPanel.btn_claim)






if __name__ == '__main__':
    bp = BasePage()
    mail_viewport = MailPanel.get_mail_viewport(bp)
    mail_viewport.move_until_appear(mail_viewport.item_id_list[0])
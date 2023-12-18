from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport
from common import resource


class TaskPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Task.btn_close)
        if TaskPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Task.TaskPanel):
            return True
        return False

    def get_viewport(self):
        viewport = Viewport(self, element_viewport=ElementsData.Task.view_port, element_item_list=ElementsData.Task.task_list)
        return viewport

    def get_clickable_index_list(self, viewport: Viewport):
        viewport.element_item_list = ElementsData.Task.task_list
        clickable_index_list = viewport.get_clickable_index_list()
        return clickable_index_list

    def get_award_dict(self, task_id_list:list, index:int):
        task_id = task_id_list[index]
        icon_id_list = self.get_offspring_id_list(offspring_path=">item_model_new>icon", object_id=task_id)
        quantity_id_list = self.get_offspring_id_list(offspring_path=">item_model_new>quantity>value", object_id=task_id)
        icon_list = self.get_icon_list(object_id_list=icon_id_list)
        quantity_list = self.get_text_list(object_id_list=quantity_id_list)
        str_to_int_list(quantity_list)
        item_dict = resource.make_item_dict(item_coin_list=icon_list, item_quantity_list=quantity_list)
        return item_dict

    def get_task_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.Task.task_list)

    def get_btn_status_and_position_list(self, task_id_list:list):
        # 0代表go 1代表collect 2代表completed
        btn_status_list = []
        btn_position_list = []
        cur = 0
        while cur < len(task_id_list):
            btn_undone_id_list = self.get_offspring_id_list(offspring_path="btn_undone", object_id=task_id_list[cur])
            if btn_undone_id_list:
                btn_status_list.append(0)
                btn_position = self.get_position(object_id=btn_undone_id_list[0])
                btn_position_list.append(btn_position)
                cur += 1
                continue
            btn_completed_id_list = self.get_offspring_id_list(offspring_path="btn_completed", object_id=task_id_list[cur])
            if btn_completed_id_list:
                btn_status_list.append(1)
                btn_position = self.get_position(object_id=btn_completed_id_list[0])
                btn_position_list.append(btn_position)
                cur += 1
                continue
            finish_id_list = self.get_offspring_id_list(offspring_path="finish", object_id=task_id_list[cur])
            if finish_id_list:
                btn_status_list.append(2)
                btn_position = self.get_position(object_id=finish_id_list[0])
                btn_position_list.append(btn_position)
                cur += 1
                continue
            btn_status_list.append(3)
            btn_position_list.append([0, 0])
        return btn_status_list, btn_position_list

    def switch_tab(self, index:int):
        # 0是日常 1是周常 2是月常
        if index == 0:
            self.click_element(element_data=ElementsData.Task.tab_daily)
            return
        if index == 1:
            self.click_element(element_data=ElementsData.Task.tab_weekly)
            return
        if index == 2:
            self.click_element(element_data=ElementsData.Task.tab_month)

    def get_clickable_icon_and_position_list(self, viewport: Viewport):
        viewport.change_item(element_data=ElementsData.Task.item_icon_list)
        clickable_icon_list, clickable_position_list = viewport.get_clickable_icon_and_position_list()
        return clickable_icon_list, clickable_position_list


    def get_box_status_and_position_list(self):
        box_id_list = self.get_object_id_list(element_data=ElementsData.Task.box_list)
        # 0 代表未完成  1 代表未领奖  2 代表已领奖
        box_status_list = []
        box_position_list = []
        cur = 0
        while cur < len(box_id_list):
            ing_id_list = self.get_offspring_id_list(offspring_path="ing", object_id=box_id_list[cur])
            if ing_id_list:
                box_status_list.append(0)
                btn_position = self.get_position(object_id=ing_id_list[0])
                box_position_list.append(btn_position)
                cur += 1
                continue
            award_id_list = self.get_offspring_id_list(offspring_path="award", object_id=box_id_list[cur])
            if award_id_list:
                box_status_list.append(1)
                btn_position = self.get_position(object_id=award_id_list[0])
                box_position_list.append(btn_position)
                cur += 1
                continue
            done_id_list = self.get_offspring_id_list(offspring_path="done", object_id=box_id_list[cur])
            if done_id_list:
                box_status_list.append(2)
                btn_position = self.get_position(object_id=done_id_list[0])
                box_position_list.append(btn_position)
                cur += 1
                continue
            cur += 1
        return box_status_list, box_position_list

    def get_box_award_icon_list(self):
        award_icon_list = self.get_icon_list(element_data=ElementsData.Task.award_icon_list)
        return award_icon_list

    def get_box_award_quantity_list(self):
        award_quantity_list = self.get_text_list(element_data=ElementsData.Task.award_quantity_list)
        str_to_int_list(award_quantity_list)
        return award_quantity_list

    def get_box_award_position_list(self):
        award_position_list = self.get_position_list(element_data=ElementsData.Task.award_icon_list)
        return award_position_list

    def get_box_award_dict(self):
        box_award_icon_list = TaskPanel.get_box_award_icon_list(self)
        box_award_quantity_list = TaskPanel.get_box_award_quantity_list(self)
        return resource.make_item_dict(item_coin_list=box_award_icon_list, item_quantity_list=box_award_quantity_list)

    def get_progress_value(self):
        progress_value = self.get_slider_value(element_data=ElementsData.Task.progress_value)
        return progress_value

    def get_duel_task_index(self):
        text_list = self.get_text_list(element_data=ElementsData.Task.text_list)
        cur = 0
        while cur < len(text_list):
            if text_list[cur] == "Complete 1 Duel":
                break
            cur += 1
        return cur

    def get_task_kind(self):
        task_kind = self.get_text_list(element_data=ElementsData.Task.kind_list)[0]
        return task_kind





if __name__ == '__main__':
    bp = BasePage()
    v = TaskPanel.get_viewport(bp)
    # print(v.viewport_range)
    v.change_item(ElementsData.Task.item_icon_list)
    il,pl =v.get_clickable_icon_and_position_list()
    bp.click_position(pl[0])
    # task_id_list = TaskPanel.get_task_id_list(bp)
    # # btn_status_list, btn_position_list = TaskPanel.get_btn_status_and_position_list(bp, task_id_list)
    # # bp.click_position(btn_position_list[1])
    # # v.move_until_appear(task_id_list[8])
    # print(TaskPanel.get_box_award_icon_list(bp))






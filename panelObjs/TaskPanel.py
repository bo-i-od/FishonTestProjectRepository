from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport
from common import resource
from panelObjs.ItemTipsPanel import ItemTipsPanel


class TaskPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.TaskPanel.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.TaskPanel.TaskPanel):
            return True
        return False

    def get_viewport(self):
        viewport = Viewport(self, element_viewport=ElementsData.TaskPanel.viewport, element_item_list=ElementsData.TaskPanel.task_list,  viewport_direction="row")
        return viewport


    def get_task_award_dict(self, task_id_list:list, index:int):
        task_id = task_id_list[index]
        icon_id_list = self.get_offspring_id_list(offspring_path=">item_model_new>icon", object_id=task_id)
        quantity_id_list = self.get_offspring_id_list(offspring_path=">item_model_new>quantity>value", object_id=task_id)
        icon_list = self.get_icon_list(object_id_list=icon_id_list)
        icon_list = merge_list(icon_list)
        quantity_list = self.get_text_list(object_id_list=quantity_id_list)
        quantity_list = merge_list(quantity_list )
        str_to_int_list(quantity_list)
        item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
        return item_dict

    def get_task_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.TaskPanel.task_list)

    def get_btn_status(self, task_id_list:list):
        # 0代表go 1代表collect 2代表completed
        uncollectable_list = []
        collectable_list = []
        collected_list = []
        cur = 0
        while cur < len(task_id_list):
            btn_undone_id_list = self.get_offspring_id_list(offspring_path="btn_undone", object_id=task_id_list[cur])
            if btn_undone_id_list:
                uncollectable_list.append(cur)
                cur += 1
                continue
            btn_completed_id_list = self.get_offspring_id_list(offspring_path="btn_completed", object_id=task_id_list[cur])
            if btn_completed_id_list:
                collectable_list.append(cur)
                cur += 1
                continue
            finish_id_list = self.get_offspring_id_list(offspring_path="finish", object_id=task_id_list[cur])
            if finish_id_list:
                collected_list.append(cur)
                cur += 1
                continue
        return uncollectable_list, collectable_list, collected_list

    def get_btn_position_list(self, task_id_list: list):
        # 0代表go 1代表collect 2代表completed
        btn_position_list = []
        cur = 0
        while cur < len(task_id_list):
            btn_undone_id_list = self.get_offspring_id_list(offspring_path="btn_undone", object_id=task_id_list[cur])
            if btn_undone_id_list:
                btn_position = self.get_position(object_id=btn_undone_id_list[0])
                btn_position_list.append(btn_position)
                cur += 1
                continue
            btn_completed_id_list = self.get_offspring_id_list(offspring_path="btn_completed", object_id=task_id_list[cur])
            if btn_completed_id_list:
                btn_position = self.get_position(object_id=btn_completed_id_list[0])
                btn_position_list.append(btn_position)
                cur += 1
                continue
            finish_id_list = self.get_offspring_id_list(offspring_path="finish", object_id=task_id_list[cur])
            if finish_id_list:
                btn_position = self.get_position(object_id=finish_id_list[0])
                btn_position_list.append(btn_position)
                cur += 1
                continue
            btn_position_list.append([0, 0])
        return btn_position_list

    def switch_tab(self, index=-1):
        # 0是日常 1是周常 2是月常
        self.click_object_of_plural_objects(element_data=ElementsData.TaskPanel.tab_list, index=index)

    def get_task_award_icon_list(self):
        task_award_icon_list = self.get_icon_list(element_data=ElementsData.TaskPanel.task_award_icon_list)
        return task_award_icon_list

    def get_task_award_position_list(self):
        task_award_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.task_award_icon_list)
        return task_award_position_list

    def get_box_status(self):
        box_id_list = self.get_object_id_list(element_data=ElementsData.TaskPanel.box_list)
        uncollectable_list = []
        collectable_list = []
        collected_list = []
        cur = 0
        while cur < len(box_id_list):
            ing_id_list = self.get_offspring_id_list(offspring_path="ing", object_id=box_id_list[cur])
            if ing_id_list:
                uncollectable_list.append(cur)
                cur += 1
                continue
            award_id_list = self.get_offspring_id_list(offspring_path="award", object_id=box_id_list[cur])
            if award_id_list:
                collectable_list.append(cur)
                cur += 1
                continue
            done_id_list = self.get_offspring_id_list(offspring_path="done", object_id=box_id_list[cur])
            if done_id_list:
                collected_list.append(cur)
                cur += 1
                continue
            cur += 1
        return uncollectable_list, collectable_list, collected_list


    def get_box_position_list(self):
        box_id_list = self.get_object_id_list(element_data=ElementsData.TaskPanel.box_list)
        # 0 代表未完成  1 代表未领奖  2 代表已领奖
        box_position_list = []
        cur = 0
        while cur < len(box_id_list):
            ing_id_list = self.get_offspring_id_list(offspring_path="ing", object_id=box_id_list[cur])
            if ing_id_list:
                btn_position = self.get_position(object_id=ing_id_list[0])
                box_position_list.append(btn_position)
                cur += 1
                continue
            award_id_list = self.get_offspring_id_list(offspring_path="award", object_id=box_id_list[cur])
            if award_id_list:
                btn_position = self.get_position(object_id=award_id_list[0])
                box_position_list.append(btn_position)
                cur += 1
                continue
            done_id_list = self.get_offspring_id_list(offspring_path="done", object_id=box_id_list[cur])
            if done_id_list:
                btn_position = self.get_position(object_id=done_id_list[0])
                box_position_list.append(btn_position)
                cur += 1
                continue
            cur += 1
        return box_position_list

    def make_award_detail_appear(self, position):
        # 点击宝箱
        self.click_position(position)
        cur = 0
        while not TaskPanel.is_award_detail_active:
            # 防止没点上
            self.click_position(position)
            cur += 1
            if cur > 10:
                raise FindNoElementError

    def make_award_detail_month_appear(self, position):
        # 点击宝箱
        self.click_position(position)
        cur = 0
        while not TaskPanel.is_month_award_detail_active:
            # 防止没点上
            self.click_position(position)
            cur += 1
            if cur > 10:
                raise FindNoElementError

    def get_award_detail(self, position):
        # 点击箱子得到下一个箱子的奖励图标和数量
        TaskPanel.make_award_detail_appear(self, position=position)
        reward_icon_list = TaskPanel.get_box_award_icon_list(self)
        reward_quantity_list = TaskPanel.get_box_award_quantity_list(self)
        item_dict = resource.make_item_dict(item_icon_list=reward_icon_list, item_quantity_list=reward_quantity_list)
        self.click_position([0.5, 0.9])
        self.sleep(1)
        return item_dict

    def get_month_award_detail(self, position):
        # 点击箱子得到下一个箱子的奖励图标和数量
        TaskPanel.make_award_detail_month_appear(self, position=position)
        reward_icon_list = TaskPanel.get_month_box_award_icon_list(self)
        reward_quantity_list = TaskPanel.get_month_box_award_quantity_list(self)
        item_dict = resource.make_item_dict(item_icon_list=reward_icon_list, item_quantity_list=reward_quantity_list)
        self.click_position([0.5, 0.1])
        return item_dict

    def make_ItemTipsPanel_appear(self, position):
        self.click_position(position)
        cur = 0
        while not ItemTipsPanel.is_panel_active(self):
            # 防止没点上
            self.click_position(position)
            cur += 1
            if cur > 10:
                raise FindNoElementError

    def is_award_detail_active(self):
        return self.exist(element_data=ElementsData.TaskPanel.award_detail)

    def is_month_award_detail_active(self):
        return self.exist(element_data=ElementsData.TaskPanel.month_award_detail)

    def get_box_award_icon_list(self):
        award_icon_list = self.get_icon_list(element_data=ElementsData.TaskPanel.award_icon_list)
        return award_icon_list

    def get_box_award_quantity_list(self):
        award_quantity_list = self.get_text_list(element_data=ElementsData.TaskPanel.award_quantity_list)
        str_to_int_list(award_quantity_list)
        return award_quantity_list

    def get_month_box_award_icon_list(self):
        award_icon_list = self.get_icon_list(element_data=ElementsData.TaskPanel.month_award_icon_list)
        return award_icon_list

    def get_month_box_award_quantity_list(self):
        award_quantity_list = self.get_text_list(element_data=ElementsData.TaskPanel.month_award_quantity_list)
        str_to_int_list(award_quantity_list)
        return award_quantity_list

    def get_box_award_position_list(self):
        award_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.award_icon_list)
        return award_position_list

    def get_box_award_dict(self):
        box_award_icon_list = TaskPanel.get_box_award_icon_list(self)
        box_award_quantity_list = TaskPanel.get_box_award_quantity_list(self)
        return resource.make_item_dict(item_icon_list=box_award_icon_list, item_quantity_list=box_award_quantity_list)

    def get_progress_value(self):
        progress_value = self.get_slider_value(element_data=ElementsData.TaskPanel.progress_value)
        return progress_value

    def get_duel_task_index(self):
        text_list = self.get_text_list(element_data=ElementsData.TaskPanel.text_list)
        cur = 0
        while cur < len(text_list):
            if text_list[cur] == "Complete 1 Duel":
                break
            cur += 1
        return cur

    def get_task_kind(self):
        task_kind = self.get_text_list(element_data=ElementsData.TaskPanel.kind_list)[0]
        return task_kind

    # 月度任务的宝箱路径跟日和周不一样
    def get_month_box_position(self):
        ing_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.month_box_list, offspring_path="ing")
        if ing_position_list:
            return ing_position_list[0]
        award_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.month_box_list, offspring_path="award")
        if award_position_list:
            return award_position_list[0]
        done_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.month_box_list, offspring_path="done")
        return done_position_list[0]

    def get_month_box_status(self):
        ing_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.month_box_list, offspring_path="ing")
        if ing_position_list:
            return 0
        award_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.month_box_list, offspring_path="award")
        if award_position_list:
            return 1
        done_position_list = self.get_position_list(element_data=ElementsData.TaskPanel.month_box_list, offspring_path="done")
        if done_position_list:
            return 2
        return -1

    def click_box(self, index=-1):
        self.click_object_of_plural_objects(element_data_list=[ElementsData.TaskPanel.box_list_done, ElementsData.TaskPanel.box_list_award, ElementsData.TaskPanel.box_list_ing], index=index)

    def click_btn(self, index=-1):
        viewport = TaskPanel.get_viewport(self)
        self.click_object_of_plural_objects(element_data_list=[ElementsData.TaskPanel.btn_completed_list,ElementsData.TaskPanel.btn_undone_list,ElementsData.TaskPanel.btn_finish_list], viewport=viewport, index=index)


    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.TaskPanel.item_list, element_viewport=ElementsData.TaskPanel.viewport, delta_len=0.1, viewport_edge=[-0.05, 0],viewport_direction="row", index=index)

    def click_item_detail(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.TaskPanel.item_list_detail, index=index)

    operation_pool = [
        {"element_data": ElementsData.TaskPanel.box_list, "func": click_box, "weight": 1},
        {"element_data": ElementsData.TaskPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.TaskPanel.TaskPanel, "func": click_btn, "weight": 1},
        {"element_data": ElementsData.TaskPanel.item_list, "func": click_item, "weight": 1},
        {"element_data": ElementsData.TaskPanel.item_list_detail, "func": click_item_detail, "weight": 10},
        {"element_data": ElementsData.TaskPanel.tab_list, "func": switch_tab, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # TaskPanel.click_box(bp, 3)
    # TaskPanel.click_btn_close(bp)
    # TaskPanel.click_btn(bp, 0)
    TaskPanel.click_item(bp,6)
    # TaskPanel.click_item_detail(bp)
    # TaskPanel.switch_tab(bp)
    bp.connect_close()






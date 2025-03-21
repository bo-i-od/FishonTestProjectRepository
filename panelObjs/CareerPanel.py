import re
from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.RewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *
from common.viewport import Viewport

class CareerPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.CareerPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.CareerPanel.CareerPanel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.CareerPanel.CareerPanel, interval=1, timeout=3)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.CareerPanel.btn_i)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.CareerPanel.btn_close_tips)

    def is_tips_active(self):
        return self.exist(element_data=ElementsData.CareerPanel.tips)

    #获取总天赋值
    def get_rating_total(self):
        self.get_text(element_data=ElementsData.CareerPanel.rating_total)

    def click_rating_total(self):
        self.click_element(element_data=ElementsData.CareerPanel.rating_total)

    def is_rating_tips_active(self):
        return self.exist(element_data=ElementsData.CareerPanel.rating_tips)

    #比较tipspanel中的天赋值和总天赋值
    def compare_rating_total(self):
        rating_total = self.get_text(element_data=ElementsData.CareerPanel.rating_total)
        rating_child = self.get_text(element_data=ElementsData.CareerPanel.rating_child)
        if rating_child==rating_total:
            return True
        return False

    #获取顶部栏金币、积分
    def get_cash_value(self):
        cash_value = self.get_text(element_data=ElementsData.CareerPanel.text_100000)
        return str_to_int(cash_value)

    def get_points_value(self):
        points_value=self.get_text(element_data=ElementsData.CareerPanel.text_100400)
        return str_to_int(points_value)

    def get_item_rating(self):
        self.get_text(element_data=ElementsData.CareerPanel.rating)

    def get_item_lv(self):
        self.get_text(element_data=ElementsData.CareerPanel.item_lv)

    #获取每页的mid节点
    def get_page_item_id_list(self):
        page_item_middle_id_list = self.get_object_id_list(element_data=ElementsData.CareerPanel.page_item_middle_list)
        return page_item_middle_id_list

    #突破至某节点出现
    def enhance_until_item_exist(self, index):

        page_item_middle_id_list = CareerPanel.get_page_item_id_list(self)

        icon_size_list = self.get_size_list(object_id=page_item_middle_id_list[0],offspring_path="icon_bg")
        edge = [icon_size_list[0][0],0.01]
        viewport = Viewport(self, element_viewport=ElementsData.CareerPanel.career_viewport, item_id_list=page_item_middle_id_list, viewport_edge=edge)
        range_r = viewport.get_viewport_range()[0]
        range_l = self.get_position(element_data=ElementsData.CareerPanel.btn_enhance)[0] + self.get_size(element_data=ElementsData.CareerPanel.btn_enhance)[0] * 0.5
        #print(self.get_position(element_data=ElementsData.Career.btn_enhance))
        viewport.viewport_range = [range_r,range_l]
        cur = index
        while cur >= 0:
            if self.exist(object_id=page_item_middle_id_list[cur],offspring_path="lock"):
                cur -=1
            else:
                break
        begin = cur
        #print(begin)
        while begin < index:

            #判断下一节点是否解锁
            if self.exist(object_id=page_item_middle_id_list[begin+1],offspring_path="lock"):
                # 判断当前节点是否已满级
                if not self.exist(element_data=ElementsData.CareerPanel.btn_enhance):
                    group_id = self.get_parent_id(object_id=page_item_middle_id_list[begin])
                    page_id = self.get_parent_id(object_id=group_id)
                    text = self.get_text(object_id=page_id, offspring_path="arrow_Next_lock>text")
                    level = re.findall(pattern='\d+', string=text)
                    str_to_int(level)
                    CareerPanel.click_btn_close(self)
                    self.cmd(f"levelupto {level}")
                    self.clear_popup()
                    self.go_to_panel("CareerPanel")
                cur_item_id = page_item_middle_id_list[begin]
                viewport.move_until_appear(cur_item_id)
                self.sleep(0.5)
                self.click_element(object_id=cur_item_id,offspring_path="icon_bg")
                self.sleep(0.5)
                CareerPanel.enhance(self)
            else:
                begin +=1
        viewport.move_until_appear(page_item_middle_id_list[index])
        self.sleep(0.5)
        self.click_element(object_id=page_item_middle_id_list[index],offspring_path="icon_bg")


    #突破消耗数量列表
    def get_cost_qulity_list(self):
        cost_qulity_list = self.get_text_list(element_data=ElementsData.CareerPanel.cost_quantity_list)
        #print(cost_qulity_list)
        str_to_int_list(cost_qulity_list)
        return cost_qulity_list

    def click_btn_enhance(self):
        self.click_element(element_data=ElementsData.CareerPanel.btn_enhance)

    #突破已在屏幕中的节点
    def enhance(self):
        cost_qulity_list = CareerPanel.get_cost_qulity_list(self)
        #print(cost_qulity_list)
        cost_cash_value = cost_qulity_list[1]
        cost_points_value = cost_qulity_list[0]
        self.cmd(f"add 1 100000 {cost_cash_value}")
        self.cmd(f"add 1 100400 {cost_points_value}")
        CareerPanel.click_btn_enhance(self)
        self.sleep(0.5)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.CareerPanel.top_res_btns, index=index)

    def click_btn_guide(self):
        self.click_element(element_data=ElementsData.CareerPanel.btn_guide)

    def click_rating(self):
        self.click_element(element_data=ElementsData.CareerPanel.rating)

    def click_item(self, index=-1):
        edge = [0.1, 0.1]
        viewport = Viewport(self, element_viewport=ElementsData.CareerPanel.career_viewport, element_item_list=ElementsData.CareerPanel.item_list, viewport_edge=edge)
        self.click_object_of_plural_objects(element_data=ElementsData.CareerPanel.item_list, viewport=viewport, index=index)


    operation_pool = [
        {"element_data": ElementsData.CareerPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.CareerPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.CareerPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 10},
        {"element_data": ElementsData.CareerPanel.btn_enhance, "func": click_btn_enhance, "weight": 1},
        {"element_data": ElementsData.CareerPanel.btn_guide, "func": click_btn_guide, "weight": 1},
        {"element_data": ElementsData.CareerPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
        {"element_data": ElementsData.CareerPanel.rating, "func": click_rating_total, "weight": 1},
        {"element_data": ElementsData.CareerPanel.rating_total, "func": click_rating, "weight": 1},
        {"element_data": ElementsData.CareerPanel.item_list, "func": click_item, "weight": 1},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    # CareerPanel.click_rating_total(bp)
    #
    # CareerPanel.click_rating(bp)
    CareerPanel.click_btn_close_tips(bp)
    # CareerPanel.click_item(bp)

    bp.connect_close()
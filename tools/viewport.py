import random

from common import basePage
from configs.elementsData import ElementsData
class Viewport:
    def __init__(self, bp, element_viewport,element_item_list):
        self.basePage = bp
        self.element_viewport = element_viewport
        self.element_item_list = element_item_list
        self.viewport_objectId = self.get_viewport_objectId()
        self.viewport_position = self.get_viewport_position()
        # self.viewport_range = self.get_viewport_range()
        self.child_id_list = self.get_item_id_list()
        self.viewport_direction = self.get_viewport_direction()
        self.delta_len = self.get_delta_len()
    def get_viewport_objectId(self):
         return self.basePage.get_object_id(element_data=self.element_viewport)

    def get_viewport_position(self):
        return self.basePage.get_position(element_data=self.element_viewport)
    # def get_viewport_range(self):
    #     viewport_size = self.basePage.get_size(element_data=self.element_viewport)
    #     viewport_position = self.basePage.get_position(element_data=self.element_viewport)
    #     print(viewport_size)
    #     print(viewport_position)
    #     self.basePage.get_element_shoot(element_data=self.element_viewport)
    #     return viewport_position[0] - 0.5 * viewport_size[0], viewport_position[1] - 0.5 * viewport_size[1], viewport_position[0] + 0.5 * viewport_size[0], viewport_position[1] + 0.5 * viewport_size[1]
    def get_item_id_list(self):
        return self.basePage.get_object_id_list(element_data=self.element_item_list)

    def get_viewport_direction(self):
        child_count = len(self.child_id_list)
        if child_count < 2:
            return "any"
        position_item_start = self.basePage.get_position(self.child_id_list[0])
        position_item_end = self.basePage.get_position(self.child_id_list[child_count - 1])
        # X坐标差大于Y坐标
        if abs(position_item_start[0] - position_item_end[0]) > abs(position_item_start[1] - position_item_end[1]):
            return "row"
        return "column"

    def get_delta_len(self):
        if self.viewport_direction == "row":
            return self.basePage.get_size(self.child_id_list[0])[0]
        if self.viewport_direction == "column":
            return self.basePage.get_size(self.child_id_list[0])[1]
        print("列表元素不足")
        return 0

    def move_delta_len(self, target_id):
        target_position = self.basePage.get_position(target_id)
        point_end = [0, 0]
        point_end[0] = self.viewport_position[0]
        point_end[1] = self.viewport_position[1]
        if self.viewport_direction == "row":
            if target_position[0] > (self.viewport_position[0] - self.delta_len) and target_position[0] < (self.viewport_position[0] + self.delta_len):
                return False
            if target_position[0] > self.viewport_position[0]:
                point_end[0] -= self.delta_len
                self.basePage.swipe(point_start=self.viewport_position, point_end=point_end)
                return True
            point_end[0] += self.delta_len
            self.basePage.swipe(point_start=self.viewport_position, point_end=point_end)
            return True

        if target_position[1] > (self.viewport_position[1] - self.delta_len) and target_position[1] < (self.viewport_position[1] + self.delta_len):
            return False
        if target_position[1] > self.viewport_position[1]:
            point_end[1] = self.viewport_position[1] - self.delta_len
            self.basePage.swipe(point_start=self.viewport_position, point_end=point_end)
            return True
        point_end[1] = self.viewport_position[1] + self.delta_len
        self.basePage.swipe(point_start=self.viewport_position, point_end=point_end)
        return True

    def move_until_close(self, target_id):
        while(self.move_delta_len(target_id)):
            target_position = self.basePage.get_position(target_id)
            print(target_position[0])
            print(self.delta_len)






if __name__ == "__main__":

    bp = basePage.BasePage()
    # viewport = Viewport(bp, ElementsData.Login.DropdownList_Viewport, ElementsData.Login.DropdownList)
    viewport = Viewport(bp, ElementsData.BattlePass.Viewport, ElementsData.BattlePass.reward_icon_list)
    index = 80
    viewport.move_until_close(viewport.child_id_list[index])



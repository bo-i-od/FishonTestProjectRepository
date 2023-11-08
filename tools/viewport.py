from common.basePage import BasePage
from configs.elementsData import ElementsData
from items.resource import *
class Viewport:
    def __init__(self, bp, element_viewport,element_item_list):
        self.basePage = bp
        self.element_viewport = element_viewport
        self.element_item_list = element_item_list
        self.viewport_objectId = self.get_viewport_objectId()
        self.viewport_position = self.get_viewport_position()
        self.child_id_list = self.get_item_id_list()
        self.viewport_direction = self.get_viewport_direction()
        self.viewport_size = self.get_viewport_size()
        self.viewport_range = self.get_viewport_range()
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
        # print("列表元素不足,无法判断是row还是column")
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

    def get_viewport_range(self):
        size = self.viewport_size
        position = self.viewport_position
        if self.viewport_direction == "column":
            range_start = position[1] - size[1] * 0.5
            range_end = position[1] + size[1] * 0.5
        else :
            range_start = position[0] - size[0] * 0.5
            range_end = position[0] + size[0] * 0.5
        return [range_start, range_end]

    def get_viewport_size(self):
        viewport_size = self.basePage.get_size(element_data=self.element_viewport)
        return viewport_size

    def get_clickable_icon_and_position_list(self):
        cur = 0
        icon_list = self.basePage.get_icon_list(element_data=self.element_item_list)
        position_list = self.basePage.get_position_list(element_data=self.element_item_list)
        clickable_icon_list = []
        clickable_position_list = []
        while cur < len(position_list):
            if self.viewport_direction == "column":
                if position_list[cur][1] > self.viewport_range[1]:
                    break
            else:
                if position_list[cur][0] > self.viewport_range[1]:
                    break
            clickable_icon_list.append(icon_list[cur])
            clickable_position_list.append(position_list[cur])
            cur += 1
        check_icon_list(clickable_icon_list)
        return clickable_icon_list, clickable_position_list






if __name__ == "__main__":

    bp = BasePage()
    # viewport = Viewport(bp, ElementsData.Login.DropdownList_Viewport, ElementsData.Login.DropdownList)
    viewport = Viewport(bp, ElementsData.BattlePass.Viewport, ElementsData.BattlePass.reward_icon_list)
    index = 80
    viewport.move_until_close(viewport.child_id_list[index])



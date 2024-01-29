from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.gears import GearAttribute
from tools.commonTools import *


class BaitAndRodAlbumPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BaitAndRodAlbum.BaitAndRodAlbumPanel):
            return True
        return False

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BaitAndRodAlbum.btn_close)

    def get_gear_list(self):
        gear_id_list = self.get_object_id_list(element_data=ElementsData.BaitAndRodAlbum.model_list)
        gear_all_list = []
        gear_owned_list = []
        for gear_id in gear_id_list:
            stars = 0
            level = 0
            rating = 0
            attribute_add_count = 0
            attribute_icon_list = []
            kinds_icon_id = self.get_offspring_id("kinds>icon", object_id=gear_id)
            kind = self.get_icon(object_id=kinds_icon_id)
            fragments_value_id = self.get_offspring_id("fragments>value", object_id=gear_id)
            fragments_value = self.get_text(object_id=fragments_value_id)
            fragments_value_list = fragments_value.split("/")
            fragments_numerator = int(fragments_value_list[0])
            fragments_denominator = int(fragments_value_list[1])
            bg_id = self.get_offspring_id("bg", object_id=gear_id)
            bg = self.get_icon(object_id=bg_id)
            name_id = self.get_offspring_id("name", object_id=gear_id)
            name = self.get_text(object_id=name_id)
            temp_gear = GearAttribute(bg=bg, name=name, stars=stars, rating=rating, kind=kind, level=level, fragments_numerator=fragments_numerator, fragments_denominator=fragments_denominator, attribute_add_count=attribute_add_count,
                                      attribute_icon_list=attribute_icon_list)
            lock_id = self.get_offspring_id_list("lock", object_id=gear_id)
            if lock_id:
                stars_id = self.get_offspring_id("stars", object_id=gear_id)
                stars = BaitAndRodAlbumPanel.get_stars(self, stars_id)
                level = BaitAndRodAlbumPanel.get_level(self, gear_id)
                rating_value_id = self.get_offspring_id("rating>value", object_id=gear_id)
                rating = int(self.get_text(object_id=rating_value_id))
                attribute_icon_list = BaitAndRodAlbumPanel.get_attribute_icon_list(self, gear_id)
                attribute_add_id_list = self.get_offspring_id_list("attribute_list>>add", object_id=gear_id)
                temp_gear.stars = stars
                temp_gear.level = level
                temp_gear.rating = rating
                temp_gear.attribute_icon_list = attribute_icon_list
                temp_gear.attribute_add_count = len(attribute_add_id_list)
                gear_owned_list.append(temp_gear)
            # 检查孔和星数是否对应
            compare(stars, temp_gear.attribute_add_count + len(temp_gear.attribute_icon_list))
            gear_all_list.append(temp_gear)
        return gear_all_list, gear_owned_list

    def get_stars(self, stars_id):
        stars = 0
        star_y_id_list = self.get_offspring_id_list(">star_y", object_id=stars_id)
        for star_y_id in star_y_id_list:
            star_y_icon = self.get_icon(object_id=star_y_id)
            if star_y_icon == "fish_star":
                stars += 1
            elif star_y_icon == "fish_star_red":
                stars += 2
        return stars

    def get_level(self, gear_id):
        level = 0
        if self.exist(element_data=ElementsData.BaitAndRodAlbum.panel_bag_bait):
            return level
        level_value_id = self.get_offspring_id("level>value", object_id=gear_id)
        level = int(self.get_text(object_id=level_value_id))
        return level

    def get_attribute_icon_list(self, gear_id):
        attribute_icon_list = []
        attribute_icon_id_list = self.get_offspring_id_list("attribute_list>>icon", object_id=gear_id)
        for attribute_icon_id in attribute_icon_id_list:
            attribute_icon_list.append(self.get_icon(object_id=attribute_icon_id))
        return attribute_icon_list

    def switch_tab(self, index):
        position_list = self.get_position_list(element_data=ElementsData.BaitAndRodAlbum.tab_list)
        self.click_position(position_list[index])



    def switch_filter(self, rarity=0, available_location=0, hide_unowned=False):
        # 打开筛选面板
        self.click_a_until_b_appear(element_data_a=ElementsData.BaitAndRodAlbum.btn_filter, element_data_b=ElementsData.BaitAndRodAlbum.options)
        # 根据rarity，available_location和hide_unowned进行选项点击
        toggle_position_list1 = self.get_position_list(element_data=ElementsData.BaitAndRodAlbum.toggle_rarity_list)
        toggle_position_list2 = self.get_position_list(element_data=ElementsData.BaitAndRodAlbum.toggle_available_location_list)
        self.click_position(toggle_position_list1[rarity])
        self.click_position(toggle_position_list2[available_location])
        toggle_is_on_list1 = self.get_toggle_is_on_list(element_data=ElementsData.BaitAndRodAlbum.toggle_rarity_list)
        toggle_is_on_list2 = self.get_toggle_is_on_list(element_data=ElementsData.BaitAndRodAlbum.toggle_available_location_list)
        checktoggle(toggle_is_on_list1, rarity)
        checktoggle(toggle_is_on_list2, available_location)
        hide_unowned_cur = self.get_toggle_is_on(element_data=ElementsData.BaitAndRodAlbum.toggle_hide_unowned)
        if hide_unowned_cur != hide_unowned:
            self.click_element(element_data=ElementsData.BaitAndRodAlbum.toggle_hide_unowned)
        # 点击apply按钮
        self.click_element(element_data=ElementsData.BaitAndRodAlbum.btn_apply)
        print("筛选成功")

    def reset_filter(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.BaitAndRodAlbum.btn_filter, element_data_b=ElementsData.BaitAndRodAlbum.options)
        self.click_element(element_data=ElementsData.BaitAndRodAlbum.btn_reset)
        toggle_is_on_list1 = self.get_toggle_is_on_list(element_data=ElementsData.BaitAndRodAlbum.toggle_rarity_list)
        toggle_is_on_list2 = self.get_toggle_is_on_list(element_data=ElementsData.BaitAndRodAlbum.toggle_available_location_list)
        checktoggle(toggle_is_on_list1, 0)
        checktoggle(toggle_is_on_list2, 0)
        hide_unowned_cur = self.get_toggle_is_on(element_data=ElementsData.BaitAndRodAlbum.toggle_hide_unowned)
        compare(hide_unowned_cur, True)
        self.click_a_until_b_disappear(element_data_a=ElementsData.BaitAndRodAlbum.btn_filter, element_data_b=ElementsData.BaitAndRodAlbum.options)
        print("筛选重置成功")

    def get_rod_list(self):
        BaitAndRodAlbumPanel.switch_tab(self, 0)
        BaitAndRodAlbumPanel.switch_filter(self, 0, 0, True)
        rod_owned_hide_unowned_list = BaitAndRodAlbumPanel.get_gear_list(self)[0]
        return rod_owned_hide_unowned_list

    def get_bait_list(self):
        BaitAndRodAlbumPanel.switch_tab(self, 1)
        BaitAndRodAlbumPanel.switch_filter(self, 0, 0, True)
        bait_owned_hide_unowned_list = BaitAndRodAlbumPanel.get_gear_list(self)[0]
        return bait_owned_hide_unowned_list

    # 根据dir滑动列表
    def swipe_gear_list(self, direction):
        position = self.get_position(element_data=ElementsData.BaitAndRodAlbum.Viewport)
        if direction > 0:
            self.swipe(point_start=position, point_end=(0.9, 0.5))
        if direction < 0:
            self.swipe(point_start=position, point_end=(0.1, 0.5))


if __name__ == "__main__":
    bp = BaitAndRodAlbumPanel()
    a = BaitAndRodAlbumPanel.get_gear_list(bp)
    print(a)

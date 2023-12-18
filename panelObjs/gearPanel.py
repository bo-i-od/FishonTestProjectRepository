import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.baitAndRodAlbumPanel import BaitAndRodAlbumPanel
from common.resource import *


class GearPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Gear.btn_close)
        if GearPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Gear.GearPanel):
            return True
        return False

    def get_resource(self):
        res_value_list = self.get_text_list(element_data=ElementsData.Gear.res_value_list)
        res_icon_list = self.get_icon_list(element_data=ElementsData.Gear.res_icon_list)
        item_count_list = self.get_item_count_list(res_icon_list)
        cur = 0
        while cur < len(res_value_list):
            if res_icon_list[cur] == "coin_gold":
                compare(unit_conversion_int_to_str(item_count_list[cur]), res_value_list[cur])
            else:
                compare(item_count_list[cur], int(res_value_list[cur]))
            cur += 1
        return res_icon_list, item_count_list

    def click_tab_info(self):
        self.click_element(element_data=ElementsData.Gear.tab_info)
        if self.exist(element_data=ElementsData.Gear.panel_info):
            return True
        return False

    def click_tab_level_up(self):
        self.click_element(element_data=ElementsData.Gear.tab_level_up)
        if self.exist(element_data=ElementsData.Gear.panel_upgrade):
            return True
        return False

    def click_tab_enhance(self):
        self.click_element(element_data=ElementsData.Gear.tab_enhance)
        if self.exist(element_data=ElementsData.Gear.panel_enhance):
            return True
        return False

    def click_tab_draw_perk(self):
        self.click_element(element_data=ElementsData.Gear.tab_draw)
        if self.exist(element_data=ElementsData.Gear.panel_draw):
            return True
        return False

    def switch_gear(self, direction: int):
        if direction > 0:
            if not self.exist(element_data=ElementsData.Gear.btn_next):
                print("后面没有了")
                return False
            self.click_element(element_data=ElementsData.Gear.btn_next)
        elif direction < 0:
            if not self.exist(element_data=ElementsData.Gear.btn_previous):
                print("前面没有了")
                return False
            self.click_element(element_data=ElementsData.Gear.btn_previous)
        return True

    def click_5d(self):
        if self.exist(element_data=ElementsData.Gear.tips_5d):
            value_5d_list = GearPanel.get_5d_value(self, ElementsData.Gear.value_5d_list)
            self.click_element(element_data=ElementsData.Gear.img_5d)
            if self.exist(element_data=ElementsData.Gear.tips_5d):
                raise FindElementError
            return value_5d_list
        self.click_element(element_data=ElementsData.Gear.img_5d)
        if not self.exist(element_data=ElementsData.Gear.tips_5d):
            raise FindNoElementError
        value_5d_list = GearPanel.get_5d_value(self, ElementsData.Gear.value_5d_list)
        print("雷达图成功")
        return value_5d_list

    def click_talent(self):
        if self.exist(element_data=ElementsData.Gear.tips_talent):
            self.click_element(element_data=ElementsData.Gear.talent)
            if self.exist(element_data=ElementsData.Gear.tips_talent):
                raise FindElementError
        self.click_element(element_data=ElementsData.Gear.talent)
        if not self.exist(element_data=ElementsData.Gear.tips_talent):
            raise FindNoElementError
        print("点击天赋成功")

    def click_magnifier(self):
        if self.exist(element_data=ElementsData.Gear.btn_magnifier_close):
            self.click_element(element_data=ElementsData.Gear.btn_magnifier_close)
            if self.exist(element_data=ElementsData.Gear.btn_magnifier_close):
                raise FindElementError
        self.click_element(element_data=ElementsData.Gear.btn_magnifier_open)
        if not self.exist(element_data=ElementsData.Gear.btn_magnifier_close):
            raise FindNoElementError
        print("放大缩小按钮成功")

    def get_info_data(self):
        name = self.get_text(element_data=ElementsData.Gear.name)
        kind = self.get_icon(element_data=ElementsData.Gear.kind)
        level_list = self.get_text(element_data=ElementsData.Gear.level).split('/')
        level = int(level_list[0])
        damage = int(self.get_text(element_data=ElementsData.Gear.damage))
        rating = int(self.get_text(element_data=ElementsData.Gear.rating))
        stars_id = self.get_object_id(element_data=ElementsData.Gear.stars)
        stars = BaitAndRodAlbumPanel.get_stars(self, stars_id=stars_id)
        return name, kind, level, damage, rating, stars

    def get_5d_value(self, value_5d_list):
        res_list = self.get_text_list(element_data=value_5d_list)
        positive_percentage_to_float(text_list=res_list)
        return res_list

    def get_attrbuite_icon_text_value_list(self):
        attribute_icon_list = self.get_icon_list(element_data=ElementsData.Gear.Info.attribute_icon_list)
        attribute_text_list = self.get_text_list(element_data=ElementsData.Gear.Info.attribute_text_list)
        attribute_value_list = self.get_text_list(element_data=ElementsData.Gear.Info.attribute_value_list)
        positive_percentage_to_float(text_list=attribute_value_list)
        return attribute_icon_list, attribute_text_list, attribute_value_list

    def get_perk_postion_list(self):
        attribute_position_list = self.get_position_list(element_data=ElementsData.Gear.Info.attribute_text_list)
        attribute_add_position_list = self.get_position_list(element_data=ElementsData.Gear.Info.attribute_add_list)
        attribute_lock_position_list = self.get_position_list(element_data=ElementsData.Gear.Info.attribute_lock_list)
        return attribute_position_list, attribute_add_position_list, attribute_lock_position_list

    def click_attribute(self):
        attribute_icon_list, attribute_text_list, attribute_value_list = GearPanel.get_attrbuite_icon_text_value_list(self)
        attribute_position_list, attribute_add_position_list, attribute_lock_position_list = GearPanel.get_perk_postion_list(self)
        attribute_text_id_list = self.get_object_id_list(element_data=ElementsData.Gear.Info.attribute_text_list)
        y_max = 1 - self.get_size(element_data=ElementsData.Gear.tab)[1]
        # 保证列表里的元素在可点击范围内，去除不可点击元素
        cur = 0
        while cur < len(attribute_position_list):
            if attribute_position_list[cur][1] > y_max:
                attribute_position_list.remove(attribute_position_list[cur])
                attribute_text_list.remove(attribute_text_list[cur])
                attribute_text_id_list.remove(attribute_text_id_list[cur])
                cur -= 1
            cur += 1
        attribute_position_count = len(attribute_position_list)
        print(attribute_position_count)
        if attribute_position_count > 0:
            # 随机选取一个可点击的特性
            index_random = random.randint(0, attribute_position_count - 1)
            self.click_position(attribute_position_list[index_random])
            # 看弹窗与属性是否一致
            title = self.get_text(element_data=ElementsData.Gear.Info.EffectTips)
            compare(title, attribute_text_list[index_random])
            # 看是否有选中框亮起
            select_model_id = self.get_parent_id(element_data=ElementsData.Gear.Info.select)
            temp_id = self.get_parent_id(object_id=attribute_text_id_list[index_random])
            attribute_model_id = self.get_parent_id(object_id=temp_id)
            compare(select_model_id, attribute_model_id)
            print("随机点击特性成功")

    def click_attribute_add(self):
        attribute_position_list, attribute_add_position_list, attribute_lock_position_list = GearPanel.get_perk_postion_list(self)
        y_max = 1 - self.get_size(element_data=ElementsData.Gear.tab)[1]
        # 保证列表里的元素在可点击范围内，去除不可点击元素
        cur = 0
        while cur < len(attribute_add_position_list):
            if attribute_add_position_list[cur][1] > y_max:
                attribute_add_position_list.remove(attribute_add_position_list[cur])
                cur -= 1
            cur += 1
        attribute_add_position_count = len(attribute_add_position_list)
        if attribute_add_position_count > 0:
            # 随机选取一个可点击的➕
            index_random = random.randint(0, attribute_add_position_count - 1)
            self.click_position(attribute_add_position_list[index_random])
            print("点击空洗练位成功")
        # 判断是否跳转到洗练界面
        if not self.exist(element_data=ElementsData.Gear.panel_draw):
            raise FindNoElementError

    def click_attribute_lock(self):
        attribute_position_list, attribute_add_position_list, attribute_lock_position_list = GearPanel.get_perk_postion_list(self)
        y_max = 1 - self.get_size(element_data=ElementsData.Gear.tab)[1]
        # 保证列表里的元素在可点击范围内，去除不可点击元素
        cur = 0
        while cur < len(attribute_lock_position_list):
            if attribute_lock_position_list[cur][1] > y_max:
                attribute_lock_position_list.remove(attribute_lock_position_list[cur])
                cur -= 1
            cur += 1
        attribute_lock_position_count = len(attribute_lock_position_list)
        if attribute_lock_position_count > 0:
            # 随机选取一个可点击的➕
            index_random = random.randint(0, attribute_lock_position_count - 1)
            self.click_position(attribute_lock_position_list[index_random])
            print("点击上锁洗练位成功")

    def get_level_up_data(self):
        if self.exist(element_data=ElementsData.Gear.Upgrade.max):
            level_list = self.get_text(element_data=ElementsData.Gear.Upgrade.level_max).split('.')
            level = int(level_list[1])
            rating = int(self.get_text(element_data=ElementsData.Gear.Upgrade.rating_max))
            damage = int(self.get_text(element_data=ElementsData.Gear.Upgrade.damage_max))
            return level, rating, damage
        level_list = self.get_text(element_data=ElementsData.Gear.Upgrade.level).split('.')
        level = int(level_list[1])
        level_next_list = self.get_text(element_data=ElementsData.Gear.Upgrade.level_next).split('.')
        level_next = int(level_next_list[1])
        level_select = int(self.get_text(element_data=ElementsData.Gear.Upgrade.level_select))
        level_max_list = self.get_text(element_data=ElementsData.Gear.Upgrade.level_denominator).split('/')
        level_max = int(level_max_list[1])
        rating = int(self.get_text(element_data=ElementsData.Gear.Upgrade.rating))
        rating_next = int(self.get_text(element_data=ElementsData.Gear.Upgrade.rating_next))
        damage = int(self.get_text(element_data=ElementsData.Gear.Upgrade.damage))
        damage_next = int(self.get_text(element_data=ElementsData.Gear.Upgrade.damage_next))
        cost_icon_list = self.get_icon_list(element_data=ElementsData.Gear.Upgrade.cost_icon_list)
        # check_icon_list(cost_icon_list)
        cost_value_list = self.get_text_list(element_data=ElementsData.Gear.Upgrade.cost_value_list)
        str_to_int_list(cost_value_list)
        compare(level_next, level_select)
        if level >= level_next or level_next > level_max or rating > rating_next or damage > damage_next:
            raise CompareError
        return level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list

    def click_add_level(self):
        level_up_data = GearPanel.get_level_up_data(self)
        if len(level_up_data) < 4:
            print("升到满级了，没有按钮可以点击")
            return
        level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = level_up_data
        compare(level_next, level_select)
        level_select_backup = level_select
        self.click_element(element_data=ElementsData.Gear.Upgrade.btn_add)
        if level_select == level_max:
            level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = GearPanel.get_level_up_data(self)
            compare(level_select, level_select_backup)
            print("点击加号成功，因为按钮置灰，所以没有响应")
            return
        level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = GearPanel.get_level_up_data(self)
        compare(level_next, level_select)
        compare(level_select, level_select_backup + 1)
        print("点击加号成功")

    def click_sub_level(self):
        level_up_data = GearPanel.get_level_up_data(self)
        if len(level_up_data) < 4:
            print("升到满级了，没有按钮可以点击")
            return
        level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = level_up_data
        level_select_backup = level_select
        self.click_element(element_data=ElementsData.Gear.Upgrade.btn_sub)
        # 点到了上限
        if level_select == level + 1:
            level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = GearPanel.get_level_up_data(self)
            compare(level_select, level_select_backup)
            print("点击减号成功，因为按钮置灰，所以没有响应")
            return
        # 没点到上限
        level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = GearPanel.get_level_up_data(self)
        compare(level_select, level_select_backup - 1)
        print("点击减号成功")

    def click_level_up(self):
        level_up_data = GearPanel.get_level_up_data(self)
        if len(level_up_data) < 4:
            print("升到满级了，没有按钮可以点击")
            return
        level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = level_up_data
        target_icon_list = cost_icon_list
        if self.is_resource_enough(cost_icon_list, cost_value_list):
            cosumed_item_count_list = self.get_cosumed_item_count_list(cost_icon_list, cost_value_list)
            target_level = level_select
            target_rating = rating_next
            target_damage = damage_next
            self.click_element(element_data=ElementsData.Gear.Upgrade.btn_upgrade)
            self.sleep(1)
            level_up_data = GearPanel.get_level_up_data(self)
            if len(level_up_data) < 4:
                level, rating, damage = level_up_data
            else:
                level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = level_up_data
            item_count_list = self.get_item_count_list(target_icon_list)
            compare(level, target_level)
            compare(rating, target_rating)
            compare(damage, target_damage)
            compare(cosumed_item_count_list, item_count_list)
            print("资源充足，升级成功")
            return
        target_level = level
        target_rating = rating
        target_damage = damage
        target_item_count_list = self.get_item_count_list(cost_icon_list)
        self.click_element(element_data=ElementsData.Gear.Upgrade.btn_upgrade)
        level_up_data = GearPanel.get_level_up_data(self)
        if len(level_up_data) < 4:
            level, rating, damage = level_up_data
        else:
            level, level_next, level_select, level_max, rating, rating_next, damage, damage_next, cost_icon_list, cost_value_list = level_up_data
        item_count_list = self.get_item_count_list(target_icon_list)
        compare(level, target_level)
        compare(rating, target_rating)
        compare(damage, target_damage)
        compare(target_item_count_list, item_count_list)
        print("资源不足，数据不变")

    def get_enhance_data(self):
        stars_id = self.get_object_id(element_data=ElementsData.Gear.Enhance.stars)
        stars = BaitAndRodAlbumPanel.get_stars(self, stars_id)
        stars_next_id = self.get_object_id(element_data=ElementsData.Gear.Enhance.stars_next)
        stars_next = BaitAndRodAlbumPanel.get_stars(self, stars_next_id)
        rating = int(self.get_text(element_data=ElementsData.Gear.Enhance.rating))
        rating_next = int(self.get_text(element_data=ElementsData.Gear.Enhance.rating_next))
        value_5d_list = GearPanel.get_5d_value(self, ElementsData.Gear.Enhance.value_5d_list)
        compare(stars+1, stars_next)
        if rating > rating_next:
            raise CompareError
        return stars, stars_next, rating, rating_next, value_5d_list

    def get_draw_data(self):
        name = self.get_text(element_data=ElementsData.Gear.Draw.name)
        rating = int(self.get_text(element_data=ElementsData.Gear.Draw.rating))
        attribute_icon_list = self.get_icon_list(element_data=ElementsData.Gear.Draw.attribute_icon_list)
        attribute_value_list = self.get_text_list(element_data=ElementsData.Gear.Draw.attribute_value_list)
        positive_percentage_to_float(text_list=attribute_value_list)
        attribute_text_list = self.get_text_list(element_data=ElementsData.Gear.Draw.attribute_text_list)
        attribute_add_list = self.get_position_list(element_data=ElementsData.Gear.Draw.attribute_add_list)
        return name, rating, attribute_icon_list, attribute_value_list, attribute_text_list, attribute_add_list

    def click_draw(self, element_cost, element_icon, element_btn):
        cost = int(self.get_text(element_data=element_cost))
        icon = self.get_icon(element_data=element_icon)
        res_icon_list, res_count_list = GearPanel.get_resource(self)
        count_expect = 0
        cur = 0
        while cur < len(res_count_list):
            if res_icon_list[cur] != icon:
                cur += 1
                continue
            count_expect = res_count_list[cur]
            if res_count_list[cur] < cost:
                btn_disabled_id_list = self.get_offspring_id_list("btn_disabled", element_data=element_btn)
                if not btn_disabled_id_list:
                    raise FindNoElementError
                break
            count_expect -= cost
            break
        self.click_element(element_data=element_btn)
        res_icon_list, res_count_list = GearPanel.get_resource(self)
        compare(res_count_list[cur], count_expect)
        print(f"点击成功，当前剩余数量为{res_count_list[cur]}")

    def click_draw_perk_gold(self):
        GearPanel.click_draw(self, element_cost=ElementsData.Gear.Draw.cost_perk_glod, element_icon=ElementsData.Gear.Draw.icon_perk_glod, element_btn=ElementsData.Gear.Draw.btn_draw_perk_glod)

    def click_draw_perk(self):
        GearPanel.click_draw(self, element_cost=ElementsData.Gear.Draw.cost_perk, element_icon=ElementsData.Gear.Draw.icon_perk, element_btn=ElementsData.Gear.Draw.btn_draw_perk)

    def click_draw_value_10(self):
        if self.exist(element_data=ElementsData.Gear.Draw.tips_draw_value):
            object_id_list = self.get_object_id_list(element_data=ElementsData.Gear.Draw.attribute_icon_list)
            compare(object_id_list,[])
            print("没有特性可以洗数值")
            return
        GearPanel.click_draw(self, element_cost=ElementsData.Gear.Draw.cost_value_10, element_icon=ElementsData.Gear.Draw.icon_value_10, element_btn=ElementsData.Gear.Draw.btn_draw_value_10)
        attribute_model_id = self.get_parent_id(element_data=ElementsData.Gear.Draw.select)
        value_id = self.get_offspring_id(">progress>text", object_id=attribute_model_id)
        value = self.get_text(object_id=value_id)
        value = positive_percentage_to_float(text=value)
        self.sleep(30)
        icon_machine, text_machine, value_machine = GearPanel.get_draw_result(self)
        value_expect = value
        if value_machine > value:
            value_expect = value_machine
        value = self.get_text(object_id=value_id)
        value = positive_percentage_to_float(text=value)
        compare(value, value_expect)
        print("数值洗练成功")

    def click_draw_value(self):
        if self.exist(element_data=ElementsData.Gear.Draw.tips_draw_value):
            object_id_list = self.get_object_id_list(element_data=ElementsData.Gear.Draw.attribute_icon_list)
            compare(object_id_list,[])
            print("没有特性可以洗数值")
            return
        GearPanel.click_draw(self, element_cost=ElementsData.Gear.Draw.cost_value, element_icon=ElementsData.Gear.Draw.icon_value, element_btn=ElementsData.Gear.Draw.btn_draw_value)
        attribute_model_id = self.get_parent_id(element_data=ElementsData.Gear.Draw.select)
        value_id = self.get_offspring_id(">progress>text", object_id=attribute_model_id)
        value = self.get_text(object_id=value_id)
        value = positive_percentage_to_float(text=value)
        self.sleep(4)
        icon_machine, text_machine, value_machine = GearPanel.get_draw_result(self)
        value_expect = value
        if value_machine > value:
            value_expect = value_machine
        value = self.get_text(object_id=value_id)
        value = positive_percentage_to_float(text=value)
        compare(value, value_expect)
        print("数值洗练成功")

    def get_draw_result(self):
        icon_list = self.get_icon_list(element_data=ElementsData.Gear.Draw.perk_icon_list)
        text_list = self.get_text_list(element_data=ElementsData.Gear.Draw.perk_text_list)
        value_list = self.get_text_list(element_data=ElementsData.Gear.Draw.perk_value_list)
        icon = icon_list[2]
        text = text_list[2]
        value = value_list[2]
        value = float(value.split('%')[0])
        return icon, text, value

    def save_draw_result(self):
        btn_disabled_id_list = self.get_offspring_id_list("btn_disabled", element_data=ElementsData.Gear.Draw.btn_save)
        # 无法点击的情况
        if btn_disabled_id_list:
            attribute_model_id = self.get_parent_id(element_data=ElementsData.Gear.Draw.select)
            text_id = self.get_offspring_id(">text", object_id=attribute_model_id)
            text_pre = self.get_text(object_id=text_id)
            self.click_element(element_data=ElementsData.Gear.Draw.btn_save)
            text_id = self.get_offspring_id(">text", object_id=attribute_model_id)
            text = self.get_text(object_id=text_id)
            print(text_pre, text)
            compare(text_pre, text)
            print("按钮置灰，点击无效")
            return
        if self.exist(element_data=ElementsData.Gear.Draw.Panel_Tip):
            self.click_position([0.9, 0.5])
        icon_machine, text_machine, value_machine = GearPanel.get_draw_result(self)
        self.click_element(element_data=ElementsData.Gear.Draw.btn_save)
        attribute_model_id = self.get_parent_id(element_data=ElementsData.Gear.Draw.select)
        text_id = self.get_offspring_id(">text", object_id=attribute_model_id)
        text = self.get_text(object_id=text_id)
        icon_id = self.get_offspring_id(">icon", object_id=attribute_model_id)
        icon = self.get_icon(object_id=icon_id)
        value_id = self.get_offspring_id(">progress>text", object_id=attribute_model_id)
        value = self.get_text(object_id=value_id)
        value = positive_percentage_to_float(text=value)
        print(icon_machine, icon)
        # compare(icon_machine, icon)
        # compare(value_machine, value)
        # compare(text_machine, text)
        # print("保存成功")




if __name__ == "__main__":
    bp = GearPanel()
    # a = BaitAndRodAlbumPanel.get_all_rod_list(bp)
    # b = BaitAndRodAlbumPanel.get_all_bait_list(bp)
    while True:
        bp.click_draw_perk_gold()
        bp.get_draw_data()
        bp.sleep(0.5)
        bp.save_draw_result()


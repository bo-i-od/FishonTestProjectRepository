from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class TreasureChestPanel(BasePage):
    """
    输出箱子点的分子和分母
    """
    def get_box_points(self):
        box_points_str = self.get_text(element_data= ElementsData.TreasureChest.box_points)
        box_points_split_str = box_points_str.split("/")
        # 分子
        box_points_numerator = int(box_points_split_str[0])
        # 分母
        box_points_denominator = int(box_points_split_str[1])
        return box_points_numerator, box_points_denominator


    def select_box(self, index):
        box_id = self.get_object_id_list(element_data=ElementsData.TreasureChest.box_list)[index]
        self.click_element(object_id=box_id)

    def get_box_icon_and_quantity_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.TreasureChest.box_list)
        quantity_list = self.get_text_list(element_data=ElementsData.TreasureChest.quantity_list)
        str_to_int_list(quantity_list)
        return icon_list, quantity_list


    def get_open_x_n(self):
        open_x_n = self.get_text(element_data=ElementsData.TreasureChest.btn_open)
        n = open_x_n.split('x')[1]
        return int(n)

    def click_open_x(self):
        self.click_element(element_data=ElementsData.TreasureChest.btn_open)

    def get_box_main_icon(self):
        box_main_icon = self.get_icon(element_data=ElementsData.TreasureChest.box).split("_")[0]
        return box_main_icon

    def get_progressbar_box(self):
        progressbar_box = self.get_icon(element_data=ElementsData.TreasureChest.progressbar_box)
        return progressbar_box

    def goto_TreasureChestMerchantPanel(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.TreasureChest.btn_buy, element_data_b=ElementsData.TreasureChestMerchant.TreasureChestMerchantPanel)

    def close_TreasureChestPanel(self):
        self.click_until_disappear(element_data=ElementsData.TreasureChest.btn_close)

    # 看箱子点是否充足，可以获得下一个箱子
    def is_box_points_enough(self):
        box_points_numerator, box_points_denominator = TreasureChestPanel.get_box_points(self)
        if box_points_numerator < box_points_denominator:
            return False
        return True

    def click_progressbar_box(self):
            self.click_element(element_data=ElementsData.TreasureChest.progressbar_box)


    def get_chest_point(self, progressbar_box_icon):
        worksheet = self.excelTools.get_worksheet("ITEM_MAIN.xlsm", "模板数据")
        tpid = self.excelTools.same_row_different_column_convert(worksheet, "iconName", "itemTpId", progressbar_box_icon)
        worksheet = self.excelTools.get_worksheet("CHEST.xlsm", "模板数据")
        chest_point = self.excelTools.same_row_different_column_convert(worksheet, "itemTpId", "chestPoint", tpid)
        return int(chest_point)








if __name__ == "__main__":
    bp = TreasureChestPanel()
    print(bp.click_progressbar_box())
from openpyxl import *

class ExceTools:
    def __init__(self, root_path):
        self.root_path = root_path

    def get_worksheet(self, book_name, sheet_name):
        workbook = load_workbook(self.root_path + book_name, data_only=True)
        worksheet = workbook[sheet_name]
        return worksheet
    def get_column_index(self, worksheet, header):
        column_index_res = 0
        for column_index_cur in range(1, worksheet.max_column + 1):
            cell_value = worksheet.cell(4, column_index_cur).value
            if cell_value == header:
                column_index_res = column_index_cur
                break
        return column_index_res

    def get_row_index(self, worksheet, column_index, target_value):
        row_index_res = 0
        for row_index_cur in range(1, worksheet.max_row + 1):
            cell_value = worksheet.cell(row_index_cur, column_index).value
            if cell_value == target_value:
                row_index_res = row_index_cur
                break
        return row_index_res

    def get_exp_limit(self, lv):
        worksheet = self.get_worksheet("PLAYER_LEVEL_UP.xlsm", "模板数据")
        header = "exp"
        col_index_exp = self.get_column_index(worksheet, header)
        # 偏移为6
        delta = 6
        exp_limit_str = worksheet.cell(delta + lv, col_index_exp).value
        exp_limit = int(exp_limit_str)
        exp_limit_all = 0
        cur = 0
        while cur < lv:
            exp_limit_all += int(worksheet.cell(delta + cur, col_index_exp).value)
            cur += 1
        return exp_limit, exp_limit_all

    def get_fish_type(self, fish_list):
        tpid = "tpId"
        fishtype = "fishType"
        worksheet = self.get_worksheet("FISH.xlsm", "模板数据")
        res_list = self.same_row_different_column_convert_list(worksheet=worksheet, source_header=tpid, target_header=fishtype, source_list=fish_list)
        return res_list

    def get_book_list(self):
        book_list = [{"book_name": "RESOURCE.xlsm", "name": "name", "id": "resourceID", "icon": "itemIcon"},
                {"book_name": "ITEM_MAIN.xlsm", "name": "name", "id": "itemTpId", "icon": "iconName"}]
        return book_list

    # def item_name_to_item_icon_name(self, book_name,item_name):
    #     worksheet = self.get_worksheet(book_name, "模板数据")
    #     return self.same_row_different_column_convert(worksheet, "name", "iconName", item_name)
    #
    # def item_name_to_item_tpid(self, book_name, item_name):
    #     worksheet = self.get_worksheet(book_name, "模板数据")
    #     return self.same_row_different_column_convert(worksheet, "name", "itemTpId", item_name)
    #
    # def item_icon_name_to_item_name(self, book_name, item_icon_name):
    #     worksheet = self.get_worksheet(book_name, "模板数据")
    #     return self.same_row_different_column_convert(worksheet, "iconName", "name", item_icon_name)
    # def item_icon_name_to_item_tpid(self, book_name, item_icon_name):
    #     worksheet = self.get_worksheet(book_name, "模板数据")
    #     return self.same_row_different_column_convert(worksheet, "iconName", "itemTpId", item_icon_name)
    #
    # def item_tpid_to_item_name(self, book_name, item_icon_name):
    #     worksheet = self.get_worksheet(book_name, "模板数据")
    #     return self.same_row_different_column_convert(worksheet, "itemTpId", "name", item_icon_name)
    #
    # def item_tpid_to_item_icon_name(self, book_name, item_icon_name):
    #     worksheet = self.get_worksheet(book_name, "模板数据")
    #     return self.same_row_different_column_convert(worksheet, "itemTpId", "iconName", item_icon_name)


    def same_row_different_column_convert(self, worksheet, source_header, target_header, source):
        try:
            column_index_source = self.get_column_index(worksheet, source_header)
            column_index_target = self.get_column_index(worksheet, target_header)
            row_index = self.get_row_index(worksheet, column_index_source, source)
            return worksheet.cell(row_index, column_index_target).value
        except:
            return None

    def same_row_different_column_convert_list(self, worksheet, source_header, target_header, source_list):
        res_list = []
        column_index_source = self.get_column_index(worksheet, source_header)
        column_index_target = self.get_column_index(worksheet, target_header)
        for source in source_list:
            row_index = self.get_row_index(worksheet, column_index_source, source)
            res_list.append(worksheet.cell(row_index, column_index_target).value)
        return res_list
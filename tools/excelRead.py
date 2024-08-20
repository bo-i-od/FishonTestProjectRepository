from openpyxl import *
from openpyxl.utils import get_column_letter



class ExceTools:
    def __init__(self, root_path):
        self.root_path = root_path

    def get_worksheet(self, book_name, sheet_name):
        path = self.root_path + book_name
        workbook = load_workbook(path, data_only=True)
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

    def get_unlock_lv(self, system_name):
        table_data = self.get_table_data("UNLOCK_SYSTEM.xlsm")
        self.get_value_from_key(table_data, header_key='name', header_value='content', key=system_name)
        index = table_data['name'].index(system_name)
        unlock_lv = int(table_data['content'][index])
        return unlock_lv

    @staticmethod
    def get_value_from_key(table_data, header_key, header_value, key):
        index = table_data[header_key].index(key)
        value = int(table_data[header_value][index])
        return value

    def get_fish_type(self, fish, table_data):
        if fish == '':
            return "钓鱼失败"
        index = table_data["tpId"].index(int(fish))

        if table_data["fishClass"][index] == 1:
            if table_data["fishType"][index] == 1:
                return "小"
            if table_data["fishType"][index] == 2:
                return "中"
            if table_data["fishType"][index] == 3:
                return "大"
            if table_data["fishType"][index] == 4:
                return "特大"
            if table_data["fishType"][index] == 5:
                return "超巨"
        if table_data["fishClass"][index] == 2:
            return "奇珍"
        if table_data["fishClass"][index] == 3:
            return "超奇珍"
        if table_data["fishClass"][index] == 4:
            return "典藏"
        return "其它"


    def get_fish_type_list(self, fish_list):
        fish_type_list = []
        table_data = self.get_table_data(book_name="FISH.xlsm")
        cur = 0
        while cur < len(fish_list):
            fish_type = self.get_fish_type(fish=fish_list[cur], table_data=table_data)
            fish_type_list.append(fish_type)
            cur += 1
        return fish_type_list

    def get_book_list(self):
        book_list = [{"book_name": "RESOURCE.xlsm", "name": "name", "id": "resourceID", "icon": "itemIcon"},
                {"book_name": "ITEM_MAIN.xlsm", "name": "name", "id": "itemTpId", "icon": "iconName"}]
        return book_list


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


    def get_table_struct(self, book_name):
        res_dict = {}
        worksheet = self.get_worksheet(book_name=book_name, sheet_name="OrgData")
        ItemName1_column_index = 3
        cell_value_pre = ""
        row_index_cur = 2
        while worksheet.cell(row_index_cur, ItemName1_column_index - 1).value is not None:
            cell_value = worksheet.cell(row_index_cur, ItemName1_column_index).value
            # 数组的添加索引列表
            if cell_value == cell_value_pre:
                res_dict[cell_value].append(row_index_cur - 1)
                row_index_cur += 1
                continue
            # 普通的也直接添加
            if cell_value is not None:
                res_dict[cell_value] = [row_index_cur - 1]
                cell_value_pre = cell_value
                row_index_cur += 1
                continue
            dict_list_len = len(res_dict[cell_value_pre])
            res_dict[cell_value_pre][dict_list_len - 1] = {}
            ItemName2_column_index = ItemName1_column_index + 1
            res_dict[cell_value_pre][dict_list_len - 1][worksheet.cell(row_index_cur - 1, ItemName2_column_index).value] = [row_index_cur - 2]
            cur = row_index_cur
            while worksheet.cell(cur, ItemName1_column_index).value is None and worksheet.cell(cur, ItemName1_column_index - 1).value is not None:
                res_dict[cell_value_pre][dict_list_len - 1][worksheet.cell(cur, ItemName2_column_index).value] = [cur - 1]
                cur += 1
            row_index_cur = cur
        return res_dict, row_index_cur - 2

    def get_table_data(self, book_name):
        table_data, table_data_len = self.get_table_struct(book_name=book_name)
        worksheet = self.get_worksheet(book_name=book_name, sheet_name="模板数据")
        # 去除空白列
        bias_list = self.get_bias_list(worksheet, table_data_len)
        # table_data = {}
        for key in table_data:
            if len(table_data[key]) == 1:
                if isinstance(table_data[key][0], int):
                    table_data[key] = self.get_column_data(worksheet, table_data[key][0], bias_list)
                    continue
                # table_data[key] = []
                # table_data[key].append({})
                for key_sub in table_data[key][0]:
                    table_data[key][0][key_sub] = self.get_column_data(worksheet, table_data[key][0][key_sub][0], bias_list)
                continue
            cur = 0
            while cur < len(table_data[key]):

                if isinstance(table_data[key][cur], int):
                    table_data[key][cur] = self.get_column_data(worksheet, table_data[key][cur], bias_list)
                else:
                    for key_sub in table_data[key][cur]:
                        table_data[key][cur][key_sub] = self.get_column_data(worksheet,
                                                                             table_data[key][cur][key_sub][0], bias_list)
                cur += 1
        return table_data


    def get_bias_list(self, worksheet, table_data_len):
        bias_list = []
        bias = 0
        cur = 1
        while cur < table_data_len + 1:
            if worksheet.cell(2, cur + bias).value is None:
                bias += 1
                continue
            bias_list.append(bias)
            cur += 1
        return bias_list



    def get_column_data(self, worksheet, column_index, bias_list):
        column_data = []
        # 第六行开始
        cur = 6
        while worksheet.cell(cur, 1).value is not None:
            index = column_index - 1
            column_data.append(worksheet.cell(cur, column_index + bias_list[index]).value)
            cur += 1
        return column_data

    def get_item_tpid_list(self, icon):
        table_data = self.get_table_data("ITEM_MAIN.xlsm")
        icon_list = table_data['iconName']
        tpid_list = table_data['itemTpId']
        res_list = []
        cur = 0
        while cur < len(icon_list):
            if icon_list[cur] != icon:
                cur += 1
                continue
            res_list.append(tpid_list[cur])
            cur += 1
        return res_list







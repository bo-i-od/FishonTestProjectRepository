import json

from openpyxl import *

from common.error import PluralElementError
from tools import baseDataRead


class ExcelTools:
    def __init__(self, root_path):
        self.root_path = root_path

    def get_worksheet(self, book_name, sheet_name):
        path = self.root_path + book_name
        workbook = load_workbook(path, data_only=True)
        worksheet = workbook[sheet_name]
        return worksheet

    @staticmethod
    def get_column_index(worksheet, header):
        column_index_res = 0
        for column_index_cur in range(1, worksheet.max_column + 1):
            cell_value = worksheet.cell(4, column_index_cur).value
            if cell_value == header:
                column_index_res = column_index_cur
                break
        return column_index_res

    @staticmethod
    def get_row_index(worksheet, column_index, target_value):
        row_index_res = 0
        for row_index_cur in range(1, worksheet.max_row + 1):
            cell_value = worksheet.cell(row_index_cur, column_index).value
            if cell_value == target_value:
                row_index_res = row_index_cur
                break
        return row_index_res


    @staticmethod
    def get_value_from_key(table_data, header_key, header_value, key):
        index = table_data[header_key].index(key)
        value = int(table_data[header_value][index])
        return value


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
                    cur += 1
                    continue
                for key_sub in table_data[key][cur]:
                    table_data[key][cur][key_sub] = self.get_column_data(worksheet, table_data[key][cur][key_sub][0], bias_list)
                cur += 1
        return table_data

    def get_table_data_object_list_by_excel(self, book_name):
        table_data_object_list = []
        table_data, table_data_len = self.get_table_struct(book_name=book_name)
        worksheet = self.get_worksheet(book_name=book_name, sheet_name="模板数据")
        cur = 6
        while worksheet.cell(cur, 1).value is not None:
            table_data_template = table_data.copy()
            row_data = self.get_row_data(worksheet, row_index=cur, table_data_len=table_data_len)
            table_data_object = self.fill_template(template=table_data_template, data=row_data)
            table_data_object_list.append(table_data_object)
            cur += 1
        return table_data_object_list

    def get_table_data_detail(self, book_name):
        base_data_path = self.root_path.split("策划模板导出工具/")[0] + r"ElementData/BaseData/"
        prefix = book_name.split('.')[0]
        table_data_detail = baseDataRead.convert_to_json(path=base_data_path, prefix=prefix)
        return table_data_detail

    def get_table_data_object_list(self, book_name):
        table_data_object_list, _, _ = self.get_table_data_detail(book_name=book_name)
        return table_data_object_list


    def get_table_data_object_list_by_key_value(self, key, value, book_name=None, table_data_detail=None):
        res = []
        if table_data_detail is None:
            table_data_detail = self.get_table_data_detail(book_name=book_name)
        table_data_object_list, structs, prefix = table_data_detail

        # 给值转为正确的类型
        type_value = structs[prefix.upper()][key][0]
        if type_value == "int":
            value = int(value)
        elif type_value == "float":
            value = float(value)
        elif type_value == "string":
            value = str(value)
        for table_data_object in table_data_object_list:
            if key not in table_data_object:
                continue
            if table_data_object[key] != value:
                continue
            res.append(table_data_object)
        return res

    def get_table_data_object_by_key_value(self, key, value, book_name=None, table_data_detail=None):
        if table_data_detail is None:
            table_data_detail = self.get_table_data_detail(book_name=book_name)
        table_data_object_list, structs, prefix = table_data_detail
        type_value = structs[prefix.upper()][key][0]
        if type_value == "int":
            value = int(value)
        elif type_value == "float":
            value = float(value)
        elif type_value == "string":
            value = str(value)
        res = None
        cur = 0
        for table_data_object in table_data_object_list:
            if key not in table_data_object:
                continue
            if table_data_object[key] != value:
                continue
            cur += 1
            res = table_data_object
        if cur != 1:
            raise PluralElementError("表中键值的匹配项不是唯一，请使用get_table_data_object_list_by_key_value")
        return res


    @staticmethod
    def fill_template(template, data):
        result = str(template)
        for i, value in enumerate(data, start=1):
            if isinstance(value, str):
                result = result.replace(f'[{i}]', f"'{value}'")
            else:
                result = result.replace(f'[{i}]', str(value))
        result = result.replace("'", '"')
        result = json.loads(result)
        return result

    @staticmethod
    def get_row_data(worksheet, row_index, table_data_len):
        row_data = []
        # 第六行开始
        cur = 1
        while cur <= table_data_len:
            row_data.append(worksheet.cell(row_index, cur).value)
            cur += 1
        return row_data


    @staticmethod
    def get_bias_list(worksheet, table_data_len):
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

    @staticmethod
    def get_column_data(worksheet, column_index, bias_list):
        column_data = []
        # 第六行开始
        cur = 6
        while worksheet.cell(cur, 1).value is not None:
            index = column_index - 1
            column_data.append(worksheet.cell(cur, column_index + bias_list[index]).value)
            cur += 1
        return column_data


if __name__ == '__main__':
    et = ExcelTools("C:/trunkCHS/datapool/策划模板导出工具/")










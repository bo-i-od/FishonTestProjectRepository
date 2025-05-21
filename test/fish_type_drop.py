from activities.decl.NEW_PLOT_FISH_TYPE_DROP import NEW_PLOT_FISH_TYPE_DROP
from tools import baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    new_plot_fish_type_drop_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_FISH_TYPE_DROP.xlsm")
    instance_object: NEW_PLOT_FISH_TYPE_DROP
    json_object, instance_object = excel_tool.get_object(key="tpId",value=50030302, table_data_detail=new_plot_fish_type_drop_detail, cls=NEW_PLOT_FISH_TYPE_DROP)
    res = {}
    add_value = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
    weight_total = 0
    for fr in instance_object.fishResult:
        if fr.fishClass > 1:
            fish_kind = fr.fishClass + 4
        else:
            fish_kind = fr.fishType
        weight_total += fr.weight * add_value[fish_kind]

    for fr in instance_object.fishResult:
        if fr.fishClass > 1:
            fish_kind = fr.fishClass + 4
        else:
            fish_kind = fr.fishType
        res[fish_kind] = fr.weight * add_value[fish_kind] / weight_total
    print(res)





if __name__ == '__main__':
    main()
from activities.decl.CHAMPIONSHIPS import CHAMPIONSHIPS
from activities.decl.FISH import FISH
from activities.decl.FISHERIES import FISHERIES
from activities.decl.FISHERIES_LANGUAGE import FISHERIES_LANGUAGE
from activities.decl.PRESENT import PRESENT
from configs.pathConfig import EXCEL_PATH
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities

def fish(excel_tool: ExcelToolsForActivities, fishery_index):
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    common_fish_id_start =350001 + fishery_index * 100
    rare_fish_id_start = 360001 + fishery_index * 100
    fish_bone_id_start = 380001 + 15 * (fishery_index - 1)
    gold_fish_bone_id_start = 385001 + 15 * (fishery_index - 1)
    template_common_fish_id_start = common_fish_id_start - 100
    template_rare_fish_id_start = rare_fish_id_start - 100
    template_fish_bone_id_start = fish_bone_id_start - 15
    template_gold_fish_bone_id_start = gold_fish_bone_id_start - 15
    key = "tpId"
    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=common_fish_id_start, table_data_detail=fish_detail)
    if json_objects:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: FISH
        if mode == 1:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_common_fish_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)
        else:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=common_fish_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)

        instance_object.name = f"渔场{fishery_index}-{cur + 1}"
        instance_object.tpId = common_fish_id_start + cur
        instance_object.id = instance_object.tpId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fish_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fish_detail)
        cur += 1

    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=rare_fish_id_start, table_data_detail=fish_detail)
    if json_objects:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: FISH
        if mode == 1:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_rare_fish_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)
        else:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=rare_fish_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)

        instance_object.name = f"渔场{fishery_index}-{cur + 1}-改"
        instance_object.tpId = rare_fish_id_start + cur
        instance_object.id = instance_object.tpId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fish_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fish_detail)
        cur += 1

    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fish_bone_id_start, table_data_detail=fish_detail)
    if json_objects:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: FISH
        if mode == 1:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_fish_bone_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)
        else:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=fish_bone_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)

        instance_object.name = f"渔场{fishery_index}_信物鱼{cur + 1}"
        instance_object.tpId = fish_bone_id_start + cur
        instance_object.id = instance_object.tpId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fish_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fish_detail)
        cur += 1

    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=gold_fish_bone_id_start, table_data_detail=fish_detail)
    if json_objects:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        if mode == 1:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key,value=template_gold_fish_bone_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)
        else:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=gold_fish_bone_id_start + cur, table_data_detail=fish_detail)
            instance_object = json_to_instance(json_object=json_object, cls=FISH)

        instance_object.name = f"渔场{fishery_index}_黄金鱼骨{cur + 1}"
        instance_object.tpId = gold_fish_bone_id_start + cur
        instance_object.id = instance_object.tpId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fish_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fish_detail)
        cur += 1

def fisheries(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index):
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    template_tpId = fishery_id - 1
    key = "tpId"
    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fishery_id, table_data_detail=fisheries_detail)
    instance_object: FISHERIES
    if json_objects:
        mode = 2
        instance_object = json_to_instance(json_object=json_objects[0], cls=FISHERIES)
    else:
        mode = 1
        json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_tpId, table_data_detail=fisheries_detail)
        instance_object = json_to_instance(json_object=json_objects[0], cls=FISHERIES)
    instance_object.name = f"新主线{fishery_id}"
    instance_object.tpId = fishery_id
    instance_object.id = instance_object.tpId
    instance_object.fish = []
    cur = 0
    while cur < 15:
        fish_id = 350001 + fishery_index * 100 + cur
        instance_object.fish.append(fish_id)
        cur += 1
    cur = 0
    while cur < 15:
        fish_id = 360001 + fishery_index * 100 + cur
        instance_object.fish.append(fish_id)
        cur += 1
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fisheries_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fisheries_detail)

def fisheries_language(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index):
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    template_tpId = fishery_id - 1
    key = "tpId"
    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fishery_id, table_data_detail=fisheries_language_detail)
    instance_object: FISHERIES_LANGUAGE
    if json_objects:
        mode = 2
        instance_object = json_to_instance(json_object=json_objects[0], cls=FISHERIES_LANGUAGE)
    else:
        mode = 1
        json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_tpId, table_data_detail=fisheries_language_detail)
        instance_object = json_to_instance(json_object=json_objects[0], cls=FISHERIES_LANGUAGE)

    instance_object.name = f"新主线渔场{fishery_index}"
    instance_object.tpId = fishery_id
    instance_object.id = instance_object.tpId
    instance_object.t_name = instance_object.name
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fisheries_language_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fisheries_language_detail)

def present(excel_tool: ExcelToolsForActivities, fishery_index):
    present_detail = excel_tool.get_table_data_detail(book_name="PRESENT.xlsm")
    fish_bone_id_start = 380001 + 15 * (fishery_index - 1)
    gold_fish_bone_id_start = 385001 + 15 * (fishery_index - 1)
    template_fish_bone_id_start = fish_bone_id_start - 15
    template_gold_fish_bone_id_start = gold_fish_bone_id_start - 15
    key = "presentId"
    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fish_bone_id_start, table_data_detail=present_detail)
    if json_objects:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: PRESENT
        if mode == 1:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_fish_bone_id_start + cur, table_data_detail=present_detail)
            instance_object = json_to_instance(json_object=json_object, cls=PRESENT)
        else:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=fish_bone_id_start + cur, table_data_detail=present_detail)
            instance_object = json_to_instance(json_object=json_object, cls=PRESENT)

        instance_object.name = f"渔场{fishery_index}_信物鱼{cur + 1}"
        instance_object.presentId = fish_bone_id_start + cur
        instance_object.id = instance_object.presentId
        instance_object.presentDescription = instance_object.name
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.presentId, instance_object=instance_object, table_data_detail=present_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.presentId, instance_object=instance_object, table_data_detail=present_detail)
        cur += 1

    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=gold_fish_bone_id_start, table_data_detail=present_detail)
    if json_objects:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        if mode == 1:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key,value=template_gold_fish_bone_id_start + cur, table_data_detail=present_detail)
            instance_object = json_to_instance(json_object=json_object, cls=PRESENT)
        else:
            json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=gold_fish_bone_id_start + cur, table_data_detail=present_detail)
            instance_object = json_to_instance(json_object=json_object, cls=PRESENT)
        instance_object.name = f"渔场{fishery_index}_黄金鱼骨{cur + 1}"
        instance_object.presentId = gold_fish_bone_id_start + cur
        instance_object.id = instance_object.presentId
        instance_object.presentDescription = instance_object.name
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.presentId, instance_object=instance_object, table_data_detail=present_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.presentId, instance_object=instance_object, table_data_detail=present_detail)
        cur += 1

def championships(excel_tool: ExcelToolsForActivities, fishery_id):
    championships_detail = excel_tool.get_table_data_detail(book_name="CHAMPIONSHIPS.xlsm")
    template_fishery_id = fishery_id - 1
    key = "fishSceneTpId"
    json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fishery_id, table_data_detail=championships_detail)
    instance_object: CHAMPIONSHIPS
    if json_objects:
        mode = 2
        instance_object = json_to_instance(json_object=json_objects[0], cls=CHAMPIONSHIPS)
    else:
        mode = 1
        json_objects = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_fishery_id, table_data_detail=championships_detail)
        instance_object = json_to_instance(json_object=json_objects[0], cls=CHAMPIONSHIPS)
        instance_object.name = int(json_objects[0]["name"]) + 1
        instance_object.tpId = json_objects[0]["tpId"] + 1

    instance_object.fishSceneTpId = fishery_id
    instance_object.id = instance_object.tpId
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.fishSceneTpId, instance_object=instance_object, table_data_detail=championships_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.fishSceneTpId, instance_object=instance_object, table_data_detail=championships_detail)

def main(excel_tool: ExcelToolsForActivities, fishery_id):
    fishery_index = fishery_id - 500300
    fish(excel_tool=excel_tool, fishery_index=fishery_index)
    fisheries(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index)
    fisheries_language(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index)
    present(excel_tool=excel_tool, fishery_index=fishery_index)
    championships(excel_tool=excel_tool, fishery_id=fishery_id)



if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool=excel_tool, fishery_id=500307)

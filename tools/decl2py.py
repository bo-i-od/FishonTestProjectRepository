import re
from pathlib import Path
from typing import Dict, List

from configs.pathConfig import EXCEL_PATH
from tools.baseDataRead import parse_decl_file

import dataclasses
from typing import Any, Union, get_origin, get_args

TYPE_MAPPING = {
    "int": "int",
    "string": "str",
    "float": "float",
    "double": "float",
    "char": "str",
    "bool": "bool",
}

def generate_python_class(struct_name: str, struct_info: dict) -> str:
    """改进版类生成器"""
    lines = [
        f"@dataclass",
        f"class {struct_name}:"
    ]

    for field_name, (field_type, is_array) in struct_info.items():
        if field_type in TYPE_MAPPING:
            field_type = TYPE_MAPPING[field_type]
        # 处理数组类型
        if is_array:
            type_hint = f"Optional[List[{field_type}]]"
            default = "field(default=None)"
        else:
            type_hint = f"Optional[{field_type}]"
            default = "None"

        lines.append(f"    {field_name}: {type_hint} = {default}")

    return '\n'.join(lines)


def process_file(input_path: Path, output_dir: Path):
    structs = parse_decl_file(input_path)
    print(structs)
    output = ["from dataclasses import dataclass, field"]
    output.append("from typing import Optional, List\n")

    # 修复点：使用items()遍历字典
    for struct_name, struct_info in structs.items():
        output.append(generate_python_class(struct_name, struct_info))
        output.append("\n\n")  # 添加两个空行
    print('\n'.join(output))
    output_path = output_dir / f"{input_path.stem.split('.')[0]}.py"
    output_path.write_text('\n'.join(output), encoding="utf-8")


def batch_process(input_files: List[Path], output_dir: Path):
    """批量处理"""
    output_dir.mkdir(exist_ok=True, parents=True)

    for input_file in input_files:
        if not input_file.is_file():
            continue
        if not input_file.suffix == ".h":
            continue
        # if not input_file.name == "ACTIVITY_NEW_YEAR_BET_WEIGHT.decl.h":
        #     continue
        try:
            process_file(input_file, output_dir)
            print(f"Processed: {input_file.name}")
        except Exception as e:
            print(f"Error processing {input_file.name}: {str(e)}")


def json_list_to_instance_list(json_object_list, cls: type):
    instance_object_list = []
    for json_object in json_object_list:
        instance_object = json_to_instance(json_object=json_object, cls=cls)
        instance_object_list.append(instance_object)
    return instance_object_list


def json_to_instance(json_object: dict, cls: type) -> Any:
    """将字典转换为数据类实例"""
    if not dataclasses.is_dataclass(cls):
        return None

    kwargs = {}
    for field in dataclasses.fields(cls):
        field_name = field.name
        field_type = field.type

        # 处理字段不存在的情况
        if field_name not in json_object:
            kwargs[field_name] = None
            continue

        raw_value = json_object[field_name]

        # 处理Optional类型
        if get_origin(field_type) is not Union:
            # 普通类型处理
            kwargs[field_name] = _parse_value(raw_value, field_type)
            continue
        type_args = get_args(field_type)
        if len(type_args) != 2:
            kwargs[field_name] = _parse_value(raw_value, field_type)
            continue
        if type(None) not in type_args:
            kwargs[field_name] = _parse_value(raw_value, field_type)
            continue
        # Optional[T] 的情况
        actual_type = next(t for t in type_args if t is not type(None))
        if raw_value is None:
            kwargs[field_name] = None
            continue
        # 递归处理实际类型
        kwargs[field_name] = _parse_value(raw_value, actual_type)
        continue

    return cls(**kwargs)


def _parse_value(raw_value: Any, target_type: type) -> Any:
    """递归解析值"""
    # 处理列表类型
    if get_origin(target_type) is list:
        item_type = get_args(target_type)[0]
        return [_parse_value(item, item_type) for item in raw_value]

    # 处理数据类
    if dataclasses.is_dataclass(target_type):
        return json_to_instance(raw_value, target_type)

    # 处理嵌套的Optional
    if get_origin(target_type) is not Union:
        return raw_value
    type_args = get_args(target_type)
    if len(type_args) != 2:
        return raw_value
    if type(None) not in type_args:
        return raw_value
    return _parse_value(raw_value, type_args[0])


def instance_list_to_json_list(instance_object_list):
    json_object_list = []
    for instance_object in instance_object_list:
        data = instance_to_json(instance_object=instance_object)
        json_object_list.append(data)
    return json_object_list


def instance_to_json(instance_object: Any) -> Any:
    """将数据类实例转换为字典"""
    if not dataclasses.is_dataclass(instance_object):
        if isinstance(instance_object, list):
            return [instance_to_json(item) for item in instance_object]
        elif isinstance(instance_object, dict):
            return {k: instance_to_json(v) for k, v in instance_object.items()}
        else:
            return instance_object
    result = {}
    for field in dataclasses.fields(instance_object):  # 保持字段顺序
        value = getattr(instance_object, field.name)
        # 递归处理值并过滤None
        parsed_value = instance_to_json(value)
        if parsed_value is None:
            continue
        result[field.name] = parsed_value
    return result


def json_to_block(json_object, name='', indent=0):
    """严格格式转换工具"""
    INDENT_UNIT = '\t'  # 使用制表符缩进
    indent_str = INDENT_UNIT * (indent // 1)  # 每级缩进1个制表符

    lines = []
    if isinstance(json_object, list):
        # 顶层列表处理
        for item in json_object:
            lines.append(json_to_block(item, name, indent))
        return '\n'.join(lines)
    if not isinstance(json_object, dict):
        return '\n'.join(lines)
    # 块头
    lines.append(f'{indent_str}{name}{{')

    # 处理每个字段
    for k, v in json_object.items():
        next_indent = indent + 1

        if isinstance(v, dict):
            # 嵌套对象
            lines.append(json_to_block(v, k, next_indent))
            continue

        if not isinstance(v, list):
            # 基础类型
            lines.append(f'{INDENT_UNIT * next_indent}{k}="{_strict_format(v)}";')
            continue

        # 列表处理
        if all(not isinstance(i, (dict, list)) for i in v):
            # 简单列表展开
            for item in v:
                lines.append(f'{INDENT_UNIT * next_indent}{k}="{_strict_format(item)}";')
            continue
        # 复杂列表递归处理
        for item in v:
            lines.append(json_to_block(item, k, next_indent))
        continue

    # 块尾
    lines.append(f'{indent_str}}};')

    return '\n'.join(lines)

def instance_to_block(instance_object, name='', indent=0):
    json_object = instance_to_json(instance_object=instance_object)
    return json_to_block(json_object=json_object, name=name, indent=indent)


def _strict_format(value):
    """精确数值格式化"""
    if isinstance(value, float):
        # 处理整数值浮点数
        if value.is_integer():
            return f"{int(value)}"
        # 保留原始精度表示
        return f"{value:.10f}".rstrip('0').rstrip('.') if '.' in str(value) else str(value)
    if isinstance(value, bool):
        return str(int(value))
    return str(value)


def json_list_to_blocks(json_object_list, name):
    blocks = ""
    for data in json_object_list:
        blocks += json_to_block(json_object=data, name=name)
        blocks += "\n\n"
    return blocks

def update_h(output_dir="../activities/decl"):
    # 生成excel表解析
    base_data_path = Path(EXCEL_PATH.split("策划模板导出工具/")[0] + r"ElementData/BaseData/")
    direct_files = list(base_data_path.glob("*"))  # 包含文件和目录
    direct_files = [p for p in direct_files if p.is_file()]
    batch_process(
        input_files=direct_files,
        output_dir=Path(output_dir)
    )

if __name__ == "__main__":
    # base_data_path = Path(EXCEL_PATH.split("策划模板导出工具/")[0] + r"ElementData/BaseData/")
    update_h()
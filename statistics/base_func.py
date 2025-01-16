from statistics.load_log import load_log_new
from tools.excelRead import ExcelTools
from configs.pathConfig import EXCEL_PATH
S=1
M=2
L=3
H=4
B=5
Rare=11
Elite=12
Monster=13

excelTools =  ExcelTools(EXCEL_PATH)

fish_table_data = excelTools.get_table_data("FISH.xlsm")
fish_tpId_list = fish_table_data['tpId']
fishType_list = fish_table_data['fishType']
fishClass_list = fish_table_data['fishClass']


def get_fish_type_class(fish_id):
    index=fish_tpId_list.index(fish_id)
    return fishType_list[index],fishClass_list[index]


def get_fish_size(fish_id):
    fish_type,fish_class=get_fish_type_class(fish_id)
    fish_size = ["Special","Common","Rare","Elite","Monster"][fish_class]
    if fish_size=="Common":
        fish_size=["Small","Median","Large","Huge","Giant"][fish_type-1]
    return fish_size


"""
mission_condition_data=excelTools.get_table_data("MISSION_CONDITION.xlsm")
triggerKeyS=mission_condition_data["triggerKeyS"]
missionConditionID=mission_condition_data["missionConditionID"]

fish_state_data=excelTools.get_table_data("FISH_STATE.xlsm")
startConditionId=fish_state_data["startConditionId"]
fishChange=fish_state_data["fishChange"][0]['fish']

def get_yugu_data(yugu_id):
    index=triggerKeyS.index(yugu_id)
    m_c_id=missionConditionID[index]

    index=startConditionId.index(m_c_id)
    fish=fishChange[index]
    return fish

def get_yugu_type(yugu_id):
    fish_id=get_yugu_data(yugu_id)
    fish_data=get_fish_type_class(fish_id)
    return fish_data[1]



def get_fish_type(fish_id):
    fish_type,fish_class=get_fish_type_class(fish_id)
    fish_type='fish'
    if 380000>fish_id>370000:
        fish_type = "gold_yugu"
    elif 392000>fish_id>391000:
        fish_type = "yugu"
    elif 391000>fish_id>390000:
        fish_type='boss'

    if fish_type in ["gold_yugu","yugu"]:
        fish_id=get_yugu_data(fish_id)
    fish_size=get_fish_size(*get_fish_type_class(fish_id))

    return {'fish_size':fish_size,'fish_type':fish_type}

def statistic_fish_size(numbers):
    count = {}
    for i in numbers:
        fish_result=get_fish_type(i)
        if fish_result['fish_type'] in ['fish','boss']:
            fish_size=fish_result['fish_size']
            count.setdefault(fish_size,0)
            count[fish_size]+=1
    return count

"""

if __name__ == '__main__':
    # 测试
    # 测试
    data=load_log_new("new_hook_log.txt")
    numbers=[i['fishes']['1']['tpId'] for i in data]
    count=statistic_fish_size(numbers)
    print(len(numbers),count)
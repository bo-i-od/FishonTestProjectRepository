import copy
import json
from configs.pathConfig import EXCEL_PATH

from tools.txtTableRead.get_table_data import get_table_data,write_table_data
from icecream import ic


data_keys = "FISHCARD_REWARD_GROUP"
fishcard_data=get_table_data(data_keys)



rewardGroupId_list=[10001+i for i in range(10)]
rewardGroupId_title=[
    '卡包10',
    '卡包20',
    '卡包50',
    '卡包100',
    '卡包200',
    '卡包1000',
    '特大20',
    '特大100',
    '超巨20',
    '超巨100',
]

fishcard_group_data={}
for j in fishcard_data.values():
    if j['fisheriesId'] not in fishcard_group_data:
        fishcard_group_data[j['fisheriesId']]={}
    fishcard_group_data[j['fisheriesId']][j['rewardGroupId']]=j['fishcardItemId']


convert_keys = "ITEM_CONVERT_RULE"
convert_data=get_table_data(convert_keys)
start_key=1001

for fisheriesId,fisheriesData in fishcard_group_data.items():
    for j in range(len(rewardGroupId_list)):
        rewardGroupId=rewardGroupId_list[j]
        rewardGroupName=str(fisheriesId)+rewardGroupId_title[j]
        item_id=fisheriesData[str(rewardGroupId)]

        convert_data[str(start_key)]={
            'id':start_key,
            'name':rewardGroupName,
            'autoId':start_key,
            'convertGroup':rewardGroupId,
            'toConvertItemType':2,
            'toConvertItemTpId':item_id,
            'changeType':3,
            'changeArg':[fisheriesId,0,0],
            # 'valueMultil':0,
            # 'roundType':0,
        }
        start_key+=1

ic(convert_data)
# 写回txt
write_table_data(convert_keys,convert_data)
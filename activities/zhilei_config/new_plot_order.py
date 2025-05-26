import copy
import json

from tools.txtTableRead.get_table_data import get_table_data,write_table_data
from icecream import ic

def get_code_type(code):
    if 3000000<code<4000000:
        return 199
    elif 7000000<code<8000000:
        return 200

data_keys = "ALLOT_CONFIG"
allot_config_data=get_table_data(data_keys)
# 清理原有allot
# for i in copy.deepcopy(list(allot_config_data.keys())):
#     if i[0]=='3' and len(i)==7:
#         allot_config_data.pop(i)

def add_allot_base(code_list,allot_id,allot_name,allot_type,weight_list=[]):
    """ 标准的allot添加形式，支持 权重、不放回抽取、按次数 等类型 """
    now_allotData=[]
    count=0
    for i in range(len(code_list)):
        # 权重是0则不配置
        if weight_list and weight_list[i]==0:
            continue
        code = code_list[i]
        count += 1
        if allot_type in ['times_reset','times']:
            num=count # 次数型 依次出
        elif allot_type == 'no_repeat': # 不放回重置型，num代表数量
            num=1
        elif weight_list:
            num=weight_list[i] # 权重
        else:
            num=100 # 默认为等权重
        now_allotData.append({
            'num': num,
            'type': get_code_type(code),  # type
            'code': code,  # mission_id 或者 allot_id
            'count': 1,
        })
    if allot_type == 'no_repeat':
        allotType = 6
    elif allot_type == 'weight':
        allotType = 5
    elif allot_type == 'times_reset':
        allotType = 4
    elif allot_type == 'times':
        allotType = 3
    else:
        print("errror!!!",code_list)
    allot_config_data[str(allot_id)] = {
        'id': allot_id,
        'name': allot_name,
        'allotId': allot_id,
        'allotType': allotType,
        'allotData': now_allotData,
    }

first_allot_id=3000005  # 订单入口
# 新手前x个订单，
xinshou_num = 5
# D、B、C、A
order_level_name=['D','C','B','A','S','SS','SSS',]
# ------------------------------分体型（SMLHGREM）的任务 D-SSS 3000101-7, 3000201-7,3000301-7------------------------------
# 1为单鱼得分、2为分体型累计得分、3为分体型条数
# 分体型（SMLHGREM）的任务，基于allot_id 拆分到具体的mission_id，
# 要根据weight 去具体拆分，像比如典藏类型的任务，单次要求次数太高就用不上了
# 整体是越稀有的订单，对应体型要求会偏好一些
allot_id_single_fish=3000101
allot_id_fish_type_total=3000201
allot_id_fish_type_num=3000301

weight_list1=[
[1,1,1,0,0,0,0,0],
[1,1,1,0,0,0,0,0],
[1,1,1,1,1,0,0,0],
[1,1,1,1,1,0,0,0],
[0,1,1,1,1,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
]
weight_list2=[
[1,1,1,0,0,0,0,0],
[1,1,1,0,0,0,0,0],
[1,1,1,1,1,0,0,0],
[1,1,1,1,1,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,1,1,1,0,0],
[0,0,0,0,1,1,0,0],
]
weight_list3=[
[1,1,1,0,0,0,0,0],
[1,1,1,0,0,0,0,0],
[1,1,1,0,0,0,0,0],
[1,1,1,1,1,0,0,0],
[0,1,1,1,1,0,0,0],
[0,0,1,1,1,0,0,0],
[0,0,0,1,1,0,0,0],
]

fish_type_name=['S','M','L','H','G','R','E','M']

for i in range(len(order_level_name)):
    code_list1=[7111001+(j+1)*10+i for j in range(8)]  # 单鱼考虑bet最大得分
    add_allot_base(code_list1,allot_id_single_fish+i,'订单-单鱼考虑bet最大得分-稀有度' + order_level_name[i],'no_repeat',weight_list1[i])
for i in range(len(order_level_name)):
    code_list2=[7112001+(j+1)*10+i for j in range(8)]  # 分体型累计得分
    add_allot_base(code_list2, allot_id_fish_type_total+i, '订单-分体型累计得分-稀有度' + order_level_name[i],
                   'no_repeat', weight_list2[i])
for i in range(len(order_level_name)):
    code_list3=[7113001+(j+1)*10+i for j in range(8)]  # 次数型任务
    add_allot_base(code_list3, allot_id_fish_type_num+i, '订单-次数型任务-稀有度' + order_level_name[i],
                   'no_repeat', weight_list3[i])

# ------------------------------战斗类型任务聚合  D-SSS  3000401-7 ---------------------------------
allot_id_start=3000401
mission_name=[
    "累计QTE次数",
    # "拔竿次数",
    # "爆气次数", 太难做了
    "完美刺鱼x次",
    "条数池"
]
for i in range(len(order_level_name)):
    code_list = [j + i + 1 for j in [7114200,7114300,7114600]]
    add_allot_base(code_list,allot_id_start+i,'订单-战斗类任务-稀有度' + order_level_name[i],'no_repeat')
# ----------------------------------次数类型任务总聚合 ------------------------------------

allot_id_cishu_final = 3000002
now_code_list=[7114201,7114202,3000401,3000402,3000303]  # 条数任务 + 战斗任务 + 难度任务
add_allot_base(now_code_list,allot_id_cishu_final,"次数型任务总入口",'no_repeat')

# --------------------------高难分数型任务，各类型任务的组合 D-SSS  3000501-7 -----------------------------
allot_id_hard_start = 3000501
weight_list_total=[
    [100,0,0],
    [100,0,0],
    [100,0,0],
    [200,100,0],
    [150,100,50],
    [100,100,50],
    [100,100,100],
]
code_id_start=[7114101,allot_id_fish_type_total,allot_id_single_fish]  # 分数、分类型得分、单鱼
for i in range(len(order_level_name)):
    code_list=[code_id_start[j]+i for j in range(3)]
    add_allot_base(code_list,allot_id_hard_start+i,'高难订单'+order_level_name[i]+'组合','weight',weight_list_total[i])

# --------------------------不同等级鱼卡分发不同级别（D-SSS） 普通分数和 高难的任务------------------------
card_level=[5,10,15,20,25,30,35,40,45,9999]
allot_id_hard_final = 3000003
allot_id_hard_card_start = 3000601
allot_id_normal_final = 3000004
allot_id_normal_card_start = 3000701

def add_allot_card_level(allot_id_final,allot_id_start,allot_name):
    """ 创建按鱼卡等级分发的订单入口 """
    start_allotData=[
        {
            'num':card_level[i],  # 具体level
            'type':199,   # 嵌套循环
            'code':allot_id_start+i, #分发下一层id
            'count':1,
        } for i in range(len(card_level))
    ]
    allot_config_data[str(allot_id_final)]={
        'id':allot_id_final,
        'name': allot_name,
        'allotId': allot_id_final,
        'tagName':'FishCardLevel',  # 按鱼卡等级
        'allotType':'2', #  (ChooseCeil)
        'allotData':start_allotData,
    }
add_allot_card_level(allot_id_hard_final,allot_id_hard_card_start,'高难订单入口')
add_allot_card_level(allot_id_normal_final,allot_id_normal_card_start,'普通订单入口')

# -------------高难订单各级鱼卡----分发到具体任务-------------------
# 高难订单，不同鱼卡等级下， A\S\SS\SSS的任务出现的分布
now_times_total=[
    [1, 0, 0, 0],
    [2, 1, 0, 0],
    [2, 3, 0, 0],
    [1, 2, 0, 0],
    [1, 3, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 3, 0],
    [0, 0, 2, 1],
    [0, 0, 1, 2],
    [0, 0, 0, 1],
]
# mission_id或者allot_id,  由于从A开始  D=0,C=1,B=2,A=3
code_id_start = allot_id_hard_start + 3
def temp_get_code_list(now_times_list,start_id):
    """根据 now_times_total（每档评级的任务出现几次） 和起始id，生成最终的code_list """
    code_list_result = []
    for j in range(len(now_times_list)):
        if now_times_list[j]>0:
            for k in range(now_times_list[j]):
                code_list_result.append(start_id+j)
    return code_list_result

# 生成每档鱼卡对应的配置
for i in range(len(card_level)):
    code_list = temp_get_code_list(now_times_total[i], code_id_start)
    add_allot_base(code_list, allot_id_hard_card_start+i, "高难订单"+str(card_level[i])+"级鱼卡入口",'no_repeat')

# -------------普通订单各级鱼卡----分发到具体任务-------------------
# 纯分数型任务 不同鱼卡等级下， C\B\A\S的任务出现的分布
now_times_total=[
    [1, 2, 0, 0],
    [1, 2, 1, 0],
    [0, 2, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 2, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 2],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
]
score_mission_start_id=7114101
# mission_id或者allot_id,  由于从C开始  D=0,C=1,B=2,A=3
code_id_start=score_mission_start_id+1 #
# 生成每档鱼卡对应的配置
for i in range(len(card_level)):
    code_list = temp_get_code_list(now_times_total[i], code_id_start)
    add_allot_base(code_list,allot_id_normal_card_start+i,"普通订单"+str(card_level[i])+"级鱼卡入口",'no_repeat')

# -------------最终订单终极汇总-------------

now_code_list=[allot_id_cishu_final,allot_id_normal_final,allot_id_hard_final]
add_allot_base(now_code_list,first_allot_id,"订单总入口",'times_reset')
# -------------增加额外 新手 订单体验 ------
final_allot_id=3000001
now_code_list= [
7114201	,
7114101	,
7114102	,
7114201	,
7114102	,
3000203	,
first_allot_id]
add_allot_base(now_code_list,final_allot_id,"订单究极总入口",'times')


# ic(allot_config_data)
# fix
for key,value in allot_config_data.items():
    if 'tb' not in value:
        value['tb']='allot_config'
    dis_len=20-len(value['allotData'])
    if dis_len>0:
        for i in range(dis_len):
            value['allotData'].append({})



# 写回txt
write_table_data("allot_config",allot_config_data)


# if __name__ == '__main__':
    # print(battle_buff_data)
    # print(battle_skill_data)


    # with open('test_data.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(fish_data, json_file, ensure_ascii=False, indent=4)

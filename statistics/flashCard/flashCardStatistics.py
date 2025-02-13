from statistics.load_log import *
from statistics.fishStatistics.fishNum import total_dict
from statistics.base_func import get_fish_size

cast_log=load_log_new('../new_cast_log.txt')
hook_log=load_log_new('../new_hook_log.txt')

DebugInfo='debugInfos'

for index,i in enumerate(cast_log):

    pid=int(i[DebugInfo][ProtectiveId])
    if pid>0 and pid not in [60010,20040,20041,520040,520041]:
            print("special_protect",index,pid)

flash_card={}
# card_num=[8,3,2]
card_num=[15,9,6]
per_cost = 100
per_print_cast = 50
def get_card_type(f_fish_id):
    fish_type=get_fish_size(f_fish_id)
    if fish_type in ["Small","Median","Large","Huge","Giant"]:
        return 0
    elif fish_type in ["Rare","Elite"]:
        return 1
    elif fish_type in ["Monster"]:
        return 2

def check_card_status():
    card_status = [0, 0, 0]
    for j,k in flash_card.items():
        if k['flash_card_num']>0:
            card_level=get_card_type(j)
            card_status[card_level]+=1
    return card_status
def check_fish_id(fish_id):
    return (300000 < fish_id < 320000) or (390000 < fish_id < 391000)
def check_fish_id_new_plot(fish_id):
    return 350000<=fish_id<=369999

def init_flash_card_data(f_fish_id):

    return


total_energy_cost = 0
for index,i in enumerate(hook_log):
    f_fish_id = get_fish_id(i)
    if f_fish_id:
        f_fish_id = int(f_fish_id)
        energy_cost = get_energy_cost(i)
        total_energy_cost+=energy_cost

        if check_fish_id_new_plot(f_fish_id):

            flash_card_data=get_flashcard_data(i)
            f_id = get_flashcard_id(i)

            flash_card.setdefault(f_fish_id, {'fish_num': 0, 'flash_card_num': 0, 'flash_card_times': 0, 'first_collect_index': 0, 'all_index': [], 'f_type': get_card_type(f_fish_id)})
            flash_card[f_fish_id]['fish_num'] += 1
            flash_card[f_fish_id]['all_index'].append(index)
            if f_id:
                f_num = int(flash_card_data['count'])
                if flash_card[f_fish_id]['flash_card_num']==0:
                    flash_card[f_fish_id]['first_collect_index']=index
                    flash_card[f_fish_id]['first_collect_energy_cost']=total_energy_cost # cast_log[index][DebugInfo]["energyCost"]
                flash_card[f_fish_id]['flash_card_num'] += f_num
                flash_card[f_fish_id]['flash_card_times']+=1
    if (index>0 and index%per_print_cast==0) or index==len(hook_log)-1 :
        card_status=check_card_status()
        print("cost:",total_energy_cost,"    card_list:",card_status)


sorted_dict = sorted(flash_card.items(), key=lambda x: x[1]['f_type'], reverse=False)

for i in sorted_dict:
    print(i[1]['f_type'],i)

check_card_status()
from load_log import load_log

data1=load_log('cast_log.txt')
data2=load_log('hook_log.txt')
# print(data1)
for index,i in enumerate(data1):
    pid=i['protectiveId']
    if pid:
        pid=int(eval(pid))
        if pid>0:
            print("special_protect",index,i['protectiveId'])

flash_card={}
card_num=[15,6,3]
per_cost = 10
per_print_cast = 20
def get_card_level(num):
    total=0
    for index,i in enumerate(card_num):
        total+=i
        if num<total:
            return index

def check_card_status():
    card_status = [0, 0, 0]
    for j,k in flash_card.items():
        f_id=k['f_id']
        if f_id:
            card_index=f_id%100-1
            card_level=get_card_level(card_index)
            card_status[card_level]+=1
    return card_status

for index,i in enumerate(data2):
    f_id=i['flash_card_id']
    f_fish_id = i['fish_id']
    if f_fish_id:
        f_fish_id=int(f_fish_id)
        if 1:  # 注释代表仅看鱼(300000<f_fish_id<320000) or (390000<f_fish_id<391000):
            flash_card.setdefault(f_fish_id, {'fish_num': 0, 'flash_card_num': 0, 'flash_card_times':0,'first_collect_index':0,'all_index':[],'f_id':0})
            flash_card[f_fish_id]['fish_num'] += 1
            flash_card[f_fish_id]['all_index'].append(index)
            if f_id:
                f_id=int(f_id)
                flash_card[f_fish_id]['f_id']=f_id
                f_num = int(i['flash_card_num'])
                if flash_card[f_fish_id]['flash_card_num']==0:
                    flash_card[f_fish_id]['first_collect_index']=index
                    flash_card[f_fish_id]['first_collect_energy_cost']=data1[index]["energyCost"]
                flash_card[f_fish_id]['flash_card_num'] += f_num
                flash_card[f_fish_id]['flash_card_times']+=1
    if (index>0 and index%per_print_cast==0) or index==(len(data2)-1):
        card_status=check_card_status()
        print("cost:",index*per_cost,"    card_list:",card_status)


sorted_dict = sorted(flash_card.items(), key=lambda x: x[0], reverse=False)
print(len(data2))
for i in sorted_dict:
    print(i)

check_card_status()
from load_log import load_log
data=load_log()
flash_card={}
for i in data:
    f_id=i['flash_card_id']
    f_fish_id = i['fish_id']
    if f_fish_id:
        flash_card.setdefault(f_fish_id, {'fish_num': 0, 'flash_card_num': 0, 'first_collect_index':0})
        flash_card[f_fish_id]['fish_num'] += 1
        if f_id:
            f_num = int(i['flash_card_num'])
            flash_card[f_fish_id]['flash_card_num'] += f_num
sorted_dict = sorted(flash_card.items(), key=lambda x: x[0], reverse=False)
print(len(data))
for i in sorted_dict:
    print(i)
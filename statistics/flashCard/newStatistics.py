from common.basePage import BasePage
from statistics.load_log import *

cast_log=load_log_new('../new_cast_log.txt')
hook_log=load_log_new('../new_hook_log.txt')

bp = BasePage()

for i,j in zip(cast_log,hook_log):
    debug_info=i['debugInfos']
    drop_rate= int(debug_info['flashCardFinalDropRate'])

    if drop_rate>0:
        fish_id=get_fish_id(i)
        energy_cost=debug_info['energyCostFcAll']
        fish_type= bp.get_fish_type(fish_id)
        card_data=get_flashcard_data(j)
        print("fish_id:",fish_id,"   ",drop_rate,"   ",fish_type,"    " ,energy_cost)
        if card_data:
            print(card_data)
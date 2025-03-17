from common.basePage import BasePage
from statistics.load_log import *
from common.basePage import BasePageMain, BasePage

cast_log=load_log_new('../new_cast_log.txt')
hook_log=load_log_new('../new_hook_log.txt')
num = 0
bp = BasePage()
silver_card = 0
purple_card = 0
gold_card = 0
count_3 = 0
count_2 = 0
count_1 = 0
for i in hook_log:
    if i["otherItems"]:
        flashcard = i["otherItems"]
        flash_card_id = flashcard["tiacs"]['1']['id']
        count = flashcard["tiacs"]['1']['count']
        num += count
        if count == 1:
            count_1 += 1
        elif count == 2:
            count_2 += 1
        else:
            count_3 += 1
        flash_card_type = bp.get_flash_card_type(flash_card_id=flash_card_id)
        if flash_card_type == 1:
            silver_card += 1
        elif flash_card_type == 2:
            purple_card += 1
        else:
            gold_card+= 1
        print("count:",flashcard["tiacs"]['1']['count'],"id:", flash_card_id,"type:",flash_card_type)
print("银卡：", silver_card, "紫卡：", purple_card, "金卡：", gold_card)
print("3张次数：", count_3,"2张次数：", count_2, "1张次数：", count_1)
print("钓鱼次数:", len(hook_log))
print("闪卡总数:", num)
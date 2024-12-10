import json
import queue

from common.basePage import BasePage




def qte(bp: BasePage, params_str):
    params = json.loads(params_str)
    qte_input_mask = params[0]
    qte_input = params[1]
    bp.qte_queue = queue.Queue()

    cur = 0
    while cur < 6:
        # if qte_input_mask & (1 << cur) == 0:
        #     cur += 1
        #     continue
        is_on = qte_input & (1 << cur) != 0
        # is_change = qte_input_mask & (1 << cur) != 0
        if is_on:
            bp.qte_queue.put(cur)
            cur += 1
            continue
        cur += 1

    # qte_up = (qte_input & 0x1) != 0
    # qte_left = (qte_input & 0x2) != 0
    # qte_right = (qte_input & 0x4) != 0
    # qte_jump_left = (qte_input & 0x8) != 0
    # qte_jump_right = (qte_input & 0x10) != 0
    # qte_power = (qte_input & 0x20) != 0
    # print(qte_up, qte_left, qte_right, qte_jump_left, qte_jump_right, qte_power)
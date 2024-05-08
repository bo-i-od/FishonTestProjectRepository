# coding=utf-8
from common.basePage import BasePage
from common.rpcMethod import *



if __name__ == '__main__':
    bp = BasePage()
    bp.set_item_count(target_count=123456789, item_tpid="100500")
    fish(bp.poco, spot_id="40030101", times=10)












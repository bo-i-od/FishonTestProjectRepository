
from netMsg import csMsgAll, luaLog
from common.basePage import BasePage
from tools.commonTools import lua_dict_to_python_dict


# 卖掉贝壳
def merge_sell_item(bp, grid_id=None, grid_id_list=None):
    if grid_id is not None:
        merge_sell_item(bp, grid_id_list=[grid_id])
        return

    lua_code = csMsgAll.get_CSMergeSellItemMsg(gridIds=grid_id_list)
    bp.lua_console(lua_code)

def sell_all(bp):
    cur = 1
    while cur <= 54:
        merge_sell_item(bp, grid_id=cur)
        bp.sleep(0.1)
        cur += 1


def merge_product_item(bp, product_type):
    lua_code = csMsgAll.get_CSMergeProductItemMsg(type=product_type)

    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    # 发送lua请求
    bp.lua_console(lua_code)

    msg_name = "MergeProductItemMsg"

    target_log = bp.receive_until_get_msg(msg_name=msg_name)

    if target_log is None:
        return []

    sc_msg = lua_dict_to_python_dict(target_log)

    info = sc_msg["info"]
    product_list = info.split(",")

    gridIds = sc_msg["gridIds"]

    grid_id_list = []
    for index in gridIds:
        grid_id_list.append(gridIds[index])

    merge_sell_item(bp, grid_id_list=grid_id_list)
    bp.sleep(0.1)

    return product_list


def main(bp):
    # 清空下贝壳
    sell_all(bp)

    # 设置代币数量
    merge_coin = 200000
    bp.cmd(f"add 1 102100 {merge_coin}")

    res = {}
    # 生成方式
    product_type = 1

    # 生成次数
    cur = 0
    times = 10000
    while cur < times:
        product_list = merge_product_item(bp, product_type=product_type)
        print(product_list)
        # 累计结果
        for product in product_list:
            if product not in res:
                res[product] = 1
                continue
            res[product] += 1
        cur += 1
        print(cur, res)






if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20052", is_mobile_device=False)
    # merge_sell_item(bp, grid_id=31)
    main(bp)

    bp.connect_close()
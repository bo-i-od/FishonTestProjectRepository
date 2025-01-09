import re
from common.basePage import BasePage
from netMsg import csMsgAll
from scripts import battleTest, duelTest, gearTest, fishCardTest


def guide_skip(bp):
    text = bp.lua_console_with_response(lua_code_return="_G.PassiveNewbieGuideEnum")
    pattern = '"([^"]*)"'
    result = re.findall(pattern, text)
    lua_code_list = []
    for r in result:
        lua_code = csMsgAll.get_CSNewGuideStoreMsg(key=r)
        lua_code_list.append(lua_code)
    bp.lua_console_list(command_list=lua_code_list)


def full_gear(bp):
    bp.cmd("allrod 500")
    bp.sleep(1)
    bp.set_item_count(target_count=10000000000, item_tpid="100000")
    bp.set_item_count(target_count=10000000, item_tpid="200300")
    gearTest.full_star(bp)
    gearTest.full_level(bp)

def talent_all(bp):
    bp.cmd("talentall")




if __name__ == '__main__':
    base_page = BasePage()

    # 跳过引导 需要重启Unity
    guide_skip(base_page)

    # # 钓一次鱼 备战界面
    # battleTest.fish_once(base_page, is_quick=False)

    # 循环钓鱼 备战界面
    # 填渔场id会将该渔场鱼钓一遍
    # battleTest.circulate_fish(base_page, is_quick=True, times=100)

    # rank0-7代表黑铁到传奇 对决大厅界面
    # duelTest.duel_once(base_page, rank=1)

    # 装备满级满星
    full_gear(base_page)

    # 所有鱼卡满级
    fishCardTest.fish_card_one_key_level_up(base_page)

    # 天赋满级
    # talent_all(base_page)

    # 设定指定对决杯数
    # duelTest.set_duelcup(base_page, 3000)

    base_page.connect_close()

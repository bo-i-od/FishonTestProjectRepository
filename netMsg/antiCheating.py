from common.basePage import BasePage
import hashlib

from netMsg import csMsgAll, netMsgTest, luaLog, fishingMsg


def md5(string):
    # 创建MD5对象
    md5_obj = hashlib.md5()

    # 对字符串进行编码,因为MD5只接受bytes类型
    string_bytes = string.encode('utf-8')

    # 更新MD5对象
    md5_obj.update(string_bytes)

    # 获取MD5值
    md5_value = md5_obj.hexdigest()

    return md5_value

def cast(bp: BasePage):
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True
    spot_id = "40030201"
    scene_id = spot_id[:6]
    rod_id = fishingMsg.get_rod_id(scene_id)
    otherArgMap103 = spot_id[len(spot_id) - 2];


    # 发送cs请求
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingCastMsg")\n'
                'local equipMap =NetworkMgr:NewMsg("SCFishEquip")\n'
                f'equipMap.rodTpId={rod_id}\n'
                'cmd.equip = equipMap\n'
                'cmd.castGType = 0\n'
                f'cmd.sceneArg1 = {scene_id}\n'
                f'local otherArgMap = {{[101] = 0, [102] = {spot_id}, [103]={otherArgMap103}}}\n'
                'cmd.otherArgMap = otherArgMap\n'
                'cmd.sceneType =1\n'
                'NetworkMgr:Send(cmd)'
                )
    bp.lua_console(lua_code)

    # 停止接收消息
    bp.sleep(0.5)
    bp.log_list_flag = False

    # 找到SC消息
    key_sc = '<==== [Lua] Receive Net Msg "SC'
    msg_name = "FishingCastMsg"
    msg_key = key_sc + msg_name
    target_log = netMsgTest.get_target_log(bp, msg_key)

    # 取到castFlag
    expect_key = "castFlag"
    castFlag = luaLog.get_value(msg=target_log, key=expect_key, is_str=False)

    return castFlag

def hook(lua_code_list):
    # 拼装lua_code
    lua_code = ''
    cur = 0
    while cur < len(lua_code_list):
        lua_code += lua_code_list[cur]
        cur += 1

    # 发送cs请求
    bp.lua_console(lua_code)


def get_hook_msg_template(castFlag):
    lua_code_list = []
    lua_code_list.append('local cmd = NetworkMgr:NewMsg("CSFishingHookMsg")\n')
    lua_code_list.append('cmd.fishSceneArgs = {}\n')
    lua_code_list.append('cmd.use_ULT_Ts = 0\n')
    lua_code_list.append('cmd.result = 1\n')
    lua_code_list.append('cmd.qteInfos = {}\n')
    lua_code_list.append('local qteInfo = NetworkMgr:NewMsg("FishingQTEInfo")\n')
    lua_code_list.append('qteInfo.done = true\n')
    lua_code_list.append('table.insert(cmd.qteInfos, qteInfo)\n')
    lua_code_list.append('table.insert(cmd.qteInfos, qteInfo)\n')
    lua_code_list.append('table.insert(cmd.qteInfos, qteInfo)\n')
    lua_code_list.append('table.insert(cmd.qteInfos, qteInfo)\n')
    lua_code_list.append('cmd.counterSuccessNum = 1\n')
    lua_code_list.append('cmd.timeCost = 18640\n')
    lua_code_list.append('local ain = {}\n')
    lua_code_list.append('ain.ATTACK_INTERVAL_NORMAL = "200"\n')
    lua_code_list.append('ain.ULT_MODIFIER = "150"\n')
    lua_code_list.append('ain.SWING_MODIFIER = "110"\n')
    lua_code_list.append('ain.HOOK_DAMAGE = "10020"\n')
    lua_code_list.append('ain.DAMAGE = "531"\n')
    lua_code_list.append('ain.ATTACK_INTERVAL_ULT = "150"\n')
    lua_code_list.append('ain.DIZZY_DAMAGE_MODIFIER = "200"\n')
    lua_code_list.append('cmd.rodArgs = ain\n')
    lua_code_list.append('cmd.fishArgs = {}\n')
    lua_code_list.append('local bra = {}\n')
    lua_code_list.append('bra.preFrame = "156"\n')
    lua_code_list.append('bra.digest = "c6f2458fbf52e4fe4ea7c18e2d08dfb2"\n')
    lua_code_list.append('bra.fixedTickFps = "25"\n')
    lua_code_list.append('bra.fixedTickMSec = "40"\n')
    lua_code_list.append('bra.statDamage = "0|2|0|0|0,1|41|588|1276|1075,2|19|1951|2234|2102,4|1|14128|14128|14128,5|1|11389|11389|11389,6|1|5402|5402|5402"\n')
    lua_code_list.append('bra.statUlt = "4|0|1|10000|417|1"\n')
    lua_code_list.append('bra.totalDamage = "0|0,4|14128|1|0.94,0|0,1|599|5877|101,1|599|5139|101,1|588|4401|99,1|927|3663|101,1|899|2925|98,1|918|2187|100,1|1149|1689|101,1|1115|951|98,1|1138|942|100,1|1160|567|102,1|1149|72|101,1|1126|1077|99,1|1138|825|100,1|1276|1299|102,1|927|2010|101,6|5402,1|784|4887|100,1|768|4149|98,1|1235|3411|102,1|1223|2673|101,1|1251|1935|100,1|1264|1926|101,1|999|2274|99,1|999|2505|99,1|1019|2010|101,1|1251|1635|100,1|1276|1866|102,1|1251|1614|100,1|1251|1359|100,1|1226|1953|98,1|1226|1701|98,1|1276|1812|102,2|2190|1566|100,2|2011|1566|101,2|1971|1566|99,2|2031|1566|102,2|2234|1566|102,2|2212|1566|101,2|2190|1566|100,2|2212|1566|101,2|2190|1566|100,2|2190|1566|100,2|2190|1566|100,2|2234|1566|102,2|2190|1566|100,2|1971|1566|99,2|2031|1566|102,2|1951|1566|98,2|1951|1566|98,2|2031|1566|102,2|1951|1566|98,1|899|2643|98,1|1138|1905|100,1|1149|1653|101,1|1115|1887|98,1|1138|1635|100,1|918|2100|100,1|1149|1605|101,1|1115|1842|98,1|1149|1842|101,5|11389,1|1264|1842|101"\n')
    lua_code_list.append('bra.constHash = "0547ce93b9caeafae71a3ba447165401"\n')
    lua_code_list.append('bra.lastFrame = "259"\n')
    lua_code_list.append('cmd.battleResultArgs = bra\n')
    lua_code_list.append(r'cmd.battleResult = "\0\0\0\5"' + '\n')
    lua_code_list.append('local pa = {}\n')
    lua_code_list.append('pa.AddStaminaDecreasePer = "850"\n')
    lua_code_list.append('pa.AddUltDamageModifier = "25"\n')
    lua_code_list.append('pa.AddStaminaDecreaseValue = "0"\n')
    lua_code_list.append('pa.AddDizzyDamageModifier = "0"\n')
    lua_code_list.append('pa.STAMINA_DECREASE = "1080"\n')
    lua_code_list.append('pa.AddJumpQteDamageModifier = "0"\n')
    lua_code_list.append('pa.HOOK_DAMAGE = "15030"\n')
    lua_code_list.append('pa.AutoUltEnergyIncrease = "1250"\n')
    lua_code_list.append('pa.AddHookDamageValue = "0"\n')
    lua_code_list.append('cmd.playerArgs = pa\n')
    lua_code_list.append(f'cmd.castFlag = {castFlag}\n')
    lua_code_list.append(f'cmd.hook_result = 4\n')
    lua_code_list.append('NetworkMgr:Send(cmd)')
    return lua_code_list

def cheat_content_replace(lua_code_list, key_field,lua_code):
    cur = 0
    while cur < len(lua_code_list):
        if key_field not in lua_code_list[cur]:
            cur += 1
            continue
        lua_code_list[cur] = lua_code
        break

def condition_1(lua_code_list):
    cheat_content = ""
    lua_code = f'bra.constHash = "{cheat_content}"\n'
    cheat_content_replace(lua_code_list, "constHash", lua_code)


def condition_2(lua_code_list):
    cheat_content = ""
    lua_code = f'bra.totalDamage = "{cheat_content}"\n'
    cheat_content_replace(lua_code_list, "totalDamage", lua_code)


def main(bp: BasePage):
    cf = cast(bp)
    hook_msg_template = get_hook_msg_template(cf)
    condition_1(hook_msg_template)
    hook(hook_msg_template)



if __name__ == '__main__':
    # constHash = "7d37951f4164f48a9de9e4a61e21df7f"
    bp = BasePage("192.168.111.80:20086")
    main(bp)
    bp.connect_close()




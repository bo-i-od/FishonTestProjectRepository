import random
import re

from common.basePage import BasePage
import hashlib

from netMsg import  netMsgTest, luaLog, fishingMsg


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
    spot_id = "40030101"
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
    cast_flag = luaLog.get_value(msg=target_log, key=expect_key, is_str=False)

    return cast_flag


def hook(bp:BasePage, lua_code_list):
    key = "battleResultArgs.frameNum"
    frameNum = get_value(lua_code_list, key)
    bp.sleep(float(frameNum[1:-1]) * 0.05)
    # 拼装lua_code
    lua_code = ''
    cur = 0
    while cur < len(lua_code_list):
        lua_code += lua_code_list[cur]
        cur += 1
    print(lua_code)
    # 发送cs请求
    bp.lua_console(lua_code)


def get_hook_msg_template(cast_flag):
    const_hash = md5("15d17855ee54dc53a91b4a278e80683f" + cast_flag)
    lua_code_list = ['local cmd = NetworkMgr:NewMsg("CSFishingHookMsg")\n',
                     'cmd.fishSceneArgs = {}\n',
                     'cmd.use_ULT_Ts = 0\n',
                     'cmd.result = 1\n',
                     'cmd.qteInfos = {}\n',
                     'local qteInfo = NetworkMgr:NewMsg("FishingQTEInfo")\n',
                     'qteInfo.done = true\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'table.insert(cmd.qteInfos, qteInfo)\n',
                     'cmd.counterSuccessNum = 4\n',
                     'cmd.timeCost = 36440\n',
                     'local rodArgs = {}\n',
                     'rodArgs.ATTACK_INTERVAL_NORMAL = "200"\n',
                     'rodArgs.ULT_MODIFIER = "150"\n',
                     'rodArgs.SWING_MODIFIER = "110"\n',
                     'rodArgs.HOOK_DAMAGE = "2900"\n',
                     'rodArgs.DAMAGE = "157"\n',
                     'rodArgs.ATTACK_INTERVAL_ULT = "150"\n',
                     'rodArgs.DIZZY_DAMAGE_MODIFIER = "200"\n',
                     'cmd.rodArgs = rodArgs\n',
                     'cmd.fishArgs = {}\n',
                     'local battleResultArgs = {}\n',
                     'battleResultArgs.preFrame = "199"\n',
                     'digest',
                     'battleResultArgs.fixedTickFps = "25"\n',
                     'battleResultArgs.fixedTickMSec = "40"\n',
                     'battleResultArgs.statDamage = "0|1|0|0|0|0|0,1|94|133|316|257|843|166|1020|0|1,2|26|380|435|414|914|200|1020|1|0,6|4|1208|1295|1230|937|209"\n',
                     'battleResultArgs.statUlt = "9|1|1|10000|998|2|0"\n',
                     'battleResultArgs.totalDamage = "0|0|0|0,1|133|413|330|1010|0|0,1|148|419|313|1020|1|0,1|144|499|291|990|1|0,1|145|579|264|1000|1|0,1|225|660|236|1000|1|0,1|229|740|209|1020|1|0,1|253|821|202|980|0|0,1|282|901|201|990|1|0,1|284|897|217|1000|1|0,1|279|927|207|980|1|0,1|253|883|204|980|0|0,1|253|964|199|980|0|0,1|284|917|216|1000|1|0,1|287|972|202|1010|1|0,6|1295|937|209,1|248|759|209|1010|0|1,1|313|839|172|1010|0|1,1|316|843|166|1020|0|1,1|303|873|170|980|0|1,1|256|903|179|990|0|0,1|208|778|231|1020|0|0,1|256|858|212|990|0|0,1|261|854|214|1010|0|0,1|261|935|197|1010|0|0,1|261|964|202|1010|0|0,1|261|858|209|1010|0|0,1|253|913|197|980|0|0,1|279|818|221|980|1|0,1|284|822|214|1000|1|0,1|223|752|219|990|1|0,6|1208|708|213,1|178|553|210|1020|1|1,1|264|634|174|980|1|1,1|264|714|138|980|1|1,1|275|795|125|1020|1|1,1|200|788|141|980|0|0,1|204|794|197|1000|0|0,1|204|775|214|1000|0|0,1|264|805|205|1020|0|0,1|256|885|201|990|0|0,1|264|854|211|1020|0|0,1|261|909|197|1010|0|0,1|253|862|210|980|0|0,1|256|892|201|990|0|0,1|290|873|203|1020|1|0,1|284|928|201|1000|1|0,1|284|858|205|1000|1|0,1|290|887|204|1020|1|0,2|431|914|197|1010|1|0,2|435|914|200|1020|1|0,2|423|914|198|990|1|0,2|431|914|199|1010|1|0,2|418|914|199|980|1|0,2|435|914|198|1020|1|0,2|427|914|199|1000|1|0,2|423|914|199|990|1|0,2|435|914|199|1020|1|0,2|435|914|199|1020|1|0,2|423|914|196|990|1|0,2|384|914|197|990|0|0,2|396|914|200|1020|0|0,1|208|783|216|1020|0|0,1|253|864|196|980|0|0,1|261|944|203|1010|0|0,1|261|923|205|1010|0|0,1|259|902|201|1000|0|0,1|256|833|212|990|0|0,1|264|888|197|1020|0|0,1|287|880|200|1010|1|0,1|264|824|215|1020|0|0,1|284|879|200|1000|1|0,1|290|885|206|1020|1|0,1|290|889|203|1020|1|0,1|279|869|210|980|1|0,1|279|899|199|980|1|0,1|287|954|197|1010|1|0,1|279|907|212|980|1|0,1|279|937|203|980|1|0,1|279|867|211|980|1|0,1|259|922|197|1000|0|0,1|259|881|220|1000|0|0,2|388|922|210|1000|0|0,2|435|922|195|1020|1|0,2|388|922|197|1000|0|0,2|418|922|198|980|1|0,2|380|922|199|980|0|0,2|384|922|199|990|0|0,2|423|922|200|990|1|0,2|431|922|199|1010|1|0,2|427|922|199|1000|1|0,2|431|922|199|1010|1|0,2|380|922|197|980|0|0,2|396|922|200|1020|0|0,2|380|922|199|980|0|0,1|279|900|207|980|1|0,1|290|842|210|1020|1|0,1|256|922|198|990|0|0,6|1208|696|232,1|178|565|231|1020|1|1,1|270|645|194|1000|1|1,1|275|726|151|1020|1|1,1|264|730|149|980|1|1,1|275|785|151|1020|1|1,1|256|803|172|990|0|0,1|259|832|208|1000|0|0,1|253|838|236|980|0|0,1|287|893|248|1010|1|0,1|261|922|262|1010|0|0,1|261|940|279|1010|0|0,1|261|970|287|1010|0|0,1|279|999|276|980|1|0,1|256|978|272|990|0|0,1|282|933|269|990|1|0,1|279|962|258|980|1|0,1|279|992|244|980|1|0,6|1208|680|275,1|162|597|275|1020|0|1,1|243|627|248|990|0|1,1|240|634|208|980|0|1,1|243|714|199|990|0|1,1|206|771|194|1010|0|0,1|279|851|204|980|1|0,1|264|894|216|1020|0|0,1|282|949|224|990|1|0"\n',
                     f'battleResultArgs.constHash = "{const_hash}"\n',
                     'battleResultArgs.frameNum = "1419"\n',
                     'battleResultArgs.lastFrame = "483"\n',
                     'cmd.battleResultArgs = battleResultArgs\n',
                     r'cmd.battleResult = "\0\0\0\5"' + '\n',
                     'local playerArgs = {}\n',
                     'playerArgs.AddStaminaDecreasePer = "400"\n',
                     'playerArgs.AddUltDamageModifier = "0"\n',
                     'playerArgs.AddStaminaDecreaseValue = "0"\n',
                     'playerArgs.AddDizzyDamageModifier = "0"\n',
                     'playerArgs.STAMINA_DECREASE = "241"\n',
                     'playerArgs.AddJumpQteDamageModifier = "0"\n',
                     'playerArgs.AddHookDamagePer = "500"\n',
                     'playerArgs.HOOK_DAMAGE = "15030"\n',
                     'playerArgs.AutoUltEnergyIncrease = "1250"\n',
                     'playerArgs.AddHookDamageValue = "0"\n',
                     'cmd.playerArgs = playerArgs\n',
                     f'cmd.castFlag = {cast_flag}\n',
                     f'cmd.hook_result = 4\n',
                     'NetworkMgr:Send(cmd)']
    return lua_code_list


def gen_digest(lua_code_list):
    args_key_list = ["rodArgs", "battleResultArgs", "fishArgs", "playerArgs", "fishSceneArgs"]
    args_key_list.sort()
    builder = ""
    cur = 0
    while cur < len(args_key_list):
        builder += calc_string(lua_code_list, args_key_list[cur])
        cur += 1
    print(builder)
    digest = md5(builder)
    key = "digest"
    cur = 0
    while cur < len(lua_code_list):
        if key not in lua_code_list[cur]:
            cur += 1
            continue
        lua_code_list[cur] = f'battleResultArgs.digest = "{digest}"\n'
        break
    print(digest)
    # set_value(lua_code_list, key, digest)


def calc_string(lua_code_list, args_key):
    string = ""
    args_key += "."
    arg_list = []
    cur = 0
    while cur < len(lua_code_list):
        if args_key not in lua_code_list[cur]:
            cur += 1
            continue
        arg = lua_code_list[cur].split('.')
        if len(arg) < 2:
            cur += 1
            continue
        key = get_key(arg[1])
        value = get_value([arg[1]], key)
        value = value.replace('"', '')
        arg_list.append(key + value)
        cur += 1
    arg_list.sort()
    cur = 0
    while cur < len(arg_list):
        string += arg_list[cur]
        cur += 1
    return string


def get_key(line):
    pattern = r'^(.+?)\s*='
    match = re.match(pattern, line)
    key = ""
    if match:
        key = match.group(1)
    return key


def get_value(lua_code_list, key):
    value = ""
    cur = 0
    while cur < len(lua_code_list):
        get_key(lua_code_list[cur])
        if key != get_key(lua_code_list[cur]):
            cur += 1
            continue

        pattern = r'=\s*(.+?)(?=\n)'
        regex = re.compile(pattern)
        match = regex.search(lua_code_list[cur])
        if match:
            value = match.group(1)
        break
    return value


def set_value(lua_code_list, key, value):
    cur = 0
    while cur < len(lua_code_list):
        if key not in lua_code_list[cur]:
            cur += 1
            continue
        if get_key(lua_code_list[cur]) != key:
            cur += 1
            continue
        pattern = r'(=\s*)(.+?)(?=\n)'
        # old_value = re.search(pattern, lua_code_list[cur]).group(2)

        if "\\" in value:
            value = re.escape(value)
        replacement = rf'\1#{value}'
        # if old_value.startswith('"') and old_value.endswith('"'):
        #     replacement = rf'\1"{value}"'
        lua_code_list[cur] = re.sub(pattern, replacement, lua_code_list[cur])
        lua_code_list[cur] = lua_code_list[cur].replace("#", "")
        print(lua_code_list[cur])
        break


# constHash常数的hash值有误
def condition_1(lua_code_list):
    key = "battleResultArgs.constHash"
    cheat_content = '""'
    set_value(lua_code_list, key, cheat_content)


# totalDamage战斗伤害有非法值
def condition_2(lua_code_list):
    key = "battleResultArgs.totalDamage"
    cheat_content = '"->1xada"'
    set_value(lua_code_list, key, cheat_content)


# totalDamage战斗伤害超出阈值倍率
def condition_3(lua_code_list):
    key = "battleResultArgs.totalDamage"
    value = get_value(lua_code_list, key)
    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', value)

    # 将每个数字乘以1.5并取整
    new_numbers = [str(int(float(num) * 1.5)) for num in numbers]

    # 构建新的字符串
    cheat_content = re.sub(r'\d+', lambda match: new_numbers.pop(0), value)
    set_value(lua_code_list, key, cheat_content)


# totalDamage伤害次数超过阈值
def condition_4(lua_code_list):
    key = "battleResultArgs.totalDamage"
    value = get_value(lua_code_list, key)
    # 十遍伤害次数
    cheat_content = value * 10
    set_value(lua_code_list, key, cheat_content)


#  timeCost战斗时间有问题
def condition_6(lua_code_list):
    key = "cmd.timeCost"
    value = get_value(lua_code_list, key)
    cheat_content = str(int(value) // 2)
    set_value(lua_code_list, key, cheat_content)


# battleResult战斗结果版本有误，传了但是传错了
def condition_7(lua_code_list):
    key = "cmd.battleResult"
    value = get_value(lua_code_list, key)
    c = int(value[-2])
    c += 1
    if c > 9:
        c = 0
    cheat_content = value[:-3] + str(c) + value[-1:]
    set_value(lua_code_list, key, cheat_content)


# totalDamage战斗序列未回传
def condition_8(lua_code_list):
    key = "battleResultArgs.totalDamage"
    cheat_content = '""'
    set_value(lua_code_list, key, cheat_content)


# totalDamage战斗伤害不足
def condition_9(lua_code_list):
    key = "battleResultArgs.totalDamage"
    value = get_value(lua_code_list, key)

    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', value)

    # 将每个数字乘以1.5并取整
    new_numbers = [str(int(float(num) * 0.5)) for num in numbers]

    # 构建新的字符串
    cheat_content = re.sub(r'\d+', lambda match: new_numbers.pop(0), value)

    set_value(lua_code_list, key, cheat_content)


# battleResult版本长度错误
def condition_11(lua_code_list):
    key = "cmd.battleResult"
    value = get_value(lua_code_list, key)
    insert_string = str(random.randint(0, 9))
    cheat_content = value[:-2] + insert_string + value[-2:]
    set_value(lua_code_list, key, cheat_content)


# DAMAGE HOOK_DAMAGE修改
def condition_12(lua_code_list):
    # 'rodArgs.HOOK_DAMAGE = "10020"\n',
    # 'rodArgs.DAMAGE = "531"\n',
    key = "rodArgs.HOOK_DAMAGE"
    value = get_value(lua_code_list, key)
    damage = value[1:-1]
    cheat_content = str(int(damage) // 2)
    set_value(lua_code_list, key, cheat_content)


# battleResultArgs参数校验失败(少参数)
def condition_13(lua_code_list):
    # 'battleResultArgs.preFrame = "156"\n',
    # 'battleResultArgs.digest = "c6f2458fbf52e4fe4ea7c18e2d08dfb2"\n',
    # 'battleResultArgs.fixedTickFps = "25"\n',
    # 'battleResultArgs.fixedTickMSec = "40"\n',
    # 'battleResultArgs.statDamage = "0|2|0|0|0,1|41|588|1276|1075,2|19|1951|2234|2102,4|1|14128|14128|14128,5|1|11389|11389|11389,6|1|5402|5402|5402"\n',
    # 'battleResultArgs.statUlt = "4|0|1|10000|417|1"\n',
    # 'battleResultArgs.totalDamage = "0|0,4|14128|1|0.94,0|0,1|599|5877|101,1|599|5139|101,1|588|4401|99,1|927|3663|101,1|899|2925|98,1|918|2187|100,1|1149|1689|101,1|1115|951|98,1|1138|942|100,1|1160|567|102,1|1149|72|101,1|1126|1077|99,1|1138|825|100,1|1276|1299|102,1|927|2010|101,6|5402,1|784|4887|100,1|768|4149|98,1|1235|3411|102,1|1223|2673|101,1|1251|1935|100,1|1264|1926|101,1|999|2274|99,1|999|2505|99,1|1019|2010|101,1|1251|1635|100,1|1276|1866|102,1|1251|1614|100,1|1251|1359|100,1|1226|1953|98,1|1226|1701|98,1|1276|1812|102,2|2190|1566|100,2|2011|1566|101,2|1971|1566|99,2|2031|1566|102,2|2234|1566|102,2|2212|1566|101,2|2190|1566|100,2|2212|1566|101,2|2190|1566|100,2|2190|1566|100,2|2190|1566|100,2|2234|1566|102,2|2190|1566|100,2|1971|1566|99,2|2031|1566|102,2|1951|1566|98,2|1951|1566|98,2|2031|1566|102,2|1951|1566|98,1|899|2643|98,1|1138|1905|100,1|1149|1653|101,1|1115|1887|98,1|1138|1635|100,1|918|2100|100,1|1149|1605|101,1|1115|1842|98,1|1149|1842|101,5|11389,1|1264|1842|101"\n',
    # f'battleResultArgs.constHash = "{const_hash}"\n',
    # 'battleResultArgs.lastFrame = "259"\n',
    key = "battleResultArgs.lastFrame"
    cur = 0
    while cur < len(lua_code_list):
        if key not in lua_code_list[cur]:
            cur += 1
            continue
        lua_code_list.pop(cur)
        break


# digest摘要校验失败
def condition_14(lua_code_list):
    # 'rodArgs.HOOK_DAMAGE = "10020"\n',
    # 'rodArgs.DAMAGE = "531"\n',
    key = "battleResultArgs.digest"
    value = get_value(lua_code_list, key)
    # 前后交换
    cheat_content = value[16:] + value[:16]
    set_value(lua_code_list, key, cheat_content)


# statDamage战斗统计伤害有非法值
def condition_15(lua_code_list):
    key = "battleResultArgs.statDamage"
    cheat_content = '"->1xada"'
    set_value(lua_code_list, key, cheat_content)


# statDamage战斗统计伤害超出阈值倍率
def condition_16(lua_code_list):
    key = "battleResultArgs.statDamage"
    value = get_value(lua_code_list, key)

    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', value)

    # 将每个数字乘以1.5并取整
    new_numbers = [str(int(float(num) * 1.5)) for num in numbers]

    # 构建新的字符串
    cheat_content = re.sub(r'\d+', lambda match: new_numbers.pop(0), value)

    set_value(lua_code_list, key, cheat_content)


# statDamage战斗伤害不足
def condition_17(lua_code_list):
    key = "battleResultArgs.statDamage"
    value = get_value(lua_code_list, key)

    # 使用正则表达式提取数字
    numbers = re.findall(r'\d+', value)

    # 将每个数字乘以1.5并取整
    new_numbers = [str(int(float(num) * 0.5)) for num in numbers]

    # 构建新的字符串
    cheat_content = re.sub(r'\d+', lambda match: new_numbers.pop(0), value)

    set_value(lua_code_list, key, cheat_content)


# statUlt曝气统计序列有非法值
def condition_18(lua_code_list):
    key = "battleResultArgs.statUlt"
    cheat_content = '"->1xada"'
    set_value(lua_code_list, key, cheat_content)


# statUlt曝气统计序列验证失败
def condition_19(lua_code_list):
    key = "battleResultArgs.statUlt"
    value = get_value(lua_code_list, key)
    half_len = len(value) // 2
    cheat_content = value[half_len:] + value[:half_len]
    set_value(lua_code_list, key, cheat_content)






def main(bp: BasePage):
    cast_flag = cast(bp)
    # cast_flag = "1773175"
    hook_msg = get_hook_msg_template(cast_flag)
    condition_1(hook_msg)
    gen_digest(hook_msg)
    hook(bp, hook_msg)



if __name__ == '__main__':
    # constHash = "7d37951f4164f48a9de9e4a61e21df7f"
    bp = BasePage("192.168.111.80:20086")
    main(bp)
    bp.connect_close()




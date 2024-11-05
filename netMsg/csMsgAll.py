

# # categoryTpId: i32
def get_CSAchieveCategoryRewardMsg(addition_part="", categoryTpId: int = None):
    cmd_part = ''
    if categoryTpId is not None:
        arg = categoryTpId
        if isinstance(categoryTpId, str):
            arg = f'"{categoryTpId}"'
        if isinstance(categoryTpId, bool):
            arg = str(categoryTpId).lower()
        if isinstance(categoryTpId, list):
            arg = '{'
            for index, j in enumerate(categoryTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.categoryTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveCategoryRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # categoryTpId: i32, fishTpId: i32
def get_CSAchieveCategoryFishLightMsg(addition_part="", categoryTpId: int = None, fishTpId: int = None):
    cmd_part = ''
    if categoryTpId is not None:
        arg = categoryTpId
        if isinstance(categoryTpId, str):
            arg = f'"{categoryTpId}"'
        if isinstance(categoryTpId, bool):
            arg = str(categoryTpId).lower()
        if isinstance(categoryTpId, list):
            arg = '{'
            for index, j in enumerate(categoryTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.categoryTpId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveCategoryFishLightMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # categoryTpId: i32
def get_CSAchieveCategoryUnlockMsg(addition_part="", categoryTpId: int = None):
    cmd_part = ''
    if categoryTpId is not None:
        arg = categoryTpId
        if isinstance(categoryTpId, str):
            arg = f'"{categoryTpId}"'
        if isinstance(categoryTpId, bool):
            arg = str(categoryTpId).lower()
        if isinstance(categoryTpId, list):
            arg = '{'
            for index, j in enumerate(categoryTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.categoryTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveCategoryUnlockMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # wantedTpId: i32
def get_CSAchieveWantedRewardMsg(addition_part="", wantedTpId: int = None):
    cmd_part = ''
    if wantedTpId is not None:
        arg = wantedTpId
        if isinstance(wantedTpId, str):
            arg = f'"{wantedTpId}"'
        if isinstance(wantedTpId, bool):
            arg = str(wantedTpId).lower()
        if isinstance(wantedTpId, list):
            arg = '{'
            for index, j in enumerate(wantedTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.wantedTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveWantedRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # wantedTpId: i32, fishTpId: i32
def get_CSAchieveWantedFishLightMsg(addition_part="", wantedTpId: int = None, fishTpId: int = None):
    cmd_part = ''
    if wantedTpId is not None:
        arg = wantedTpId
        if isinstance(wantedTpId, str):
            arg = f'"{wantedTpId}"'
        if isinstance(wantedTpId, bool):
            arg = str(wantedTpId).lower()
        if isinstance(wantedTpId, list):
            arg = '{'
            for index, j in enumerate(wantedTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.wantedTpId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveWantedFishLightMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # wantedTpId: i32
def get_CSAchieveWantedUnlockMsg(addition_part="", wantedTpId: int = None):
    cmd_part = ''
    if wantedTpId is not None:
        arg = wantedTpId
        if isinstance(wantedTpId, str):
            arg = f'"{wantedTpId}"'
        if isinstance(wantedTpId, bool):
            arg = str(wantedTpId).lower()
        if isinstance(wantedTpId, list):
            arg = '{'
            for index, j in enumerate(wantedTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.wantedTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveWantedUnlockMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # achieveGroupTpId: i32, num: i32
def get_CSAchieveGroupRewardMsg(addition_part="", achieveGroupTpId: int = None, num: int = None):
    cmd_part = ''
    if achieveGroupTpId is not None:
        arg = achieveGroupTpId
        if isinstance(achieveGroupTpId, str):
            arg = f'"{achieveGroupTpId}"'
        if isinstance(achieveGroupTpId, bool):
            arg = str(achieveGroupTpId).lower()
        if isinstance(achieveGroupTpId, list):
            arg = '{'
            for index, j in enumerate(achieveGroupTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.achieveGroupTpId = {arg}\n'
        
    if num is not None:
        arg = num
        if isinstance(num, str):
            arg = f'"{num}"'
        if isinstance(num, bool):
            arg = str(num).lower()
        if isinstance(num, list):
            arg = '{'
            for index, j in enumerate(num):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.num = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveGroupRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # achieveGroupTpId: i32
def get_CSAchieveGroupUnlockMsg(addition_part="", achieveGroupTpId: int = None):
    cmd_part = ''
    if achieveGroupTpId is not None:
        arg = achieveGroupTpId
        if isinstance(achieveGroupTpId, str):
            arg = f'"{achieveGroupTpId}"'
        if isinstance(achieveGroupTpId, bool):
            arg = str(achieveGroupTpId).lower()
        if isinstance(achieveGroupTpId, list):
            arg = '{'
            for index, j in enumerate(achieveGroupTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.achieveGroupTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAchieveGroupUnlockMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # code: string
def get_CSActivationCodeUseMsg(addition_part="", code: str = None):
    cmd_part = ''
    if code is not None:
        arg = code
        if isinstance(code, str):
            arg = f'"{code}"'
        if isinstance(code, bool):
            arg = str(code).lower()
        if isinstance(code, list):
            arg = '{'
            for index, j in enumerate(code):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.code = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSActivationCodeUseMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # advertId: i32
def get_CSAdBeginViewMsg(addition_part="", advertId: int = None):
    cmd_part = ''
    if advertId is not None:
        arg = advertId
        if isinstance(advertId, str):
            arg = f'"{advertId}"'
        if isinstance(advertId, bool):
            arg = str(advertId).lower()
        if isinstance(advertId, list):
            arg = '{'
            for index, j in enumerate(advertId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.advertId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAdBeginViewMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, lv: i32
def get_CSAquariumProsperityLvUpMsg(addition_part="", tpId: int = None, lv: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if lv is not None:
        arg = lv
        if isinstance(lv, str):
            arg = f'"{lv}"'
        if isinstance(lv, bool):
            arg = str(lv).lower()
        if isinstance(lv, list):
            arg = '{'
            for index, j in enumerate(lv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.lv = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumProsperityLvUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, buildingTpId: i32
def get_CSAquariumBuildingUpLvMsg(addition_part="", tpId: int = None, buildingTpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if buildingTpId is not None:
        arg = buildingTpId
        if isinstance(buildingTpId, str):
            arg = f'"{buildingTpId}"'
        if isinstance(buildingTpId, bool):
            arg = str(buildingTpId).lower()
        if isinstance(buildingTpId, list):
            arg = '{'
            for index, j in enumerate(buildingTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.buildingTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumBuildingUpLvMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, buildingTpId: i32, skinTpId: i32
def get_CSAquariumBuildingChangeSkinMsg(addition_part="", tpId: int = None, buildingTpId: int = None, skinTpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if buildingTpId is not None:
        arg = buildingTpId
        if isinstance(buildingTpId, str):
            arg = f'"{buildingTpId}"'
        if isinstance(buildingTpId, bool):
            arg = str(buildingTpId).lower()
        if isinstance(buildingTpId, list):
            arg = '{'
            for index, j in enumerate(buildingTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.buildingTpId = {arg}\n'
        
    if skinTpId is not None:
        arg = skinTpId
        if isinstance(skinTpId, str):
            arg = f'"{skinTpId}"'
        if isinstance(skinTpId, bool):
            arg = str(skinTpId).lower()
        if isinstance(skinTpId, list):
            arg = '{'
            for index, j in enumerate(skinTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.skinTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumBuildingChangeSkinMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, mFishTpId: i32, ornamentalFishTpId: i32
def get_CSAquariumPutFishMsg(addition_part="", tpId: int = None, mFishTpId: int = None, ornamentalFishTpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if mFishTpId is not None:
        arg = mFishTpId
        if isinstance(mFishTpId, str):
            arg = f'"{mFishTpId}"'
        if isinstance(mFishTpId, bool):
            arg = str(mFishTpId).lower()
        if isinstance(mFishTpId, list):
            arg = '{'
            for index, j in enumerate(mFishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.mFishTpId = {arg}\n'
        
    if ornamentalFishTpId is not None:
        arg = ornamentalFishTpId
        if isinstance(ornamentalFishTpId, str):
            arg = f'"{ornamentalFishTpId}"'
        if isinstance(ornamentalFishTpId, bool):
            arg = str(ornamentalFishTpId).lower()
        if isinstance(ornamentalFishTpId, list):
            arg = '{'
            for index, j in enumerate(ornamentalFishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ornamentalFishTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumPutFishMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, mFishTpId: i32, ornamentalFishTpId: i32
def get_CSAquariumRemoveFishMsg(addition_part="", tpId: int = None, mFishTpId: int = None, ornamentalFishTpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if mFishTpId is not None:
        arg = mFishTpId
        if isinstance(mFishTpId, str):
            arg = f'"{mFishTpId}"'
        if isinstance(mFishTpId, bool):
            arg = str(mFishTpId).lower()
        if isinstance(mFishTpId, list):
            arg = '{'
            for index, j in enumerate(mFishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.mFishTpId = {arg}\n'
        
    if ornamentalFishTpId is not None:
        arg = ornamentalFishTpId
        if isinstance(ornamentalFishTpId, str):
            arg = f'"{ornamentalFishTpId}"'
        if isinstance(ornamentalFishTpId, bool):
            arg = str(ornamentalFishTpId).lower()
        if isinstance(ornamentalFishTpId, list):
            arg = '{'
            for index, j in enumerate(ornamentalFishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ornamentalFishTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumRemoveFishMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, ornamentalFishTpId: i32
def get_CSAquariumBuyOrnamentalFishMsg(addition_part="", tpId: int = None, ornamentalFishTpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if ornamentalFishTpId is not None:
        arg = ornamentalFishTpId
        if isinstance(ornamentalFishTpId, str):
            arg = f'"{ornamentalFishTpId}"'
        if isinstance(ornamentalFishTpId, bool):
            arg = str(ornamentalFishTpId).lower()
        if isinstance(ornamentalFishTpId, list):
            arg = '{'
            for index, j in enumerate(ornamentalFishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ornamentalFishTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumBuyOrnamentalFishMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSAquariumRemoveAllFishMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumRemoveAllFishMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32, fishTpId: i32
def get_CSAquariumFeedFishMsg(addition_part="", tpId: int = None, fishTpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumFeedFishMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSAquariumSwitchMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumSwitchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSAquariumSeeHangUpRewardMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumSeeHangUpRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSAquariumHangUpRewardMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumHangUpRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSAquariumSurpriseRewardMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumSurpriseRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSAquariumSeeFishChangeMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSAquariumSeeFishChangeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # itemType: i32, itemTpId: i32, useTimes: i32, extArgs: list<string>, customArgs: list<i32>
def get_CSUseItemMsg(addition_part="", itemType: int = None, itemTpId: int = None, useTimes: int = None, extArgs: list = None, customArgs: list = None):
    cmd_part = ''
    if itemType is not None:
        arg = itemType
        if isinstance(itemType, str):
            arg = f'"{itemType}"'
        if isinstance(itemType, bool):
            arg = str(itemType).lower()
        if isinstance(itemType, list):
            arg = '{'
            for index, j in enumerate(itemType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemType = {arg}\n'
        
    if itemTpId is not None:
        arg = itemTpId
        if isinstance(itemTpId, str):
            arg = f'"{itemTpId}"'
        if isinstance(itemTpId, bool):
            arg = str(itemTpId).lower()
        if isinstance(itemTpId, list):
            arg = '{'
            for index, j in enumerate(itemTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemTpId = {arg}\n'
        
    if useTimes is not None:
        arg = useTimes
        if isinstance(useTimes, str):
            arg = f'"{useTimes}"'
        if isinstance(useTimes, bool):
            arg = str(useTimes).lower()
        if isinstance(useTimes, list):
            arg = '{'
            for index, j in enumerate(useTimes):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.useTimes = {arg}\n'
        
    if extArgs is not None:
        arg = extArgs
        if isinstance(extArgs, str):
            arg = f'"{extArgs}"'
        if isinstance(extArgs, bool):
            arg = str(extArgs).lower()
        if isinstance(extArgs, list):
            arg = '{'
            for index, j in enumerate(extArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.extArgs = {arg}\n'
        
    if customArgs is not None:
        arg = customArgs
        if isinstance(customArgs, str):
            arg = f'"{customArgs}"'
        if isinstance(customArgs, bool):
            arg = str(customArgs).lower()
        if isinstance(customArgs, list):
            arg = '{'
            for index, j in enumerate(customArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.customArgs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSUseItemMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # useList: list<backPack_struct.UseItem>
def get_CSBatchUseItemMsg(addition_part="", useList: list = None):
    cmd_part = ''
    if useList is not None:
        arg = useList
        if isinstance(useList, str):
            arg = f'"{useList}"'
        if isinstance(useList, bool):
            arg = str(useList).lower()
        if isinstance(useList, list):
            arg = '{'
            for index, j in enumerate(useList):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.useList = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBatchUseItemMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, itemType: i32, itemTpId: i32, count: i32, priceTpId: i32
def get_CSBuyItemMsg(addition_part="", source: int = None, itemType: int = None, itemTpId: int = None, count: int = None, priceTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if itemType is not None:
        arg = itemType
        if isinstance(itemType, str):
            arg = f'"{itemType}"'
        if isinstance(itemType, bool):
            arg = str(itemType).lower()
        if isinstance(itemType, list):
            arg = '{'
            for index, j in enumerate(itemType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemType = {arg}\n'
        
    if itemTpId is not None:
        arg = itemTpId
        if isinstance(itemTpId, str):
            arg = f'"{itemTpId}"'
        if isinstance(itemTpId, bool):
            arg = str(itemTpId).lower()
        if isinstance(itemTpId, list):
            arg = '{'
            for index, j in enumerate(itemTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemTpId = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    if priceTpId is not None:
        arg = priceTpId
        if isinstance(priceTpId, str):
            arg = f'"{priceTpId}"'
        if isinstance(priceTpId, bool):
            arg = str(priceTpId).lower()
        if isinstance(priceTpId, list):
            arg = '{'
            for index, j in enumerate(priceTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.priceTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBuyItemMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, itemType: i32, itemTpId: i32, count: i32
def get_CSSellItemMsg(addition_part="", source: int = None, itemType: int = None, itemTpId: int = None, count: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if itemType is not None:
        arg = itemType
        if isinstance(itemType, str):
            arg = f'"{itemType}"'
        if isinstance(itemType, bool):
            arg = str(itemType).lower()
        if isinstance(itemType, list):
            arg = '{'
            for index, j in enumerate(itemType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemType = {arg}\n'
        
    if itemTpId is not None:
        arg = itemTpId
        if isinstance(itemTpId, str):
            arg = f'"{itemTpId}"'
        if isinstance(itemTpId, bool):
            arg = str(itemTpId).lower()
        if isinstance(itemTpId, list):
            arg = '{'
            for index, j in enumerate(itemTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemTpId = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSellItemMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, itemType: i32, itemTpId: i32
def get_CSOpenItemMsg(addition_part="", source: int = None, itemType: int = None, itemTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if itemType is not None:
        arg = itemType
        if isinstance(itemType, str):
            arg = f'"{itemType}"'
        if isinstance(itemType, bool):
            arg = str(itemType).lower()
        if isinstance(itemType, list):
            arg = '{'
            for index, j in enumerate(itemType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemType = {arg}\n'
        
    if itemTpId is not None:
        arg = itemTpId
        if isinstance(itemTpId, str):
            arg = f'"{itemTpId}"'
        if isinstance(itemTpId, bool):
            arg = str(itemTpId).lower()
        if isinstance(itemTpId, list):
            arg = '{'
            for index, j in enumerate(itemTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSOpenItemMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32
def get_CSBaitAndRodComposeMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodComposeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32
def get_CSBaitAndRodLevelUpMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodLevelUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32, targetLevel: i32
def get_CSBaitAndRodLevelUpToMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None, targetLevel: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if targetLevel is not None:
        arg = targetLevel
        if isinstance(targetLevel, str):
            arg = f'"{targetLevel}"'
        if isinstance(targetLevel, bool):
            arg = str(targetLevel).lower()
        if isinstance(targetLevel, list):
            arg = '{'
            for index, j in enumerate(targetLevel):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetLevel = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodLevelUpToMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32, idx: i32
def get_CSBaitAndRodGenEffectMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None, idx: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if idx is not None:
        arg = idx
        if isinstance(idx, str):
            arg = f'"{idx}"'
        if isinstance(idx, bool):
            arg = str(idx).lower()
        if isinstance(idx, list):
            arg = '{'
            for index, j in enumerate(idx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.idx = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodGenEffectMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32, idx: i32
def get_CSBaitAndRodGenEffectConfirmMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None, idx: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if idx is not None:
        arg = idx
        if isinstance(idx, str):
            arg = f'"{idx}"'
        if isinstance(idx, bool):
            arg = str(idx).lower()
        if isinstance(idx, list):
            arg = '{'
            for index, j in enumerate(idx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.idx = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodGenEffectConfirmMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32, idx: i32, times: i32
def get_CSBaitAndRodWashMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None, idx: int = None, times: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if idx is not None:
        arg = idx
        if isinstance(idx, str):
            arg = f'"{idx}"'
        if isinstance(idx, bool):
            arg = str(idx).lower()
        if isinstance(idx, list):
            arg = '{'
            for index, j in enumerate(idx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.idx = {arg}\n'
        
    if times is not None:
        arg = times
        if isinstance(times, str):
            arg = f'"{times}"'
        if isinstance(times, bool):
            arg = str(times).lower()
        if isinstance(times, list):
            arg = '{'
            for index, j in enumerate(times):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.times = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodWashMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32
def get_CSBaitAndRodStarLevelUpMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodStarLevelUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, ioIdType: i32, tpId: i32, idx: i32, effectIdx: i32
def get_CSBaitAndRodStarChooseMsg(addition_part="", source: int = None, ioIdType: int = None, tpId: int = None, idx: int = None, effectIdx: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if idx is not None:
        arg = idx
        if isinstance(idx, str):
            arg = f'"{idx}"'
        if isinstance(idx, bool):
            arg = str(idx).lower()
        if isinstance(idx, list):
            arg = '{'
            for index, j in enumerate(idx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.idx = {arg}\n'
        
    if effectIdx is not None:
        arg = effectIdx
        if isinstance(effectIdx, str):
            arg = f'"{effectIdx}"'
        if isinstance(effectIdx, bool):
            arg = str(effectIdx).lower()
        if isinstance(effectIdx, list):
            arg = '{'
            for index, j in enumerate(effectIdx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.effectIdx = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBaitAndRodStarChooseMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, lv: i32, pay: bool
def get_CSBattlePassGetRewardMsg(addition_part="", groupId: int = None, lv: int = None, pay: bool = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if lv is not None:
        arg = lv
        if isinstance(lv, str):
            arg = f'"{lv}"'
        if isinstance(lv, bool):
            arg = str(lv).lower()
        if isinstance(lv, list):
            arg = '{'
            for index, j in enumerate(lv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.lv = {arg}\n'
        
    if pay is not None:
        arg = pay
        if isinstance(pay, str):
            arg = f'"{pay}"'
        if isinstance(pay, bool):
            arg = str(pay).lower()
        if isinstance(pay, list):
            arg = '{'
            for index, j in enumerate(pay):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.pay = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBattlePassGetRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32
def get_CSBattlePassGetAllRewardMsg(addition_part="", groupId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBattlePassGetAllRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSQueryChallengeRankMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryChallengeRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSQueryChallengeSelfRankMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryChallengeSelfRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSQueryChampionshipsRankMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryChampionshipsRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, road: i32, championshipsId: i32, endTime: i64, slv: i32, limitedPlaySpotId: i32
def get_CSChampionshipsBeginLimitedPlayMsg(addition_part="", source: int = None, road: int = None, championshipsId: int = None, endTime: int = None, slv: int = None, limitedPlaySpotId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if road is not None:
        arg = road
        if isinstance(road, str):
            arg = f'"{road}"'
        if isinstance(road, bool):
            arg = str(road).lower()
        if isinstance(road, list):
            arg = '{'
            for index, j in enumerate(road):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.road = {arg}\n'
        
    if championshipsId is not None:
        arg = championshipsId
        if isinstance(championshipsId, str):
            arg = f'"{championshipsId}"'
        if isinstance(championshipsId, bool):
            arg = str(championshipsId).lower()
        if isinstance(championshipsId, list):
            arg = '{'
            for index, j in enumerate(championshipsId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.championshipsId = {arg}\n'
        
    if endTime is not None:
        arg = endTime
        if isinstance(endTime, str):
            arg = f'"{endTime}"'
        if isinstance(endTime, bool):
            arg = str(endTime).lower()
        if isinstance(endTime, list):
            arg = '{'
            for index, j in enumerate(endTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.endTime = {arg}\n'
        
    if slv is not None:
        arg = slv
        if isinstance(slv, str):
            arg = f'"{slv}"'
        if isinstance(slv, bool):
            arg = str(slv).lower()
        if isinstance(slv, list):
            arg = '{'
            for index, j in enumerate(slv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.slv = {arg}\n'
        
    if limitedPlaySpotId is not None:
        arg = limitedPlaySpotId
        if isinstance(limitedPlaySpotId, str):
            arg = f'"{limitedPlaySpotId}"'
        if isinstance(limitedPlaySpotId, bool):
            arg = str(limitedPlaySpotId).lower()
        if isinstance(limitedPlaySpotId, list):
            arg = '{'
            for index, j in enumerate(limitedPlaySpotId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.limitedPlaySpotId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChampionshipsBeginLimitedPlayMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, road: i32, championshipsId: i32, endTime: i64, slv: i32
def get_CSChampionshipsQueryLimitedPlayInfoMsg(addition_part="", source: int = None, road: int = None, championshipsId: int = None, endTime: int = None, slv: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if road is not None:
        arg = road
        if isinstance(road, str):
            arg = f'"{road}"'
        if isinstance(road, bool):
            arg = str(road).lower()
        if isinstance(road, list):
            arg = '{'
            for index, j in enumerate(road):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.road = {arg}\n'
        
    if championshipsId is not None:
        arg = championshipsId
        if isinstance(championshipsId, str):
            arg = f'"{championshipsId}"'
        if isinstance(championshipsId, bool):
            arg = str(championshipsId).lower()
        if isinstance(championshipsId, list):
            arg = '{'
            for index, j in enumerate(championshipsId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.championshipsId = {arg}\n'
        
    if endTime is not None:
        arg = endTime
        if isinstance(endTime, str):
            arg = f'"{endTime}"'
        if isinstance(endTime, bool):
            arg = str(endTime).lower()
        if isinstance(endTime, list):
            arg = '{'
            for index, j in enumerate(endTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.endTime = {arg}\n'
        
    if slv is not None:
        arg = slv
        if isinstance(slv, str):
            arg = f'"{slv}"'
        if isinstance(slv, bool):
            arg = str(slv).lower()
        if isinstance(slv, list):
            arg = '{'
            for index, j in enumerate(slv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.slv = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChampionshipsQueryLimitedPlayInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, road: i32, championshipsId: i32, endTime: i64, slv: i32
def get_CSChampionshipsGetUnGetRewardsMsg(addition_part="", source: int = None, road: int = None, championshipsId: int = None, endTime: int = None, slv: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if road is not None:
        arg = road
        if isinstance(road, str):
            arg = f'"{road}"'
        if isinstance(road, bool):
            arg = str(road).lower()
        if isinstance(road, list):
            arg = '{'
            for index, j in enumerate(road):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.road = {arg}\n'
        
    if championshipsId is not None:
        arg = championshipsId
        if isinstance(championshipsId, str):
            arg = f'"{championshipsId}"'
        if isinstance(championshipsId, bool):
            arg = str(championshipsId).lower()
        if isinstance(championshipsId, list):
            arg = '{'
            for index, j in enumerate(championshipsId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.championshipsId = {arg}\n'
        
    if endTime is not None:
        arg = endTime
        if isinstance(endTime, str):
            arg = f'"{endTime}"'
        if isinstance(endTime, bool):
            arg = str(endTime).lower()
        if isinstance(endTime, list):
            arg = '{'
            for index, j in enumerate(endTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.endTime = {arg}\n'
        
    if slv is not None:
        arg = slv
        if isinstance(slv, str):
            arg = f'"{slv}"'
        if isinstance(slv, bool):
            arg = str(slv).lower()
        if isinstance(slv, list):
            arg = '{'
            for index, j in enumerate(slv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.slv = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChampionshipsGetUnGetRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # newName: string
def get_CSCharaRenameMsg(addition_part="", newName: str = None):
    cmd_part = ''
    if newName is not None:
        arg = newName
        if isinstance(newName, str):
            arg = f'"{newName}"'
        if isinstance(newName, bool):
            arg = str(newName).lower()
        if isinstance(newName, list):
            arg = '{'
            for index, j in enumerate(newName):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.newName = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaRenameMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # icon: i32
def get_CSCharaSetIconMsg(addition_part="", icon: int = None):
    cmd_part = ''
    if icon is not None:
        arg = icon
        if isinstance(icon, str):
            arg = f'"{icon}"'
        if isinstance(icon, bool):
            arg = str(icon).lower()
        if isinstance(icon, list):
            arg = '{'
            for index, j in enumerate(icon):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.icon = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaSetIconMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # iconBox: i32
def get_CSCharaSetIconBoxMsg(addition_part="", iconBox: int = None):
    cmd_part = ''
    if iconBox is not None:
        arg = iconBox
        if isinstance(iconBox, str):
            arg = f'"{iconBox}"'
        if isinstance(iconBox, bool):
            arg = str(iconBox).lower()
        if isinstance(iconBox, list):
            arg = '{'
            for index, j in enumerate(iconBox):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.iconBox = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaSetIconBoxMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # sex: i32
def get_CSCharaSetSexMsg(addition_part="", sex: int = None):
    cmd_part = ''
    if sex is not None:
        arg = sex
        if isinstance(sex, str):
            arg = f'"{sex}"'
        if isinstance(sex, bool):
            arg = str(sex).lower()
        if isinstance(sex, list):
            arg = '{'
            for index, j in enumerate(sex):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sex = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaSetSexMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # sign: string
def get_CSCharaSetSignMsg(addition_part="", sign: str = None):
    cmd_part = ''
    if sign is not None:
        arg = sign
        if isinstance(sign, str):
            arg = f'"{sign}"'
        if isinstance(sign, bool):
            arg = str(sign).lower()
        if isinstance(sign, list):
            arg = '{'
            for index, j in enumerate(sign):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sign = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaSetSignMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # lang: i32
def get_CSCharaSetLangMsg(addition_part="", lang: int = None):
    cmd_part = ''
    if lang is not None:
        arg = lang
        if isinstance(lang, str):
            arg = f'"{lang}"'
        if isinstance(lang, bool):
            arg = str(lang).lower()
        if isinstance(lang, list):
            arg = '{'
            for index, j in enumerate(lang):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.lang = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaSetLangMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # vipLv: i32
def get_CSCharaGetVipGiftMsg(addition_part="", vipLv: int = None):
    cmd_part = ''
    if vipLv is not None:
        arg = vipLv
        if isinstance(vipLv, str):
            arg = f'"{vipLv}"'
        if isinstance(vipLv, bool):
            arg = str(vipLv).lower()
        if isinstance(vipLv, list):
            arg = '{'
            for index, j in enumerate(vipLv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.vipLv = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaGetVipGiftMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tuYouUerId: i64
def get_CSUnbindThirdPartySdkMsg(addition_part="", tuYouUerId: int = None):
    cmd_part = ''
    if tuYouUerId is not None:
        arg = tuYouUerId
        if isinstance(tuYouUerId, str):
            arg = f'"{tuYouUerId}"'
        if isinstance(tuYouUerId, bool):
            arg = str(tuYouUerId).lower()
        if isinstance(tuYouUerId, list):
            arg = '{'
            for index, j in enumerate(tuYouUerId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tuYouUerId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSUnbindThirdPartySdkMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # id: i64
def get_CSCharaReceiveUnGetRewardsMsg(addition_part="", id: int = None):
    cmd_part = ''
    if id is not None:
        arg = id
        if isinstance(id, str):
            arg = f'"{id}"'
        if isinstance(id, bool):
            arg = str(id).lower()
        if isinstance(id, list):
            arg = '{'
            for index, j in enumerate(id):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.id = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCharaReceiveUnGetRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSSetPlayerSourceTypeMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSetPlayerSourceTypeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # nationalFlag: string
def get_CSSetPlayerNationalFlagMsg(addition_part="", nationalFlag: str = None):
    cmd_part = ''
    if nationalFlag is not None:
        arg = nationalFlag
        if isinstance(nationalFlag, str):
            arg = f'"{nationalFlag}"'
        if isinstance(nationalFlag, bool):
            arg = str(nationalFlag).lower()
        if isinstance(nationalFlag, list):
            arg = '{'
            for index, j in enumerate(nationalFlag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.nationalFlag = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSetPlayerNationalFlagMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fbIconUrl: string
def get_CSSetPlayerFbIconUrlMsg(addition_part="", fbIconUrl: str = None):
    cmd_part = ''
    if fbIconUrl is not None:
        arg = fbIconUrl
        if isinstance(fbIconUrl, str):
            arg = f'"{fbIconUrl}"'
        if isinstance(fbIconUrl, bool):
            arg = str(fbIconUrl).lower()
        if isinstance(fbIconUrl, list):
            arg = '{'
            for index, j in enumerate(fbIconUrl):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fbIconUrl = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSetPlayerFbIconUrlMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # index: i32, badge: i32
def get_CSSetPlayerBadgeMsg(addition_part="", index: int = None, badge: int = None):
    cmd_part = ''
    if index is not None:
        arg = index
        if isinstance(index, str):
            arg = f'"{index}"'
        if isinstance(index, bool):
            arg = str(index).lower()
        if isinstance(index, list):
            arg = '{'
            for index, j in enumerate(index):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.index = {arg}\n'
        
    if badge is not None:
        arg = badge
        if isinstance(badge, str):
            arg = f'"{badge}"'
        if isinstance(badge, bool):
            arg = str(badge).lower()
        if isinstance(badge, list):
            arg = '{'
            for index, j in enumerate(badge):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.badge = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSetPlayerBadgeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # charId: string, source: i8, name: string, icon: i32
def get_CSQueryPlayerCardInfoMsg(addition_part="", charId: str = None, source: int = None, name: str = None, icon: int = None):
    cmd_part = ''
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if name is not None:
        arg = name
        if isinstance(name, str):
            arg = f'"{name}"'
        if isinstance(name, bool):
            arg = str(name).lower()
        if isinstance(name, list):
            arg = '{'
            for index, j in enumerate(name):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.name = {arg}\n'
        
    if icon is not None:
        arg = icon
        if isinstance(icon, str):
            arg = f'"{icon}"'
        if isinstance(icon, bool):
            arg = str(icon).lower()
        if isinstance(icon, list):
            arg = '{'
            for index, j in enumerate(icon):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.icon = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryPlayerCardInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # indexToBadge: map<i32,i32>
def get_CSSetPlayerBadgeAllMsg(addition_part="", indexToBadge: dict = None):
    cmd_part = ''
    if indexToBadge is not None:
        arg = indexToBadge
        if isinstance(indexToBadge, str):
            arg = f'"{indexToBadge}"'
        if isinstance(indexToBadge, bool):
            arg = str(indexToBadge).lower()
        if isinstance(indexToBadge, list):
            arg = '{'
            for index, j in enumerate(indexToBadge):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.indexToBadge = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSetPlayerBadgeAllMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i8, params: list<string>
def get_CSQueryPlayerAvatarShowMsg(addition_part="", source: int = None, params: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if params is not None:
        arg = params
        if isinstance(params, str):
            arg = f'"{params}"'
        if isinstance(params, bool):
            arg = str(params).lower()
        if isinstance(params, list):
            arg = '{'
            for index, j in enumerate(params):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.params = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryPlayerAvatarShowMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSChatLoginMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChatLoginMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # clientTime: double
def get_CSChatPingMsg(addition_part="", clientTime: float = None):
    cmd_part = ''
    if clientTime is not None:
        arg = clientTime
        if isinstance(clientTime, str):
            arg = f'"{clientTime}"'
        if isinstance(clientTime, bool):
            arg = str(clientTime).lower()
        if isinstance(clientTime, list):
            arg = '{'
            for index, j in enumerate(clientTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientTime = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChatPingMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, channelId: i64, content: string, charIdB: string, charSimpleB: i64, otherArgs: list<string>
def get_CSChatSendContentMsg(addition_part="", source: int = None, channelId: int = None, content: str = None, charIdB: str = None, charSimpleB: int = None, otherArgs: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if channelId is not None:
        arg = channelId
        if isinstance(channelId, str):
            arg = f'"{channelId}"'
        if isinstance(channelId, bool):
            arg = str(channelId).lower()
        if isinstance(channelId, list):
            arg = '{'
            for index, j in enumerate(channelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.channelId = {arg}\n'
        
    if content is not None:
        arg = content
        if isinstance(content, str):
            arg = f'"{content}"'
        if isinstance(content, bool):
            arg = str(content).lower()
        if isinstance(content, list):
            arg = '{'
            for index, j in enumerate(content):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.content = {arg}\n'
        
    if charIdB is not None:
        arg = charIdB
        if isinstance(charIdB, str):
            arg = f'"{charIdB}"'
        if isinstance(charIdB, bool):
            arg = str(charIdB).lower()
        if isinstance(charIdB, list):
            arg = '{'
            for index, j in enumerate(charIdB):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charIdB = {arg}\n'
        
    if charSimpleB is not None:
        arg = charSimpleB
        if isinstance(charSimpleB, str):
            arg = f'"{charSimpleB}"'
        if isinstance(charSimpleB, bool):
            arg = str(charSimpleB).lower()
        if isinstance(charSimpleB, list):
            arg = '{'
            for index, j in enumerate(charSimpleB):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charSimpleB = {arg}\n'
        
    if otherArgs is not None:
        arg = otherArgs
        if isinstance(otherArgs, str):
            arg = f'"{otherArgs}"'
        if isinstance(otherArgs, bool):
            arg = str(otherArgs).lower()
        if isinstance(otherArgs, list):
            arg = '{'
            for index, j in enumerate(otherArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.otherArgs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChatSendContentMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, channelId: i64, msgNo: i64
def get_CSChatSyncContentMsg(addition_part="", source: int = None, channelId: int = None, msgNo: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if channelId is not None:
        arg = channelId
        if isinstance(channelId, str):
            arg = f'"{channelId}"'
        if isinstance(channelId, bool):
            arg = str(channelId).lower()
        if isinstance(channelId, list):
            arg = '{'
            for index, j in enumerate(channelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.channelId = {arg}\n'
        
    if msgNo is not None:
        arg = msgNo
        if isinstance(msgNo, str):
            arg = f'"{msgNo}"'
        if isinstance(msgNo, bool):
            arg = str(msgNo).lower()
        if isinstance(msgNo, list):
            arg = '{'
            for index, j in enumerate(msgNo):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.msgNo = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChatSyncContentMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, channelIdToMaxMsgNo: map<i64, i64>
def get_CSChatSyncPrivateContentMsg(addition_part="", source: int = None, channelIdToMaxMsgNo: dict = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if channelIdToMaxMsgNo is not None:
        arg = channelIdToMaxMsgNo
        if isinstance(channelIdToMaxMsgNo, str):
            arg = f'"{channelIdToMaxMsgNo}"'
        if isinstance(channelIdToMaxMsgNo, bool):
            arg = str(channelIdToMaxMsgNo).lower()
        if isinstance(channelIdToMaxMsgNo, list):
            arg = '{'
            for index, j in enumerate(channelIdToMaxMsgNo):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.channelIdToMaxMsgNo = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChatSyncPrivateContentMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, arg1: string, arg2: i32
def get_CSChatSelectChannelMsg(addition_part="", source: int = None, arg1: str = None, arg2: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if arg1 is not None:
        arg = arg1
        if isinstance(arg1, str):
            arg = f'"{arg1}"'
        if isinstance(arg1, bool):
            arg = str(arg1).lower()
        if isinstance(arg1, list):
            arg = '{'
            for index, j in enumerate(arg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.arg1 = {arg}\n'
        
    if arg2 is not None:
        arg = arg2
        if isinstance(arg2, str):
            arg = f'"{arg2}"'
        if isinstance(arg2, bool):
            arg = str(arg2).lower()
        if isinstance(arg2, list):
            arg = '{'
            for index, j in enumerate(arg2):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.arg2 = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSChatSelectChannelMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, arg1: string, arg2: string
def get_CSTryEnterChannelMsg(addition_part="", source: int = None, arg1: str = None, arg2: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if arg1 is not None:
        arg = arg1
        if isinstance(arg1, str):
            arg = f'"{arg1}"'
        if isinstance(arg1, bool):
            arg = str(arg1).lower()
        if isinstance(arg1, list):
            arg = '{'
            for index, j in enumerate(arg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.arg1 = {arg}\n'
        
    if arg2 is not None:
        arg = arg2
        if isinstance(arg2, str):
            arg = f'"{arg2}"'
        if isinstance(arg2, bool):
            arg = str(arg2).lower()
        if isinstance(arg2, list):
            arg = '{'
            for index, j in enumerate(arg2):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.arg2 = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSTryEnterChannelMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # chestPointId: i32
def get_CSGetChestRewardsMsg(addition_part="", chestPointId: int = None):
    cmd_part = ''
    if chestPointId is not None:
        arg = chestPointId
        if isinstance(chestPointId, str):
            arg = f'"{chestPointId}"'
        if isinstance(chestPointId, bool):
            arg = str(chestPointId).lower()
        if isinstance(chestPointId, list):
            arg = '{'
            for index, j in enumerate(chestPointId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.chestPointId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGetChestRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # itemTpId: i32, count: i32
def get_CSOpenChestMsg(addition_part="", itemTpId: int = None, count: int = None):
    cmd_part = ''
    if itemTpId is not None:
        arg = itemTpId
        if isinstance(itemTpId, str):
            arg = f'"{itemTpId}"'
        if isinstance(itemTpId, bool):
            arg = str(itemTpId).lower()
        if isinstance(itemTpId, list):
            arg = '{'
            for index, j in enumerate(itemTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.itemTpId = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSOpenChestMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # exchangeId: i32, buyTimes: i32
def get_CSCommonExchangeMsg(addition_part="", exchangeId: int = None, buyTimes: int = None):
    cmd_part = ''
    if exchangeId is not None:
        arg = exchangeId
        if isinstance(exchangeId, str):
            arg = f'"{exchangeId}"'
        if isinstance(exchangeId, bool):
            arg = str(exchangeId).lower()
        if isinstance(exchangeId, list):
            arg = '{'
            for index, j in enumerate(exchangeId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.exchangeId = {arg}\n'
        
    if buyTimes is not None:
        arg = buyTimes
        if isinstance(buyTimes, str):
            arg = f'"{buyTimes}"'
        if isinstance(buyTimes, bool):
            arg = str(buyTimes).lower()
        if isinstance(buyTimes, list):
            arg = '{'
            for index, j in enumerate(buyTimes):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.buyTimes = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCommonExchangeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # applyType: i32, simpleCharId: i64, charId: string, sourceType: i32, guildSimpleId: i64
def get_CSCooperateApplyMsg(addition_part="", applyType: int = None, simpleCharId: int = None, charId: str = None, sourceType: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if applyType is not None:
        arg = applyType
        if isinstance(applyType, str):
            arg = f'"{applyType}"'
        if isinstance(applyType, bool):
            arg = str(applyType).lower()
        if isinstance(applyType, list):
            arg = '{'
            for index, j in enumerate(applyType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.applyType = {arg}\n'
        
    if simpleCharId is not None:
        arg = simpleCharId
        if isinstance(simpleCharId, str):
            arg = f'"{simpleCharId}"'
        if isinstance(simpleCharId, bool):
            arg = str(simpleCharId).lower()
        if isinstance(simpleCharId, list):
            arg = '{'
            for index, j in enumerate(simpleCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleCharId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    if sourceType is not None:
        arg = sourceType
        if isinstance(sourceType, str):
            arg = f'"{sourceType}"'
        if isinstance(sourceType, bool):
            arg = str(sourceType).lower()
        if isinstance(sourceType, list):
            arg = '{'
            for index, j in enumerate(sourceType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sourceType = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # acceptType: i32, simpleCharId: i64, charId: string, sourceType: i32
def get_CSCooperateAcceptMsg(addition_part="", acceptType: int = None, simpleCharId: int = None, charId: str = None, sourceType: int = None):
    cmd_part = ''
    if acceptType is not None:
        arg = acceptType
        if isinstance(acceptType, str):
            arg = f'"{acceptType}"'
        if isinstance(acceptType, bool):
            arg = str(acceptType).lower()
        if isinstance(acceptType, list):
            arg = '{'
            for index, j in enumerate(acceptType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.acceptType = {arg}\n'
        
    if simpleCharId is not None:
        arg = simpleCharId
        if isinstance(simpleCharId, str):
            arg = f'"{simpleCharId}"'
        if isinstance(simpleCharId, bool):
            arg = str(simpleCharId).lower()
        if isinstance(simpleCharId, list):
            arg = '{'
            for index, j in enumerate(simpleCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleCharId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    if sourceType is not None:
        arg = sourceType
        if isinstance(sourceType, str):
            arg = f'"{sourceType}"'
        if isinstance(sourceType, bool):
            arg = str(sourceType).lower()
        if isinstance(sourceType, list):
            arg = '{'
            for index, j in enumerate(sourceType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sourceType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateAcceptMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # onlyScoreChange: bool
def get_CSCooperateInfoMsg(addition_part="", onlyScoreChange: bool = None):
    cmd_part = ''
    if onlyScoreChange is not None:
        arg = onlyScoreChange
        if isinstance(onlyScoreChange, str):
            arg = f'"{onlyScoreChange}"'
        if isinstance(onlyScoreChange, bool):
            arg = str(onlyScoreChange).lower()
        if isinstance(onlyScoreChange, list):
            arg = '{'
            for index, j in enumerate(onlyScoreChange):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.onlyScoreChange = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # index: i32, spinLevel: i32
def get_CSCooperateSpinMsg(addition_part="", index: int = None, spinLevel: int = None):
    cmd_part = ''
    if index is not None:
        arg = index
        if isinstance(index, str):
            arg = f'"{index}"'
        if isinstance(index, bool):
            arg = str(index).lower()
        if isinstance(index, list):
            arg = '{'
            for index, j in enumerate(index):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.index = {arg}\n'
        
    if spinLevel is not None:
        arg = spinLevel
        if isinstance(spinLevel, str):
            arg = f'"{spinLevel}"'
        if isinstance(spinLevel, bool):
            arg = str(spinLevel).lower()
        if isinstance(spinLevel, list):
            arg = '{'
            for index, j in enumerate(spinLevel):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.spinLevel = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateSpinMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # index: i32
def get_CSCooperateRewardMsg(addition_part="", index: int = None):
    cmd_part = ''
    if index is not None:
        arg = index
        if isinstance(index, str):
            arg = f'"{index}"'
        if isinstance(index, bool):
            arg = str(index).lower()
        if isinstance(index, list):
            arg = '{'
            for index, j in enumerate(index):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.index = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSCooperateMatchStartMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateMatchStartMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSCooperateMatchCancelMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateMatchCancelMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSCooperateMatchConfirmMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateMatchConfirmMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSCooperateMatchRefuseMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateMatchRefuseMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildCooperateApplyMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildCooperateApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # index: i32
def get_CSCooperateDisbandMsg(addition_part="", index: int = None):
    cmd_part = ''
    if index is not None:
        arg = index
        if isinstance(index, str):
            arg = f'"{index}"'
        if isinstance(index, bool):
            arg = str(index).lower()
        if isinstance(index, list):
            arg = '{'
            for index, j in enumerate(index):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.index = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCooperateDisbandMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # roomId: i64, fromRank: i32, count: i32
def get_CSQueryDivisionRankMsg(addition_part="", roomId: int = None, fromRank: int = None, count: int = None):
    cmd_part = ''
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryDivisionRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # season: i32, fishSceneTpId: i32, roomId: i64, fromRank: i32, count: i32
def get_CSDoubleWeekQueryOverallRankMsg(addition_part="", season: int = None, fishSceneTpId: int = None, roomId: int = None, fromRank: int = None, count: int = None):
    cmd_part = ''
    if season is not None:
        arg = season
        if isinstance(season, str):
            arg = f'"{season}"'
        if isinstance(season, bool):
            arg = str(season).lower()
        if isinstance(season, list):
            arg = '{'
            for index, j in enumerate(season):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.season = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDoubleWeekQueryOverallRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # season: i32, fishSceneTpId: i32, roomId: i64, fishTpId: i32, fromRank: i32, count: i32
def get_CSDoubleWeekQueryFishRankMsg(addition_part="", season: int = None, fishSceneTpId: int = None, roomId: int = None, fishTpId: int = None, fromRank: int = None, count: int = None):
    cmd_part = ''
    if season is not None:
        arg = season
        if isinstance(season, str):
            arg = f'"{season}"'
        if isinstance(season, bool):
            arg = str(season).lower()
        if isinstance(season, list):
            arg = '{'
            for index, j in enumerate(season):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.season = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDoubleWeekQueryFishRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSQueryDuelInfoMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryDuelInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # seriesId: i32
def get_CSEnterMatchMsg(addition_part="", seriesId: int = None):
    cmd_part = ''
    if seriesId is not None:
        arg = seriesId
        if isinstance(seriesId, str):
            arg = f'"{seriesId}"'
        if isinstance(seriesId, bool):
            arg = str(seriesId).lower()
        if isinstance(seriesId, list):
            arg = '{'
            for index, j in enumerate(seriesId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.seriesId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSEnterMatchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSCancelMatchMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSCancelMatchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, matcherId: i64, seriesId: i32
def get_CSGlobalEnterMatchMsg(addition_part="", source: int = None, matcherId: int = None, seriesId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if matcherId is not None:
        arg = matcherId
        if isinstance(matcherId, str):
            arg = f'"{matcherId}"'
        if isinstance(matcherId, bool):
            arg = str(matcherId).lower()
        if isinstance(matcherId, list):
            arg = '{'
            for index, j in enumerate(matcherId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.matcherId = {arg}\n'
        
    if seriesId is not None:
        arg = seriesId
        if isinstance(seriesId, str):
            arg = f'"{seriesId}"'
        if isinstance(seriesId, bool):
            arg = str(seriesId).lower()
        if isinstance(seriesId, list):
            arg = '{'
            for index, j in enumerate(seriesId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.seriesId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalEnterMatchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, matcherId: i64
def get_CSGlobalCancelMatchMsg(addition_part="", source: int = None, matcherId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if matcherId is not None:
        arg = matcherId
        if isinstance(matcherId, str):
            arg = f'"{matcherId}"'
        if isinstance(matcherId, bool):
            arg = str(matcherId).lower()
        if isinstance(matcherId, list):
            arg = '{'
            for index, j in enumerate(matcherId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.matcherId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalCancelMatchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # duelId: i32, cardTpId: i32
def get_CSDuelSelectCardMsg(addition_part="", duelId: int = None, cardTpId: int = None):
    cmd_part = ''
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if cardTpId is not None:
        arg = cardTpId
        if isinstance(cardTpId, str):
            arg = f'"{cardTpId}"'
        if isinstance(cardTpId, bool):
            arg = str(cardTpId).lower()
        if isinstance(cardTpId, list):
            arg = '{'
            for index, j in enumerate(cardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.cardTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelSelectCardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # duelId: i32
def get_CSDuelConfirmCardMsg(addition_part="", duelId: int = None):
    cmd_part = ''
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelConfirmCardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64, cardTpId: i32
def get_CSGlobalDuelSelectCardMsg(addition_part="", source: int = None, duelId: int = None, cardTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if cardTpId is not None:
        arg = cardTpId
        if isinstance(cardTpId, str):
            arg = f'"{cardTpId}"'
        if isinstance(cardTpId, bool):
            arg = str(cardTpId).lower()
        if isinstance(cardTpId, list):
            arg = '{'
            for index, j in enumerate(cardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.cardTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelSelectCardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64
def get_CSGlobalDuelConfirmCardMsg(addition_part="", source: int = None, duelId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelConfirmCardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # duelId: i32, reEnter: bool
def get_CSSceneLoadedMsg(addition_part="", duelId: int = None, reEnter: bool = None):
    cmd_part = ''
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if reEnter is not None:
        arg = reEnter
        if isinstance(reEnter, str):
            arg = f'"{reEnter}"'
        if isinstance(reEnter, bool):
            arg = str(reEnter).lower()
        if isinstance(reEnter, list):
            arg = '{'
            for index, j in enumerate(reEnter):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.reEnter = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSceneLoadedMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64, reEnter: bool
def get_CSGlobalSceneLoadedMsg(addition_part="", source: int = None, duelId: int = None, reEnter: bool = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if reEnter is not None:
        arg = reEnter
        if isinstance(reEnter, str):
            arg = f'"{reEnter}"'
        if isinstance(reEnter, bool):
            arg = str(reEnter).lower()
        if isinstance(reEnter, list):
            arg = '{'
            for index, j in enumerate(reEnter):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.reEnter = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalSceneLoadedMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # duelId: i32
def get_CSDuelGiveUpMsg(addition_part="", duelId: int = None):
    cmd_part = ''
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelGiveUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64
def get_CSGlobalDuelGiveUpMsg(addition_part="", source: int = None, duelId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelGiveUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64
def get_CSGlobalDuelBreakMsg(addition_part="", source: int = None, duelId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelBreakMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # duelId: i32
def get_CSDuelEndMsg(addition_part="", duelId: int = None):
    cmd_part = ''
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelEndMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSExistDuelMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSExistDuelMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64
def get_CSGlobalExistDuelMsg(addition_part="", source: int = None, duelId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalExistDuelMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # clientTime: double
def get_CSDuelPingMsg(addition_part="", clientTime: float = None):
    cmd_part = ''
    if clientTime is not None:
        arg = clientTime
        if isinstance(clientTime, str):
            arg = f'"{clientTime}"'
        if isinstance(clientTime, bool):
            arg = str(clientTime).lower()
        if isinstance(clientTime, list):
            arg = '{'
            for index, j in enumerate(clientTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientTime = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelPingMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64, clientTime: double
def get_CSGlobalDuelPingMsg(addition_part="", source: int = None, duelId: int = None, clientTime: float = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if clientTime is not None:
        arg = clientTime
        if isinstance(clientTime, str):
            arg = f'"{clientTime}"'
        if isinstance(clientTime, bool):
            arg = str(clientTime).lower()
        if isinstance(clientTime, list):
            arg = '{'
            for index, j in enumerate(clientTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientTime = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelPingMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fromRank: i32, count: i32, type: i32
def get_CSQueryDuelRankMsg(addition_part="", fromRank: int = None, count: int = None, type: int = None):
    cmd_part = ''
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryDuelRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64, castFlag: i64
def get_CSGlobalDuelSetTheHookMsg(addition_part="", source: int = None, duelId: int = None, castFlag: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if castFlag is not None:
        arg = castFlag
        if isinstance(castFlag, str):
            arg = f'"{castFlag}"'
        if isinstance(castFlag, bool):
            arg = str(castFlag).lower()
        if isinstance(castFlag, list):
            arg = '{'
            for index, j in enumerate(castFlag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.castFlag = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelSetTheHookMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # duelId: i32
def get_CSBonusMsg(addition_part="", duelId: int = None):
    cmd_part = ''
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSBonusMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64, castFlag: i64
def get_CSGlobalBonusMsg(addition_part="", source: int = None, duelId: int = None, castFlag: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if castFlag is not None:
        arg = castFlag
        if isinstance(castFlag, str):
            arg = f'"{castFlag}"'
        if isinstance(castFlag, bool):
            arg = str(castFlag).lower()
        if isinstance(castFlag, list):
            arg = '{'
            for index, j in enumerate(castFlag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.castFlag = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalBonusMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # emojiId: i32, duelId: i32
def get_CSDuelEmojiMsg(addition_part="", emojiId: int = None, duelId: int = None):
    cmd_part = ''
    if emojiId is not None:
        arg = emojiId
        if isinstance(emojiId, str):
            arg = f'"{emojiId}"'
        if isinstance(emojiId, bool):
            arg = str(emojiId).lower()
        if isinstance(emojiId, list):
            arg = '{'
            for index, j in enumerate(emojiId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.emojiId = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelEmojiMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, duelId: i64, emojiId: i32
def get_CSGlobalDuelEmojiMsg(addition_part="", source: int = None, duelId: int = None, emojiId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if duelId is not None:
        arg = duelId
        if isinstance(duelId, str):
            arg = f'"{duelId}"'
        if isinstance(duelId, bool):
            arg = str(duelId).lower()
        if isinstance(duelId, list):
            arg = '{'
            for index, j in enumerate(duelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelId = {arg}\n'
        
    if emojiId is not None:
        arg = emojiId
        if isinstance(emojiId, str):
            arg = f'"{emojiId}"'
        if isinstance(emojiId, bool):
            arg = str(emojiId).lower()
        if isinstance(emojiId, list):
            arg = '{'
            for index, j in enumerate(emojiId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.emojiId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelEmojiMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSDuelRoomQueryMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDuelRoomQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64
def get_CSGlobalDuelRoomQueryMsg(addition_part="", source: int = None, roomId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, generatorId: i64
def get_CSGlobalDuelRoomCreateMsg(addition_part="", source: int = None, generatorId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if generatorId is not None:
        arg = generatorId
        if isinstance(generatorId, str):
            arg = f'"{generatorId}"'
        if isinstance(generatorId, bool):
            arg = str(generatorId).lower()
        if isinstance(generatorId, list):
            arg = '{'
            for index, j in enumerate(generatorId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.generatorId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomCreateMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64
def get_CSGlobalDuelRoomJoinMsg(addition_part="", source: int = None, roomId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomJoinMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64
def get_CSGlobalDuelRoomLeaveMsg(addition_part="", source: int = None, roomId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomLeaveMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, charId: string
def get_CSGlobalDuelRoomKickMsg(addition_part="", source: int = None, roomId: int = None, charId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomKickMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fair: bool, duelType: i32, fishBalance: bool
def get_CSGlobalDuelRoomChangeModeMsg(addition_part="", source: int = None, roomId: int = None, fair: bool = None, duelType: int = None, fishBalance: bool = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fair is not None:
        arg = fair
        if isinstance(fair, str):
            arg = f'"{fair}"'
        if isinstance(fair, bool):
            arg = str(fair).lower()
        if isinstance(fair, list):
            arg = '{'
            for index, j in enumerate(fair):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fair = {arg}\n'
        
    if duelType is not None:
        arg = duelType
        if isinstance(duelType, str):
            arg = f'"{duelType}"'
        if isinstance(duelType, bool):
            arg = str(duelType).lower()
        if isinstance(duelType, list):
            arg = '{'
            for index, j in enumerate(duelType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.duelType = {arg}\n'
        
    if fishBalance is not None:
        arg = fishBalance
        if isinstance(fishBalance, str):
            arg = f'"{fishBalance}"'
        if isinstance(fishBalance, bool):
            arg = str(fishBalance).lower()
        if isinstance(fishBalance, list):
            arg = '{'
            for index, j in enumerate(fishBalance):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishBalance = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomChangeModeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, ready: bool
def get_CSGlobalDuelRoomSetReadyMsg(addition_part="", source: int = None, roomId: int = None, ready: bool = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if ready is not None:
        arg = ready
        if isinstance(ready, str):
            arg = f'"{ready}"'
        if isinstance(ready, bool):
            arg = str(ready).lower()
        if isinstance(ready, list):
            arg = '{'
            for index, j in enumerate(ready):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ready = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomSetReadyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64
def get_CSGlobalDuelRoomStartMsg(addition_part="", source: int = None, roomId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomStartMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, charId: string
def get_CSGlobalDuelRoomInviteMsg(addition_part="", source: int = None, roomId: int = None, charId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomInviteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64
def get_CSGlobalDuelRoomInviteReplyMsg(addition_part="", source: int = None, roomId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalDuelRoomInviteReplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # exchangeId: i32, num: i32
def get_CSExchangeItemsMsg(addition_part="", exchangeId: int = None, num: int = None):
    cmd_part = ''
    if exchangeId is not None:
        arg = exchangeId
        if isinstance(exchangeId, str):
            arg = f'"{exchangeId}"'
        if isinstance(exchangeId, bool):
            arg = str(exchangeId).lower()
        if isinstance(exchangeId, list):
            arg = '{'
            for index, j in enumerate(exchangeId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.exchangeId = {arg}\n'
        
    if num is not None:
        arg = num
        if isinstance(num, str):
            arg = f'"{num}"'
        if isinstance(num, bool):
            arg = str(num).lower()
        if isinstance(num, list):
            arg = '{'
            for index, j in enumerate(num):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.num = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSExchangeItemsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # wearInfo: map<i32, i32>, unitId: i32
def get_CSUpdateFacadeMsg(addition_part="", wearInfo: dict = None, unitId: int = None):
    cmd_part = ''
    if wearInfo is not None:
        arg = wearInfo
        if isinstance(wearInfo, str):
            arg = f'"{wearInfo}"'
        if isinstance(wearInfo, bool):
            arg = str(wearInfo).lower()
        if isinstance(wearInfo, list):
            arg = '{'
            for index, j in enumerate(wearInfo):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.wearInfo = {arg}\n'
        
    if unitId is not None:
        arg = unitId
        if isinstance(unitId, str):
            arg = f'"{unitId}"'
        if isinstance(unitId, bool):
            arg = str(unitId).lower()
        if isinstance(unitId, list):
            arg = '{'
            for index, j in enumerate(unitId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.unitId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSUpdateFacadeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSSeeFacadeMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSeeFacadeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSUpdateFacadeDBMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSUpdateFacadeDBMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # sex: i32
def get_CSSelectSexMsg(addition_part="", sex: int = None):
    cmd_part = ''
    if sex is not None:
        arg = sex
        if isinstance(sex, str):
            arg = f'"{sex}"'
        if isinstance(sex, bool):
            arg = str(sex).lower()
        if isinstance(sex, list):
            arg = '{'
            for index, j in enumerate(sex):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sex = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSelectSexMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # rodId: i32, rodSkinId: i32, outwardId: i32
def get_CSSaveAvatarShowMsg(addition_part="", rodId: int = None, rodSkinId: int = None, outwardId: int = None):
    cmd_part = ''
    if rodId is not None:
        arg = rodId
        if isinstance(rodId, str):
            arg = f'"{rodId}"'
        if isinstance(rodId, bool):
            arg = str(rodId).lower()
        if isinstance(rodId, list):
            arg = '{'
            for index, j in enumerate(rodId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rodId = {arg}\n'
        
    if rodSkinId is not None:
        arg = rodSkinId
        if isinstance(rodSkinId, str):
            arg = f'"{rodSkinId}"'
        if isinstance(rodSkinId, bool):
            arg = str(rodSkinId).lower()
        if isinstance(rodSkinId, list):
            arg = '{'
            for index, j in enumerate(rodSkinId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rodSkinId = {arg}\n'
        
    if outwardId is not None:
        arg = outwardId
        if isinstance(outwardId, str):
            arg = f'"{outwardId}"'
        if isinstance(outwardId, bool):
            arg = str(outwardId).lower()
        if isinstance(outwardId, list):
            arg = '{'
            for index, j in enumerate(outwardId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.outwardId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSaveAvatarShowMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSSeeAvatarIdMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSeeAvatarIdMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, sceneArg1: i32, otherArgMap: map<i32, i32>, fixedFishTpId: i32, boosterIds: list<i32>, castG: i32, castGType: i32
def get_CSFishingCastMsg(addition_part="", source: int = None, sceneArg1: int = None, otherArgMap: dict = None, fixedFishTpId: int = None, boosterIds: list = None, castG: int = None, castGType: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if sceneArg1 is not None:
        arg = sceneArg1
        if isinstance(sceneArg1, str):
            arg = f'"{sceneArg1}"'
        if isinstance(sceneArg1, bool):
            arg = str(sceneArg1).lower()
        if isinstance(sceneArg1, list):
            arg = '{'
            for index, j in enumerate(sceneArg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sceneArg1 = {arg}\n'
        
    if otherArgMap is not None:
        arg = otherArgMap
        if isinstance(otherArgMap, str):
            arg = f'"{otherArgMap}"'
        if isinstance(otherArgMap, bool):
            arg = str(otherArgMap).lower()
        if isinstance(otherArgMap, list):
            arg = '{'
            for index, j in enumerate(otherArgMap):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.otherArgMap = {arg}\n'
        
    if fixedFishTpId is not None:
        arg = fixedFishTpId
        if isinstance(fixedFishTpId, str):
            arg = f'"{fixedFishTpId}"'
        if isinstance(fixedFishTpId, bool):
            arg = str(fixedFishTpId).lower()
        if isinstance(fixedFishTpId, list):
            arg = '{'
            for index, j in enumerate(fixedFishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fixedFishTpId = {arg}\n'
        
    if boosterIds is not None:
        arg = boosterIds
        if isinstance(boosterIds, str):
            arg = f'"{boosterIds}"'
        if isinstance(boosterIds, bool):
            arg = str(boosterIds).lower()
        if isinstance(boosterIds, list):
            arg = '{'
            for index, j in enumerate(boosterIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.boosterIds = {arg}\n'
        
    if castG is not None:
        arg = castG
        if isinstance(castG, str):
            arg = f'"{castG}"'
        if isinstance(castG, bool):
            arg = str(castG).lower()
        if isinstance(castG, list):
            arg = '{'
            for index, j in enumerate(castG):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.castG = {arg}\n'
        
    if castGType is not None:
        arg = castGType
        if isinstance(castGType, str):
            arg = f'"{castGType}"'
        if isinstance(castGType, bool):
            arg = str(castGType).lower()
        if isinstance(castGType, list):
            arg = '{'
            for index, j in enumerate(castGType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.castGType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingCastMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, castFlag: i64, timeCost: i32, qteInfos: list<FishingQTEInfo>, use_ULT_Ts: i32, minEstimateTimeMills: i32, hook_result: i32, battleResult: string, battleResultArgs: map<string,string>, fishArgs: map<string,string>, rodArgs: map<string,string>, playerArgs: map<string,string>, fishSceneArgs: map<string,string>, counterSuccessNum: i32, time: i32
def get_CSFishingHookMsg(addition_part="", source: int = None, castFlag: int = None, timeCost: int = None, qteInfos: list = None, use_ULT_Ts: int = None, minEstimateTimeMills: int = None, hook_result: int = None, battleResult: str = None, battleResultArgs: dict = None, fishArgs: dict = None, rodArgs: dict = None, playerArgs: dict = None, fishSceneArgs: dict = None, counterSuccessNum: int = None, time: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if castFlag is not None:
        arg = castFlag
        if isinstance(castFlag, str):
            arg = f'"{castFlag}"'
        if isinstance(castFlag, bool):
            arg = str(castFlag).lower()
        if isinstance(castFlag, list):
            arg = '{'
            for index, j in enumerate(castFlag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.castFlag = {arg}\n'
        
    if timeCost is not None:
        arg = timeCost
        if isinstance(timeCost, str):
            arg = f'"{timeCost}"'
        if isinstance(timeCost, bool):
            arg = str(timeCost).lower()
        if isinstance(timeCost, list):
            arg = '{'
            for index, j in enumerate(timeCost):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.timeCost = {arg}\n'
        
    if qteInfos is not None:
        arg = qteInfos
        if isinstance(qteInfos, str):
            arg = f'"{qteInfos}"'
        if isinstance(qteInfos, bool):
            arg = str(qteInfos).lower()
        if isinstance(qteInfos, list):
            arg = '{'
            for index, j in enumerate(qteInfos):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.qteInfos = {arg}\n'
        
    if use_ULT_Ts is not None:
        arg = use_ULT_Ts
        if isinstance(use_ULT_Ts, str):
            arg = f'"{use_ULT_Ts}"'
        if isinstance(use_ULT_Ts, bool):
            arg = str(use_ULT_Ts).lower()
        if isinstance(use_ULT_Ts, list):
            arg = '{'
            for index, j in enumerate(use_ULT_Ts):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.use_ULT_Ts = {arg}\n'
        
    if minEstimateTimeMills is not None:
        arg = minEstimateTimeMills
        if isinstance(minEstimateTimeMills, str):
            arg = f'"{minEstimateTimeMills}"'
        if isinstance(minEstimateTimeMills, bool):
            arg = str(minEstimateTimeMills).lower()
        if isinstance(minEstimateTimeMills, list):
            arg = '{'
            for index, j in enumerate(minEstimateTimeMills):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.minEstimateTimeMills = {arg}\n'
        
    if hook_result is not None:
        arg = hook_result
        if isinstance(hook_result, str):
            arg = f'"{hook_result}"'
        if isinstance(hook_result, bool):
            arg = str(hook_result).lower()
        if isinstance(hook_result, list):
            arg = '{'
            for index, j in enumerate(hook_result):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.hook_result = {arg}\n'
        
    if battleResult is not None:
        arg = battleResult
        if isinstance(battleResult, str):
            arg = f'"{battleResult}"'
        if isinstance(battleResult, bool):
            arg = str(battleResult).lower()
        if isinstance(battleResult, list):
            arg = '{'
            for index, j in enumerate(battleResult):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.battleResult = {arg}\n'
        
    if battleResultArgs is not None:
        arg = battleResultArgs
        if isinstance(battleResultArgs, str):
            arg = f'"{battleResultArgs}"'
        if isinstance(battleResultArgs, bool):
            arg = str(battleResultArgs).lower()
        if isinstance(battleResultArgs, list):
            arg = '{'
            for index, j in enumerate(battleResultArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.battleResultArgs = {arg}\n'
        
    if fishArgs is not None:
        arg = fishArgs
        if isinstance(fishArgs, str):
            arg = f'"{fishArgs}"'
        if isinstance(fishArgs, bool):
            arg = str(fishArgs).lower()
        if isinstance(fishArgs, list):
            arg = '{'
            for index, j in enumerate(fishArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishArgs = {arg}\n'
        
    if rodArgs is not None:
        arg = rodArgs
        if isinstance(rodArgs, str):
            arg = f'"{rodArgs}"'
        if isinstance(rodArgs, bool):
            arg = str(rodArgs).lower()
        if isinstance(rodArgs, list):
            arg = '{'
            for index, j in enumerate(rodArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rodArgs = {arg}\n'
        
    if playerArgs is not None:
        arg = playerArgs
        if isinstance(playerArgs, str):
            arg = f'"{playerArgs}"'
        if isinstance(playerArgs, bool):
            arg = str(playerArgs).lower()
        if isinstance(playerArgs, list):
            arg = '{'
            for index, j in enumerate(playerArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.playerArgs = {arg}\n'
        
    if fishSceneArgs is not None:
        arg = fishSceneArgs
        if isinstance(fishSceneArgs, str):
            arg = f'"{fishSceneArgs}"'
        if isinstance(fishSceneArgs, bool):
            arg = str(fishSceneArgs).lower()
        if isinstance(fishSceneArgs, list):
            arg = '{'
            for index, j in enumerate(fishSceneArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneArgs = {arg}\n'
        
    if counterSuccessNum is not None:
        arg = counterSuccessNum
        if isinstance(counterSuccessNum, str):
            arg = f'"{counterSuccessNum}"'
        if isinstance(counterSuccessNum, bool):
            arg = str(counterSuccessNum).lower()
        if isinstance(counterSuccessNum, list):
            arg = '{'
            for index, j in enumerate(counterSuccessNum):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.counterSuccessNum = {arg}\n'
        
    if time is not None:
        arg = time
        if isinstance(time, str):
            arg = f'"{time}"'
        if isinstance(time, bool):
            arg = str(time).lower()
        if isinstance(time, list):
            arg = '{'
            for index, j in enumerate(time):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.time = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingHookMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # done: bool, perfect: bool
def get_FishingQTEInfo(addition_part="", done: bool = None, perfect: bool = None):
    cmd_part = ''
    if done is not None:
        arg = done
        if isinstance(done, str):
            arg = f'"{done}"'
        if isinstance(done, bool):
            arg = str(done).lower()
        if isinstance(done, list):
            arg = '{'
            for index, j in enumerate(done):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.done = {arg}\n'
        
    if perfect is not None:
        arg = perfect
        if isinstance(perfect, str):
            arg = f'"{perfect}"'
        if isinstance(perfect, bool):
            arg = str(perfect).lower()
        if isinstance(perfect, list):
            arg = '{'
            for index, j in enumerate(perfect):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.perfect = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("FishingQTEInfo")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, fishTpId: i32, isInDoubleWeek: bool
def get_CSFishingSelectFishMsg(addition_part="", fishSceneTpId: int = None, fishTpId: int = None, isInDoubleWeek: bool = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    if isInDoubleWeek is not None:
        arg = isInDoubleWeek
        if isinstance(isInDoubleWeek, str):
            arg = f'"{isInDoubleWeek}"'
        if isinstance(isInDoubleWeek, bool):
            arg = str(isInDoubleWeek).lower()
        if isinstance(isInDoubleWeek, list):
            arg = '{'
            for index, j in enumerate(isInDoubleWeek):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.isInDoubleWeek = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingSelectFishMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, fishTpId: i32, rewardStarIdx: i32
def get_CSFishingGetFishStarRewardMsg(addition_part="", fishSceneTpId: int = None, fishTpId: int = None, rewardStarIdx: int = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    if rewardStarIdx is not None:
        arg = rewardStarIdx
        if isinstance(rewardStarIdx, str):
            arg = f'"{rewardStarIdx}"'
        if isinstance(rewardStarIdx, bool):
            arg = str(rewardStarIdx).lower()
        if isinstance(rewardStarIdx, list):
            arg = '{'
            for index, j in enumerate(rewardStarIdx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rewardStarIdx = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingGetFishStarRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, rewardStarIdx: i32
def get_CSFishingGetSceneStarRewardMsg(addition_part="", fishSceneTpId: int = None, rewardStarIdx: int = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if rewardStarIdx is not None:
        arg = rewardStarIdx
        if isinstance(rewardStarIdx, str):
            arg = f'"{rewardStarIdx}"'
        if isinstance(rewardStarIdx, bool):
            arg = str(rewardStarIdx).lower()
        if isinstance(rewardStarIdx, list):
            arg = '{'
            for index, j in enumerate(rewardStarIdx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rewardStarIdx = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingGetSceneStarRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, sceneArg1: i32, save: bool
def get_CSFishingEquipChangeMsg(addition_part="", source: int = None, sceneArg1: int = None, save: bool = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if sceneArg1 is not None:
        arg = sceneArg1
        if isinstance(sceneArg1, str):
            arg = f'"{sceneArg1}"'
        if isinstance(sceneArg1, bool):
            arg = str(sceneArg1).lower()
        if isinstance(sceneArg1, list):
            arg = '{'
            for index, j in enumerate(sceneArg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sceneArg1 = {arg}\n'
        
    if save is not None:
        arg = save
        if isinstance(save, str):
            arg = f'"{save}"'
        if isinstance(save, bool):
            arg = str(save).lower()
        if isinstance(save, list):
            arg = '{'
            for index, j in enumerate(save):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.save = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingEquipChangeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, ioIdType: i32, tpId: i32, doPin: bool
def get_CSFishingEquipPinMsg(addition_part="", fishSceneTpId: int = None, ioIdType: int = None, tpId: int = None, doPin: bool = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if ioIdType is not None:
        arg = ioIdType
        if isinstance(ioIdType, str):
            arg = f'"{ioIdType}"'
        if isinstance(ioIdType, bool):
            arg = str(ioIdType).lower()
        if isinstance(ioIdType, list):
            arg = '{'
            for index, j in enumerate(ioIdType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ioIdType = {arg}\n'
        
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    if doPin is not None:
        arg = doPin
        if isinstance(doPin, str):
            arg = f'"{doPin}"'
        if isinstance(doPin, bool):
            arg = str(doPin).lower()
        if isinstance(doPin, list):
            arg = '{'
            for index, j in enumerate(doPin):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.doPin = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingEquipPinMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpIds: list<i32>, opens: list<bool>
def get_CSFishingBoosterOpenMsg(addition_part="", tpIds: list = None, opens: list = None):
    cmd_part = ''
    if tpIds is not None:
        arg = tpIds
        if isinstance(tpIds, str):
            arg = f'"{tpIds}"'
        if isinstance(tpIds, bool):
            arg = str(tpIds).lower()
        if isinstance(tpIds, list):
            arg = '{'
            for index, j in enumerate(tpIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpIds = {arg}\n'
        
    if opens is not None:
        arg = opens
        if isinstance(opens, str):
            arg = f'"{opens}"'
        if isinstance(opens, bool):
            arg = str(opens).lower()
        if isinstance(opens, list):
            arg = '{'
            for index, j in enumerate(opens):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.opens = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingBoosterOpenMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, fishSceneTpId: i32, fishSpotId: i32, isInDoubleWeek: bool
def get_CSFishingSaveFishSpotMsg(addition_part="", source: int = None, fishSceneTpId: int = None, fishSpotId: int = None, isInDoubleWeek: bool = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if fishSpotId is not None:
        arg = fishSpotId
        if isinstance(fishSpotId, str):
            arg = f'"{fishSpotId}"'
        if isinstance(fishSpotId, bool):
            arg = str(fishSpotId).lower()
        if isinstance(fishSpotId, list):
            arg = '{'
            for index, j in enumerate(fishSpotId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSpotId = {arg}\n'
        
    if isInDoubleWeek is not None:
        arg = isInDoubleWeek
        if isinstance(isInDoubleWeek, str):
            arg = f'"{isInDoubleWeek}"'
        if isinstance(isInDoubleWeek, bool):
            arg = str(isInDoubleWeek).lower()
        if isinstance(isInDoubleWeek, list):
            arg = '{'
            for index, j in enumerate(isInDoubleWeek):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.isInDoubleWeek = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingSaveFishSpotMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, fishTpIds: list<i32>
def get_CSFishSceneFishNewMsg(addition_part="", fishSceneTpId: int = None, fishTpIds: list = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if fishTpIds is not None:
        arg = fishTpIds
        if isinstance(fishTpIds, str):
            arg = f'"{fishTpIds}"'
        if isinstance(fishTpIds, bool):
            arg = str(fishTpIds).lower()
        if isinstance(fishTpIds, list):
            arg = '{'
            for index, j in enumerate(fishTpIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpIds = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishSceneFishNewMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSFishingContinueLimitedSpotMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingContinueLimitedSpotMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, chooseEnergyCostId: i32
def get_CSFishingSaveLimitedSpotEnergyCostIdMsg(addition_part="", source: int = None, chooseEnergyCostId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if chooseEnergyCostId is not None:
        arg = chooseEnergyCostId
        if isinstance(chooseEnergyCostId, str):
            arg = f'"{chooseEnergyCostId}"'
        if isinstance(chooseEnergyCostId, bool):
            arg = str(chooseEnergyCostId).lower()
        if isinstance(chooseEnergyCostId, list):
            arg = '{'
            for index, j in enumerate(chooseEnergyCostId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.chooseEnergyCostId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingSaveLimitedSpotEnergyCostIdMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, sumPoint: i32
def get_CSFishSceneRewardSumPointMsg(addition_part="", fishSceneTpId: int = None, sumPoint: int = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if sumPoint is not None:
        arg = sumPoint
        if isinstance(sumPoint, str):
            arg = f'"{sumPoint}"'
        if isinstance(sumPoint, bool):
            arg = str(sumPoint).lower()
        if isinstance(sumPoint, list):
            arg = '{'
            for index, j in enumerate(sumPoint):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.sumPoint = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishSceneRewardSumPointMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, fishTpId: i32, useSeasonSkin: i32
def get_CSFishSwitchSkinMsg(addition_part="", fishSceneTpId: int = None, fishTpId: int = None, useSeasonSkin: int = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if fishTpId is not None:
        arg = fishTpId
        if isinstance(fishTpId, str):
            arg = f'"{fishTpId}"'
        if isinstance(fishTpId, bool):
            arg = str(fishTpId).lower()
        if isinstance(fishTpId, list):
            arg = '{'
            for index, j in enumerate(fishTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishTpId = {arg}\n'
        
    if useSeasonSkin is not None:
        arg = useSeasonSkin
        if isinstance(useSeasonSkin, str):
            arg = f'"{useSeasonSkin}"'
        if isinstance(useSeasonSkin, bool):
            arg = str(useSeasonSkin).lower()
        if isinstance(useSeasonSkin, list):
            arg = '{'
            for index, j in enumerate(useSeasonSkin):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.useSeasonSkin = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishSwitchSkinMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # castG: i32
def get_CSFishingCastDistanceMsg(addition_part="", castG: int = None):
    cmd_part = ''
    if castG is not None:
        arg = castG
        if isinstance(castG, str):
            arg = f'"{castG}"'
        if isinstance(castG, bool):
            arg = str(castG).lower()
        if isinstance(castG, list):
            arg = '{'
            for index, j in enumerate(castG):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.castG = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingCastDistanceMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishSceneTpId: i32, modeType: i32
def get_CSFishSceneStarChangeModeMsg(addition_part="", fishSceneTpId: int = None, modeType: int = None):
    cmd_part = ''
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if modeType is not None:
        arg = modeType
        if isinstance(modeType, str):
            arg = f'"{modeType}"'
        if isinstance(modeType, bool):
            arg = str(modeType).lower()
        if isinstance(modeType, list):
            arg = '{'
            for index, j in enumerate(modeType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.modeType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishSceneStarChangeModeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishCardTpId: i32
def get_CSFishCardLevelUpMsg(addition_part="", fishCardTpId: int = None):
    cmd_part = ''
    if fishCardTpId is not None:
        arg = fishCardTpId
        if isinstance(fishCardTpId, str):
            arg = f'"{fishCardTpId}"'
        if isinstance(fishCardTpId, bool):
            arg = str(fishCardTpId).lower()
        if isinstance(fishCardTpId, list):
            arg = '{'
            for index, j in enumerate(fishCardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishCardTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishCardLevelUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # fishCardTpIds: list<i32>
def get_CSFishCardOneKeyLevelUpMsg(addition_part="", fishCardTpIds: list = None):
    cmd_part = ''
    if fishCardTpIds is not None:
        arg = fishCardTpIds
        if isinstance(fishCardTpIds, str):
            arg = f'"{fishCardTpIds}"'
        if isinstance(fishCardTpIds, bool):
            arg = str(fishCardTpIds).lower()
        if isinstance(fishCardTpIds, list):
            arg = '{'
            for index, j in enumerate(fishCardTpIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishCardTpIds = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishCardOneKeyLevelUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # seasonId: i32
def get_CSFlashCardSeasonRewardMsg(addition_part="", seasonId: int = None):
    cmd_part = ''
    if seasonId is not None:
        arg = seasonId
        if isinstance(seasonId, str):
            arg = f'"{seasonId}"'
        if isinstance(seasonId, bool):
            arg = str(seasonId).lower()
        if isinstance(seasonId, list):
            arg = '{'
            for index, j in enumerate(seasonId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.seasonId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardSeasonRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # rewardId: i32
def get_CSFlashCardChapterRewardMsg(addition_part="", rewardId: int = None):
    cmd_part = ''
    if rewardId is not None:
        arg = rewardId
        if isinstance(rewardId, str):
            arg = f'"{rewardId}"'
        if isinstance(rewardId, bool):
            arg = str(rewardId).lower()
        if isinstance(rewardId, list):
            arg = '{'
            for index, j in enumerate(rewardId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rewardId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardChapterRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # shopTpId: i32, cardInfos: map<i32,i32>
def get_CSFlashCardShopExchangeMsg(addition_part="", shopTpId: int = None, cardInfos: dict = None):
    cmd_part = ''
    if shopTpId is not None:
        arg = shopTpId
        if isinstance(shopTpId, str):
            arg = f'"{shopTpId}"'
        if isinstance(shopTpId, bool):
            arg = str(shopTpId).lower()
        if isinstance(shopTpId, list):
            arg = '{'
            for index, j in enumerate(shopTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.shopTpId = {arg}\n'
        
    if cardInfos is not None:
        arg = cardInfos
        if isinstance(cardInfos, str):
            arg = f'"{cardInfos}"'
        if isinstance(cardInfos, bool):
            arg = str(cardInfos).lower()
        if isinstance(cardInfos, list):
            arg = '{'
            for index, j in enumerate(cardInfos):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.cardInfos = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardShopExchangeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # flashCardTpId: i32
def get_CSFlashCardGuildRequestMsg(addition_part="", flashCardTpId: int = None):
    cmd_part = ''
    if flashCardTpId is not None:
        arg = flashCardTpId
        if isinstance(flashCardTpId, str):
            arg = f'"{flashCardTpId}"'
        if isinstance(flashCardTpId, bool):
            arg = str(flashCardTpId).lower()
        if isinstance(flashCardTpId, list):
            arg = '{'
            for index, j in enumerate(flashCardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flashCardTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardGuildRequestMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # flashCardTpId: i32, receiveCharId: string, receiveSimpleCharId: i64
def get_CSFlashCardGuildDonateMsg(addition_part="", flashCardTpId: int = None, receiveCharId: str = None, receiveSimpleCharId: int = None):
    cmd_part = ''
    if flashCardTpId is not None:
        arg = flashCardTpId
        if isinstance(flashCardTpId, str):
            arg = f'"{flashCardTpId}"'
        if isinstance(flashCardTpId, bool):
            arg = str(flashCardTpId).lower()
        if isinstance(flashCardTpId, list):
            arg = '{'
            for index, j in enumerate(flashCardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flashCardTpId = {arg}\n'
        
    if receiveCharId is not None:
        arg = receiveCharId
        if isinstance(receiveCharId, str):
            arg = f'"{receiveCharId}"'
        if isinstance(receiveCharId, bool):
            arg = str(receiveCharId).lower()
        if isinstance(receiveCharId, list):
            arg = '{'
            for index, j in enumerate(receiveCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.receiveCharId = {arg}\n'
        
    if receiveSimpleCharId is not None:
        arg = receiveSimpleCharId
        if isinstance(receiveSimpleCharId, str):
            arg = f'"{receiveSimpleCharId}"'
        if isinstance(receiveSimpleCharId, bool):
            arg = str(receiveSimpleCharId).lower()
        if isinstance(receiveSimpleCharId, list):
            arg = '{'
            for index, j in enumerate(receiveSimpleCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.receiveSimpleCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardGuildDonateMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # flashCardTpId: i32
def get_CSFlashCardGuildCancelRequestMsg(addition_part="", flashCardTpId: int = None):
    cmd_part = ''
    if flashCardTpId is not None:
        arg = flashCardTpId
        if isinstance(flashCardTpId, str):
            arg = f'"{flashCardTpId}"'
        if isinstance(flashCardTpId, bool):
            arg = str(flashCardTpId).lower()
        if isinstance(flashCardTpId, list):
            arg = '{'
            for index, j in enumerate(flashCardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flashCardTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardGuildCancelRequestMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # flashCardTpId: i32, num: i32
def get_CSFlashCardWildExchangeMsg(addition_part="", flashCardTpId: int = None, num: int = None):
    cmd_part = ''
    if flashCardTpId is not None:
        arg = flashCardTpId
        if isinstance(flashCardTpId, str):
            arg = f'"{flashCardTpId}"'
        if isinstance(flashCardTpId, bool):
            arg = str(flashCardTpId).lower()
        if isinstance(flashCardTpId, list):
            arg = '{'
            for index, j in enumerate(flashCardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flashCardTpId = {arg}\n'
        
    if num is not None:
        arg = num
        if isinstance(num, str):
            arg = f'"{num}"'
        if isinstance(num, bool):
            arg = str(num).lower()
        if isinstance(num, list):
            arg = '{'
            for index, j in enumerate(num):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.num = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFlashCardWildExchangeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64
def get_CSGlobalFriendsQueryMsg(addition_part="", source: int = None, simpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetCharId: string, targetSimpleId: i64, type: i32
def get_CSGlobalFriendsApplyMsg(addition_part="", source: int = None, simpleId: int = None, targetCharId: str = None, targetSimpleId: int = None, type: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetCharId: string
def get_CSGlobalFriendsIgnoreApplyMsg(addition_part="", source: int = None, simpleId: int = None, targetCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsIgnoreApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64
def get_CSGlobalFriendsIgnoreAllAppliesMsg(addition_part="", source: int = None, simpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsIgnoreAllAppliesMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetCharId: string, targetSimpleId: i64
def get_CSGlobalFriendsAcceptMsg(addition_part="", source: int = None, simpleId: int = None, targetCharId: str = None, targetSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsAcceptMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64
def get_CSGlobalFriendsAcceptAllMsg(addition_part="", source: int = None, simpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsAcceptAllMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetCharId: string, targetSimpleId: i64
def get_CSGlobalFriendsDeleteMsg(addition_part="", source: int = None, simpleId: int = None, targetCharId: str = None, targetSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsDeleteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetCharId: string, targetSimpleId: i64
def get_CSGlobalFriendsInviteMsg(addition_part="", source: int = None, simpleId: int = None, targetCharId: str = None, targetSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsInviteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64
def get_CSGlobalFriendsRefreshMsg(addition_part="", source: int = None, simpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsRefreshMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetSimpleId: i64, targetName: string
def get_CSGlobalFriendsSearchMsg(addition_part="", source: int = None, simpleId: int = None, targetSimpleId: int = None, targetName: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    if targetName is not None:
        arg = targetName
        if isinstance(targetName, str):
            arg = f'"{targetName}"'
        if isinstance(targetName, bool):
            arg = str(targetName).lower()
        if isinstance(targetName, list):
            arg = '{'
            for index, j in enumerate(targetName):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetName = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsSearchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64
def get_CSGlobalFriendsQueryEnergyMsg(addition_part="", source: int = None, simpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsQueryEnergyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetSimpleId: i64, targetCharId: string
def get_CSGlobalFriendsSendMsg(addition_part="", source: int = None, simpleId: int = None, targetSimpleId: int = None, targetCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsSendMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64
def get_CSGlobalFriendsSendAllMsg(addition_part="", source: int = None, simpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsSendAllMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, targetSimpleId: i64, targetCharId: string, rebate: bool, time: i64
def get_CSGlobalFriendsGetMsg(addition_part="", source: int = None, simpleId: int = None, targetSimpleId: int = None, targetCharId: str = None, rebate: bool = None, time: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if targetSimpleId is not None:
        arg = targetSimpleId
        if isinstance(targetSimpleId, str):
            arg = f'"{targetSimpleId}"'
        if isinstance(targetSimpleId, bool):
            arg = str(targetSimpleId).lower()
        if isinstance(targetSimpleId, list):
            arg = '{'
            for index, j in enumerate(targetSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if rebate is not None:
        arg = rebate
        if isinstance(rebate, str):
            arg = f'"{rebate}"'
        if isinstance(rebate, bool):
            arg = str(rebate).lower()
        if isinstance(rebate, list):
            arg = '{'
            for index, j in enumerate(rebate):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rebate = {arg}\n'
        
    if time is not None:
        arg = time
        if isinstance(time, str):
            arg = f'"{time}"'
        if isinstance(time, bool):
            arg = str(time).lower()
        if isinstance(time, list):
            arg = '{'
            for index, j in enumerate(time):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.time = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsGetMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, simpleId: i64, rebate: bool
def get_CSGlobalFriendsGetAllMsg(addition_part="", source: int = None, simpleId: int = None, rebate: bool = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if simpleId is not None:
        arg = simpleId
        if isinstance(simpleId, str):
            arg = f'"{simpleId}"'
        if isinstance(simpleId, bool):
            arg = str(simpleId).lower()
        if isinstance(simpleId, list):
            arg = '{'
            for index, j in enumerate(simpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleId = {arg}\n'
        
    if rebate is not None:
        arg = rebate
        if isinstance(rebate, str):
            arg = f'"{rebate}"'
        if isinstance(rebate, bool):
            arg = str(rebate).lower()
        if isinstance(rebate, list):
            arg = '{'
            for index, j in enumerate(rebate):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rebate = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalFriendsGetAllMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, type: i32, group: i32, groupArg: i32, groupArg1: i32, groupArg2: i32, clientArgs: list<string>, startIndex: i32, endIndex: i32
def get_CSGlobalRankQueryMsg(addition_part="", source: int = None, type: int = None, group: int = None, groupArg: int = None, groupArg1: int = None, groupArg2: int = None, clientArgs: list = None, startIndex: int = None, endIndex: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if group is not None:
        arg = group
        if isinstance(group, str):
            arg = f'"{group}"'
        if isinstance(group, bool):
            arg = str(group).lower()
        if isinstance(group, list):
            arg = '{'
            for index, j in enumerate(group):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.group = {arg}\n'
        
    if groupArg is not None:
        arg = groupArg
        if isinstance(groupArg, str):
            arg = f'"{groupArg}"'
        if isinstance(groupArg, bool):
            arg = str(groupArg).lower()
        if isinstance(groupArg, list):
            arg = '{'
            for index, j in enumerate(groupArg):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg = {arg}\n'
        
    if groupArg1 is not None:
        arg = groupArg1
        if isinstance(groupArg1, str):
            arg = f'"{groupArg1}"'
        if isinstance(groupArg1, bool):
            arg = str(groupArg1).lower()
        if isinstance(groupArg1, list):
            arg = '{'
            for index, j in enumerate(groupArg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg1 = {arg}\n'
        
    if groupArg2 is not None:
        arg = groupArg2
        if isinstance(groupArg2, str):
            arg = f'"{groupArg2}"'
        if isinstance(groupArg2, bool):
            arg = str(groupArg2).lower()
        if isinstance(groupArg2, list):
            arg = '{'
            for index, j in enumerate(groupArg2):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg2 = {arg}\n'
        
    if clientArgs is not None:
        arg = clientArgs
        if isinstance(clientArgs, str):
            arg = f'"{clientArgs}"'
        if isinstance(clientArgs, bool):
            arg = str(clientArgs).lower()
        if isinstance(clientArgs, list):
            arg = '{'
            for index, j in enumerate(clientArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientArgs = {arg}\n'
        
    if startIndex is not None:
        arg = startIndex
        if isinstance(startIndex, str):
            arg = f'"{startIndex}"'
        if isinstance(startIndex, bool):
            arg = str(startIndex).lower()
        if isinstance(startIndex, list):
            arg = '{'
            for index, j in enumerate(startIndex):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.startIndex = {arg}\n'
        
    if endIndex is not None:
        arg = endIndex
        if isinstance(endIndex, str):
            arg = f'"{endIndex}"'
        if isinstance(endIndex, bool):
            arg = str(endIndex).lower()
        if isinstance(endIndex, list):
            arg = '{'
            for index, j in enumerate(endIndex):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.endIndex = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalRankQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, type: i32, groupToGroupArg: map<i32, i32>, groupArg1: i32, groupArg2: i32, clientArgs: list<string>
def get_CSGlobalRankFirstQueryMsg(addition_part="", source: int = None, type: int = None, groupToGroupArg: dict = None, groupArg1: int = None, groupArg2: int = None, clientArgs: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if groupToGroupArg is not None:
        arg = groupToGroupArg
        if isinstance(groupToGroupArg, str):
            arg = f'"{groupToGroupArg}"'
        if isinstance(groupToGroupArg, bool):
            arg = str(groupToGroupArg).lower()
        if isinstance(groupToGroupArg, list):
            arg = '{'
            for index, j in enumerate(groupToGroupArg):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupToGroupArg = {arg}\n'
        
    if groupArg1 is not None:
        arg = groupArg1
        if isinstance(groupArg1, str):
            arg = f'"{groupArg1}"'
        if isinstance(groupArg1, bool):
            arg = str(groupArg1).lower()
        if isinstance(groupArg1, list):
            arg = '{'
            for index, j in enumerate(groupArg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg1 = {arg}\n'
        
    if groupArg2 is not None:
        arg = groupArg2
        if isinstance(groupArg2, str):
            arg = f'"{groupArg2}"'
        if isinstance(groupArg2, bool):
            arg = str(groupArg2).lower()
        if isinstance(groupArg2, list):
            arg = '{'
            for index, j in enumerate(groupArg2):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg2 = {arg}\n'
        
    if clientArgs is not None:
        arg = clientArgs
        if isinstance(clientArgs, str):
            arg = f'"{clientArgs}"'
        if isinstance(clientArgs, bool):
            arg = str(clientArgs).lower()
        if isinstance(clientArgs, list):
            arg = '{'
            for index, j in enumerate(clientArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientArgs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalRankFirstQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, clientArgs: list<string>
def get_CSGlobalSpecialRankFirstQueryS1Msg(addition_part="", source: int = None, clientArgs: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if clientArgs is not None:
        arg = clientArgs
        if isinstance(clientArgs, str):
            arg = f'"{clientArgs}"'
        if isinstance(clientArgs, bool):
            arg = str(clientArgs).lower()
        if isinstance(clientArgs, list):
            arg = '{'
            for index, j in enumerate(clientArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientArgs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalSpecialRankFirstQueryS1Msg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSGmCommandMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGmCommandMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildDragonQueryMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildDragonQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildDragonQueryDetailMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildDragonQueryDetailMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, group: i32, type: i32
def get_CSGuildDragonQueryRankMsg(addition_part="", source: int = None, guildSimpleId: int = None, group: int = None, type: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if group is not None:
        arg = group
        if isinstance(group, str):
            arg = f'"{group}"'
        if isinstance(group, bool):
            arg = str(group).lower()
        if isinstance(group, list):
            arg = '{'
            for index, j in enumerate(group):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.group = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildDragonQueryRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildDragonQueryMemberMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildDragonQueryMemberMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, rewardId: i32
def get_CSGuildDragonRewardMsg(addition_part="", source: int = None, guildSimpleId: int = None, rewardId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if rewardId is not None:
        arg = rewardId
        if isinstance(rewardId, str):
            arg = f'"{rewardId}"'
        if isinstance(rewardId, bool):
            arg = str(rewardId).lower()
        if isinstance(rewardId, list):
            arg = '{'
            for index, j in enumerate(rewardId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rewardId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildDragonRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildRefreshMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildRefreshMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildAutoEnterMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildAutoEnterMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, name: string
def get_CSGuildSearchMsg(addition_part="", source: int = None, guildSimpleId: int = None, name: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if name is not None:
        arg = name
        if isinstance(name, str):
            arg = f'"{name}"'
        if isinstance(name, bool):
            arg = str(name).lower()
        if isinstance(name, list):
            arg = '{'
            for index, j in enumerate(name):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.name = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildSearchMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, name: string, flag: i32, pattern: i32, color: i32, introduce: string, labels: set<i32>, joinType: i32, joinLv: i32
def get_CSGameGuildCreateMsg(addition_part="", source: int = None, guildSimpleId: int = None, name: str = None, flag: int = None, pattern: int = None, color: int = None, introduce: str = None, labels: set = None, joinType: int = None, joinLv: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if name is not None:
        arg = name
        if isinstance(name, str):
            arg = f'"{name}"'
        if isinstance(name, bool):
            arg = str(name).lower()
        if isinstance(name, list):
            arg = '{'
            for index, j in enumerate(name):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.name = {arg}\n'
        
    if flag is not None:
        arg = flag
        if isinstance(flag, str):
            arg = f'"{flag}"'
        if isinstance(flag, bool):
            arg = str(flag).lower()
        if isinstance(flag, list):
            arg = '{'
            for index, j in enumerate(flag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flag = {arg}\n'
        
    if pattern is not None:
        arg = pattern
        if isinstance(pattern, str):
            arg = f'"{pattern}"'
        if isinstance(pattern, bool):
            arg = str(pattern).lower()
        if isinstance(pattern, list):
            arg = '{'
            for index, j in enumerate(pattern):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.pattern = {arg}\n'
        
    if color is not None:
        arg = color
        if isinstance(color, str):
            arg = f'"{color}"'
        if isinstance(color, bool):
            arg = str(color).lower()
        if isinstance(color, list):
            arg = '{'
            for index, j in enumerate(color):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.color = {arg}\n'
        
    if introduce is not None:
        arg = introduce
        if isinstance(introduce, str):
            arg = f'"{introduce}"'
        if isinstance(introduce, bool):
            arg = str(introduce).lower()
        if isinstance(introduce, list):
            arg = '{'
            for index, j in enumerate(introduce):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.introduce = {arg}\n'
        
    if labels is not None:
        arg = labels
        if isinstance(labels, str):
            arg = f'"{labels}"'
        if isinstance(labels, bool):
            arg = str(labels).lower()
        if isinstance(labels, list):
            arg = '{'
            for index, j in enumerate(labels):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.labels = {arg}\n'
        
    if joinType is not None:
        arg = joinType
        if isinstance(joinType, str):
            arg = f'"{joinType}"'
        if isinstance(joinType, bool):
            arg = str(joinType).lower()
        if isinstance(joinType, list):
            arg = '{'
            for index, j in enumerate(joinType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.joinType = {arg}\n'
        
    if joinLv is not None:
        arg = joinLv
        if isinstance(joinLv, str):
            arg = f'"{joinLv}"'
        if isinstance(joinLv, bool):
            arg = str(joinLv).lower()
        if isinstance(joinLv, list):
            arg = '{'
            for index, j in enumerate(joinLv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.joinLv = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGameGuildCreateMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildQueryApplyGuildMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildQueryApplyGuildMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildQueryMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildQueryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildQueryOtherMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildQueryOtherMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, simpleIds: list<i64>
def get_CSGuildQueryOtherBaseMsg(addition_part="", source: int = None, guildSimpleId: int = None, simpleIds: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if simpleIds is not None:
        arg = simpleIds
        if isinstance(simpleIds, str):
            arg = f'"{simpleIds}"'
        if isinstance(simpleIds, bool):
            arg = str(simpleIds).lower()
        if isinstance(simpleIds, list):
            arg = '{'
            for index, j in enumerate(simpleIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.simpleIds = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildQueryOtherBaseMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, permission: i32
def get_CSGuildQueryAppliesMsg(addition_part="", source: int = None, guildSimpleId: int = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildQueryAppliesMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildApplyMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildCancelApplyMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildCancelApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, targetCharId: string, permission: i32
def get_CSGuildIgnoreApplyMsg(addition_part="", source: int = None, guildSimpleId: int = None, targetCharId: str = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildIgnoreApplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, permission: i32
def get_CSGuildIgnoreAllAppliesMsg(addition_part="", source: int = None, guildSimpleId: int = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildIgnoreAllAppliesMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, targetCharId: string, permission: i32
def get_CSGuildAcceptMsg(addition_part="", source: int = None, guildSimpleId: int = None, targetCharId: str = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildAcceptMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, permission: i32
def get_CSGuildAcceptAllMsg(addition_part="", source: int = None, guildSimpleId: int = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildAcceptAllMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, targetCharId: string, permission: i32
def get_CSGuildDeleteMsg(addition_part="", source: int = None, guildSimpleId: int = None, targetCharId: str = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildDeleteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, name: string, flag: i32, pattern: i32, color: i32, introduce: string, labels: set<i32>, joinType: i32, joinLv: i32, permission: i32
def get_CSGameGuildSetGuildInfoCostMsg(addition_part="", source: int = None, guildSimpleId: int = None, name: str = None, flag: int = None, pattern: int = None, color: int = None, introduce: str = None, labels: set = None, joinType: int = None, joinLv: int = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if name is not None:
        arg = name
        if isinstance(name, str):
            arg = f'"{name}"'
        if isinstance(name, bool):
            arg = str(name).lower()
        if isinstance(name, list):
            arg = '{'
            for index, j in enumerate(name):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.name = {arg}\n'
        
    if flag is not None:
        arg = flag
        if isinstance(flag, str):
            arg = f'"{flag}"'
        if isinstance(flag, bool):
            arg = str(flag).lower()
        if isinstance(flag, list):
            arg = '{'
            for index, j in enumerate(flag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flag = {arg}\n'
        
    if pattern is not None:
        arg = pattern
        if isinstance(pattern, str):
            arg = f'"{pattern}"'
        if isinstance(pattern, bool):
            arg = str(pattern).lower()
        if isinstance(pattern, list):
            arg = '{'
            for index, j in enumerate(pattern):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.pattern = {arg}\n'
        
    if color is not None:
        arg = color
        if isinstance(color, str):
            arg = f'"{color}"'
        if isinstance(color, bool):
            arg = str(color).lower()
        if isinstance(color, list):
            arg = '{'
            for index, j in enumerate(color):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.color = {arg}\n'
        
    if introduce is not None:
        arg = introduce
        if isinstance(introduce, str):
            arg = f'"{introduce}"'
        if isinstance(introduce, bool):
            arg = str(introduce).lower()
        if isinstance(introduce, list):
            arg = '{'
            for index, j in enumerate(introduce):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.introduce = {arg}\n'
        
    if labels is not None:
        arg = labels
        if isinstance(labels, str):
            arg = f'"{labels}"'
        if isinstance(labels, bool):
            arg = str(labels).lower()
        if isinstance(labels, list):
            arg = '{'
            for index, j in enumerate(labels):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.labels = {arg}\n'
        
    if joinType is not None:
        arg = joinType
        if isinstance(joinType, str):
            arg = f'"{joinType}"'
        if isinstance(joinType, bool):
            arg = str(joinType).lower()
        if isinstance(joinType, list):
            arg = '{'
            for index, j in enumerate(joinType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.joinType = {arg}\n'
        
    if joinLv is not None:
        arg = joinLv
        if isinstance(joinLv, str):
            arg = f'"{joinLv}"'
        if isinstance(joinLv, bool):
            arg = str(joinLv).lower()
        if isinstance(joinLv, list):
            arg = '{'
            for index, j in enumerate(joinLv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.joinLv = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGameGuildSetGuildInfoCostMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, labels: set<i32>, joinType: i32, joinLv: i32, permission: i32
def get_CSGuildSetGuildInfoMsg(addition_part="", source: int = None, guildSimpleId: int = None, labels: set = None, joinType: int = None, joinLv: int = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if labels is not None:
        arg = labels
        if isinstance(labels, str):
            arg = f'"{labels}"'
        if isinstance(labels, bool):
            arg = str(labels).lower()
        if isinstance(labels, list):
            arg = '{'
            for index, j in enumerate(labels):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.labels = {arg}\n'
        
    if joinType is not None:
        arg = joinType
        if isinstance(joinType, str):
            arg = f'"{joinType}"'
        if isinstance(joinType, bool):
            arg = str(joinType).lower()
        if isinstance(joinType, list):
            arg = '{'
            for index, j in enumerate(joinType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.joinType = {arg}\n'
        
    if joinLv is not None:
        arg = joinLv
        if isinstance(joinLv, str):
            arg = f'"{joinLv}"'
        if isinstance(joinLv, bool):
            arg = str(joinLv).lower()
        if isinstance(joinLv, list):
            arg = '{'
            for index, j in enumerate(joinLv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.joinLv = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildSetGuildInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, targetCharId: string, pos: i32, permission: i32
def get_CSGuildSetMemberPosMsg(addition_part="", source: int = None, guildSimpleId: int = None, targetCharId: str = None, pos: int = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if pos is not None:
        arg = pos
        if isinstance(pos, str):
            arg = f'"{pos}"'
        if isinstance(pos, bool):
            arg = str(pos).lower()
        if isinstance(pos, list):
            arg = '{'
            for index, j in enumerate(pos):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.pos = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildSetMemberPosMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, targetCharId: string, permission: i32
def get_CSGuildTransferPresidentMsg(addition_part="", source: int = None, guildSimpleId: int = None, targetCharId: str = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if targetCharId is not None:
        arg = targetCharId
        if isinstance(targetCharId, str):
            arg = f'"{targetCharId}"'
        if isinstance(targetCharId, bool):
            arg = str(targetCharId).lower()
        if isinstance(targetCharId, list):
            arg = '{'
            for index, j in enumerate(targetCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.targetCharId = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildTransferPresidentMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildMemberQuitMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildMemberQuitMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, title: string, content: string, permission: i32
def get_CSGuildSendMailToAllMsg(addition_part="", source: int = None, guildSimpleId: int = None, title: str = None, content: str = None, permission: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if title is not None:
        arg = title
        if isinstance(title, str):
            arg = f'"{title}"'
        if isinstance(title, bool):
            arg = str(title).lower()
        if isinstance(title, list):
            arg = '{'
            for index, j in enumerate(title):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.title = {arg}\n'
        
    if content is not None:
        arg = content
        if isinstance(content, str):
            arg = f'"{content}"'
        if isinstance(content, bool):
            arg = str(content).lower()
        if isinstance(content, list):
            arg = '{'
            for index, j in enumerate(content):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.content = {arg}\n'
        
    if permission is not None:
        arg = permission
        if isinstance(permission, str):
            arg = f'"{permission}"'
        if isinstance(permission, bool):
            arg = str(permission).lower()
        if isinstance(permission, list):
            arg = '{'
            for index, j in enumerate(permission):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.permission = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildSendMailToAllMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGuildQueryDialogMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildQueryDialogMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, rewardId: i32
def get_CSGameGuildProgressRewardMsg(addition_part="", source: int = None, guildSimpleId: int = None, rewardId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if rewardId is not None:
        arg = rewardId
        if isinstance(rewardId, str):
            arg = f'"{rewardId}"'
        if isinstance(rewardId, bool):
            arg = str(rewardId).lower()
        if isinstance(rewardId, list):
            arg = '{'
            for index, j in enumerate(rewardId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rewardId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGameGuildProgressRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGameGuildReportMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGameGuildReportMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, charSimpleId: i64, charId: string
def get_CSGuildMemberPlayerCardMsg(addition_part="", source: int = None, guildSimpleId: int = None, charSimpleId: int = None, charId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if charSimpleId is not None:
        arg = charSimpleId
        if isinstance(charSimpleId, str):
            arg = f'"{charSimpleId}"'
        if isinstance(charSimpleId, bool):
            arg = str(charSimpleId).lower()
        if isinstance(charSimpleId, list):
            arg = '{'
            for index, j in enumerate(charSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charSimpleId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGuildMemberPlayerCardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64
def get_CSGameGuildSendRedEnvelopeMsg(addition_part="", source: int = None, guildSimpleId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGameGuildSendRedEnvelopeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, guildSimpleId: i64, redEnvelopeId: i64
def get_CSGameGuildRewardRedEnvelopeMsg(addition_part="", source: int = None, guildSimpleId: int = None, redEnvelopeId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if guildSimpleId is not None:
        arg = guildSimpleId
        if isinstance(guildSimpleId, str):
            arg = f'"{guildSimpleId}"'
        if isinstance(guildSimpleId, bool):
            arg = str(guildSimpleId).lower()
        if isinstance(guildSimpleId, list):
            arg = '{'
            for index, j in enumerate(guildSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.guildSimpleId = {arg}\n'
        
    if redEnvelopeId is not None:
        arg = redEnvelopeId
        if isinstance(redEnvelopeId, str):
            arg = f'"{redEnvelopeId}"'
        if isinstance(redEnvelopeId, bool):
            arg = str(redEnvelopeId).lower()
        if isinstance(redEnvelopeId, list):
            arg = '{'
            for index, j in enumerate(redEnvelopeId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.redEnvelopeId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGameGuildRewardRedEnvelopeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64, stage: i32, digXs: list<i32>, digYs: list<i32>
def get_CSHiddenTreasureDigMsg(addition_part="", groupId: int = None, roomId: int = None, stage: int = None, digXs: list = None, digYs: list = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if stage is not None:
        arg = stage
        if isinstance(stage, str):
            arg = f'"{stage}"'
        if isinstance(stage, bool):
            arg = str(stage).lower()
        if isinstance(stage, list):
            arg = '{'
            for index, j in enumerate(stage):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.stage = {arg}\n'
        
    if digXs is not None:
        arg = digXs
        if isinstance(digXs, str):
            arg = f'"{digXs}"'
        if isinstance(digXs, bool):
            arg = str(digXs).lower()
        if isinstance(digXs, list):
            arg = '{'
            for index, j in enumerate(digXs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.digXs = {arg}\n'
        
    if digYs is not None:
        arg = digYs
        if isinstance(digYs, str):
            arg = f'"{digYs}"'
        if isinstance(digYs, bool):
            arg = str(digYs).lower()
        if isinstance(digYs, list):
            arg = '{'
            for index, j in enumerate(digYs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.digYs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSHiddenTreasureDigMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64, stage: i32, multiple: i32
def get_CSHiddenTreasureSetMultipleMsg(addition_part="", groupId: int = None, roomId: int = None, stage: int = None, multiple: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if stage is not None:
        arg = stage
        if isinstance(stage, str):
            arg = f'"{stage}"'
        if isinstance(stage, bool):
            arg = str(stage).lower()
        if isinstance(stage, list):
            arg = '{'
            for index, j in enumerate(stage):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.stage = {arg}\n'
        
    if multiple is not None:
        arg = multiple
        if isinstance(multiple, str):
            arg = f'"{multiple}"'
        if isinstance(multiple, bool):
            arg = str(multiple).lower()
        if isinstance(multiple, list):
            arg = '{'
            for index, j in enumerate(multiple):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.multiple = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSHiddenTreasureSetMultipleMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64, fromRank: i32, count: i32
def get_CSHiddenTreasureQueryRankMsg(addition_part="", groupId: int = None, roomId: int = None, fromRank: int = None, count: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSHiddenTreasureQueryRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64
def get_CSHiddenTreasureGetProgressRewardMsg(addition_part="", groupId: int = None, roomId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSHiddenTreasureGetProgressRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # starNum: i32
def get_CSIOSStarNumMsg(addition_part="", starNum: int = None):
    cmd_part = ''
    if starNum is not None:
        arg = starNum
        if isinstance(starNum, str):
            arg = f'"{starNum}"'
        if isinstance(starNum, bool):
            arg = str(starNum).lower()
        if isinstance(starNum, list):
            arg = '{'
            for index, j in enumerate(starNum):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.starNum = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSIOSStarNumMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSLoginAuthMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSLoginAuthMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSLoginMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSLoginMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSReconnectMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSReconnectMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSQueryServerListInfoMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryServerListInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSSwitchRealmMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSwitchRealmMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSQueryLoginIdxMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryLoginIdxMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSQuerySdkBoundSnsMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQuerySdkBoundSnsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSEnterGameMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSEnterGameMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # needReEnter: bool
def get_CSReEnterGameMsg(addition_part="", needReEnter: bool = None):
    cmd_part = ''
    if needReEnter is not None:
        arg = needReEnter
        if isinstance(needReEnter, str):
            arg = f'"{needReEnter}"'
        if isinstance(needReEnter, bool):
            arg = str(needReEnter).lower()
        if isinstance(needReEnter, list):
            arg = '{'
            for index, j in enumerate(needReEnter):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.needReEnter = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSReEnterGameMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32
def get_CSLotteryDrawOnceMsg(addition_part="", groupId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSLotteryDrawOnceMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32
def get_CSLotteryDrawRoundMsg(addition_part="", groupId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSLotteryDrawRoundMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # mailId: i64
def get_CSMailReadMsg(addition_part="", mailId: int = None):
    cmd_part = ''
    if mailId is not None:
        arg = mailId
        if isinstance(mailId, str):
            arg = f'"{mailId}"'
        if isinstance(mailId, bool):
            arg = str(mailId).lower()
        if isinstance(mailId, list):
            arg = '{'
            for index, j in enumerate(mailId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.mailId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMailReadMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # mailIds: list<i64>
def get_CSMailDeleteAllReadMsg(addition_part="", mailIds: list = None):
    cmd_part = ''
    if mailIds is not None:
        arg = mailIds
        if isinstance(mailIds, str):
            arg = f'"{mailIds}"'
        if isinstance(mailIds, bool):
            arg = str(mailIds).lower()
        if isinstance(mailIds, list):
            arg = '{'
            for index, j in enumerate(mailIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.mailIds = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMailDeleteAllReadMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # mailId: i64
def get_CSMailGetAttachmentsMsg(addition_part="", mailId: int = None):
    cmd_part = ''
    if mailId is not None:
        arg = mailId
        if isinstance(mailId, str):
            arg = f'"{mailId}"'
        if isinstance(mailId, bool):
            arg = str(mailId).lower()
        if isinstance(mailId, list):
            arg = '{'
            for index, j in enumerate(mailId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.mailId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMailGetAttachmentsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSMailGetAllAttachmentsMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMailGetAllAttachmentsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # mailIds: list<i64>
def get_CSMailGetIdsAttachmentsMsg(addition_part="", mailIds: list = None):
    cmd_part = ''
    if mailIds is not None:
        arg = mailIds
        if isinstance(mailIds, str):
            arg = f'"{mailIds}"'
        if isinstance(mailIds, bool):
            arg = str(mailIds).lower()
        if isinstance(mailIds, list):
            arg = '{'
            for index, j in enumerate(mailIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.mailIds = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMailGetIdsAttachmentsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSGetMissionMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGetMissionMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # missionType: i32
def get_CSClearFailMissionMsg(addition_part="", missionType: int = None):
    cmd_part = ''
    if missionType is not None:
        arg = missionType
        if isinstance(missionType, str):
            arg = f'"{missionType}"'
        if isinstance(missionType, bool):
            arg = str(missionType).lower()
        if isinstance(missionType, list):
            arg = '{'
            for index, j in enumerate(missionType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.missionType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSClearFailMissionMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # missionType: i32
def get_CSGetMissionRewardsMsg(addition_part="", missionType: int = None):
    cmd_part = ''
    if missionType is not None:
        arg = missionType
        if isinstance(missionType, str):
            arg = f'"{missionType}"'
        if isinstance(missionType, bool):
            arg = str(missionType).lower()
        if isinstance(missionType, list):
            arg = '{'
            for index, j in enumerate(missionType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.missionType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGetMissionRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSJumpMissionMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSJumpMissionMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64, multiple: i32
def get_CSMonopolyRollDiceMsg(addition_part="", groupId: int = None, roomId: int = None, multiple: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if multiple is not None:
        arg = multiple
        if isinstance(multiple, str):
            arg = f'"{multiple}"'
        if isinstance(multiple, bool):
            arg = str(multiple).lower()
        if isinstance(multiple, list):
            arg = '{'
            for index, j in enumerate(multiple):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.multiple = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMonopolyRollDiceMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64, fromRank: i32, count: i32
def get_CSMonopolyQueryRankMsg(addition_part="", groupId: int = None, roomId: int = None, fromRank: int = None, count: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMonopolyQueryRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64
def get_CSMonopolyGetProgressRewardMsg(addition_part="", groupId: int = None, roomId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMonopolyGetProgressRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64
def get_CSMonopolyQueryFreeDiceMsg(addition_part="", groupId: int = None, roomId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMonopolyQueryFreeDiceMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, matcherId: i64, fishSceneTpId: i32
def get_CSGlobalEnterDormitoryMsg(addition_part="", source: int = None, matcherId: int = None, fishSceneTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if matcherId is not None:
        arg = matcherId
        if isinstance(matcherId, str):
            arg = f'"{matcherId}"'
        if isinstance(matcherId, bool):
            arg = str(matcherId).lower()
        if isinstance(matcherId, list):
            arg = '{'
            for index, j in enumerate(matcherId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.matcherId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalEnterDormitoryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, type: i32
def get_CSGlobalQueryRoomMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, type: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalQueryRoomMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, newFishSceneTpId: i32
def get_CSGlobalExchangeDormitoryMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, newFishSceneTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if newFishSceneTpId is not None:
        arg = newFishSceneTpId
        if isinstance(newFishSceneTpId, str):
            arg = f'"{newFishSceneTpId}"'
        if isinstance(newFishSceneTpId, bool):
            arg = str(newFishSceneTpId).lower()
        if isinstance(newFishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(newFishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.newFishSceneTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalExchangeDormitoryMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, charId: string
def get_CSGlobalExchangeTeamMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, charId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalExchangeTeamMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, eventType: i32, otherArgs: list<string>
def get_CSGlobalRoomEventMsg(addition_part="", source: int = None, roomId: int = None, eventType: int = None, otherArgs: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if eventType is not None:
        arg = eventType
        if isinstance(eventType, str):
            arg = f'"{eventType}"'
        if isinstance(eventType, bool):
            arg = str(eventType).lower()
        if isinstance(eventType, list):
            arg = '{'
            for index, j in enumerate(eventType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.eventType = {arg}\n'
        
    if otherArgs is not None:
        arg = otherArgs
        if isinstance(otherArgs, str):
            arg = f'"{otherArgs}"'
        if isinstance(otherArgs, bool):
            arg = str(otherArgs).lower()
        if isinstance(otherArgs, list):
            arg = '{'
            for index, j in enumerate(otherArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.otherArgs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalRoomEventMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, charId: string, fishSceneTpId: i32
def get_CSGlobalTeamRoomInviteMsg(addition_part="", source: int = None, roomId: int = None, charId: str = None, fishSceneTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalTeamRoomInviteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32
def get_CSGlobalTeamRoomInviteAcceptMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalTeamRoomInviteAcceptMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, result: i32, inviteRoomId: i32, inviteCharId: string
def get_CSGlobalTeamRoomInviteReplyMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, result: int = None, inviteRoomId: int = None, inviteCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if result is not None:
        arg = result
        if isinstance(result, str):
            arg = f'"{result}"'
        if isinstance(result, bool):
            arg = str(result).lower()
        if isinstance(result, list):
            arg = '{'
            for index, j in enumerate(result):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.result = {arg}\n'
        
    if inviteRoomId is not None:
        arg = inviteRoomId
        if isinstance(inviteRoomId, str):
            arg = f'"{inviteRoomId}"'
        if isinstance(inviteRoomId, bool):
            arg = str(inviteRoomId).lower()
        if isinstance(inviteRoomId, list):
            arg = '{'
            for index, j in enumerate(inviteRoomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.inviteRoomId = {arg}\n'
        
    if inviteCharId is not None:
        arg = inviteCharId
        if isinstance(inviteCharId, str):
            arg = f'"{inviteCharId}"'
        if isinstance(inviteCharId, bool):
            arg = str(inviteCharId).lower()
        if isinstance(inviteCharId, list):
            arg = '{'
            for index, j in enumerate(inviteCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.inviteCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalTeamRoomInviteReplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, type: i32
def get_CSGlobalQuitRoomMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, type: int = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalQuitRoomMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, type: i32, deleteCharId: string
def get_CSGlobalTeamRoomDeleteMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, type: int = None, deleteCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if deleteCharId is not None:
        arg = deleteCharId
        if isinstance(deleteCharId, str):
            arg = f'"{deleteCharId}"'
        if isinstance(deleteCharId, bool):
            arg = str(deleteCharId).lower()
        if isinstance(deleteCharId, list):
            arg = '{'
            for index, j in enumerate(deleteCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.deleteCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalTeamRoomDeleteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, type: i32, ownerCharId: string
def get_CSGlobalTeamRoomOwnerMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, type: int = None, ownerCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if ownerCharId is not None:
        arg = ownerCharId
        if isinstance(ownerCharId, str):
            arg = f'"{ownerCharId}"'
        if isinstance(ownerCharId, bool):
            arg = str(ownerCharId).lower()
        if isinstance(ownerCharId, list):
            arg = '{'
            for index, j in enumerate(ownerCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.ownerCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalTeamRoomOwnerMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, type: i32, likeCharId: string
def get_CSGlobalRoomLikeMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, type: int = None, likeCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if likeCharId is not None:
        arg = likeCharId
        if isinstance(likeCharId, str):
            arg = f'"{likeCharId}"'
        if isinstance(likeCharId, bool):
            arg = str(likeCharId).lower()
        if isinstance(likeCharId, list):
            arg = '{'
            for index, j in enumerate(likeCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.likeCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalRoomLikeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, type: i32, replyCharId: string
def get_CSGlobalRoomLikeQuickReplyMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, type: int = None, replyCharId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if replyCharId is not None:
        arg = replyCharId
        if isinstance(replyCharId, str):
            arg = f'"{replyCharId}"'
        if isinstance(replyCharId, bool):
            arg = str(replyCharId).lower()
        if isinstance(replyCharId, list):
            arg = '{'
            for index, j in enumerate(replyCharId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.replyCharId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalRoomLikeQuickReplyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, roomId: i64, fishSceneTpId: i32, charId: string
def get_CSGlobalCreateTeamInviteMsg(addition_part="", source: int = None, roomId: int = None, fishSceneTpId: int = None, charId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fishSceneTpId is not None:
        arg = fishSceneTpId
        if isinstance(fishSceneTpId, str):
            arg = f'"{fishSceneTpId}"'
        if isinstance(fishSceneTpId, bool):
            arg = str(fishSceneTpId).lower()
        if isinstance(fishSceneTpId, list):
            arg = '{'
            for index, j in enumerate(fishSceneTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fishSceneTpId = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGlobalCreateTeamInviteMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # key: string
def get_CSNewGuideStoreMsg(addition_part="", key: str = None):
    cmd_part = ''
    if key is not None:
        arg = key
        if isinstance(key, str):
            arg = f'"{key}"'
        if isinstance(key, bool):
            arg = str(key).lower()
        if isinstance(key, list):
            arg = '{'
            for index, j in enumerate(key):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.key = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSNewGuideStoreMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32
def get_CSNDaysEventGetTokenRewardsMsg(addition_part="", groupId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSNDaysEventGetTokenRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, roomId: i64, fromRank: i32, count: i32
def get_CSNDaysEventQueryRankMsg(addition_part="", groupId: int = None, roomId: int = None, fromRank: int = None, count: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if roomId is not None:
        arg = roomId
        if isinstance(roomId, str):
            arg = f'"{roomId}"'
        if isinstance(roomId, bool):
            arg = str(roomId).lower()
        if isinstance(roomId, list):
            arg = '{'
            for index, j in enumerate(roomId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.roomId = {arg}\n'
        
    if fromRank is not None:
        arg = fromRank
        if isinstance(fromRank, str):
            arg = f'"{fromRank}"'
        if isinstance(fromRank, bool):
            arg = str(fromRank).lower()
        if isinstance(fromRank, list):
            arg = '{'
            for index, j in enumerate(fromRank):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.fromRank = {arg}\n'
        
    if count is not None:
        arg = count
        if isinstance(count, str):
            arg = f'"{count}"'
        if isinstance(count, bool):
            arg = str(count).lower()
        if isinstance(count, list):
            arg = '{'
            for index, j in enumerate(count):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.count = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSNDaysEventQueryRankMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # cardTpId: i32
def get_CSPaymentMonthCardGetRewardsMsg(addition_part="", cardTpId: int = None):
    cmd_part = ''
    if cardTpId is not None:
        arg = cardTpId
        if isinstance(cardTpId, str):
            arg = f'"{cardTpId}"'
        if isinstance(cardTpId, bool):
            arg = str(cardTpId).lower()
        if isinstance(cardTpId, list):
            arg = '{'
            for index, j in enumerate(cardTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.cardTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSPaymentMonthCardGetRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, orderType: i32, goodsId: i32, useVouchers: bool, extArg1: i32, extArg2: i32, extArgs: list<i32>
def get_CSPaymentBuyMsg(addition_part="", source: int = None, orderType: int = None, goodsId: int = None, useVouchers: bool = None, extArg1: int = None, extArg2: int = None, extArgs: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if orderType is not None:
        arg = orderType
        if isinstance(orderType, str):
            arg = f'"{orderType}"'
        if isinstance(orderType, bool):
            arg = str(orderType).lower()
        if isinstance(orderType, list):
            arg = '{'
            for index, j in enumerate(orderType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.orderType = {arg}\n'
        
    if goodsId is not None:
        arg = goodsId
        if isinstance(goodsId, str):
            arg = f'"{goodsId}"'
        if isinstance(goodsId, bool):
            arg = str(goodsId).lower()
        if isinstance(goodsId, list):
            arg = '{'
            for index, j in enumerate(goodsId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.goodsId = {arg}\n'
        
    if useVouchers is not None:
        arg = useVouchers
        if isinstance(useVouchers, str):
            arg = f'"{useVouchers}"'
        if isinstance(useVouchers, bool):
            arg = str(useVouchers).lower()
        if isinstance(useVouchers, list):
            arg = '{'
            for index, j in enumerate(useVouchers):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.useVouchers = {arg}\n'
        
    if extArg1 is not None:
        arg = extArg1
        if isinstance(extArg1, str):
            arg = f'"{extArg1}"'
        if isinstance(extArg1, bool):
            arg = str(extArg1).lower()
        if isinstance(extArg1, list):
            arg = '{'
            for index, j in enumerate(extArg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.extArg1 = {arg}\n'
        
    if extArg2 is not None:
        arg = extArg2
        if isinstance(extArg2, str):
            arg = f'"{extArg2}"'
        if isinstance(extArg2, bool):
            arg = str(extArg2).lower()
        if isinstance(extArg2, list):
            arg = '{'
            for index, j in enumerate(extArg2):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.extArg2 = {arg}\n'
        
    if extArgs is not None:
        arg = extArgs
        if isinstance(extArgs, str):
            arg = f'"{extArgs}"'
        if isinstance(extArgs, bool):
            arg = str(extArgs).lower()
        if isinstance(extArgs, list):
            arg = '{'
            for index, j in enumerate(extArgs):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.extArgs = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSPaymentBuyMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSProgressRewardMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSProgressRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # challengeTpId: i32
def get_CSRepeatableChallengeGetRewardsMsg(addition_part="", challengeTpId: int = None):
    cmd_part = ''
    if challengeTpId is not None:
        arg = challengeTpId
        if isinstance(challengeTpId, str):
            arg = f'"{challengeTpId}"'
        if isinstance(challengeTpId, bool):
            arg = str(challengeTpId).lower()
        if isinstance(challengeTpId, list):
            arg = '{'
            for index, j in enumerate(challengeTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.challengeTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSRepeatableChallengeGetRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # rodId: i32, useType2Id: map<enums.RodAttachType,i32>
def get_CSSaveRodAttachMsg(addition_part="", rodId: int = None, useType2Id: dict = None):
    cmd_part = ''
    if rodId is not None:
        arg = rodId
        if isinstance(rodId, str):
            arg = f'"{rodId}"'
        if isinstance(rodId, bool):
            arg = str(rodId).lower()
        if isinstance(rodId, list):
            arg = '{'
            for index, j in enumerate(rodId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.rodId = {arg}\n'
        
    if useType2Id is not None:
        arg = useType2Id
        if isinstance(useType2Id, str):
            arg = f'"{useType2Id}"'
        if isinstance(useType2Id, bool):
            arg = str(useType2Id).lower()
        if isinstance(useType2Id, list):
            arg = '{'
            for index, j in enumerate(useType2Id):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.useType2Id = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSaveRodAttachMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # type: i32, attachId: i32
def get_CSSeeRodAttachMsg(addition_part="", type: int = None, attachId: int = None):
    cmd_part = ''
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    if attachId is not None:
        arg = attachId
        if isinstance(attachId, str):
            arg = f'"{attachId}"'
        if isinstance(attachId, bool):
            arg = str(attachId).lower()
        if isinstance(attachId, list):
            arg = '{'
            for index, j in enumerate(attachId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.attachId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSeeRodAttachMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSUpdateRodAttachDBMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSUpdateRodAttachDBMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # tpId: i32
def get_CSOneKeyWearRodAttachMsg(addition_part="", tpId: int = None):
    cmd_part = ''
    if tpId is not None:
        arg = tpId
        if isinstance(tpId, str):
            arg = f'"{tpId}"'
        if isinstance(tpId, bool):
            arg = str(tpId).lower()
        if isinstance(tpId, list):
            arg = '{'
            for index, j in enumerate(tpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.tpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSOneKeyWearRodAttachMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32, lv: i32
def get_CSRouletteDrawMsg(addition_part="", groupId: int = None, lv: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    if lv is not None:
        arg = lv
        if isinstance(lv, str):
            arg = f'"{lv}"'
        if isinstance(lv, bool):
            arg = str(lv).lower()
        if isinstance(lv, list):
            arg = '{'
            for index, j in enumerate(lv):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.lv = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSRouletteDrawMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # charId: string, group: i32, groupArg: i32, groupArg1: i32, groupArg2: i32, type: i32
def get_CSSelfRankLikesMsg(addition_part="", charId: str = None, group: int = None, groupArg: int = None, groupArg1: int = None, groupArg2: int = None, type: int = None):
    cmd_part = ''
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    if group is not None:
        arg = group
        if isinstance(group, str):
            arg = f'"{group}"'
        if isinstance(group, bool):
            arg = str(group).lower()
        if isinstance(group, list):
            arg = '{'
            for index, j in enumerate(group):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.group = {arg}\n'
        
    if groupArg is not None:
        arg = groupArg
        if isinstance(groupArg, str):
            arg = f'"{groupArg}"'
        if isinstance(groupArg, bool):
            arg = str(groupArg).lower()
        if isinstance(groupArg, list):
            arg = '{'
            for index, j in enumerate(groupArg):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg = {arg}\n'
        
    if groupArg1 is not None:
        arg = groupArg1
        if isinstance(groupArg1, str):
            arg = f'"{groupArg1}"'
        if isinstance(groupArg1, bool):
            arg = str(groupArg1).lower()
        if isinstance(groupArg1, list):
            arg = '{'
            for index, j in enumerate(groupArg1):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg1 = {arg}\n'
        
    if groupArg2 is not None:
        arg = groupArg2
        if isinstance(groupArg2, str):
            arg = f'"{groupArg2}"'
        if isinstance(groupArg2, bool):
            arg = str(groupArg2).lower()
        if isinstance(groupArg2, list):
            arg = '{'
            for index, j in enumerate(groupArg2):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupArg2 = {arg}\n'
        
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSelfRankLikesMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # timeType: i32
def get_CSSelfRankRecordMsg(addition_part="", timeType: int = None):
    cmd_part = ''
    if timeType is not None:
        arg = timeType
        if isinstance(timeType, str):
            arg = f'"{timeType}"'
        if isinstance(timeType, bool):
            arg = str(timeType).lower()
        if isinstance(timeType, list):
            arg = '{'
            for index, j in enumerate(timeType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.timeType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSelfRankRecordMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # city: i32, cancel: bool
def get_CSSelfRankCityChangeMsg(addition_part="", city: int = None, cancel: bool = None):
    cmd_part = ''
    if city is not None:
        arg = city
        if isinstance(city, str):
            arg = f'"{city}"'
        if isinstance(city, bool):
            arg = str(city).lower()
        if isinstance(city, list):
            arg = '{'
            for index, j in enumerate(city):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.city = {arg}\n'
        
    if cancel is not None:
        arg = cancel
        if isinstance(cancel, str):
            arg = f'"{cancel}"'
        if isinstance(cancel, bool):
            arg = str(cancel).lower()
        if isinstance(cancel, list):
            arg = '{'
            for index, j in enumerate(cancel):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.cancel = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSelfRankCityChangeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # shopTpId: i32
def get_CSShopRefreshMsg(addition_part="", shopTpId: int = None):
    cmd_part = ''
    if shopTpId is not None:
        arg = shopTpId
        if isinstance(shopTpId, str):
            arg = f'"{shopTpId}"'
        if isinstance(shopTpId, bool):
            arg = str(shopTpId).lower()
        if isinstance(shopTpId, list):
            arg = '{'
            for index, j in enumerate(shopTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.shopTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSShopRefreshMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # shopTpId: i32, goodsId: i32, refreshIdx: i32, buyTimes: i32
def get_CSShopBuyItemMsg(addition_part="", shopTpId: int = None, goodsId: int = None, refreshIdx: int = None, buyTimes: int = None):
    cmd_part = ''
    if shopTpId is not None:
        arg = shopTpId
        if isinstance(shopTpId, str):
            arg = f'"{shopTpId}"'
        if isinstance(shopTpId, bool):
            arg = str(shopTpId).lower()
        if isinstance(shopTpId, list):
            arg = '{'
            for index, j in enumerate(shopTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.shopTpId = {arg}\n'
        
    if goodsId is not None:
        arg = goodsId
        if isinstance(goodsId, str):
            arg = f'"{goodsId}"'
        if isinstance(goodsId, bool):
            arg = str(goodsId).lower()
        if isinstance(goodsId, list):
            arg = '{'
            for index, j in enumerate(goodsId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.goodsId = {arg}\n'
        
    if refreshIdx is not None:
        arg = refreshIdx
        if isinstance(refreshIdx, str):
            arg = f'"{refreshIdx}"'
        if isinstance(refreshIdx, bool):
            arg = str(refreshIdx).lower()
        if isinstance(refreshIdx, list):
            arg = '{'
            for index, j in enumerate(refreshIdx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.refreshIdx = {arg}\n'
        
    if buyTimes is not None:
        arg = buyTimes
        if isinstance(buyTimes, str):
            arg = f'"{buyTimes}"'
        if isinstance(buyTimes, bool):
            arg = str(buyTimes).lower()
        if isinstance(buyTimes, list):
            arg = '{'
            for index, j in enumerate(buyTimes):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.buyTimes = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSShopBuyItemMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # groupId: i32
def get_CSSignGiftSignMsg(addition_part="", groupId: int = None):
    cmd_part = ''
    if groupId is not None:
        arg = groupId
        if isinstance(groupId, str):
            arg = f'"{groupId}"'
        if isinstance(groupId, bool):
            arg = str(groupId).lower()
        if isinstance(groupId, list):
            arg = '{'
            for index, j in enumerate(groupId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.groupId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSSignGiftSignMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # beReportCharaId: string, reportTypes: list<enums.ReportType>, desc: string, content: string, beReportSimpleId: i64, channelId: i64
def get_CSReportMsg(addition_part="", beReportCharaId: str = None, reportTypes: list = None, desc: str = None, content: str = None, beReportSimpleId: int = None, channelId: int = None):
    cmd_part = ''
    if beReportCharaId is not None:
        arg = beReportCharaId
        if isinstance(beReportCharaId, str):
            arg = f'"{beReportCharaId}"'
        if isinstance(beReportCharaId, bool):
            arg = str(beReportCharaId).lower()
        if isinstance(beReportCharaId, list):
            arg = '{'
            for index, j in enumerate(beReportCharaId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.beReportCharaId = {arg}\n'
        
    if reportTypes is not None:
        arg = reportTypes
        if isinstance(reportTypes, str):
            arg = f'"{reportTypes}"'
        if isinstance(reportTypes, bool):
            arg = str(reportTypes).lower()
        if isinstance(reportTypes, list):
            arg = '{'
            for index, j in enumerate(reportTypes):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.reportTypes = {arg}\n'
        
    if desc is not None:
        arg = desc
        if isinstance(desc, str):
            arg = f'"{desc}"'
        if isinstance(desc, bool):
            arg = str(desc).lower()
        if isinstance(desc, list):
            arg = '{'
            for index, j in enumerate(desc):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.desc = {arg}\n'
        
    if content is not None:
        arg = content
        if isinstance(content, str):
            arg = f'"{content}"'
        if isinstance(content, bool):
            arg = str(content).lower()
        if isinstance(content, list):
            arg = '{'
            for index, j in enumerate(content):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.content = {arg}\n'
        
    if beReportSimpleId is not None:
        arg = beReportSimpleId
        if isinstance(beReportSimpleId, str):
            arg = f'"{beReportSimpleId}"'
        if isinstance(beReportSimpleId, bool):
            arg = str(beReportSimpleId).lower()
        if isinstance(beReportSimpleId, list):
            arg = '{'
            for index, j in enumerate(beReportSimpleId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.beReportSimpleId = {arg}\n'
        
    if channelId is not None:
        arg = channelId
        if isinstance(channelId, str):
            arg = f'"{channelId}"'
        if isinstance(channelId, bool):
            arg = str(channelId).lower()
        if isinstance(channelId, list):
            arg = '{'
            for index, j in enumerate(channelId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.channelId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSReportMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSDoneSharingMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDoneSharingMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # followType: i32
def get_CSDoneFollowMsg(addition_part="", followType: int = None):
    cmd_part = ''
    if followType is not None:
        arg = followType
        if isinstance(followType, str):
            arg = f'"{followType}"'
        if isinstance(followType, bool):
            arg = str(followType).lower()
        if isinstance(followType, list):
            arg = '{'
            for index, j in enumerate(followType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.followType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDoneFollowMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # questionTpId: i32
def get_CSDoneQuestionnaireMsg(addition_part="", questionTpId: int = None):
    cmd_part = ''
    if questionTpId is not None:
        arg = questionTpId
        if isinstance(questionTpId, str):
            arg = f'"{questionTpId}"'
        if isinstance(questionTpId, bool):
            arg = str(questionTpId).lower()
        if isinstance(questionTpId, list):
            arg = '{'
            for index, j in enumerate(questionTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.questionTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDoneQuestionnaireMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # cellTpId: i32, answerLis: list<QuestionnaireAnswer>
def get_CSDoneQuestionnaireCell(addition_part="", cellTpId: int = None, answerLis: list = None):
    cmd_part = ''
    if cellTpId is not None:
        arg = cellTpId
        if isinstance(cellTpId, str):
            arg = f'"{cellTpId}"'
        if isinstance(cellTpId, bool):
            arg = str(cellTpId).lower()
        if isinstance(cellTpId, list):
            arg = '{'
            for index, j in enumerate(cellTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.cellTpId = {arg}\n'
        
    if answerLis is not None:
        arg = answerLis
        if isinstance(answerLis, str):
            arg = f'"{answerLis}"'
        if isinstance(answerLis, bool):
            arg = str(answerLis).lower()
        if isinstance(answerLis, list):
            arg = '{'
            for index, j in enumerate(answerLis):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.answerLis = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSDoneQuestionnaireCell")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # selectIdx: i32, content: string
def get_QuestionnaireAnswer(addition_part="", selectIdx: int = None, content: str = None):
    cmd_part = ''
    if selectIdx is not None:
        arg = selectIdx
        if isinstance(selectIdx, str):
            arg = f'"{selectIdx}"'
        if isinstance(selectIdx, bool):
            arg = str(selectIdx).lower()
        if isinstance(selectIdx, list):
            arg = '{'
            for index, j in enumerate(selectIdx):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.selectIdx = {arg}\n'
        
    if content is not None:
        arg = content
        if isinstance(content, str):
            arg = f'"{content}"'
        if isinstance(content, bool):
            arg = str(content).lower()
        if isinstance(content, list):
            arg = '{'
            for index, j in enumerate(content):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.content = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("QuestionnaireAnswer")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # dlcNodeId: i32
def get_CSGetDLCNodeRewardsMsg(addition_part="", dlcNodeId: int = None):
    cmd_part = ''
    if dlcNodeId is not None:
        arg = dlcNodeId
        if isinstance(dlcNodeId, str):
            arg = f'"{dlcNodeId}"'
        if isinstance(dlcNodeId, bool):
            arg = str(dlcNodeId).lower()
        if isinstance(dlcNodeId, list):
            arg = '{'
            for index, j in enumerate(dlcNodeId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.dlcNodeId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSGetDLCNodeRewardsMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # type: i32
def get_CSModuleVersionMsg(addition_part="", type: int = None):
    cmd_part = ''
    if type is not None:
        arg = type
        if isinstance(type, str):
            arg = f'"{type}"'
        if isinstance(type, bool):
            arg = str(type).lower()
        if isinstance(type, list):
            arg = '{'
            for index, j in enumerate(type):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.type = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSModuleVersionMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # taskId: i32
def get_CSFinishCommunityTaskMsg(addition_part="", taskId: int = None):
    cmd_part = ''
    if taskId is not None:
        arg = taskId
        if isinstance(taskId, str):
            arg = f'"{taskId}"'
        if isinstance(taskId, bool):
            arg = str(taskId).lower()
        if isinstance(taskId, list):
            arg = '{'
            for index, j in enumerate(taskId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.taskId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFinishCommunityTaskMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # taskId: i32
def get_CSRecCommunityTaskRewardMsg(addition_part="", taskId: int = None):
    cmd_part = ''
    if taskId is not None:
        arg = taskId
        if isinstance(taskId, str):
            arg = f'"{taskId}"'
        if isinstance(taskId, bool):
            arg = str(taskId).lower()
        if isinstance(taskId, list):
            arg = '{'
            for index, j in enumerate(taskId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.taskId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSRecCommunityTaskRewardMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # 
def get_CSMarqueeMsg(addition_part="", ):
    cmd_part = ''
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSMarqueeMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # clientTime: double, flag: i8
def get_CSPingMsg(addition_part="", clientTime: float = None, flag: int = None):
    cmd_part = ''
    if clientTime is not None:
        arg = clientTime
        if isinstance(clientTime, str):
            arg = f'"{clientTime}"'
        if isinstance(clientTime, bool):
            arg = str(clientTime).lower()
        if isinstance(clientTime, list):
            arg = '{'
            for index, j in enumerate(clientTime):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.clientTime = {arg}\n'
        
    if flag is not None:
        arg = flag
        if isinstance(flag, str):
            arg = f'"{flag}"'
        if isinstance(flag, bool):
            arg = str(flag).lower()
        if isinstance(flag, list):
            arg = '{'
            for index, j in enumerate(flag):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.flag = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSPingMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, charId: string
def get_CSQueryCharInfoMsg(addition_part="", source: int = None, charId: str = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if charId is not None:
        arg = charId
        if isinstance(charId, str):
            arg = f'"{charId}"'
        if isinstance(charId, bool):
            arg = str(charId).lower()
        if isinstance(charId, list):
            arg = '{'
            for index, j in enumerate(charId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.charId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSQueryCharInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # idOrName: string
def get_CSLikeQueryCharInfoMsg(addition_part="", idOrName: str = None):
    cmd_part = ''
    if idOrName is not None:
        arg = idOrName
        if isinstance(idOrName, str):
            arg = f'"{idOrName}"'
        if isinstance(idOrName, bool):
            arg = str(idOrName).lower()
        if isinstance(idOrName, list):
            arg = '{'
            for index, j in enumerate(idOrName):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.idOrName = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSLikeQueryCharInfoMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # source: i16, orderIds: list<string>
def get_CSRecordPaymentMsg(addition_part="", source: int = None, orderIds: list = None):
    cmd_part = ''
    if source is not None:
        arg = source
        if isinstance(source, str):
            arg = f'"{source}"'
        if isinstance(source, bool):
            arg = str(source).lower()
        if isinstance(source, list):
            arg = '{'
            for index, j in enumerate(source):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.source = {arg}\n'
        
    if orderIds is not None:
        arg = orderIds
        if isinstance(orderIds, str):
            arg = f'"{orderIds}"'
        if isinstance(orderIds, bool):
            arg = str(orderIds).lower()
        if isinstance(orderIds, list):
            arg = '{'
            for index, j in enumerate(orderIds):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.orderIds = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSRecordPaymentMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # talentTpId: i32
def get_CSTalentLvUpMsg(addition_part="", talentTpId: int = None):
    cmd_part = ''
    if talentTpId is not None:
        arg = talentTpId
        if isinstance(talentTpId, str):
            arg = f'"{talentTpId}"'
        if isinstance(talentTpId, bool):
            arg = str(talentTpId).lower()
        if isinstance(talentTpId, list):
            arg = '{'
            for index, j in enumerate(talentTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.talentTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSTalentLvUpMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # talentTpId: i32
def get_CSTalentUnlockMsg(addition_part="", talentTpId: int = None):
    cmd_part = ''
    if talentTpId is not None:
        arg = talentTpId
        if isinstance(talentTpId, str):
            arg = f'"{talentTpId}"'
        if isinstance(talentTpId, bool):
            arg = str(talentTpId).lower()
        if isinstance(talentTpId, list):
            arg = '{'
            for index, j in enumerate(talentTpId):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.talentTpId = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSTalentUnlockMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    

# # triggerType: i32
def get_CSTriggerGiftTryTriggerMsg(addition_part="", triggerType: int = None):
    cmd_part = ''
    if triggerType is not None:
        arg = triggerType
        if isinstance(triggerType, str):
            arg = f'"{triggerType}"'
        if isinstance(triggerType, bool):
            arg = str(triggerType).lower()
        if isinstance(triggerType, list):
            arg = '{'
            for index, j in enumerate(triggerType):
                arg += f'[{index + 1}] = {j},'
            arg += '}'
        cmd_part += f'cmd.triggerType = {arg}\n'
        
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSTriggerGiftTryTriggerMsg")\n'
    f'{cmd_part}'
    f'{addition_part}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    
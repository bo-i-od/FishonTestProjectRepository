from slpp import slpp as lua

lua_string ="""<==== [Lua] Receive Net Msg "SCFishingHookMsg" ====>
{
    ["fishes"] =
    {
        [1] =
        {
            ["bsPoint"] = 2645,
            ["weight"] = 12373,
            ["color"] = 10,
            ["point"] = 2645,
            ["beforeMaxStar"] = 6,
            ["tpId"] = 302014,
            ["star"] = 6,
            ["beforeMaxPoint"] = 2490,
            ["colorPoint"] = 2645,
            ["beforeMaxWeight"] = 11896,
            ["seasonSkin"] = 1,
        },
    },
    ["goldAdd"] = 2645,
    ["championshipsItems"] =
    {
    },
    ["otherItems"] =
    {
    },
    ["energyMultiplying"] = 1,
    ["pointAdd"] = 10,
    ["notify"] =
    {
        ["code"] = 0,
        ["msg"] = "success",
    },
    ["result"] = 1,
    ["boosterIds"] =
    {
    },
    ["expAdd"] = 1000,
}"""

lua_string=lua_string.split("\n", 1)[1]

# 解析 Lua 字符串并装换为 Python dict
data = lua.decode(lua_string)

# 输出 Python dict
print(data)
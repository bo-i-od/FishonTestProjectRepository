from slpp import slpp as lua

lua_string ="""
{
	["fishes"] =
	{
		[1] =
		{
			["bsPoint"] = 229500,
			["weight"] = 14496,
			["color"] = 11,
			["point"] = 3040,
			["beforeMaxStar"] = 14,
			["tpId"] = 350110,
			["star"] = 8,
			["beforeMaxPoint"] = 4300,
			["colorPoint"] = 4590,
			["beforeMaxWeight"] = 22155,
			["seasonSkin"] = 0,
		},
	},
	["hasRedEnvelope"] = false,
	["goldAdd"] = 229500,
	["championshipsItems"] =
	{
	},
	["otherItems"] =
	{
	},
	["energyMultiplying"] = 50,
	["pointAdd"] = 500,
	["notify"] =
	{
		["code"] = 0,
		["msg"] = "success",
	},
	["result"] = 1,
	["boosterIds"] =
	{
	},
	["expAdd"] = 90000,
}


"""

lua_string=lua_string.split("\n", 1)[1]

# 解析 Lua 字符串并装换为 Python dict
data = lua.decode(lua_string)

# 输出 Python dict
print(data)
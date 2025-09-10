import csv
import io

raw_data = """
日期	8/11	8/12	8/13	8/14	8/15	8/16	8/17	8/18	8/19	8/20	8/21	8/22	8/23	8/24	8/25	8/26	8/27	8/28	8/29	8/30	8/31	9/1	9/2	9/3	9/4	9/5	9/6	9/7
星期	Mon	Tue	Wed	Thu	Fri	Sat	Sun	Mon	Tue	Wed	Thu	Fri	Sat	Sun	Mon	Tue	Wed	Thu	Fri	Sat	Sun	Mon	Tue	Wed	Thu	Fri	Sat	Sun
活动		夏威夷冒险			温室收益				公路大亨			夏日风格			快餐财富							
		绽放与财富				财富溪流			地产大亨汽车旅馆			利润自助餐										
锦标赛		美黑大战		铺设光荣大道		铺设光荣大道		海滨发球		牧场拉力赛				奢华拍打		富豪级										
		修剪胜利			修剪胜利		火车轨道			水塔漂移		仙人掌环道		徒步奋斗		快艇狂欢		富豪级								
mini game/社区活动/签到活动		豪华掉落							社区黄金闪电战					火车轨道	每日点心（签到）							
		园艺合作伙伴				公路旅行赛车手	社区黄金闪电战			奖品掉落								
			社交连接活动				贴纸掉落					贴纸宝藏										
			社区黄金闪电战					每日点心（签到）										
商业化&礼包		小猪存钱罐		丰收包		特惠贝壳		明信片包		地产利润			选择一个路牌	正餐特惠		软糖好礼							
		丰收包		园艺合作伙伴特惠			沙滩日捆绑包		夏日表情符号特价		公路之旅赛车手特惠			交换包特惠		棕榈树特惠		美食家优惠									
	棕榈树特惠		繁茂特惠		地产利润		选择一个花盆		太阳升起特惠登场		餐馆特惠			炎热特卖	击破特惠			火热储蓄							
		狂野飞跃包			滑道储蓄			顶级狂野			夏季糖果								
	选择一个椰子		财富之泉		一勺特惠	鸣笛储蓄			特惠点唱机		顶级狂野			防护罩冒险			
		生长特惠		击破特惠		夏季糖果			全速前进财富			特惠分配器								
	池边利润		耙扫特惠		铁路冒险						狂野飞跃包		煎饼财富									
	储蓄墨镜									储蓄停靠站			破晓特惠
"""

# 读取为表格
f = io.StringIO(raw_data.strip())
reader = list(csv.reader(f, delimiter='\t'))

# 获取日期行
header_idx = 0
while all(x.strip() == '' for x in reader[header_idx][2:]):
    header_idx += 1
date_row = reader[header_idx]
date_list = date_row[2:]

# 正式处理
activity_list = []
for i in range(header_idx+2, len(reader)):  # 跳过标题行和星期行
    line = reader[i]
    if len(line) < 2 or line[0].strip() == '':
        continue  # 跳过空行
    for idx, activity_name in enumerate(line[2:]):
        activity_name = activity_name.strip()
        if activity_name:
            day = date_list[idx]
            activity_list.append(f'{activity_name} & {day}')

# 输出
for event in activity_list:
    print(event)
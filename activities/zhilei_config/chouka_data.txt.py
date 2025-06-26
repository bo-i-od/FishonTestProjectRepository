round:1:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 5, 0, 2, 5, 3, 1, 3, 3, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 0, 2, 5, 3, 1, 3, 3, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 2, 1, 1, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 1, 1, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:2:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 2, 5, 3, 1, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:3:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[2, 5, 3, 1, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:201, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] times use over! reset to default times:1
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:1, subAllot:(1-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] new random allot subIdxList:[1, 1, 1, 1, 0, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 1, 0, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:4:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5, 3, 1, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:215, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:5:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 1, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 1, 0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:6:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:7:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:8:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:9:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:10:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:11:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 3, 2, 0, 4, 1, 5, 3, 5, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 2, 0, 4, 1, 5, 3, 5, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:12:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 0, 4, 1, 5, 3, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:13:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 4, 1, 5, 3, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:216, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:14:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 1, 5, 3, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:202, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:2, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:0 subAllot:(3-type:17 id:1700015 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700015 count:1

dropResult:[type:17 id:1700015 count:1]dropMergedResult:[type:17 id:1700015 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:15:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 5, 3, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:10

dropResult:[type:97 id:9700004 count:10]dropMergedResult:[type:97 id:9700004 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:16:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 3, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700006 count:1

dropResult:[type:17 id:1700006 count:1]dropMergedResult:[type:17 id:1700006 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:17:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:18:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:19:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:20:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:21:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 4, 5, 3, 4, 3, 0, 3, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 5, 3, 4, 3, 0, 3, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 1, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 0, 2, 1, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0, 2, 1, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:22:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 4, 3, 0, 3, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:23:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 3, 0, 3, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:24:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 3, 0, 3, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:25:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 0, 3, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:26:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 3, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:27:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:203, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:3, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 0, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:28:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:29:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700005 count:1

dropResult:[type:17 id:1700005 count:1]dropMergedResult:[type:17 id:1700005 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:30:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:217, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:31:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[0, 2, 4, 1, 3, 3, 4, 5, 3, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[2, 4, 1, 3, 3, 4, 5, 3, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:204, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:4, subAllot:(4-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 0, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:32:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 1, 3, 3, 4, 5, 3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:218, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:33:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 3, 3, 4, 5, 3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:20

dropResult:[type:97 id:9700004 count:20]dropMergedResult:[type:97 id:9700004 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:34:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 3, 4, 5, 3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:35:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 5, 3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:36:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5, 3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 1, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:37:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:20

dropResult:[type:97 id:9700005 count:20]dropMergedResult:[type:97 id:9700005 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:38:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:39:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:40:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:41:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[1, 4, 3, 3, 4, 5, 3, 0, 2, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 3, 3, 4, 5, 3, 0, 2, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:42:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 3, 4, 5, 3, 0, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 1, 1, 0, 2, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 0, 2, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:43:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 5, 3, 0, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:44:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5, 3, 0, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:45:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 0, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 0, 2, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:46:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 0, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:47:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:48:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:205, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:5, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] new random allot subIdxList:[1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[0, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002028)]
round:49:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:219, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:50:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:51:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 0, 4, 3, 5, 1, 2, 3, 3, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 4, 3, 5, 1, 2, 3, 3, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 0, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:52:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 3, 5, 1, 2, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:206, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:6, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:1 subAllot:(3-type:17 id:1700016 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700016 count:1

dropResult:[type:17 id:1700016 count:1]dropMergedResult:[type:17 id:1700016 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002023), (6-1002022)]
round:53:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 1, 2, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:54:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 1, 2, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:55:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1, 2, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:56:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[2, 3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:57:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:220, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:58:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700002 count:1

dropResult:[type:17 id:1700002 count:1]dropMergedResult:[type:17 id:1700002 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:59:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:60:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:61:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 1, 3, 2, 4, 3, 5, 0, 5, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 3, 2, 4, 3, 5, 0, 5, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 1, 2, 2, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 2, 2, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:62:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 2, 4, 3, 5, 0, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:63:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 4, 3, 5, 0, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:64:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 3, 5, 0, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:221, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:65:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 0, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 2, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:66:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 0, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700002 count:1

dropResult:[type:17 id:1700002 count:1]dropMergedResult:[type:17 id:1700002 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:67:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:68:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:207, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:7, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002033), (5-1002026)]
round:69:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:70:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:71:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 2, 5, 4, 1, 3, 0, 3, 5, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 5, 4, 1, 3, 0, 3, 5, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:20

dropResult:[type:97 id:9700005 count:20]dropMergedResult:[type:97 id:9700005 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:72:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5, 4, 1, 3, 0, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:222, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:73:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 1, 3, 0, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:74:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 3, 0, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:75:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 0, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:76:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:77:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:208, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:8, subAllot:(8-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:78:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:79:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:80:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:81:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 3, 5, 4, 5, 0, 3, 1, 2, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 4, 5, 0, 3, 1, 2, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[1, 2, 2, 0, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 2, 0, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:82:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 4, 5, 0, 3, 1, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:83:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 5, 0, 3, 1, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 0, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:84:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 0, 3, 1, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:20

dropResult:[type:97 id:9700005 count:20]dropMergedResult:[type:97 id:9700005 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:85:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 3, 1, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:86:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 1, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:209, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:9, subAllot:(9-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002033), (5-1002027)]
round:87:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:88:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700006 count:1

dropResult:[type:17 id:1700006 count:1]dropMergedResult:[type:17 id:1700006 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:89:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:223, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:90:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:91:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 0, 3, 1, 3, 4, 2, 5, 5, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 3, 1, 3, 4, 2, 5, 5, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:92:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 1, 3, 4, 2, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:210, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:10, subAllot:(10-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] new random allot subIdxList:[1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:1 subAllot:(3-type:17 id:1700016 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700016 count:1

dropResult:[type:17 id:1700016 count:1]dropMergedResult:[type:17 id:1700016 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:93:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 3, 4, 2, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:94:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 4, 2, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:95:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 2, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:96:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:97:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:224, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:98:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:99:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700002 count:1

dropResult:[type:17 id:1700002 count:1]dropMergedResult:[type:17 id:1700002 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:100:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:101:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[0, 5, 4, 5, 2, 3, 3, 4, 3, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 4, 5, 2, 3, 3, 4, 3, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:211, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] times use over! reset to default times:1
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:1, subAllot:(1-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] new random allot subIdxList:[1, 1, 1, 1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 1, 0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:102:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 5, 2, 3, 3, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 0, 1, 2, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 2, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:103:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 2, 3, 3, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 2, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:104:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 3, 3, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:105:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 3, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:225, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:106:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:107:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:108:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:109:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:110:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:111:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 4, 3, 3, 4, 1, 5, 3, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 3, 3, 4, 1, 5, 3, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 1, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:112:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 3, 4, 1, 5, 3, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:113:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 1, 5, 3, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:114:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 1, 5, 3, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:115:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 5, 3, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:20

dropResult:[type:97 id:9700004 count:20]dropMergedResult:[type:97 id:9700004 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:116:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 3, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:117:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:118:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:119:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:226, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:120:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:212, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:2, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:121:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 1, 0, 4, 3, 5, 5, 4, 3, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 0, 4, 3, 5, 5, 4, 3, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:20

dropResult:[type:97 id:9700003 count:20]dropMergedResult:[type:97 id:9700003 count:20]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:122:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[0, 4, 3, 5, 5, 4, 3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:123:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 3, 5, 5, 4, 3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:213, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:3, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:0 subAllot:(1-type:199 id:1002021 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002021 count:1
[INFO]enter allot:(6-1002021)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] choose subIdx:0 subAllot:(3-type:17 id:1700009 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] do allot result:type:17 id:1700009 count:1

dropResult:[type:17 id:1700009 count:1]dropMergedResult:[type:17 id:1700009 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002021)]
round:124:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 5, 4, 3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[1, 1, 2, 0, 0, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 2, 0, 0, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:125:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 5, 4, 3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:126:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 4, 3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:127:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 0, 0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:128:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:129:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:130:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:227, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:131:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 3, 2, 4, 3, 4, 5, 1, 0, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 2, 4, 3, 4, 5, 1, 0, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:20

dropResult:[type:97 id:9700003 count:20]dropMergedResult:[type:97 id:9700003 count:20]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:132:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 4, 3, 4, 5, 1, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:133:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 3, 4, 5, 1, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:228, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:134:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 4, 5, 1, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:135:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5, 1, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700002 count:1

dropResult:[type:17 id:1700002 count:1]dropMergedResult:[type:17 id:1700002 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:136:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 1, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:137:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:138:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700006 count:1

dropResult:[type:17 id:1700006 count:1]dropMergedResult:[type:17 id:1700006 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:139:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:214, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:4, subAllot:(4-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:140:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:141:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[1, 4, 2, 3, 4, 5, 0, 5, 3, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 2, 3, 4, 5, 0, 5, 3, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:142:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 3, 4, 5, 0, 5, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 2, 1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 1, 0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:143:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 4, 5, 0, 5, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:229, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:144:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5, 0, 5, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:145:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 0, 5, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:146:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 5, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:147:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:215, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:5, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] new random allot subIdxList:[1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002028)]
round:148:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:149:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:150:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:151:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 4, 0, 5, 2, 3, 3, 4, 1, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 0, 5, 2, 3, 3, 4, 1, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:152:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 5, 2, 3, 3, 4, 1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:153:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 2, 3, 3, 4, 1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:216, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:6, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:0 subAllot:(3-type:17 id:1700015 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700015 count:1

dropResult:[type:17 id:1700015 count:1]dropMergedResult:[type:17 id:1700015 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002023), (6-1002022)]
round:154:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 3, 3, 4, 1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:155:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 3, 4, 1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:230, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:156:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:157:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:158:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:159:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:160:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:161:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 3, 1, 4, 5, 3, 0, 3, 4, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 1, 4, 5, 3, 0, 3, 4, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:162:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 4, 5, 3, 0, 3, 4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:163:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 5, 3, 0, 3, 4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700005 count:1

dropResult:[type:17 id:1700005 count:1]dropMergedResult:[type:17 id:1700005 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:164:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 0, 3, 4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 2, 0, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 0, 1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:165:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 0, 3, 4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700002 count:1

dropResult:[type:17 id:1700002 count:1]dropMergedResult:[type:17 id:1700002 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:166:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 3, 4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:167:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:217, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:7, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002033), (5-1002027)]
round:168:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:169:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:170:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:231, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:171:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 0, 3, 2, 3, 4, 3, 1, 5, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 3, 2, 3, 4, 3, 1, 5, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:172:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 2, 3, 4, 3, 1, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:218, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:8, subAllot:(8-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002033), (5-1002027)]
round:173:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 3, 4, 3, 1, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:174:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 4, 3, 1, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:232, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:175:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 3, 1, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:176:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 1, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:10

dropResult:[type:97 id:9700004 count:10]dropMergedResult:[type:97 id:9700004 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:177:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700001 count:1

dropResult:[type:17 id:1700001 count:1]dropMergedResult:[type:17 id:1700001 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:178:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:179:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:180:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:181:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 5, 1, 4, 5, 3, 4, 0, 2, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 1, 4, 5, 3, 4, 0, 2, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 1, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:182:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1, 4, 5, 3, 4, 0, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:183:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 5, 3, 4, 0, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:184:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 4, 0, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 0, 2, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 2, 1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:185:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 0, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:186:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 0, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:187:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:188:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:219, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:9, subAllot:(9-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:189:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:233, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:190:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:20

dropResult:[type:97 id:9700003 count:20]dropMergedResult:[type:97 id:9700003 count:20]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:191:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 0, 2, 4, 4, 3, 5, 3, 1, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 2, 4, 4, 3, 5, 3, 1, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:192:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[2, 4, 4, 3, 5, 3, 1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:220, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:10, subAllot:(10-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] new random allot subIdxList:[1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] new random allot subIdxList:[0, 0, 1, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:0 subAllot:(3-type:17 id:1700015 count:1) leftIdxLis:[0, 1, 1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700015 count:1

dropResult:[type:17 id:1700015 count:1]dropMergedResult:[type:17 id:1700015 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:193:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 4, 3, 5, 3, 1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:234, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:194:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4, 3, 5, 3, 1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:195:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 3, 1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:10

dropResult:[type:97 id:9700004 count:10]dropMergedResult:[type:97 id:9700004 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:196:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:197:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:198:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:199:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:200:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:201:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 4, 2, 3, 5, 3, 4, 1, 3, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 2, 3, 5, 3, 4, 1, 3, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[1, 1, 2, 2, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 2, 2, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:202:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 3, 5, 3, 4, 1, 3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 2, 0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:10

dropResult:[type:97 id:9700004 count:10]dropMergedResult:[type:97 id:9700004 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:203:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 5, 3, 4, 1, 3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:235, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:204:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 4, 1, 3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:205:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 1, 3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:206:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 1, 3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:207:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:208:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:209:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:210:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:221, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] times use over! reset to default times:1
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:1, subAllot:(1-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] new random allot subIdxList:[0, 0, 1, 1, 1, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[0, 1, 1, 1, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002033), (5-1002026)]
round:211:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 3, 2, 1, 4, 3, 0, 3, 5, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 2, 1, 4, 3, 0, 3, 5, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:212:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 1, 4, 3, 0, 3, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:213:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[1, 4, 3, 0, 3, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:236, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:214:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 3, 0, 3, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:215:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 0, 3, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:216:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 3, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:217:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:222, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:2, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[1, 1, 1, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002033), (5-1002026)]
round:218:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:219:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:220:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:221:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 3, 2, 3, 4, 0, 1, 5, 5, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 2, 3, 4, 0, 1, 5, 5, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 0, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:222:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 3, 4, 0, 1, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:223:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 4, 0, 1, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:237, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:224:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 0, 1, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:225:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[1, 2, 0, 2, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 0, 2, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:10

dropResult:[type:97 id:9700004 count:10]dropMergedResult:[type:97 id:9700004 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:226:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1, 5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:223, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:3, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:0 subAllot:(3-type:17 id:1700015 count:1) leftIdxLis:[1, 1, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700015 count:1

dropResult:[type:17 id:1700015 count:1]dropMergedResult:[type:17 id:1700015 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:227:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:228:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 2, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:229:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:230:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:231:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 3, 3, 1, 5, 2, 3, 0, 5, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 3, 1, 5, 2, 3, 0, 5, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:232:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 1, 5, 2, 3, 0, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 2, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:233:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 5, 2, 3, 0, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:234:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 2, 3, 0, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:235:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 3, 0, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:236:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 0, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:238, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:237:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:238:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:224, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:4, subAllot:(4-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:239:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:240:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:10

dropResult:[type:97 id:9700004 count:10]dropMergedResult:[type:97 id:9700004 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:241:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 3, 4, 3, 2, 5, 3, 0, 1, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 3, 2, 5, 3, 0, 1, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:242:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 3, 2, 5, 3, 0, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:243:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 2, 5, 3, 0, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 0, 0, 1, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 0, 1, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:244:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 5, 3, 0, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:245:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5, 3, 0, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:239, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:246:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 0, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0, 1, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:247:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:248:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:225, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:5, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] new random allot subIdxList:[1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002028)]
round:249:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700006 count:1

dropResult:[type:17 id:1700006 count:1]dropMergedResult:[type:17 id:1700006 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:250:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:251:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 4, 2, 0, 1, 5, 4, 3, 5, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 2, 0, 1, 5, 4, 3, 5, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 1, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:252:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 0, 1, 5, 4, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:253:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 1, 5, 4, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:240, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:254:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1, 5, 4, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:226, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:6, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002028)]
round:255:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 4, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:256:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:20

dropResult:[type:97 id:9700005 count:20]dropMergedResult:[type:97 id:9700005 count:20]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:257:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:258:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:259:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:260:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:261:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[1, 5, 3, 3, 3, 2, 4, 5, 4, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 3, 3, 3, 2, 4, 5, 4, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:262:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 3, 3, 2, 4, 5, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 1, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700001 count:1

dropResult:[type:17 id:1700001 count:1]dropMergedResult:[type:17 id:1700001 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:263:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 3, 2, 4, 5, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:264:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 2, 4, 5, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:265:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 4, 5, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:266:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 5, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:241, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:267:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[1, 0, 2, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2, 0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:268:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 0, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:269:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:270:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:227, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:7, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:0 subAllot:(1-type:199 id:1002021 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002021 count:1
[INFO]enter allot:(6-1002021)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] choose subIdx:1 subAllot:(3-type:17 id:1700010 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] do allot result:type:17 id:1700010 count:1

dropResult:[type:17 id:1700010 count:1]dropMergedResult:[type:17 id:1700010 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002023), (6-1002021)]
round:271:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[4, 0, 5, 3, 2, 3, 5, 4, 3, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 5, 3, 2, 3, 5, 4, 3, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:272:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 3, 2, 3, 5, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:228, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:8, subAllot:(8-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:273:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 2, 3, 5, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:274:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 3, 5, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:275:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 5, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:242, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:276:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700001 count:1

dropResult:[type:17 id:1700001 count:1]dropMergedResult:[type:17 id:1700001 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:277:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:278:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:279:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:280:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700006 count:1

dropResult:[type:17 id:1700006 count:1]dropMergedResult:[type:17 id:1700006 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:281:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 3, 1, 5, 0, 4, 4, 5, 2, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 1, 5, 0, 4, 4, 5, 2, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 0, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:282:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 5, 0, 4, 4, 5, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:283:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 0, 4, 4, 5, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:284:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 4, 4, 5, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:285:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 4, 5, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:229, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:9, subAllot:(9-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] new random allot subIdxList:[0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:0 subAllot:(1-type:199 id:1002021 count:1) leftIdxLis:[1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002021 count:1
[INFO]enter allot:(6-1002021)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] choose subIdx:1 subAllot:(3-type:17 id:1700010 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] do allot result:type:17 id:1700010 count:1

dropResult:[type:17 id:1700010 count:1]dropMergedResult:[type:17 id:1700010 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002021)]
round:286:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4, 5, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 2, 0, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 0, 0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:287:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 0, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:288:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:289:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:243, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:290:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:291:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[2, 0, 4, 4, 1, 3, 5, 3, 5, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 4, 4, 1, 3, 5, 3, 5, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:244, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:292:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 4, 1, 3, 5, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:230, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:10, subAllot:(10-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:293:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4, 1, 3, 5, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:294:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 3, 5, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:295:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 5, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:296:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:297:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:298:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:299:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:300:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:301:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 0, 1, 4, 4, 3, 5, 3, 2, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 4, 4, 3, 5, 3, 2, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:302:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1, 4, 4, 3, 5, 3, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:231, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] times use over! reset to default times:1
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:1, subAllot:(1-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] new random allot subIdxList:[1, 0, 1, 0, 1, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[0, 1, 0, 1, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:303:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 4, 3, 5, 3, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:304:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4, 3, 5, 3, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 0, 1, 1, 0, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 1, 0, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:305:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 3, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:306:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:307:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:308:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:309:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:245, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:310:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:311:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[0, 3, 5, 3, 2, 4, 5, 1, 4, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 5, 3, 2, 4, 5, 1, 4, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:232, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:2, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:1 subAllot:(3-type:17 id:1700016 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700016 count:1

dropResult:[type:17 id:1700016 count:1]dropMergedResult:[type:17 id:1700016 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:312:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 2, 4, 5, 1, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:313:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 2, 4, 5, 1, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:20

dropResult:[type:97 id:9700004 count:20]dropMergedResult:[type:97 id:9700004 count:20]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:314:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 4, 5, 1, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:315:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 5, 1, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:246, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:316:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 1, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:317:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:318:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:319:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:320:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:20

dropResult:[type:97 id:9700003 count:20]dropMergedResult:[type:97 id:9700003 count:20]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:321:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 5, 0, 4, 1, 5, 2, 3, 4, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 0, 4, 1, 5, 2, 3, 4, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 0, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:322:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 4, 1, 5, 2, 3, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 2, 0, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 0, 0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:323:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 1, 5, 2, 3, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:233, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:3, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[1, 0, 1, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002033), (5-1002027)]
round:324:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 5, 2, 3, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 0, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:325:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 2, 3, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:326:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 3, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:327:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:247, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:328:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:329:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:330:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:331:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 2, 0, 4, 5, 3, 5, 3, 4, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 0, 4, 5, 3, 5, 3, 4, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:332:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 4, 5, 3, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:248, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:333:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 5, 3, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:234, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:4, subAllot:(4-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[0, 1, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:334:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:335:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700001 count:1

dropResult:[type:17 id:1700001 count:1]dropMergedResult:[type:17 id:1700001 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:336:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:337:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:338:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:339:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:340:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:341:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[1, 0, 4, 5, 3, 5, 2, 4, 3, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[0, 4, 5, 3, 5, 2, 4, 3, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:342:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 5, 3, 5, 2, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:235, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:5, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] new random allot subIdxList:[1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[1, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002033), (5-1002027)]
round:343:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 5, 2, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 1, 0, 2, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 0, 2, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:344:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 2, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 1, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:345:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 2, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:346:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:347:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:249, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:348:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:20

dropResult:[type:97 id:9700005 count:20]dropMergedResult:[type:97 id:9700005 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:349:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:350:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:351:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 2, 0, 3, 5, 3, 5, 1, 4, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 0, 3, 5, 3, 5, 1, 4, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:352:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 3, 5, 3, 5, 1, 4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:250, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:353:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 5, 3, 5, 1, 4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:236, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:6, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:1 subAllot:(3-type:17 id:1700016 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700016 count:1

dropResult:[type:17 id:1700016 count:1]dropMergedResult:[type:17 id:1700016 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002023), (6-1002022)]
round:354:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 5, 1, 4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:355:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 1, 4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:356:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 1, 4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:357:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1, 4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:358:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700006 count:1

dropResult:[type:17 id:1700006 count:1]dropMergedResult:[type:17 id:1700006 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:359:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:20

dropResult:[type:97 id:9700004 count:20]dropMergedResult:[type:97 id:9700004 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:360:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:361:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 2, 0, 4, 3, 4, 1, 5, 5, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 0, 4, 3, 4, 1, 5, 5, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:362:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 4, 3, 4, 1, 5, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:251, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:363:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 3, 4, 1, 5, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:237, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:7, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002028)]
round:364:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 4, 1, 5, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 1, 1, 0, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 1, 0, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:365:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 1, 5, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:366:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 5, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 0, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:367:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:368:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:20

dropResult:[type:97 id:9700004 count:20]dropMergedResult:[type:97 id:9700004 count:20]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:369:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:370:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:371:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 4, 3, 4, 2, 3, 3, 5, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 3, 4, 2, 3, 3, 5, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:100

dropResult:[type:97 id:9700003 count:100]dropMergedResult:[type:97 id:9700003 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:372:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 4, 2, 3, 3, 5, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:373:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 2, 3, 3, 5, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:374:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 3, 3, 5, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:375:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 3, 5, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:252, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:376:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 5, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:377:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:378:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:379:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:238, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:8, subAllot:(8-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:380:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:381:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 0, 3, 5, 2, 4, 4, 1, 5, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 3, 5, 2, 4, 4, 1, 5, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 2, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:382:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 5, 2, 4, 4, 1, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:239, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:9, subAllot:(9-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] new random allot subIdxList:[1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:0 subAllot:(3-type:17 id:1700015 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700015 count:1

dropResult:[type:17 id:1700015 count:1]dropMergedResult:[type:17 id:1700015 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:383:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 2, 4, 4, 1, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:384:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 4, 4, 1, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 2, 0, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 0, 1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:385:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 4, 1, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:253, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:386:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4, 1, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:387:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:388:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:389:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:390:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:391:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[0, 3, 3, 5, 4, 2, 5, 3, 4, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 3, 5, 4, 2, 5, 3, 4, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:240, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:10, subAllot:(10-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:392:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 5, 4, 2, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 2, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:393:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 4, 2, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:394:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 2, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:395:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[2, 5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:396:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[5, 3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:254, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:397:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:398:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:399:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:400:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:401:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[2, 3, 3, 4, 5, 3, 4, 0, 5, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 3, 4, 5, 3, 4, 0, 5, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:255, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:402:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 5, 3, 4, 0, 5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:403:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5, 3, 4, 0, 5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:404:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 4, 0, 5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 1, 2, 0, 1, 2]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 2, 0, 1, 2] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:405:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 4, 0, 5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2, 0, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:406:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 0, 5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:407:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:10

dropResult:[type:97 id:9700005 count:10]dropMergedResult:[type:97 id:9700005 count:10]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:408:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:241, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] times use over! reset to default times:1
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:1, subAllot:(1-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] new random allot subIdxList:[1, 1, 1, 1, 0, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 1, 0, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:409:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:410:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:411:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 3, 3, 2, 3, 4, 0, 5, 4, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 3, 2, 3, 4, 0, 5, 4, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:412:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 2, 3, 4, 0, 5, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:413:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 3, 4, 0, 5, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:414:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 4, 0, 5, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:256, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:415:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 0, 5, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:416:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 5, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:417:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5, 4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:242, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:2, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:1 subAllot:(3-type:17 id:1700016 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700016 count:1

dropResult:[type:17 id:1700016 count:1]dropMergedResult:[type:17 id:1700016 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:418:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[4, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[2] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:419:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:420:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:421:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 2, 4, 5, 5, 1, 0, 4, 3, 3]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 4, 5, 5, 1, 0, 4, 3, 3] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:422:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 5, 5, 1, 0, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:257, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:423:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 5, 1, 0, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[2, 0, 2, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 2, 0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:424:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 1, 0, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:425:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[1, 0, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 0, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:426:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[0, 4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:427:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[4, 3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:243, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:3, subAllot:(2-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 1, 0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800008 count:5

dropResult:[type:18 id:1800008 count:5]dropMergedResult:[type:18 id:1800008 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:428:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:20

dropResult:[type:97 id:9700005 count:20]dropMergedResult:[type:97 id:9700005 count:20]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:429:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:430:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:431:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[2, 4, 3, 5, 5, 0, 3, 3, 1, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 3, 5, 5, 0, 3, 3, 1, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:258, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:432:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 5, 5, 0, 3, 3, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800005 count:5

dropResult:[type:18 id:1800005 count:5]dropMergedResult:[type:18 id:1800005 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:433:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 5, 0, 3, 3, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:434:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 0, 3, 3, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:20

dropResult:[type:97 id:9700004 count:20]dropMergedResult:[type:97 id:9700004 count:20]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:435:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 3, 3, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:436:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[3, 3, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:244, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:4, subAllot:(4-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[1, 0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002028)]
round:437:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:20

dropResult:[type:97 id:9700003 count:20]dropMergedResult:[type:97 id:9700003 count:20]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:438:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:439:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:440:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:441:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 3, 1, 4, 3, 4, 5, 2, 0, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 1, 4, 3, 4, 5, 2, 0, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 1, 1, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:442:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 4, 3, 4, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:443:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 3, 4, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:444:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 4, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 2, 0, 2, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 0, 2, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:445:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:446:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[0, 2, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:447:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 1, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002028)]
round:448:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:259, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:449:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:245, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:5, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] new random allot subIdxList:[1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[0, 0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002028)]
round:450:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:451:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[5, 3, 5, 0, 2, 1, 3, 4, 3, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 0, 2, 1, 3, 4, 3, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700030 count:1

dropResult:[type:17 id:1700030 count:1]dropMergedResult:[type:17 id:1700030 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:452:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 0, 2, 1, 3, 4, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:453:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[0, 2, 1, 3, 4, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700029 count:1

dropResult:[type:17 id:1700029 count:1]dropMergedResult:[type:17 id:1700029 count:1]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002025)]
round:454:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[2, 1, 3, 4, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:246, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:6, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:0 subAllot:(1-type:199 id:1002021 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002021 count:1
[INFO]enter allot:(6-1002021)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] choose subIdx:0 subAllot:(3-type:17 id:1700009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002021)] do allot result:type:17 id:1700009 count:1

dropResult:[type:17 id:1700009 count:1]dropMergedResult:[type:17 id:1700009 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002023), (6-1002021)]
round:455:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[1, 3, 4, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:260, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800016 count:3

dropResult:[type:18 id:1800016 count:3]dropMergedResult:[type:18 id:1800016 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:456:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 4, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700007 count:1

dropResult:[type:17 id:1700007 count:1]dropMergedResult:[type:17 id:1700007 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:457:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:10

dropResult:[type:97 id:9700003 count:10]dropMergedResult:[type:97 id:9700003 count:10]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:458:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:459:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:460:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:100

dropResult:[type:97 id:9700004 count:100]dropMergedResult:[type:97 id:9700004 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:461:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 4, 0, 1, 5, 3, 5, 3, 2, 4]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 0, 1, 5, 3, 5, 3, 2, 4] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 1, 2, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1, 2, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:462:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1, 5, 3, 5, 3, 2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 1, 0, 2, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[1, 0, 2, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800006 count:5

dropResult:[type:18 id:1800006 count:5]dropMergedResult:[type:18 id:1800006 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:463:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1, 5, 3, 5, 3, 2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:247, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:7, subAllot:(5-type:199 id:1002013 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002013 count:1
[INFO]enter allot:(6-1002013)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] choose subIdx:1 subAllot:(2-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002013)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002013), (6-1002011), (5-1002033), (5-1002026)]
round:464:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[5, 3, 5, 3, 2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:465:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 5, 3, 2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[0, 1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1, 0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[2, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:466:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 3, 2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:20

dropResult:[type:97 id:9700003 count:20]dropMergedResult:[type:97 id:9700003 count:20]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:467:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:468:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[2, 4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700001 count:1

dropResult:[type:17 id:1700001 count:1]dropMergedResult:[type:17 id:1700001 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:469:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:261, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:470:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:471:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[2, 4, 5, 3, 0, 1, 3, 3, 4, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[4, 5, 3, 0, 1, 3, 3, 4, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:262, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800009 count:3

dropResult:[type:18 id:1800009 count:3]dropMergedResult:[type:18 id:1800009 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:472:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 3, 0, 1, 3, 3, 4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:100

dropResult:[type:97 id:9700005 count:100]dropMergedResult:[type:97 id:9700005 count:100]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:473:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[3, 0, 1, 3, 3, 4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[2, 0, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[0, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002031)]
round:474:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[0, 1, 3, 3, 4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:475:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[1, 3, 3, 4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:248, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:8, subAllot:(8-type:199 id:1002011 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:0 subAllot:(2-type:199 id:1002033 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002011), (5-1002033), (5-1002027)]
round:476:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 3, 4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700004 count:1

dropResult:[type:17 id:1700004 count:1]dropMergedResult:[type:17 id:1700004 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:477:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:478:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:1000

dropResult:[type:97 id:9700002 count:1000]dropMergedResult:[type:97 id:9700002 count:1000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:479:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:480:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:481:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[3, 3, 1, 4, 5, 5, 2, 3, 4, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 1, 4, 5, 5, 2, 3, 4, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:482:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[1, 4, 5, 5, 2, 3, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700027 count:1

dropResult:[type:17 id:1700027 count:1]dropMergedResult:[type:17 id:1700027 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:483:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[4, 5, 5, 2, 3, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700003 count:1

dropResult:[type:17 id:1700003 count:1]dropMergedResult:[type:17 id:1700003 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:484:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[5, 5, 2, 3, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] new random allot subIdxList:[0, 2, 1, 0, 2, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1, 0, 2, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800004 count:5

dropResult:[type:18 id:1800004 count:5]dropMergedResult:[type:18 id:1800004 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:485:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[5, 2, 3, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] new random allot subIdxList:[1, 1, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[1, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1, 0, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002030)]
round:486:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 3, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:1 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[0, 2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002010), (6-1002009), (5-1002029)]
round:487:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[3, 4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:263, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002026 count:1
[INFO]enter allot:(5-1002026)
[INFO][WeightRandomAllotLogic]-[(5-1002026)] do allot result:type:18 id:1800010 count:3

dropResult:[type:18 id:1800010 count:3]dropMergedResult:[type:18 id:1800010 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002026)]
round:488:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:489:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:0 subAllot:(2-type:199 id:1002028 count:1) leftIdxLis:[2, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800003 count:5

dropResult:[type:18 id:1800003 count:5]dropMergedResult:[type:18 id:1800003 count:5]executedAllots:[(6-1002001), (6-1002009), (5-1002028)]
round:490:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:249, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:9, subAllot:(9-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] new random allot subIdxList:[0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:0 subAllot:(1-type:199 id:1002023 count:1) leftIdxLis:[1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002023 count:1
[INFO]enter allot:(6-1002023)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] new random allot subIdxList:[1, 0, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] choose subIdx:1 subAllot:(2-type:199 id:1002022 count:1) leftIdxLis:[0, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002023)] do allot result:type:199 id:1002022 count:1
[INFO]enter allot:(6-1002022)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] new random allot subIdxList:[0, 1, 1, 1, 0, 0]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] choose subIdx:0 subAllot:(3-type:17 id:1700015 count:1) leftIdxLis:[1, 1, 1, 0, 0] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002022)] do allot result:type:17 id:1700015 count:1

dropResult:[type:17 id:1700015 count:1]dropMergedResult:[type:17 id:1700015 count:1]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002023), (6-1002022)]
round:491:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] new random allot subIdxList:[1, 3, 4, 4, 3, 3, 5, 2, 0, 5]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:1 subAllot:(1-type:199 id:1002024 count:1) leftIdxLis:[3, 4, 4, 3, 3, 5, 2, 0, 5] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002024 count:1
[INFO]enter allot:(5-1002024)
[INFO][WeightRandomAllotLogic]-[(5-1002024)] do allot result:type:17 id:1700008 count:1

dropResult:[type:17 id:1700008 count:1]dropMergedResult:[type:17 id:1700008 count:1]executedAllots:[(6-1002001), (5-1002024)]
round:492:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[4, 4, 3, 3, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:5000

dropResult:[type:97 id:9700002 count:5000]dropMergedResult:[type:97 id:9700002 count:5000]executedAllots:[(6-1002001), (6-1002008), (5-1002032)]
round:493:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[4, 3, 3, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:2 subAllot:(2-type:199 id:1002030 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002030 count:1
[INFO]enter allot:(5-1002030)
[INFO][WeightRandomAllotLogic]-[(5-1002030)] do allot result:type:97 id:9700005 count:50

dropResult:[type:97 id:9700005 count:50]dropMergedResult:[type:97 id:9700005 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002030)]
round:494:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:4 subAllot:(2-type:199 id:1002009 count:1) leftIdxLis:[3, 3, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002009 count:1
[INFO]enter allot:(6-1002009)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] choose subIdx:1 subAllot:(2-type:199 id:1002029 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002009)] do allot result:type:199 id:1002029 count:1
[INFO]enter allot:(5-1002029)
[INFO][WeightRandomAllotLogic]-[(5-1002029)] do allot result:type:97 id:9700004 count:50

dropResult:[type:97 id:9700004 count:50]dropMergedResult:[type:97 id:9700004 count:50]executedAllots:[(6-1002001), (6-1002009), (5-1002029)]
round:495:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[3, 5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] new random allot subIdxList:[0, 2, 1, 1]
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:0 subAllot:(1-type:199 id:1002025 count:1) leftIdxLis:[2, 1, 1] newSubAllotIdx:true forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002025 count:1
[INFO]enter allot:(5-1002025)
[INFO][WeightRandomAllotLogic]-[(5-1002025)] do allot result:type:17 id:1700028 count:1

dropResult:[type:17 id:1700028 count:1]dropMergedResult:[type:17 id:1700028 count:1]executedAllots:[(6-1002001), (6-1002008), (5-1002025)]
round:496:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:3 subAllot:(3-type:199 id:1002008 count:1) leftIdxLis:[5, 2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:2 subAllot:(1-type:199 id:1002031 count:1) leftIdxLis:[1, 1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002031 count:1
[INFO]enter allot:(5-1002031)
[INFO][WeightRandomAllotLogic]-[(5-1002031)] do allot result:type:97 id:9700003 count:50

dropResult:[type:97 id:9700003 count:50]dropMergedResult:[type:97 id:9700003 count:50]executedAllots:[(6-1002001), (6-1002008), (5-1002031)]
round:497:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[2, 0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[0] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[1] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:2000

dropResult:[type:97 id:9700002 count:2000]dropMergedResult:[type:97 id:9700002 count:2000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]
round:498:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:2 subAllot:(1-type:199 id:1002006 count:1) leftIdxLis:[0, 5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002006 count:1
[INFO]enter allot:(3-1002006)
[INFO][TimesAllotLogic]-[(3-1002006)] times use over! fixed use max times:524
[INFO][TimesAllotLogic]-[(3-1002006)] toUseTimes:524, subAllot:(524-type:199 id:1002007 count:1)
[INFO][TimesAllotLogic]-[(3-1002006)] do allot result:type:199 id:1002007 count:1
[INFO]enter allot:(4-1002007)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] toUseTimes:264, subAllot:(1-type:199 id:1002033 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002007)] do allot result:type:199 id:1002033 count:1
[INFO]enter allot:(5-1002033)
[INFO][WeightRandomAllotLogic]-[(5-1002033)] do allot result:type:199 id:1002027 count:1
[INFO]enter allot:(5-1002027)
[INFO][WeightRandomAllotLogic]-[(5-1002027)] do allot result:type:18 id:1800015 count:3

dropResult:[type:18 id:1800015 count:3]dropMergedResult:[type:18 id:1800015 count:3]executedAllots:[(6-1002001), (3-1002006), (4-1002007), (5-1002033), (5-1002027)]
round:499:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:0 subAllot:(1-type:199 id:1002002 count:1) leftIdxLis:[5] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002002 count:1
[INFO]enter allot:(3-1002002)
[INFO][TimesAllotLogic]-[(3-1002002)] times use over! fixed use max times:531
[INFO][TimesAllotLogic]-[(3-1002002)] toUseTimes:531, subAllot:(531-type:199 id:1002003 count:1)
[INFO][TimesAllotLogic]-[(3-1002002)] do allot result:type:199 id:1002003 count:1
[INFO]enter allot:(4-1002003)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] toUseTimes:250, subAllot:(1-type:199 id:1002004 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002003)] do allot result:type:199 id:1002004 count:1
[INFO]enter allot:(4-1002004)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] toUseTimes:10, subAllot:(10-type:199 id:1002012 count:1)
[INFO][TimesWithRestAllotLogic]-[(4-1002004)] do allot result:type:199 id:1002012 count:1
[INFO]enter allot:(6-1002012)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] choose subIdx:1 subAllot:(1-type:199 id:1002011 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002012)] do allot result:type:199 id:1002011 count:1
[INFO]enter allot:(6-1002011)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] choose subIdx:1 subAllot:(5-type:199 id:1002028 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002011)] do allot result:type:199 id:1002028 count:1
[INFO]enter allot:(5-1002028)
[INFO][WeightRandomAllotLogic]-[(5-1002028)] do allot result:type:18 id:1800007 count:5

dropResult:[type:18 id:1800007 count:5]dropMergedResult:[type:18 id:1800007 count:5]executedAllots:[(6-1002001), (3-1002002), (4-1002003), (4-1002004), (6-1002012), (6-1002011), (5-1002028)]
round:500:
[INFO]enter allot:(6-1002001)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] choose subIdx:5 subAllot:(2-type:199 id:1002010 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002001)] do allot result:type:199 id:1002010 count:1
[INFO]enter allot:(6-1002010)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] choose subIdx:0 subAllot:(2-type:199 id:1002008 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002010)] do allot result:type:199 id:1002008 count:1
[INFO]enter allot:(6-1002008)
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] choose subIdx:1 subAllot:(2-type:199 id:1002032 count:1) leftIdxLis:[] newSubAllotIdx:false forceReset:false
[INFO][ShuffleListNotReturnAllotLogic]-[(6-1002008)] do allot result:type:199 id:1002032 count:1
[INFO]enter allot:(5-1002032)
[INFO][WeightRandomAllotLogic]-[(5-1002032)] do allot result:type:97 id:9700002 count:10000

dropResult:[type:97 id:9700002 count:10000]dropMergedResult:[type:97 id:9700002 count:10000]executedAllots:[(6-1002001), (6-1002010), (6-1002008), (5-1002032)]

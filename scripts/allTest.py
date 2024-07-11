import sys
import traceback

from airtest.core.api import connect_device
import achievementTest, achievementCategoryTest, achievementWantedTest, battlePassTest, dlcDownloadTest, \
    energyTest, fishCardTest, gearTest, guideTest, mailTest, minitaskTest, progressRewardsTest, \
    storeTest, taskTest, treasureChestTest, newbieTaskTest, duelTest, rankTest, playerInfoTest
from common import gameInit
from scripts import rouletteTest, fishAlbumTest, careerTest


def main():
    connect_device(f"android://127.0.0.1:5037/{serial_number}")
    content_all = ["成就鱼种", "成就照片墙", "渔获排行榜", "玩家信息、设置", "通行证", "dlc下载", "体力", "鱼卡", "鱼册", "装备", "新手、鱼册、刺鱼、成就墙、俱乐部、装备升级引导", "邮箱", "minitask", "商城", "新手7天", "鱼箱", "对决、对决排行榜", "成就", "任务", "转盘", "珍珠、贝壳进度条", "天赋"]
    en2ch = {achievementCategoryTest: "成就鱼种",
             achievementWantedTest: "成就照片墙",
             rankTest: "渔获排行榜",
             playerInfoTest: "玩家信息、设置",
             battlePassTest: "通行证",
             dlcDownloadTest: "dlc下载",
             energyTest: "体力",
             fishCardTest: "鱼卡",
             fishAlbumTest:"鱼册",
             gearTest: "装备",
             guideTest: "新手、鱼册、刺鱼、成就墙、俱乐部、装备升级引导",
             mailTest: "邮箱",
             minitaskTest: "minitask",
             storeTest: "商城",
             newbieTaskTest: "新手7天",
             treasureChestTest: "鱼箱",
             duelTest: "对决、对决排行榜",
             achievementTest: "成就",
             taskTest: "任务",
             rouletteTest: "转盘",
             progressRewardsTest: "珍珠、贝壳进度条",
             careerTest: "天赋"
             }
    test_list = [achievementCategoryTest, mailTest, treasureChestTest, achievementWantedTest, rankTest, playerInfoTest, battlePassTest, dlcDownloadTest, energyTest, fishCardTest, gearTest, guideTest, rouletteTest, progressRewardsTest, newbieTaskTest,  minitaskTest, duelTest, fishAlbumTest,  storeTest,  achievementTest, taskTest, careerTest]
    # test_list = [ battlePassTest, fishCardTest, gearTest, guideTest,
    #              mailTest, minitaskTest, storeTest, newbieTaskTest, treasureChestTest, taskTest,
    #              achievementCategoryTest, achievementWantedTest, achievementTest, duelTest, rankTest]

    print(f"当前测试模块共计{len(test_list)}个")
    cur = 0
    pass_list = []
    retry_list = []

    while cur < len(test_list):
        # 重启
        bp = gameInit.restart_to_login("com.xuejing.smallfish.official")
        try:
            test_list[cur].main(bp)
            print(cur, ":", en2ch[test_list[cur]], "执行成功")
            pass_list.append(test_list[cur])
        except Exception as e:
            print(e)
            traceback.print_exc()
            print(cur, ":", en2ch[test_list[cur]], "执行失败")
            retry_list.append(test_list[cur])

        bp.connect_close()
        cur += 1
    print(f"通过用例{len(pass_list)}个: {pass_list}")
    print(f"需重试用例{len(retry_list)}个: {retry_list}")

    if len(retry_list) < 1:
        return
    fail_list = []
    cur = 0
    while cur < len(retry_list):
        # 重启
        bp = gameInit.restart_to_login("com.xuejing.smallfish.official")
        try:
            retry_list[cur].main(bp)
            print(en2ch[retry_list[cur]], "执行成功")
            pass_list.append(retry_list[cur])
        except Exception as e:
            traceback.print_exc()
            print(en2ch[retry_list[cur]], "执行失败")
            fail_list.append(retry_list[cur])
        cur += 1
    print(f"通过用例{len(pass_list)}个: {pass_list}")
    print(f"失败用例{len(fail_list)}个: {fail_list}")


if __name__ == '__main__':
    serial_number = "b6h65hd64p5pxcyh"
    main()




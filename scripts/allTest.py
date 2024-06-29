import sys
import traceback

from airtest.core.api import connect_device
import achievementTest, achievementCategoryTest, achievementWantedTest, battlePassTest, dlcDownloadTest, \
    energyTest, fishCardTest, gearTest, guideTest, mailTest, minitaskTest, progressRewardsTest, \
    storeTest, taskTest, treasureChestTest, newbieTaskTest, duelTest, rankTest, playerInfoTest
from common import gameInit


def main():
    connect_device(f"android://127.0.0.1:5037/{serial_number}")
    test_list = [achievementCategoryTest, achievementWantedTest, rankTest, playerInfoTest, battlePassTest, dlcDownloadTest, energyTest, fishCardTest, gearTest, guideTest, mailTest, minitaskTest, storeTest,  newbieTaskTest, treasureChestTest, duelTest, achievementTest,  taskTest]
    # test_list = [ battlePassTest, fishCardTest, gearTest, guideTest,
    #              mailTest, minitaskTest, storeTest, newbieTaskTest, treasureChestTest, taskTest,
    #              achievementCategoryTest, achievementWantedTest, achievementTest, duelTest, rankTest]

    print(f"当前测试模块共计{len(test_list)}个")
    cur = 6
    res_list = []
    retry_dict = {}

    while cur < len(test_list):
        # 重启
        bp = gameInit.restart_to_login("com.xuejing.smallfish.official")
        try:
            test_list[cur].main(bp)
            print(cur + 1, ":", test_list[cur], "执行成功")
            res_list.append("成功")
        except Exception as e:
            print(e)
            traceback.print_exc()
            retry_dict[str(cur + 1)] = test_list[cur]
            print(cur + 1, ":", test_list[cur], "执行失败")
            res_list.append("失败")
        bp.connect_close()
        cur += 1
    print(res_list)
    retry_list = list(retry_dict)
    cur = 0
    while cur < len(retry_list) - 1:
        # 重启
        bp = gameInit.restart_to_login("com.xuejing.smallfish.official")
        try:
            retry_dict[retry_list[cur]].main(bp)
            print(retry_list[cur], ":", retry_list[cur], "执行成功")
            retry_dict.pop(retry_list[cur])
        except Exception as e:
            traceback.print_exc()
            print(retry_list[cur], ":", retry_list[cur], "执行失败")
        cur += 1
    print("执行失败用例：", retry_dict)


if __name__ == '__main__':
    serial_number = "192.168.111.37:20075"
    main()




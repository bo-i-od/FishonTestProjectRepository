import traceback

from airtest.core.api import connect_device
from scripts import achievementTest, achievementCategoryTest, achievementWantedTest, battlePassTest, dlcDownloadTest, energyTest, fishCardTest, gearTest, guideTest, mailTest,minitaskTest, playerSettingTest, progressRewardsTest, storeTest, taskTest, treasureChestTest

from common.basePage import BasePage
from common import gameInit

if __name__ == '__main__':
    # serial_number = "b6h65hd64p5pxcyh"
    # serial_number = "127.0.0.1:21503"
    serial_number = "192.168.111.77:20024"
    connect_device(f"android://127.0.0.1:5037/{serial_number}")
    test_list = [ playerSettingTest, battlePassTest, dlcDownloadTest, energyTest, fishCardTest, gearTest, guideTest, mailTest, minitaskTest, progressRewardsTest, storeTest,  treasureChestTest, taskTest, achievementTest, achievementCategoryTest, achievementWantedTest]
    cur = 0
    retry_times = 0
    res_list = []
    while cur < len(test_list):
        # 重试3次
        if retry_times > 2:
            print(cur + 1, ":", test_list[cur], "执行失败")
            res_list.append("失败")
            retry_times = 0
            cur += 1
            continue

        # 重启
        bp = gameInit.restart_to_login("com.xuejing.smallfish.official")
        try:
            test_list[cur].main(bp)
            print(cur + 1, ":", test_list[cur], "执行成功")
            res_list.append("成功")
        except Exception as e:
            traceback.print_exc()
            retry_times += 1
            continue
        retry_times = 0
        cur += 1
    print(res_list)


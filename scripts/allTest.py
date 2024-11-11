import multiprocessing
import traceback
import importlib
from airtest.core.api import connect_device
from common import gameInit


def worker(serial_number,is_monitor, task_list, retry_list, pass_list, fail_list, task_lock, contents):
    dev = connect_device(f"android://127.0.0.1:5037/{serial_number}")
    while True:
        task_lock.acquire()
        if task_list:
            task_name = task_list.pop(0)
            task_lock.release()
            module = importlib.import_module(task_name)

            # if task_name in ['rankTest', 'dlcDownloadTest', 'playerInfoTest', 'mailTest', 'fishAlbumTest', 'gearTest', 'minitaskTest', 'treasureChestTest', 'newbieTaskTest', 'careerTest', 'achievementWantedTest', 'achievementCategoryTest', 'energyTest']:
            #     pass_list.append(module.__name__)
            #     continue
            # if task_name in ['achievementWantedTest', 'storeTest']:
            #     fail_list.append(module.__name__)
            #     continue
            print(dev, module, "执行测试")
            do_test(dev,is_monitor, module, 0, task_list, retry_list, pass_list, fail_list, task_lock, contents)
            continue

        if retry_list:
            task_name = retry_list.pop(0)
            task_lock.release()
            module = importlib.import_module(task_name)
            print(dev, module, "执行测试")
            do_test(dev, is_monitor, module, 1, task_list, retry_list, pass_list, fail_list, task_lock, contents)
            continue

        task_lock.release()
        break


def do_test(dev, is_monitor, task, kind, task_list, retry_list, pass_list, fail_list, task_lock, contents):
    bp = gameInit.restart_to_login(dev=dev, is_monitor=is_monitor, package="com.xuejing.smallfish.official")
    print("bp连接成功", dev)
    try:
        task.main(bp)
        print(contents[task.__name__]["name"], "执行成功")
        task_lock.acquire()
        pass_list.append(task.__name__)
        task_lock.release()
    except Exception as e:
        print(e)
        traceback.print_exc()
        print(contents[task.__name__]["name"], "执行失败")
        task_lock.acquire()
        if kind == 0:
            retry_list.append(task.__name__)
        else:
            fail_list.append(task.__name__)
        task_lock.release()
    bp.connect_close()


if __name__ == '__main__':
    manager = multiprocessing.Manager()

    contents = manager.dict({
        "achievementCategoryTest": {"name": "成就鱼种", "active": True},
        "achievementWantedTest": {"name": "成就照片墙", "active": True},
        "rankTest": {"name": "渔获排行榜", "active": True},
        "playerInfoTest": {"name": "玩家信息、设置", "active": True},
        "battlePassTest": {"name": "通行证", "active": True},
        "dlcDownloadTest": {"name": "dlc下载", "active": True},
        "energyTest": {"name": "体力", "active": True},
        "fishCardTest": {"name": "鱼卡", "active": True},
        "fishAlbumTest": {"name": "鱼册", "active": True},
        "gearTest": {"name": "装备", "active": True},
        "guideTest": {"name": "新手、鱼册、刺鱼、成就墙、俱乐部、装备升级引导", "active": True},
        "mailTest": {"name": "邮箱", "active": True},
        "minitaskTest": {"name": "minitask", "active": True},
        "storeTest": {"name": "商城", "active": False},
        "newbieTaskTest": {"name": "新手7天", "active": True},
        "treasureChestTest": {"name": "鱼箱", "active": True},
        "duelTest": {"name": "对决、对决排行榜", "active": True},
        "achievementTest": {"name": "成就", "active": True},
        "taskTest": {"name": "任务", "active": True},
        "rouletteTest": {"name": "转盘", "active": True},
        "progressRewardsTest": {"name": "珍珠、贝壳进度条", "active": True},
        "careerTest": {"name": "天赋", "active": True},
    })

    task_list = manager.list()
    pass_list = manager.list()
    retry_list = manager.list()
    fail_list = manager.list()
    task_lock = manager.Lock()

    for module_name, content in contents.items():
        if content["active"]:
            task_list.append(module_name)
            print(f'测试模块：{content["name"]} - {module_name}')

    print(f"当前测试模块共计 {len(task_list)} 个")

    # 设备列表
    serial_number_list = ["127.0.0.1:21523", "127.0.0.1:21533"]

    is_monitor = True

    print(f"当前连接设备 {len(serial_number_list)} 个")

    process_list = []
    for serial_number in serial_number_list:
        p = multiprocessing.Process(target=worker,
                                    args=(serial_number, is_monitor,task_list, retry_list, pass_list, fail_list, task_lock, contents))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()

    print(f"通过用例 {len(pass_list)} 个: {list(pass_list)}")
    print(f"失败用例 {len(fail_list)} 个: {list(fail_list)}")
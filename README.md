### **#环境依赖**

1.安装adb环境

2.执行pip install -r requirements.txt 安装依赖包

### **#目录结构描述**

##### ├──common                               _# 通用文件夹_
##### │   ├──basePage.py*                     _# 页面基类的封装基础操作_
##### │   ├──error.py                         _# 自定义的错误类型_
##### │   ├──pay.py                           _# 支付相关函数_
##### ├──configs                              _# 配置文件夹_
##### │   ├──cmd.py                           _# 通过命令进行的配置_
##### │   ├──elementsData.py*                 _# 元素定位信息_
##### ├──items                                _# 物品道具相关_
##### │   ├──gears.py                         _# 装备类_
##### │   ├──resource.py                      _# 物品相关的方法_
##### ├──panelObjs                            _# 各页面的具体方法_
##### │   ├── *                               _# 省略
##### │   ├── *                               _# 省略
##### │   ├── *                               _# 省略
##### ├──scripts                              _# 由各页面的具体方法组成的测试用例_
##### │   ├── *                               _# 省略
##### │   ├── *                               _# 省略
##### │   ├── *                               _# 省略
##### ├──tools                                _# 工具文件夹_
##### │   ├── commonTools.py                  _# 通用工具方法
##### │   ├── excelRead.py                    _# excel读表相关方法
##### │   ├── rpcMethod.py*                   _# 与c#脚本通信的方法
##### │   ├── viewport.py                     _# 与viewport相关的方法
##### ├──main.py                              _# 主函数 将各用例进行串联_
##### ├──requirements.txt                     _# 项目导出的依赖包_
##### ├──requirements-all.txt                 _# 环境导出的依赖包_
（其中使用*结尾的文件是比较重要的文件）

### **#配置连接**

1.打开cmd命令窗口输入adb devices命令，获取设备号


    adb devices

2.打开basePage.py,将“设备号”替换为步骤一获取到的设备号


    def __init__(self):
        connect_device("android://127.0.0.1:5037/设备号")

### **#运行用例**

1.可以运行panelObjs文件夹下的各页面的基础方法（单元测试）
    使用方式为：打开对应的游戏界面，给方法填入参数进行运行

2.可以运行scripts文件夹下的各页面测试用例（系统测试） 
    使用方式为：打开对应的游戏界面，运行页面测试用例

3.运行main.py进行回归测试
    使用方式为：新建账号后，在起名界面运行main.py

### **#截至1027的内容**
1.框架层面

    basePage.py                            # 基本页面方法的封装
    rpcMethod.py                           # 与c#的rpc通信
2.页面方法

    baitAndRodAlbumPanel.py                # 装备相册界面
    baitAndRodShowPanel.py                 # 装备展示界面
    battlePanel.py                         # 战斗界面
    battlePassIntroPanel.py                # 通行证介绍页面
    buyEnergyPanel.py                      # 购买体力页面
    champoinshipTournamentsPanel.py        # 锦标赛排行榜
    gearPanel.py                           # 装备信息、升级、升星、洗练界面
    newbieGuidePanel.py                    # 新手引导
    playerSettingPanel.py                  # 玩家设置界面
    playerEditNamePanel.py                 # 玩家头像姓名编辑
    recharge1And1Panel.py                  # 1+1礼包
    rechargeEndlessPanel.py                # 无尽促销礼包
    resultPanel.py                         # 渔获界面
    rewardsPanel.py                        # 奖励弹窗面板
    treasureChestPanel.py                  # 鱼箱界面
    treasureChestMerchantPanel.py          # 鱼箱商人界面
    
    
    









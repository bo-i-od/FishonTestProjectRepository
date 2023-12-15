from poco.drivers.ue4 import UE4Poco
from airtest.core.api import connect_device
from tools import rpcMethod
if __name__ == '__main__':
    dev = connect_device("Windows:///?class_name=UnrealWindow&title_re=.*mp预览.*")

    poco = UE4Poco(device=dev)
    # aaa = poco.agent.rpc.call("GetSDKVersion")
    # print(aaa)
    res = rpcMethod.my_print(poco)
    print(res)







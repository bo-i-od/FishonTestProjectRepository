from configs.pathConfig import EXCEL_PATH
from tools.run_excel_vba_function import runVBAExcel
from time import sleep

if __name__ == "__main__":
    excel_list = ['FISHCARD.xlsm', 'FISHCARD_PACK_INFO.xlsm', 'PAYMENT_GIFT_GROUP.xlsm', 'ITEM_MAIN_LANGUAGE.xlsm', 'DROP_MAIN.xlsm', 'ITEM_MAIN.xlsm', 'DROP_ENTITY.xlsm', 'DROP_PACK.xlsm', 'FISH_BAG.xlsm', 'PAYMENT_GIFT.xlsm', 'FISHCARD_REWARD_GROUP.xlsm']
    for excel in excel_list:
        runVBAExcel(EXCEL_PATH + excel)
        sleep(1)

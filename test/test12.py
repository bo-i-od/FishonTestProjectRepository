from common.basePage import BasePage
from scripts import battleTest

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    bp.quick_qte = True
    battleTest.circulate_fish(bp)

    bp.connect_close()

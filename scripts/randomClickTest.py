import random
from common.basePage import BasePage
from threading import Thread

def randomClick(bp:BasePage):
    cur = 0
    count = 2 * bp.screen_w * bp.screen_h
    w_n = 1 / bp.screen_w
    h_n = 1 / bp.screen_h
    while cur < count:
        x = random.randint(0, bp.screen_w - 1)
        y = random.randint(0, bp.screen_h - 1)
        bp.click_position([x * w_n, y * h_n])
        r = random.randint(0,10)
        if r == 0:
            bp.click_position([x * w_n, y * h_n])
        cur += 1
        print(cur)


if __name__ == '__main__':
    bp = BasePage()
    randomClickThread0 = Thread(target=randomClick, args=[bp])
    randomClickThread1 = Thread(target=randomClick, args=[bp])
    randomClickThread0.start()
    # randomClickThread1.start()

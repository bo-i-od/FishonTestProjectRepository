import random
import uuid

import six

from common.basePage import BasePage
from panelObjs.ChatPanel import ChatPanel
from panelObjs.FlashTipsPanel import FlashTipsPanel


def send_test(bp: BasePage):
    cur = 495
    while cur < 500:
        ChatPanel.click_btn_enter(bp)
        bp.sleep(5)
        if ChatPanel.get_input(bp) != "":
            ChatPanel.input_text(bp, f"{six.text_type(uuid.uuid4())}")
            continue
        ChatPanel.input_text(bp, f"{cur}:{six.text_type(uuid.uuid4())}")
        cur += 1


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533")
    send_test(bp)

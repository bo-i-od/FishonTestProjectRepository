import re

from common.basePage import BasePage
from configs.elementsData import ElementsData

class RoguePrepare(BasePage):
    def get_target_num(self):
        task = self.get_text(element_data=ElementsData.BattlePreparePanel.rogue_prepare.task03)
        target = re.search(r'总怒火值(?:大于|等于|超过|小于)(\d+\.?\d*)', task)
        if target:
            num = int(target.group(1))
            # print(f"目标难度为：{num}")
            return num
        else:
            print("未找到怒火值")

    def click_btn_gohome(self):
        self.click_element(element_data=ElementsData.BattlePreparePanel.rogue_prepare.btn_gohome)
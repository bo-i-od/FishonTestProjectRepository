from common.basePage import BasePage
from configs.elementsData import ElementsData


class RogueResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RogueResultPanel.RogueResultPanel)

    def click_btn_orange(self):
        self.click_until_disappear(element_data=ElementsData.RogueResultPanel.btn_orange)

    def result(self,gear_lv, kind):
        res = f"{gear_lv}级_"
        if kind == 1:
            res += "力_"
        elif kind == 2:
            res += "敏_"
        elif kind == 3:
            res += "智_"
        if self.exist(element_data=ElementsData.RogueResultPanel.panel_succeed):
            value = self.get_text(element_data=ElementsData.RogueResultPanel.succeed_item2_value)
            res += f"难度{value}成功_"
            if self.exist(element_data=ElementsData.RogueResultPanel.tips):
                res += "无损"
            else:
                res += "非无损"
        elif self.exist(element_data=ElementsData.RogueResultPanel.panel_lost):
            value = self.get_text(element_data=ElementsData.RogueResultPanel.lost_item2_value)
            res += f"难度{value}失败_"
            jindu = self.get_text(element_data=ElementsData.RogueResultPanel.title_text1)
            res += f"进度{jindu}"
        print(res)
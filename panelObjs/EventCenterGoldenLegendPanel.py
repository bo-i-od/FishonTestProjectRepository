from common.basePage import BasePage
from configs.elementsData import ElementsData

class EventCenterGoldenLegendPanel(BasePage):
    def is_panel_avtive(self):
        return self.exist(element_data=ElementsData.EventCenterGoldenLegendPanel.EventCenterGoldenLegendPanel)

    def click_tab4(self):
        return self.click_element(element_data=ElementsData.EventCenterGoldenLegendPanel.tab_4)

    def click_btn_close(self):
        return self.click_element(element_data=ElementsData.EventCenterGoldenLegendPanel.btn_close)

    operation_pool = [
        {"element_data": ElementsData.EventCenterGoldenLegendPanel.btn_close, "func": click_btn_close, "weight": 10},
    ]

if __name__ == "__main__":
    bp = BasePage()
    EventCenterGoldenLegendPanel.click_btn_close(bp)
    bp.connect_close()
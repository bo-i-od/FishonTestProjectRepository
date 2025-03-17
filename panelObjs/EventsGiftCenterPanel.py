from common.basePage import BasePage
from configs.elementsData import ElementsData


class EventsGiftCenterPanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.EventsGiftCenterPanel.btn_close, ignore_set={"EventsGiftCenterPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.EventsGiftCenterPanel.EventsGiftCenterPanel)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.EventsGiftCenterPanel.tab_list, element_viewport=ElementsData.EventsGiftCenterPanel.viewport, viewport_direction="column", index=index, ignore_set={"EventsGiftCenterPanel"})

    operation_pool = [
        {"element_data": ElementsData.EventsGiftCenterPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.EventsGiftCenterPanel.tab_list, "func": switch_tab, "weight": 1},
        ]


if __name__ == '__main__':
    bp = BasePage()
    EventsGiftCenterPanel.switch_tab(bp)
    bp.connect_close()
import random

from common.basePage import BasePage
from configs.elementsData import ElementsData


class FlashCardBoxesPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FlashCardBoxesPanel.FlashCardBoxesPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FlashCardBoxesPanel.FlashCardBoxes_btn_close)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.FlashCardBoxesPanel.FlashCardBoxes_btn_i)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.FlashCardBoxesPanel.btn_close_tips)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FlashCardBoxesPanel.tab_list, index=index)

    def click_book(self, index=-1):
        object_id_list = self.get_object_id_list(element_data=ElementsData.FlashCardBoxesRoot.book_list)
        if index < 0:
            index = random.randint(0, len(object_id_list) - 1)
        self.click_object_of_plural_objects(object_id_list=object_id_list, element_viewport=ElementsData.FlashCardBoxesPanel.FlashCardBoxesPanel, viewport_direction="row", delta_len=0.1, camera_name="Camera3D", index=index)
        self.sleep(0.5)
        if FlashCardBoxesPanel.is_panel_active(self):
            self.click_element(object_id=object_id_list[index], camera_name="Camera3D")

    operation_pool = [
        {"element_data": ElementsData.FlashCardBoxesRoot.book_list, "func": click_book, "weight": 1},
        {"element_data": ElementsData.FlashCardBoxesPanel.FlashCardBoxes_btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FlashCardBoxesPanel.FlashCardBoxes_btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.FlashCardBoxesPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
        {"element_data": ElementsData.FlashCardBoxesPanel.tab_list, "func": switch_tab, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # FlashCardBoxesPanel.click_book(bp)
    # FlashCardBoxesPanel.click_btn_close(bp)
    # FlashCardBoxesPanel.click_btn_i(bp)
    # FlashCardBoxesPanel.is_panel_active(bp)
    # FlashCardBoxesPanel.switch_tab(bp)
    FlashCardBoxesPanel.click_btn_close_tips(bp)
    bp.connect_close()
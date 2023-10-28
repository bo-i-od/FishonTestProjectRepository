from common.basePage import BasePage
from configs.elementsData import ElementsData

class TaskPanel(BasePage):
    def get_view_port_range(self):
        view_port = self.get_element(element_data=ElementsData.Task.view_port)
        x_left = view_port.get_position()[0] - 0.5 * view_port.get_size()[0]
        x_right = view_port.get_position()[0] + 0.5 * view_port.get_size()[0]
        return x_left, x_right
    def get_button_position(self):
        btn_completed_list = self.get_elements(ElementsData.Task.btn_completed_list)
        for btn_completed in btn_completed_list:
            print(btn_completed.get_position())


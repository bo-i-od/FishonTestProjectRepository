from common.basePage import BasePage
from configs.elementsData import ElementsData

class FriendPanel(BasePage):
    def add_friend(self,id):
        self.click_element(element_data=ElementsData.Friend.btn_add_friend)
        self.click_element(element_data=ElementsData.Friend.input_search)
        self.set_text(element_data=ElementsData.Friend.input_search,text=id)
        self.sleep(1)
        self.click_element(element_data=ElementsData.Friend.btn_search)
        self.sleep(4)
        self.click_element(element_data=ElementsData.Friend.btn_search)
        self.sleep(1)
        self.click_element(element_data=ElementsData.Friend.btn_add)

if __name__ == '__main__':
    bp = BasePage()
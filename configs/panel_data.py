from enum import Enum
from configs.element_data import ElementData

class PanelType(Enum):
    All = 0
    # 常规页面
    Common = 1
    # 点击操作无法响应又无法手动关闭的窗口。例如断线重连转菊花页面。
    Waiting = 2
    # 弹窗页面，遇到了会自动清理
    Pop = 3


class PanelData:
    def __init__(self, panel_name, element_data, close_path=None, open_path=None, panel_type=None):
        # 名称
        self.panel_name = panel_name
        # UI元素定位
        self.element_data = element_data
        # 关闭页面需要哪些操作
        self.close_path = close_path if close_path is not None else []
        # 打开页面需要哪些操作
        self.open_path = open_path if open_path is not None else []
        # 页面类型
        self.panel_type = panel_type

    def __repr__(self):
        return f"<UIData: {self.panel_name}>"


PANEL_DATA_MAP = {
    "LoginPanel": PanelData(panel_name="LoginPanel", element_data=ElementData.LoginPanel.LoginPanel)
    # "UiAllianceJoinGuide": PanelData(panel_name="UiAllianceJoinGuide", element_data=ElementData.UiAllianceJoinGuide.UiAllianceJoinGuide, close_path=[{"click_element_outside": ElementData.UiAllianceJoinGuide.Sprite}], panel_type=PanelType.Pop),
    # "UIBuilding": PanelData(panel_name="UIBuilding", element_data=ElementData.UIBuilding.UIBuilding, close_path=[{"click_element_outside": ElementData.UIBuilding.bg}]),
}













from panelObjs.entryUpdateLoadind import EntryUpdateLoading
from common.basePage import BasePage
from configs.elementsData import ElementsData


def tap_to_start(bp: BasePage):
    if not EntryUpdateLoading.is_panel_active(bp):
        return
    EntryUpdateLoading.click_tap_to_start(bp)


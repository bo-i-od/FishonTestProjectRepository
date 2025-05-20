from activities.fishery import fish_bag, fishery, achievement, flash_card, ndays
from configs.pathConfig import EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities


def main(excel_tool: ExcelToolsForActivities):
    mode = 2
    fish_bag.main(excel_tool, mode=mode)
    fishery.main(excel_tool, mode=mode)
    flash_card.main(excel_tool, mode=mode)
    ndays.main(excel_tool, mode=mode)
    achievement.main(excel_tool)


if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool)

from activities.fishery import fish_bag, fishery, achievement, flash_card, ndays
from configs.pathConfig import EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities


def main(excel_tool: ExcelToolsForActivities):
    fish_bag.main(excel_tool, mode=1)
    fishery.main(excel_tool, mode=1)
    flash_card.main(excel_tool, mode=1)
    ndays.main(excel_tool, mode=1)
    achievement.main(excel_tool)


if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool)

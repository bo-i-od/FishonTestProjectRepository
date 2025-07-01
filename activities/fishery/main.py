from activities.fishery import fish_bag, fishery, achievement, flash_card, ndays, fish_template
from configs.pathConfig import EXCEL_PATH
from tools.decl2py import update_h
from tools.excelRead import ExcelToolsForActivities


def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)

    fish_template.main(excel_tool=excel_tool, fishery_id=500307)
    mode = 2
    fish_bag.main(excel_tool, mode=mode)
    fishery.main(excel_tool, mode=mode)
    flash_card.main(excel_tool, mode=mode)
    ndays.main(excel_tool, mode=mode)
    achievement.main(excel_tool)


if __name__ == '__main__':
    update_h(output_dir="../decl")
    main()

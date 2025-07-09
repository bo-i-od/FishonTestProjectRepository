from tools.decl2py import update_h
update_h(output_dir="../decl")
from activities.three_days import three_days
from configs.pathConfig import EXCEL_PATH

from tools.excelRead import ExcelToolsForActivities


def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    mode = 1

    fishery_id = 400322
    activityName = "探礁加"
    imgNameInner = "ActivityTasks_banner_bg_100"

    three_days.main(excel_tool, mode=mode, fishery_id=fishery_id, activityName=activityName, imgNameInner=imgNameInner)


if __name__ == '__main__':

    main()

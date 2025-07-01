from activities.ndays import ndays
from configs.pathConfig import EXCEL_PATH
from tools.decl2py import update_h
from tools.excelRead import ExcelToolsForActivities


def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    mode = 1

    groupId = 5100104
    groupId_battle_pass = 44
    fishery_id = 500302
    open_time = "2025-08-16 00:00:00"
    activityName = "探礁加勒比"
    imgNameInner = "ActivityTasks_banner_bg_100"
    newNDaysImgName = "ActivityTasks_ndays_logo_jlb"

    ndays.main(excel_tool=excel_tool, mode=mode, groupId=groupId, groupId_battle_pass=groupId_battle_pass, fishery_id=fishery_id, open_time=open_time, activityName=activityName, imgNameInner=imgNameInner, newNDaysImgName=newNDaysImgName)


if __name__ == '__main__':
    update_h(output_dir="../decl")
    main()

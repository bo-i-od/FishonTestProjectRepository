from common.basePage import BasePage


if __name__ == '__main__':
    bp = BasePage()
    buff = 0
    tpid = 308003
    fish_type = bp.excelTools.get_fish_type([tpid])[0]
    base1 = 1000
    base2 = base1 + 200
    FISHTYPE_ADD_common = 0
    if fish_type == 1:
        FISHTYPE_ADD_common = -950
    elif fish_type == 2:
        FISHTYPE_ADD_common = -850
    elif fish_type == 3:
        FISHTYPE_ADD_common = -600
    elif fish_type == 4:
        FISHTYPE_ADD_common = 0
    elif fish_type == 5:
        FISHTYPE_ADD_common = 1500
    base3 = base2 * (1000 + FISHTYPE_ADD_common)/1000
    point = base3 * (1000 + buff) /1000





















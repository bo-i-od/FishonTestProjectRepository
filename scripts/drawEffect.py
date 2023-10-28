from common.basePage import BasePage

from panelObjs.gearPanel import GearPanel
def draw_type_count(bp: BasePage):
    cur = 1
    count_size = 0
    count_damage = 0
    count_all_size = 0
    count_salt_fresh = 0
    while cur <= 500:
        GearPanel.click_draw_gold(bp)
        bp.sleep(5)
        res = GearPanel.get_draw_result(bp)
        if "boss_size_fish_weight_up" == res or "small_size_fish_weight_up" == res or "large_size_fish_weight_up" == res or "mid_size_fish_weight_up"== res or "hidden_size_fish_weight_up"== res:
            count_size += 1
        if "all_size_fish_weight_up"== res:
            count_all_size += 1
        if "more_damage" == res:
            count_damage += 1
        if "fresh_water_fish_weight_up" == res or "sea_fish_weight_up" == res:
            count_salt_fresh += 1
        print(f"体型:{count_size/float(cur)},所有：{count_all_size/float(cur)},伤害：{count_damage/float(cur)},咸淡水：{count_salt_fresh/float(cur)},共计{cur}")
        cur += 1

#     fishery_weight_up  Assets/InBundle/UI/Image/Term_Icon/fishery_weight_up.png



if __name__ == '__main__':
    bp = BasePage()
    draw_type_count(bp)

def check_icon_list(icon_list):
    cur = 0
    while cur < len(icon_list):
        icon_list[cur] = check_icon(icon_list[cur])
        cur += 1
def check_icon(icon):
    "store_buff_doublehook"
    s = icon.split('_')
    if s[0] == 'coin' and s[1] == "gold":
        icon = 'coin_gold'
    elif s[0] == 'store':
        if s[1] == "money":
            icon = 'coin_gem'
        elif "box" in s[1]:
            icon = s[1]
        elif s[1] == "buff":
            icon = icon.replace("store", "item")
        elif s[1] == "res" and s[2] == "gear":
            icon = f'{s[1]}_{s[2]}_{s[3]}'
    return icon




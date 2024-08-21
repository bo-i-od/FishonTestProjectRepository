from load_log import load_log

data = load_log('hook_log.txt')

# ------新增鱼获星数分布----------
star_dict={}
for i in data:
    if i['star']:
        star=int(i['star'])
        if star>0:
            star_dict.setdefault(star,0)
            star_dict[star]+=1
sort_list=sorted(star_dict.items(),key=lambda item:item[0],reverse=True)
print("钓鱼星数统计")
print(sort_list)


taiwei = [
{"name":"俊杰","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
{"name":"老葛","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
{"name":"付名","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
{"name":"李超","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
{"name":"产品","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
{"name":"开发","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
{"name":"测试","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]},
]


for i in range(0,len(taiwei)):
    person = taiwei[i]
    if person["name"] == "李超":
        print(taiwei[i])
        break
    else:
       pass

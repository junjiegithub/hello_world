

taiwei = [
{"name":"俊杰","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":"20"},
{"name":"老葛","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":"20"},
{"name":"付名","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":20},
{"name":"李超","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":20},
{"name":"李超","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":21},
{"name":"开发","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":25},
{"name":"测试","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":20},
]


for i in range(0,len(taiwei)):
    person = taiwei[i]
    # if person["name"] == "李超":
    #     print(taiwei[i])
    #
    # else:
    #    pass
    # if person["name"]=="李超" and person["age"]>20:
    #     print(person["name"])
    # else:
    #     print("________NONE______")
    if person["name"] == "李超" or int(person["age"]) > 20:
     print(taiwei[i])
    else:
     print("________NONE______")
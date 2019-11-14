#
#
# taiwei = [
# {"name":"俊杰","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":2920},
# {"name":"老葛","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":22},
# {"name":"付名","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":20},
# {"name":"李超","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":20},
# {"name":"李超","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":21},
# {"name":"开发","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":25},
# {"name":"测试","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"],"age":20},
# ]
#
#
# for i in range(0,len(taiwei)):
#     person = taiwei[i]
#     # if person["name"] == "李超":
#     #     print(taiwei[i])
#     #
#     # else:
#     #    pass
#     # if person["name"]=="李超" and person["age"]>20:
#     #     print(person["name"])
#     # else:
#     #     print("________NONE______")
#     if person["name"] == "李超" or int(person["age"]) > 20:
#      print(taiwei[i])
#     else:
#      print("________NONE______")
#
# for item in taiwei:
#     if item["name"]=="李超":
#         print(item["name"])
#     else:
#         print("______")


#第三节课
"""
字典：每个字 键值 对key，value
方式一：只对键的遍历，通过键名来获取值：
for key in 字典变量名:
    每个元素都要做的事情
取值：字典变量名【key】

方式二：对键和值都进行遍历。同时获取键和值
for key，value in 字典变量名.items():
    每个元素都要做的事情
key：键名
value：对应的值

"""


person_info = {"name":"John","age":22,"contury":"England","sex":"male","height":180,"weight":140,"thing":["apple","orange"]}
#通过键名来获取
#["name","sex"]
for key in person_info.keys():
    print(person_info[key])

#遍历 key,value
for key,value in person_info.items():
    print(key,value)


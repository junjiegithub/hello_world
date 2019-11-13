
'''
变量：存储数据    name ="hello"

列表
'''

list_A = ['老葛','李超','老板','俊杰']
print(list_A)

c =len(list_A)
print(c)
print(c-1)
print(list_A[-1])
print(list_A[c-1])

#修改
list_A[c-1]="太微"
print(list_A[-1])
del list_A[-1]
print(list_A)
#添加
asd ="sadasd"
list_A.append(asd)
print(list_A)

#字典
dict_A ={"name":"俊杰","sex":"man","city":"shenzhen","gongsi":["taiwei","yuheng"]}
print(dict_A)

#获取字典里的数据
a= dict_A["gongsi"]
print(a)
#改
dict_A["gongsi"]="yuheng"
print(dict_A)
#增加
dict_A["height"]=180
print(dict_A)
#删除
del dict_A["height"]
print(dict_A)

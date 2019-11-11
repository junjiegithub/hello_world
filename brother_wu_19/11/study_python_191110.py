
count =0
while True:
    if count ==5:
        break
    print('hello world!')
    count+=1
else:
    print("----over-----!")


# i=0   #计数器
# while i<5:
#     print("hello,world!")
#
#     i+=1
#
# print("---over---!")
'''
循环：
场景：
    1.银行：
        用户名和密码 ---》3次
    2.产生银行卡号随机数
        16
    3.。。。。
结构：
    while
    格式：
    while 条件：
        条件成立执行语句部分
注意：不要死循环
    1.改变条件： i count 计数变量
    2.在循环体中设置break

2.
while 条件:a
    条件成立执行的语句部分
    循环体
else：
    表示条件完成了规定的次数，没有遇到break
    for
验证用户名和密码是否正确，如果正确则输出登录成功，否则用户名或者密码有误
'''
#验证用户名和密码三次
#申明变量
# count =1
# while count <4:
#     username = input("请输入用户名:")
#     password = input("输入密码:")
#
#     #变量和运算符构成判断条件（admin，123456）
#
#     if username == 'admin' and password =='123456':
#         print('登录成功！')
#         break   #跳出整个循环结构
#     else:
#         print("用户名或密码有误，请重新输入")
#         # if count == 3:    #方式一
#         #     print('账户锁定！')
#     #改变计算器
#         count += 1
#
# #方式二：
# if count ==4:
#     print("账户锁定！")
#
#
#

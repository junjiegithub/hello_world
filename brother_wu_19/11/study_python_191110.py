# i=0
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
        
    for
验证用户名和密码是否正确，如果正确则输出登录成功，否则用户名或者密码有误
'''
#申明变量

username = input("请输入用户名:")
password = input("输入密码:")

#变量和运算符构成判断条件（admin，123456）

if username == 'admin' and password =='123456':
    print('登录成功！')
else:
    print("用户名或密码有误，请重新输入")
    username = input("请输入用户名:")
    password = input("输入密码:")
    if username == 'admin' and password == '123456':
        print('登录成功！')
    else:
        print("用户名或密码有误，请重新输入")
    username = input("请输入用户名:")
    password = input("输入密码:")
    if username == 'admin' and password == '123456':
        print('登录成功！')
    else:
        print("账户锁定！")



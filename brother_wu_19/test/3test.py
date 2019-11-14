'''
函数的定义：
    1，具备某一功能的代码段
    2.可以重复使用
函数的定义语法：
def 函数名称（）：
    函数体（实现功能的代码段）
注意：函数体的缩进

函数的调用
调用语法
    没有参数：
        函数名称（）
    有函数：
        函数名称（实参值）
'''

def san():
    print("遮风挡雨遮阳")

san()
san()

def get_money_from_ATM(bank_id,passwd,money):
    #验证你的银行卡是否有效，是否有余额
    #检测：密码是否正确
    #取款 金额 是否< 你的存款
    #以上符合的情况下，吐出人民币给你，完了再吐出你的银行卡
    print("******")
    print(bank_id,passwd,money)


icbc_card_id ="1111111111"
passwd="123456"
money=2000


get_money_from_ATM(icbc_card_id,passwd,money)
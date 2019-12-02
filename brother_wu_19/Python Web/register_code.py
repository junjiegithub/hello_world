#coding=utf-8
import time
import random
from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # 定义变量存webdriver

#初始化浏览器
def driver_init():
    #driver = webdriver.Chrome()#定义变量存webdriver
    driver.get("http://sitold.uhuasuan.com/login")   #get网址
    driver.maximize_window()
    # time.sleep(3)

#获取element信息
def get_element(name):
    element =driver.find_element_by_name(name)
    return element


#获取随机数
# def get_range_user():
#     user_info=''.join(random.sample('12345678980abcdefghijklmn',8))
#     return user_info

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)  # 截取整个网页并保存到D盘
    code_element =driver.find_element_by_id("imgCode")  # 定义变量获取验证码的定位元素
    # print(code_element.location)#{'x': 795, 'y': 359}       #打印验证码在网页上的坐标
    left = code_element.location['x']  # 定义验证码左边的定位数值
    top = code_element.location['y']  # 定义验证码上边的坐标
    right = code_element.size['width'] + left  # 定义验证码图片的宽度和坐标
    height = code_element.size['height'] + top  # 定义验证码图片的宽度和坐标
    im = Image.open(file_name)  # 定义打开保存的网页截图
    img = im.crop((left, top, right, height))  # 定义整个验证码的4个坐标
    img.save(file_name)  # 保存截取的验证码图片到D盘

#解析图片获取验证码
def code_online(file_name):
    image = Image.open(file_name)
    text = pytesseract.image_to_string(image)  # 识别图片
    print(text)
    return text

#运行主程序
def run_main():
    # user_name_info =get_range_user()
    login_name ="测试账号"
    password="123456"
    file_name ="D:/chrom/b.png"
    driver_init()
    get_element("users.login_name").send_keys(login_name)
    get_element("users.password").send_keys(password)
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("verificationCode").send_keys(text)

    driver.find_element_by_xpath('//*[@id="LoginForm"]/div[7]/input').click()
    # while True:
    #     if EC.title_contains("测试账号")==0:
    #         print("登录成功")
    #         break
    while EC.title_contains("测试账号")==0:
            print("登录成功")
            break


    # driver.close()
    #print(EC.title_contains("登录"))
#run_main()
#
# while run_main():
#     if driver.find_element_by_xpath('//*[@id="user_menu"]/li[2]/a')=="测试账号":
#         print("登录成功")
#         break
#     else:
#         run_main()

run_main()

#coding=utf-8
import time
import random
from PIL import Image
from selenium import webdriver
import pytesseract

driver = webdriver.Chrome()  # 定义变量存webdriver
#初始化浏览器
def driver_init():
    driver = webdriver.Chrome()#定义变量存webdriver
    driver.get("http://sitold.uhuasuan.com/login")   #get网址
    driver.maximize_window()
    time.sleep(3)

#获取element信息
def get_element(id):
    element =driver.find_element_by_id(id)

#获取随机数
def get_range_user():
    user_info=''.join(random.sample('12345678980abcdefghijklmn',8))
    return user_info

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)  # 截取整个网页并保存到D盘
    code_element = driver.find_element_by_id(file_name)  # 定义变量获取验证码的定位元素
    # print(code_element.location)#{'x': 795, 'y': 359}       #打印验证码在网页上的坐标
    left = code_element.location['x']  # 定义验证码左边的定位数值
    top = code_element.location['y']  # 定义验证码上边的坐标
    right = code_element.size['width'] + left  # 定义验证码图片的宽度和坐标
    height = code_element.size['height'] + top  # 定义验证码图片的宽度和坐标
    im = Image.open(file_name)  # 定义打开保存的网页截图
    img = im.crop((left, top, right, height))  # 定义整个验证码的4个坐标
    img.save(file_name)  # 保存截取的验证码图片到D盘

#解析图片获取验证码
def code_online():
    image = Image.open("file_name")
    text = pytesseract.image_to_string(image)  # 识别图片
    return text

#运行主程序
def run_main():
    get_element("users.login_name")

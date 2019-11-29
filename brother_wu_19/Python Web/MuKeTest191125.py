#-*- coding:utf-8 -*-
#http://www.5itest.cn/register
'''
???????????
51test???????
????-????????????  --???????????
?????  18????????9??????
????    5??20??????????????????????
????? ????????

id ??????? ????? ??????? ???? ?????
Login_01 ???  ???? ??????  1.??????????????????http://www.5itest.cn/register?     1.??????????????
id??????register-btn  ???????  2.?????id?register_email????????????1416279053@qq.com   2.??????????
'''

import time
import random
import pytesseract #识别图片的包
from PIL import Image    #截取图的模块
from selenium import webdriver          #从selenium包里导入webdriver
from selenium.webdriver.support import expected_conditions as EC        #导入异常处理模块
from selenium.webdriver.support.wait import WebDriverWait       #导入等待时间
from selenium.webdriver.common.by import By       #导入By模块

driver = webdriver.Chrome()#定义变量存webdriver
driver.get("http://sitold.uhuasuan.com/login")   #get网址
# time.sleep(5)
print(EC.title_contains("登录"))        #打印元素地址，判断网页是否包含登录，可以正常打开
# user_email=random.sample('1234567890abcdefg',5)
# for i in range(5):
#     user_email =''.join( random.sample('1234567890abcdefg', 5))+"@qq.com"
#     print(user_email)
#
driver.save_screenshot("D:/chrom/a.png")                #截取整个网页并保存到D盘
code_element=driver.find_element_by_id("imgCode")       #定义变量获取验证码的定位元素
#print(code_element.location)#{'x': 795, 'y': 359}       #打印验证码在网页上的坐标
left =code_element.location['x']                        #定义验证码左边的定位数值
top=code_element.location['y']                          #定义验证码上边的坐标
right=code_element.size['width']+left                   #定义验证码图片的宽度和坐标
height=code_element.size['height']+top                  #定义验证码图片的宽度和坐标
im=Image.open("D:/chrom/a.png")                         #定义打开保存的网页截图
img=im.crop((left,top,right,height))                    #定义整个验证码的4个坐标
img.save("D:/chrom/b.png")                              #保存截取的验证码图片到D盘
image =Image.open("D:/chrom/b.png")
text=pytesseract.image_to_string(image)#识别图片
print(text)
                                      #关闭浏览器

driver.find_element_by_name("users.login_name").send_keys("测试账号")
time.sleep(1)
driver.find_element_by_name("users.password").send_keys("123456")
time.sleep(1)
driver.find_element_by_name("verificationCode").send_keys(text)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="LoginForm"]/div[7]/input').click()
time.sleep(5)
driver.close()


#element= driver.find_elements_by_class_name("controls")
#EC.visibility_of_element_located(element)#判断这个元素可以不可以见,
# locator = (By.CLASS_NAME,"controls")
# WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
# email_element=driver.find_element_by_id("register_email")
# print(email_element.get_attribute("placeholder"))
# email_element.send_keys("test@qq.com")
# print(email_element.get_attribute("value"))

# driver.close()





# driver.find_element_by_id("register_email").send_keys("1416279053@qq.com")
# user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# user_element=user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("PythonWorld")
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys("111111")
#

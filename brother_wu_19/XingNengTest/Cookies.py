
#coding =utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

option =webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\mayn\\AppData\\Local\\Google\\Chrome\\User Data')

driver = webdriver.Chrome(chrome_options=option)
driver.get("http://sitold.uhuasuan.com/")

YongHuMing="测试账号"
actual =driver.find_element_by_tag_name("body").text
print(actual)
if YongHuMing in actual:
    print("测试通过")
else:
    print("测试失败")
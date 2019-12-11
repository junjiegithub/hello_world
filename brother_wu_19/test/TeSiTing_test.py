"""
自动化永恒不变的追求：脚本能够快速稳定的运行
1.ui自动化
    UI：User Interface，用户交互界面 （Web UI，APP UI，客户端UI）
        狭义上面来讲：UI自动化可以只是说明是WEB自动化


    面向用户的软件：所有的功能都是UI界面像用户提供的。
    UI自动化：其实就是功能自动化

2.Python标准编程规范
    创建项目
    所有的模块必须放在包里面
    指定编码
    pip install selenium

3.Python selenium 自动化
    （搞清楚自己要做什么）
    #selenium打开浏览器
    输入网址
    (问题1：driver路径配置
     问题2：加载太慢，或者使用缓存--user-dir-data=)
4.web自动化详解
    web自动化你要做哪些模块或者功能的自动化？
        web自动化是用来做自动化回归验证
        #如果你改了一个购物车的功能，但是你不知道有没有影响到其它模块的改变，不可能全部
        测试一遍，这个时候就用自动化改一下购物车的脚本。执行自动化测试。
    严格分析手动的过程，对比自动化到底那里和手动有出入
"""
#coding = utf-8
# selenium打开浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains  #模拟鼠标
import time

#https://www.cnblogs.com/dieyaxianju/p/8540740.html
#https://blog.csdn.net/qq_42735170/article/details/90712556,(unknown error: DevToolsActivePort file doesn't exist)

'''
#https://www.cnblogs.com/dieyaxianju/p/8540740.html
Selenium启动Chrome时，加载用户配置文件

#https://blog.csdn.net/qq_42735170/article/details/90712556,
(unknown error: DevToolsActivePort file doesn't exist)
在判断自己代码没错之后中与发现了问题所在
这个功能只能第一次打开的浏览器中使用，第一个不结束，第二个再使用就会出错
，最后的解决办法就是关闭所有的浏览器 然后从新启动脚本
 
'''
#添加用户文件配置
option =webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\\mayn\\AppData\\Local\\Google\\Chrome\\User Data')

# # selenium打开浏览器,executable_path='../Lib'
driver=webdriver.Chrome(chrome_options=option)
#driver.maximize_window()
#添加隐式等待
driver.implicitly_wait(5)
# driver=webdriver.Chrome()
#打开网站
driver.get('http://112.74.191.10:8000/')
# driver.get('http://sitold.uhuasuan.com/')

#点击登录按钮
#1.找到元素在哪里

ele =driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
#2.点击这个元素
ele.click()

#输入用户名
driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')

driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1234')

driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a').click()

#搜索手机
driver.find_element_by_xpath('//*[@id="q"]').send_keys('手机')
driver.find_element_by_xpath('//*[@id="sourch_form"]/a').click()

#加入购物车
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="join_cart"]').click()
#关闭弹窗
time.sleep(2)
driver.find_element_by_xpath('//*[@id="layui-layer1"]/span/a').click()

#结算，悬停

ac=ActionChains(driver)

ac.move_to_element(driver.find_element_by_xpath('//*[@id="hd-my-cart"]/a/div')).perform()
driver.find_element_by_xpath('//*[@id="show_minicart"]/div/div/div[3]/a').click()
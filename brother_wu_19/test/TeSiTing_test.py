"""
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
"""
#coding = utf-8
# selenium打开浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
# driver=webdriver.Chrome()
#打开网站
driver.get('http://112.74.191.10:8000/')
# driver.get('http://sitold.uhuasuan.com/')



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

"""
#coding = utf-8
from selenium import webdriver


driver=webdriver.Chrome()

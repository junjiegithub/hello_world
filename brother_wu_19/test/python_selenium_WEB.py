'''

python+selenium-web自动化测试（功能测试）
web自动化测试
1.web网页-系统对象
2.在浏览器中访问
3.通过浏览器与web网页进行交互（操作页面，输入，网页输出）
目标：代码代替人-驱动-完成在浏览器上操作页面中的元素。

web自动化-环境安装
1.安装浏览器-Google,Firefox,IE....
    windows平台:双击exe文件运行即可。
2.安装浏览器驱动-chromedriver.exe,geckodriver.exeiedriver.exe....
    拷贝XXdriver.exe到python安装目录下
3.安装selenium
    cmd命令行运行:pip install -U selenium

4.框架--调用款阿静


chromedriver



'''
from selenium import webdriver

driver=webdriver.Chrome()

#访问百度首页
driver.get("http://www.baidu.com")

#找到百度首页-输入框
ele =driver.find_element_by_id("kw")

#输入内容 chromedriver
ele.send_keys("chromedriver")

driver.find_element_by_id("su").click()
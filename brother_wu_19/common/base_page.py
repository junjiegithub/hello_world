from selenium import webdriver

#定义俩基础操作方便以后调用
class base():
    def click(driver,id):
        #driver = webdriver.Chrome()
        driver.find_element_by_id(id).click()
    def send_msg(driver,id,msg):
        #driver = webdriver.Chrome()
        driver.find_element_by_id(id).send_keys(msg)
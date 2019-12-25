from selenium import webdriver
import unittest
import time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # self.base_url="http://www.baidu.com"
        self.base_url ="http://sitold.uhuasuan.com/"


    # def test_baidu(self):
    #     driver=self.driver
    #     driver.get(self.base_url+"/")
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("unittest")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(2)
    #     title=driver.title
    #     #self.assertEquals(title,"unittest_百度搜索")
    #     self.assertEquals(title,"登陆-一个购物更省钱的平台")
    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        # driver.find_element_by_id("kw").clear()
        # driver.find_element_by_id("kw").send_keys("unittest")
        # driver.find_element_by_id("su").click()
        time.sleep(2)
        title=driver.title
        print(title)
        #self.assertEquals(title,"unittest_百度搜索")
        self.assertEquals(title,"登陆-一个购物更省钱的平台")
    #
    # def tearDown(self):
    #     self.driver.quit()

if __name__=="__main__":
    unittest.main()
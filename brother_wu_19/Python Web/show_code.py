import selenium
from selenium import webdriver

driver=webdriver.Chrome()

url="http://www.jinmiao.com/"

driver.get(url)

driver.find_element_by_xpath('//*[@id="__layout"]/div/header/div/div[1]/nav/ul/li[3]/a/span').click()



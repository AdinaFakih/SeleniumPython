from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/") #opening URL takes some time
driver.implicitly_wait(4) #seconds, only one time use
assert "Welcome: Mercury Tours" in driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()
time.sleep(2)
driver.close() #close browser                                                                                                                                                                   
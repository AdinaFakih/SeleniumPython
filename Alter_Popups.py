from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
#driver.switch_to_alert().accept()  #to click OK
driver.switch_to_alert().dismiss()  #closes alert by using cancel button
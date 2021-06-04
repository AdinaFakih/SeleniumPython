from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("https://en-gb.facebook.com/")
#<input type="text" name="email" id="email">

user_element = driver.find_element_by_name("email")
print(user_element.is_displayed()) #return true/false based of element status
print(user_element.is_enabled())   #return true/false

pwds_element = driver.find_element_by_name("pass")
print(pwds_element.is_displayed()) #return true/false based of element status
print(pwds_element.is_enabled())   #return true/false

user_element.send_keys("@gmail.com")
pwds_element.send_keys("")

driver.find_element_by_name("login").click()
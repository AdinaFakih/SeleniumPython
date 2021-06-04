from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_forms.asp")

input_fname = driver.find_element_by_id("fname")
input_lname = driver.find_element_by_id("lname")

input_fname.clear()
input_fname.send_keys("adi")
time.sleep(2)
input_lname.clear()
input_lname.send_keys("fakih")

#driver.find_element_by_name("login").click()
#time.sleep(2)
input_lname.submit()
#driver.quit() #closes all tabs in browsers
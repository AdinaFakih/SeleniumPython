from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.get("http://scraper.dev/test/1.html")
driver.maximize_window()
time.sleep(2)
div_title = driver.find_element_by_tag_name("div") #only one element of div on whole page

action = ActionChains(driver)
action.double_click(div_title)
action.pause(1)

for i in range(10):
    action.double_click(div_title)
    action.pause(1)
action.perform()
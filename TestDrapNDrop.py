#didn't run

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")

time.sleep(8)
#for i in range(1,5):
source_element = driver.find_element_by_id("todrag")
time.sleep(2)
target_element = driver.find_element_by_id("mydropzone")

action = ActionChains(driver)
action.drag_and_drop(source_element, target_element)
action.pause(1)

action.perform()
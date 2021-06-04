#didn't run

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
driver.maximize_window()  # Let window maximize
print(driver.title)  # print page title
Source_1 = driver.find_element_by_xpath('//*[@id="todrag"]/span[1]')
Target_1 = driver.find_element_by_xpath('//*[@id="mydropzone"]')
Actions = ActionChains(driver)
Actions.drag_and_drop(Source_1, Target_1)
Actions.perform()
time.sleep(2)

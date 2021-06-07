from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
element = driver.find_element_by_id("multi-select")  #drp object name , Select is class
M_drp = Select(element)
M_drp.select_by_index(0)
M_drp.select_by_value("Florida")
M_drp.select_by_visible_text("New Jersey")
M_drp.select_by_index(3)
M_drp.select_by_value("Ohio")
M_drp.select_by_visible_text("Texas")
time.sleep(2)
M_drp.deselect_by_index(0)
time.sleep(2)
M_drp.deselect_by_value("Florida")
time.sleep(2)
M_drp.deselect_by_visible_text("Texas")

time.sleep(5)
driver.quit()
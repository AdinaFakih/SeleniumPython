from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get("http://jqueryui.com/slider/")

driver.switch_to.frame(driver.find_element_by_class_name("demo-frame"))
silder = driver.find_element_by_id("slider")
#dim = silder.getSize()
#x = dim.getWidth()

act = ActionChains(driver)
act.drag_and_drop_by_offset(silder, -100,0)
act.perform()

time.sleep(2)
driver.close()









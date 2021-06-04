from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
#driver.get("http://essemble.co.uk/escript/drag_drop_engine/dragdrop1.html")
driver.get("https://h5p.org/h5p/embed/594591")
time.sleep(8)
for i in range(1,9):
    print(i)
    source_element = driver.find_element_by_id(f"drag{i}")
    time.sleep(2)
    target_element = driver.find_element_by_id(f"drop{i}")/html/body/div/div/div[2]/div/div[19]/div

    action = ActionChains(driver)
    action.drag_and_drop(source_element, target_element)
    action.pause(1)

    action.perform()

time.sleep(2)
btn_confirm = driver.find_element_by_id("btn")
btn_confirm.click()

'''s1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[24]")
time.sleep(2)
t1 = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[14]/div")
time.sleep(2)
action = ActionChains(driver)
action.drag_and_drop(s1, t1).perform()
action.pause(1)'''

'''s2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[6]")
time.sleep(2)
t2 = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[18]/div")
time.sleep(2)
action = ActionChains(driver)
action.drag_and_drop(s2, t2)
action.pause(1)'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("https://www.w3.org/TR/wai-aria-practices-1.1/examples/checkbox/checkbox-2/checkbox-2.html")
time.sleep(2)
result = driver.find_element_by_id("cond1").is_selected()
if result:
    print('Checkbox already selected')
else:
    driver.find_element_by_id("cond1").click()
    print("Checkbox selected")

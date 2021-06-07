from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

print(driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()) #returns True or False

driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click()   #select radio button

print(driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected())

time.sleep(3)
driver.quit()
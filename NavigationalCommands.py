from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/") #first fr

print(driver.title) #fr

driver.get("http://pavantestingtools.blogspot.in/") #tt
time.sleep(5)
print(driver.title) #tt

driver.back()
time.sleep(5)
print(driver.title) #fr

driver.forward()
time.sleep(5)
print(driver.title) #tt

#driver.close()
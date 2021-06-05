from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
'''driver.execute_script("window.scrollBy(0,1000)","") #scroll down page using pixel

flag = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[132]/div/a/img") #scroll down page till element is visible
driver.execute_script("arguments[0].scrollIntoView();",flag)'''

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll to the end of the page







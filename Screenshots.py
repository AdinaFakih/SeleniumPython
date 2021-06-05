from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.guru99.com/test/newtours/")
driver.save_screenshot("C:/Users/addyf/Desktop/Certificates/homepage.png")
time.sleep(2)

driver.close()
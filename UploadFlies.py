from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/Users/addyf/Desktop/pp.jpg")
time.sleep(2)
driver.quit()
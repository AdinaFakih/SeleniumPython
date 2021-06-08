from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

admin = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/a/b')
user_management = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a')
users = driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a')

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()

time.sleep(2)
driver.quit()
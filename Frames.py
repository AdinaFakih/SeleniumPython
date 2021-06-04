from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(2)
driver.switch_to.frame("packageListFrame")  #first frame
driver.find_element_by_link_text("org.openqa.selenium.cli").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")     #second frame
driver.find_element_by_link_text("CliCommand").click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()

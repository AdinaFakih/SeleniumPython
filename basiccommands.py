from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Index.html")
print(driver.title)  #print title of the page
print(driver.current_url)  #returns the URL of the page
driver.find_element_by_xpath("//*[@id='btn2']").click()
time.sleep(5)
#driver.close() #close browser, currently focused browser
driver.quit() #closes all tabs in browsers
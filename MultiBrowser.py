from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver=webdriver.Chrome(executable_path="C:\Program Files\webdriver\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\Program Files\webdriver\geckodriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)  #print title of the page
print(driver.current_url)  #returns the URL of the page
#print(driver.page_source) #HTML code for the page
driver.close() #close browser
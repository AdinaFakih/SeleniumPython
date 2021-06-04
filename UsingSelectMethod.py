from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("https://mdbootstrap.com/docs/b4/jquery/forms/select/")

select_element = driver.find_element_by_xpath("//*[@id='basic']/div/div[1]/section[1]/select")
select_object = Select(select_element)
#select an <option> baesd upon the <select> element's internal index
select_object.select_by_index(1)
time.sleep(2)
#select an <option> baesd upon its value attribute
select_object.select_by_value("2")
time.sleep(2)
#select an <option> baesd upon its text
select_object.select_by_visible_text('Three')
time.sleep(2)
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
time.sleep(2)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element = driver.find_element_by_id("RESULT_RadioButton-9")  #drp object name , Select is class
drp = Select(element)

#select by visible text
drp.select_by_visible_text("Morning")  #morning

#select by index
drp.select_by_index(2) #0(option,option wala) 1 2 3 #afternoon

#select by value
drp.select_by_value("Radio-2") #evening

#Count number of options
print(len(drp.options))

#Capture all the options and print them as output
all_options = drp.options

for option in all_options:
    print(option.text)

time.sleep(4)
driver.quit()
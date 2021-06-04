from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
#driver.get("https://www.expedia.com/") #opening URL takes sometime
#time.sleep(2)
'''driver.find_element(By.XPATH,"//*[@id='uitk-tabs-button-container']/li[2]/a/span").click() #flight
driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[1]/div/div/div/button").send_keys("Karachi") #origin
driver.find_element(By.XPATH,"//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[2]/div/div/div/button").send_keys("New York") #desitination
driver.find_element(By.XPATH,"//*[@id='wizard-hotel-pwa-v2-1']/div[3]/div[2]/button").click()'''

driver.get("http://testautomationpractice.blogspot.com/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='HTML9']/div[1]/button"))
    )
finally:
    time.sleep(10)
    driver.quit()

'''#Explicit Wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable(By.XPATH,"//body/div[1]/div[3]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]"))
element.click()'''
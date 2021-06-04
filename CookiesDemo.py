from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()  # Let window maximize
driver.get("https://www.amazon.in/")

cookies = driver.get_cookies() #Capture all the cookies created by browser
print(len(cookies))  #print number of cookies have been created
print(cookies) #print all the cookies pairs

#adding new cookies to the browser
cookie = {'name': 'Mycookie','value':'123243'}
driver.add_cookie(cookie)

cookies = driver.get_cookies() #Capture all the cookies created by browser
print(len(cookies))  #print number of cookies after adding new cookie
print(cookies)

#deleting cookies
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies() #Capture all the cookies created by browser
print(len(cookies))  #print number of cookies after deleting cookie
print(cookies)

#deleting all cookies
driver.delete_all_cookies() #deleting all cookies, answer 0
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)  #chrome is running so, answer 1

#driver.close()
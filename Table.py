from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()  # Let window maximize
driver.get("http://omayo.blogspot.com/")
cols = len(driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[4]/div[1]/table/thead/tr/th')) #count number of rows
rows = len(driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[4]/div[1]/table/tbody/tr'))  #count number of coloumns
print(cols)
print(rows)
'''Rows = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div[2]/main/div/div[1]/div/article/div/div/div[3]/div/div[1]/table/thead/tr/th'))
Cols = len(driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div/div[2]/main/div/div[1]/div/article/div/div/div[3]/div/div[1]/table/tbody/tr[1]/td'))
print(Rows)
print(Cols)'''''
for r in range(1,rows+1):
    for c in range(1, cols + 1):  # 5-1=4
        value = driver.find_element_by_xpath(f"//*[@id='table1']/tbody/tr[{r}]/td[{c}]").text
        print(value,end='      ')
    print()

driver.quit()
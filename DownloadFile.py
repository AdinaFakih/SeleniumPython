from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "C:\\Users\\addyf\Desktop\Certificates"})

driver = webdriver.Chrome(executable_path= "C:\webdriver\chromedriver.exe", chrome_options=chromeOptions)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")

#Download a text file
driver.find_element_by_id("textbox").send_keys("blahblah blah")
driver.find_element_by_id("createTxt").click()  #generatefile
driver.find_element_by_id("link-to-download").click()

#Download pdf file
driver.find_element_by_id("pdfbox").send_keys("blahblah blah")
driver.find_element_by_id("createPdf").click()  #generatePDFfile
driver.find_element_by_id("pdf-link-to-download").click()



time.sleep(2)
driver.close()





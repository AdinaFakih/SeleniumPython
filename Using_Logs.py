from selenium import webdriver
import time
import logging

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")


logging.basicConfig(filename="C://Users//addyf//Desktop//Certificates//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s,',
                    datefmt='%m/%d/%y: %I: %M: %S %p ',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

driver.maximize_window()
time.sleep(1)
logger.info("Browser Window is maximized")

driver.get("https://careers.gaditek.com/jobs/software-engineer-php")
time.sleep(1)
logger.info("Website opened")

ScrollToUploadBtn = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[2]/div/section[8]/div/div/div/form/div[3]/div/div[1]/span[1]/input")
driver.execute_script("arguments[0].scrollIntoView();",ScrollToUploadBtn)
time.sleep(1)
logging.info("page scrolled to upload resume Button")

UploadButton = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div[2]/div/section[8]/div/div/div/form/div[3]/div/div[1]/span[1]/input").send_keys("C://Users//addyf//Desktop//AdinaFakih_SQA.pdf")
time.sleep(1)
logging.info("Resume has uploaded")
time.sleep(5)
driver.close()
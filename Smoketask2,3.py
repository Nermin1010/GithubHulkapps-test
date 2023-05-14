#TO check whether we can change the COUNTRY/REGION

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")
driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()


driver.find_element(By. CSS_SELECTOR, "#FooterCountryForm > div > div > button").click()
driver.find_element(By. CSS_SELECTOR, "#FooterCountryList > li:nth-child(27) > a").click()

time.sleep(5)
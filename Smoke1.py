#Test whether "Sort by" work properly, "price - low to high

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")



driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()

driver.get("https://qa-practical-test.myshopify.com/collections/all")
driver.find_element(By.ID,"SortBy").click()
driver.find_element(By.CSS_SELECTOR,"#SortBy > option:nth-child(5)").click()

time.sleep(5)
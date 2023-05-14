#Test for Filter "price", it showing the price "from"(300) "to"(600)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")
driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()


driver.get("https://qa-practical-test.myshopify.com/collections/all")
driver.find_element(By.CSS_SELECTOR,"#FacetsWrapperDesktop > details:nth-child(3) > summary > div > span").click()
driver.find_element(By.ID, "Filter-Price-GTE").click()
driver.find_element(By.ID, "Filter-Price-GTE").send_keys("300")
driver.find_element(By.ID, "Filter-Price-LTE").click()
driver.find_element(By.ID, "Filter-Price-LTE").send_keys("600")

time.sleep(5)
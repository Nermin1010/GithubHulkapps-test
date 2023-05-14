#Test for Search functionality

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")
driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()


driver.find_element(By. CSS_SELECTOR, "#shopify-section-header > sticky-header > header > div > details-modal > details > summary > span > svg.modal__toggle-open.icon.icon-search").click()
driver.find_element(By. ID, "Search-In-Modal").click()
driver.find_element(By. ID, "Search-In-Modal").send_keys("Ring")
driver.find_element(By. CSS_SELECTOR, "#shopify-section-header > sticky-header > header > div > details-modal > details > div > div.search-modal__content > predictive-search > form > div.field > button > svg").click()
time.sleep(5)
#Check whether button for the quantity work properly

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")
driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()


driver.get("https://qa-practical-test.myshopify.com/products/14k-bloom-earrings")
driver.find_element(By. CSS_SELECTOR, "#ProductInfo-template--14211560177749__main > div.product-form__input.product-form__quantity > quantity-input > button:nth-child(3)").click()
driver.find_element(By. CSS_SELECTOR, "#product-form-template--14211560177749__main > div.product-form__buttons > button > span").click()
time.sleep(5)
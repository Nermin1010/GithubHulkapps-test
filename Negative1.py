#Wrong input

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")

driver.find_element(By. ID, "password").send_keys("brauf")
driver.find_element(By. CLASS_NAME, "ENTER").click()
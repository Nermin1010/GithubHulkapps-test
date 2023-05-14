#Test for Create account

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")
driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()


driver.get("https://qa-practical-test.myshopify.com/account/register")
driver.find_element(By. ID, "RegisterForm-FirstName").send_keys("Nermin")
driver.find_element(By. ID, "RegisterForm-LastName").send_keys("Jusic")
driver.find_element(By. ID, "RegisterForm-email").send_keys("nerminjusic018@gmail.com")
driver.find_element(By. ID, "RegisterForm-password").send_keys("nermin")
driver.find_element(By. CSS_SELECTOR, "#create_customer > button").click()

time.sleep(5)
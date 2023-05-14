#Test to check whether we can send a comment without enter any text

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://qa-practical-test.myshopify.com/pages/form-builder")

driver.find_element(By. ID, "password").send_keys("brauff")
driver.find_element(By. XPATH, "/html/body/div/div[2]/div[2]/form/button").click()

driver.get("https://qa-practical-test.myshopify.com/pages/contact")
driver.find_element(By.ID,"ContactForm-email").send_keys("nerminjusic018@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#ContactForm > div.contact__button > button").click()

time.sleep(5)
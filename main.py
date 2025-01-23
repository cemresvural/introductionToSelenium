from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver=webdriver.Chrome()
driver.get("https://www.miuul.com")
time.sleep(2)

btn_elements=driver.find_elements(By.XPATH,"//a[@id='login]")
btn=btn_elements[0]

btn.click()

inputs=driver.find_elements(By.XPATH,"//a[@name='arama']")
input=inputs[0]
input.send_keys("Data Science",Keys.ENTER)
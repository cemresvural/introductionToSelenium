from selenium import webdriver
from selenium.webdriver.common.by import By

import time



driver=webdriver.Chrome()
driver.get("https://www.miuul.com")
time.sleep(2)
h1_elem=driver.find_element(By.XPATH,"//h1")
a_elem=driver.find_element(By.XPATH,"//a")
p_elem=driver.find_element(By.XPATH,"//p")

p_elements=driver.find_elements(By.XPATH,"//p")
p_elements
elem=None
if p_elements:
    elem=p_elements[0]
else:
    print("Element not found")

print(elem)
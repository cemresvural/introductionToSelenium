from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get("https://www.miuul.com")

h1_elem=driver.find_element(By.XPATH,"//h1")
a_elem=driver.find_element(By.XPATH,"//a")
p_elem=driver.find_element(By.XPATH,"//p")

selector=(By.XPATH,"//p")
wait=WebDriverWait(driver,10)
p_element=wait.until(EC.visibility_of_element_located(selector))
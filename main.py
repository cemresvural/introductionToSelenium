from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import pandas as pd

# Initialize Driver
options=webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver=webdriver.Chrome(options)
driver.get("https://miuul.com/katalog")
time.sleep(2)

select_option = driver.find_elements(By.XPATH, "//select[@name='sure']/option[contains(text(), '1-3 ay')]")
select_option[0].click() if select_option else None

course_blocks=driver.find_elements(By.XPATH,"//div[contains(@class,'card catalog') and (contains(@class,'block'))]")

for block in course_blocks:
    course_title=block.find_elements(By.XPATH,".//h6")
    course_desc=block.find_elements(By.XPATH,".//p")

    course_title=course_title[0].get_attribute("innerText") if course_title else None
    course_desc=course_desc[0].get_attribute("innerText") if course_desc else None

    print(course_title)
    print(course_desc)
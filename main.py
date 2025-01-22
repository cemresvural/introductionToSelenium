from selenium import webdriver
from selenium.webdriver.common.by import By


options=webdriver.ChromeOptions()
options.add_argument("--headless")

driver=webdriver.Chrome(options)
driver.get("https://www.miuul.com")
element=driver.find_element(By.XPATH,"//a")
print(element.text)
# two argument,First;name,css selector or xpath  Second;Query that finds whichever element you want to find
# example for xpath   go to webpage and inspect ,you know links in <a> elements ,ctrl+f and write //a
element.get_attribute("innerText")
element.get_attribute("href")
element.get_attribute("innerHTML")
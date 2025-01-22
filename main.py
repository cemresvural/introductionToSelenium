from selenium import webdriver


options=webdriver.ChromeOptions()
options.add_argument("--headless")

driver=webdriver.Chrome(options)
driver.get("https://www.miuul.com")
driver.title
driver.current_url
driver.quit()
import requests
from selenium import webdriver
from extension import proxies

url='https://www.ıpaddress.my/'

proxy_username =''
proxy_password =''
proxy_ip_address = ''
proxy_port= ''

#username:password@ip_address:port
options= webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={proxy_ip_address}:{proxy_port}')

driver=webdriver.Chrome(options=options)
driver.get(url)
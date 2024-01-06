from selenium import webdriver
from time import sleep
from selenium.webdriver import Remote

def browser(url: str): 
    SELENIUM_URL = "http://chrome:4444/wd/hub"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    driver = Remote(command_executor=SELENIUM_URL, options=options)

    driver.get(url)
    sleep(5)
    return driver.page_source

    


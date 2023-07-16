from selenium import webdriver
from time import sleep

def browser(url: str): 
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    sleep(5)
    return driver.page_source

    


from selenium import webdriver
from time import sleep

def browser(url: str): 
  
    options = webdriver.ChromeOptions()
    # abre oculto
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    sleep(5)
    return driver.page_source
    # with open('page.html', 'w', encoding='utf-8') as file:
    #     file.write(html)

    

browser('https://www.inversebible.org/3am13')
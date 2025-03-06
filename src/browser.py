from selenium import webdriver
from time import sleep
from selenium.webdriver import Remote


class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        self.driver = Remote(
            command_executor="http://chrome:4444/wd/hub", options=options
        )

    def get(self, url: str) -> str:
        self.driver.get(url)
        sleep(5)
        data = self.driver.page_source
        return data

    def close(self):
        self.driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class BrowserManager:
    def __init__(self, config: dict):
        self.config = config
        self.driver = None

    def start(self):
        browser_config = self.config["browser"]

        options = Options()

        if browser_config["headless"]:
            options.add_argument("--headless=new")

        if browser_config["binary_location"]:
            options.binary_location = browser_config["binary_location"]

        if browser_config["driver_path"]:
            service = Service(browser_config["driver_path"])
        else:
            service = Service()

        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver

    def stop(self):
        if self.driver:
            self.driver.quit()
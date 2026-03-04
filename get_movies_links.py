from selenium.webdriver.common.by import By
import time


class KinopoiskScraper:
    def __init__(self, config, driver):
        self.config = config

        self.driver = driver
        self.url = config["category_url"]
        self.delay = config["delay_seconds"]

    def get_movie_links(self):
        self.driver.get(self.url)
        time.sleep(self.delay)

        elements = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/film/')]")

        movies = {}

        for el in elements:
            href = el.get_attribute("href")
            title = el.text.strip()

            if title and "/film/" in href:
                movies[title] = href

        return movies
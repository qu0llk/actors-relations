import json

from setup_browser_manager import *
from get_movies_links import *

def main():
    config_path = "config.json"

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    browser = BrowserManager(config)
    driver = browser.start()

    scraper = KinopoiskScraper(config, driver)
    # parser = MovieParser(driver)

    library = {}

    movies = scraper.get_movie_links()

    for title, link in movies.items():
        print(f"{title.split()[0]} @ {link}")
        print("-" * 100)
        # actors = parser.get_actors(link)
        # library[title] = actors

    # browser.stop()

    print(library)


if __name__ == "__main__":
    main()
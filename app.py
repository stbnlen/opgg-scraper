from bs4 import BeautifulSoup
from classes.DriverGet import DriverGet
from classes.GameStats import GameStatsExtractor
from utils.setup_driver import setup_driver
from utils.extract_game_objects import extract_game_objects
from utils.create_dataframe import create_dataframe


def main(summoner_name: str, region: str):
    with setup_driver() as driver:
        driver_get = DriverGet(driver)
        driver_get.get_page(summoner_name, region)
        driver_get.get_games()
        driver_get.get_details()

        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")

        game_stats = GameStatsExtractor(soup)
        objects = extract_game_objects(game_stats, summoner_name)

        df = create_dataframe(objects)

        df.to_csv("stats.csv")


if __name__ == "__main__":
    summoner_name = "itzpipeqlo"
    region = "las"
    main(summoner_name, region)

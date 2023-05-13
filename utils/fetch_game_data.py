from selenium import webdriver
from bs4 import BeautifulSoup
from classes.DriverGet import DriverGet
from classes.GameStats import GameStatsExtractor
from utils.extract_game_objects import extract_game_objects
from typing import Dict

def fetch_game_data(driver: webdriver, summoner_name: str, region: str) -> Dict[str, any]:
    driver_get = DriverGet(driver)
    driver_get.get_page(summoner_name, region)
    driver_get.get_games()
    driver_get.get_details()

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    game_stats = GameStatsExtractor(soup)
    objects = extract_game_objects(game_stats, summoner_name)
    return objects
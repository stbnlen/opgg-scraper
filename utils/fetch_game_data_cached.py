import functools
from selenium import webdriver
from typing import Dict
from utils.fetch_game_data import fetch_game_data

@functools.lru_cache(maxsize=None)
def fetch_game_data_cached(driver: webdriver, summoner_name: str, region: str) -> Dict[str, any]:
    return fetch_game_data(driver, summoner_name, region)
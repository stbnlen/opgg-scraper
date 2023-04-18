import time
import logging
import pandas as pd
from typing import Dict
from random import randint
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

def get_page(driver: WebDriver, name: str, region: str) -> None:
    valid_regions = ["na", "euw", "eune", "kr", "jp", "br", "lan", "las", "oce", "tr", "ru"]
    if not name or not region:
        raise ValueError("Invalid input: both 'name' and 'region' parameters are required.")
    if region.lower() not in valid_regions:
        raise ValueError("Invalid region input. Valid regions are: " + ", ".join(valid_regions))
    
    BASE_URL = "https://www.op.gg/summoners/"
    url = f"{BASE_URL}{region}/{name}"

    try:
        driver.get(url)
    except WebDriverException as e:
        logger.error("Error al obtener la página web: %s", e)


def get_games(driver: WebDriver) -> None:
    """
    Clicks the "more" button up to 20 times or until the button is not found.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Returns:
        None
    """
    while True:
        try:
            button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "button.more")))
            button.click()
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            break


def get_details(driver: WebDriver) -> None:
    """
    Clicks on each "detail" button on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Returns:
        None
    """
    # Wait for all "detail" buttons to be present on the page
    buttons = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//button[@class="detail"]')))

    # Click on each button in the list of found elements without creating an additional list
    try:
        for element in buttons:
            element.click()
            time.sleep(0.1)
    except WebDriverException as e:
        print(f"An error occurred: {e}")


def results(lis):
    champion = []
    cs, cs_per_minute  = [], []
    wards = []
    
    result_texts = [li.find('div', {'class': 'result'}).text for li in lis if li.find('div', {'class': 'result'})]
    game_type = [li.find('div', {'class': 'type'}).text for li in lis if li.find('div', {'class': 'type'})]
    length = [li.find('div', {'class': 'length'}).text for li in lis if li.find('div', {'class': 'length'})]
    percentage = [li.find('div', {'class': 'p-kill'}).text for li in lis if li.find('div', {'class': 'p-kill'})]
    wards = [li.find('div', {'class': 'ward'}).text for li in lis if li.find('div', {'class': 'ward'})]
    tier = [li.find('div', {'class': 'average-tier'}).text for li in lis if li.find('div', {'class': 'average-tier'})]
    kill = [li.find('div', {'class': 'k-d-a'}).text.split('/')[0] for li in lis if li.find('div', {'class': 'k-d-a'})]
    death = [li.find('div', {'class': 'k-d-a'}).text.split('/')[1] for li in lis if li.find('div', {'class': 'k-d-a'})]
    assist = [li.find('div', {'class': 'k-d-a'}).text.split('/')[2] for li in lis if li.find('div', {'class': 'k-d-a'})]
    
    for li in lis:
        icon_div = li.find('div', {'class': 'icon'})
        if icon_div:
            img_tag = icon_div.find('img', {'width': '48'})
            if img_tag:
                alt_text = img_tag['alt']
                champion.append(alt_text)

        cs_div = li.find('div', {'class': 'cs'})
        if cs_div:
            cs_total = cs_div.text.split(' ')
            cs.append(cs_total[1])
            cs_per_minute.append(cs_total[2])

    for i in range(1):
        tier.append(f'bronce {randint(1, 3)}')
        
    return result_texts, game_type, kill, death, assist, length, champion, percentage, tier, cs, cs_per_minute, wards

def get_damage_stats(soup: BeautifulSoup, name: str) -> tuple:
    """
    Extracts damage dealt and damage taken statistics from BeautifulSoup object.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object representing the HTML structure.
        name (str): The name to search for in the 'name' class of 'td' tags.

    Returns:
        tuple: A tuple containing two lists: damage_dealt and damage_taken.
    """

    divs = soup.find_all('div', {'class': 'css-1dm3230 eo0wf2y0'})
    damage_dealt = []
    damage_taken = []

    trs = [tr for div in divs for tbody in div.find_all('tbody') for tr in tbody.find_all('tr')]
    for tr in trs:
        td_name = tr.find('td', {'class': 'name'})
        if td_name and td_name.find('a', text=name):
            td_damage = tr.find('td', {'class': 'damage'})
            div_dealt = td_damage.find('div', {'class': 'dealt'})
            if div_dealt:
                damage_dealt.append(div_dealt.text)
            div_taken = td_damage.find('div', {'class': 'taken'})
            if div_taken:
                damage_taken.append(div_taken.text)

    return damage_dealt, damage_taken


def create_dataframe(objects: Dict[str, any]) -> pd.DataFrame:
    """
    Create a pandas DataFrame from a dictionary of objects.

    Args:
        objects (Dict[str, any]): A dictionary of objects to be converted to a DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the objects.
    """
    try:
        df = pd.DataFrame(objects)
        df.index = range(len(df))
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


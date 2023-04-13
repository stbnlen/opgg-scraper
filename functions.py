import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from bs4 import BeautifulSoup


def get_games(driver: WebDriver) -> None:
    """
    Clicks the "more" button up to 20 times or until the button is not found.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.

    Returns:
        None
    """
    for i in range(20):
        try:
            # Wait for the "more" button to be present on the page
            button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='more']")))
            button.click()
            time.sleep(2)
        except:
            # Exit the loop if the button is no longer present on the page
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
    for element in buttons:
        element.click()
        time.sleep(1)


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

    for div in divs:
        tbodies = div.find_all('tbody')
        for tbody in tbodies:
            trs = tbody.find_all('tr')
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


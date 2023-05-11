import time
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class DriverGet:
    BASE_URL: str = "https://www.op.gg/summoners/"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_page(self, name: str, region: str) -> None:
        valid_regions = {
            "na",
            "euw",
            "eune",
            "kr",
            "jp",
            "br",
            "lan",
            "las",
            "oce",
            "tr",
            "ru",
        }
        if not name or not region:
            raise ValueError(
                "Invalid input: both 'name' and 'region' parameters are required."
            )
        if region.lower() not in valid_regions:
            raise ValueError(
                "Invalid region input. Valid regions are: " + ", ".join(valid_regions)
            )

        url = f"{self.BASE_URL}{region}/{name}"

        try:
            self.driver.get(url)
        except WebDriverException as e:
            logger.error("Error al obtener la página web: %s", e)

    def get_games(self) -> None:
        while True:
            try:
                button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button.more"))
                )
                button.click()
                time.sleep(1)
            except Exception as e:
                logger.error("An error occurred: %s", e)
                break

    def get_details(self) -> None:
        buttons = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, '//button[@class="detail"]'))
        )

        try:
            for element in buttons:
                element.click()
                time.sleep(0.1)
        except WebDriverException as e:
            print(f"An error occurred: {e}")

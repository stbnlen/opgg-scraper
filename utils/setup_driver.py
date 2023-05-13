from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def setup_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("-private")
    options.add_argument("--headless")
    return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    
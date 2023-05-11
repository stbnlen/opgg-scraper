from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def setup_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("-inprivate")
    options.add_argument("headless")
    return webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()), options=options
    )

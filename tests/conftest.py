import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium"

    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

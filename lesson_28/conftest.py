import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PythonAutomation.lesson_28.main_page import MainPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # обов’язково для Jenkins
    options.add_argument("--no-sandbox")  # потрібне у контейнерах
    options.add_argument("--disable-dev-shm-usage")  # запобігає падінням у Linux
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page
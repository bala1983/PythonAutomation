import pytest
from selenium.webdriver import Chrome
from PythonAutomation.lesson_28.main_page import MainPage


@pytest.fixture
def driver():
    driver = Chrome()
    yield driver
    driver.close()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page
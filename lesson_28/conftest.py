import pytest
from selenium.webdriver import Chrome
from PythonAutomation.lesson_28.main_page import MainPage
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()


@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.close()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page
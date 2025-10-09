from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

class NPTracking:
    def __init__(self, driver):
        self.driver  = driver
        self.url = 'https://tracking.novaposhta.ua/#/uk'

    def open(self):
        self.driver.get(self.url)

    def get_status(self, tracking_number):
        input_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "en")))
        input_field.clear()
        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.ENTER)

        try:
            status_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.header__status-header")))
            status = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.header__status-text")))
            return status_header.text.strip(), status.text.strip()
        except:
            return "", "Щось пішло не так"

@pytest.mark.parametrize("tracking_number, expected_header, expected_status", [
    ("20451254638897", "Зараз:", "Отримана"),
    # ("20451254638897", "Зараз:", "У відділені"), хотів зробити ще ці два кейса, але потрібен реальний номер накладной
    # ("20451254638897", "Зараз:", "У дорозі"),
    ("204512546388975","", "Щось пішло не так")

])
def test_np_tracking(tracking_number, expected_header, expected_status):
    driver = webdriver.Chrome()
    tracker = NPTracking(driver)

    try:
        tracker.open()
        status_header, status = tracker.get_status(tracking_number)
        assert status_header == expected_header
        assert status == expected_status

    finally:
        driver.quit()
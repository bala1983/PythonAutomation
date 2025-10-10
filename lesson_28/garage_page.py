from PythonAutomation.lesson_28.base_page import BasePage
from selenium.webdriver.common.by import By

class GaragePage(BasePage):
    _root_element_locator = (By.CSS_SELECTOR, 'app-garage')
    def __init__(self, driver):
        super().__init__(driver = driver)
        self.url = None

    def _roor_element(self):
        return self._element(self._root_element_locator)

    def is_garage_page_visible(self):
        return self._roor_element().is_displayed()
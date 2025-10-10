from PythonAutomation.lesson_28.base_page import BasePage
from PythonAutomation.lesson_28.registration_form import RegistrationForm
from PythonAutomation.settings import settings
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    _sign_up_button_locator = (By.XPATH,"//button[text()='Sign up']")
    def __init__(self, driver):
        super().__init__(driver = driver)
        self.url = settings.BASE_URL


    def open_registration_form(self):
        self._sign_up_button().click()
        return RegistrationForm(self._driver)

    def _sign_up_button(self):
        return self._button(self._sign_up_button_locator)
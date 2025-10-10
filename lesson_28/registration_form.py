from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PythonAutomation.lesson_28.garage_page import GaragePage


class RegistrationForm:
    _input_firs_name_locator = (By.CSS_SELECTOR, "#signupName")
    _input_last_name_locator = (By.CSS_SELECTOR, "#signupLastName")
    _input_email_locator = (By.CSS_SELECTOR, "#signupEmail")
    _input_pass_locator = (By.CSS_SELECTOR, "#signupPassword")
    _input_re_pass_locator = (By.CSS_SELECTOR, "#signupRepeatPassword")
    _register_button_locator = (By.CSS_SELECTOR, ".modal-footer>button")
    _error_locator = (By.CSS_SELECTOR, ".invalid-feedback")

    def __init__(self, driver):
        self.driver = driver

    def register_valid_user(self, name, last_name, email, password):
        self._input_field(self._input_firs_name_locator).send_keys(name)
        self._input_field(self._input_last_name_locator).send_keys(last_name)
        self._input_field(self._input_email_locator).send_keys(email)
        self._input_field(self._input_pass_locator).send_keys(password)
        self._input_field(self._input_re_pass_locator).send_keys(password)
        self._button(self._register_button_locator).click()

        return GaragePage(self.driver)

    def _button(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(locator))

    def _input_field(self, locator):
        return WebDriverWait(self.driver, timeout=5).until(
            EC.presence_of_element_located(locator))

    def register_invalid_user(self, name, last_name, email, password, repeat_password):
        self._input_field(self._input_firs_name_locator).send_keys(name)
        self._input_field(self._input_last_name_locator).send_keys(last_name)
        self._input_field(self._input_email_locator).send_keys(email)
        self._input_field(self._input_pass_locator).send_keys(password)
        self._input_field(self._input_re_pass_locator).send_keys(repeat_password)

        form_container = self.driver.find_element(By.CSS_SELECTOR, ".modal-content")
        form_container.click()

        return self

    def is_error_visible(self, expected_error, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{expected_error}')]")
            )
        )
        return True
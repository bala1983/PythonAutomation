from faker import Faker
import pytest
import allure

@allure.feature("Позитивний сценарій реєстрації")
@allure.title("Реєстрація валідного користувача")
@allure.description("Перевіряє, що користувач може успішно зареєструватися з коректними даними.")
@pytest.mark.positive
def test_happy_pass_registration(driver, main_page):
    user_faker = Faker()

    registration_form = main_page.open_registration_form()
    garage_page = registration_form.register_valid_user(user_faker.first_name(), user_faker.last_name(), user_faker.email(),
                                          user_faker.password())
    assert garage_page.is_garage_page_visible()

@allure.feature("Негативні сценарії реєстрації")
@allure.title("Валідація помилкових даних під час реєстрації")
@allure.description("Перевіряє, що при введенні некоректних даних відображається правильне повідомлення про помилку.")
@pytest.mark.negative
@pytest.mark.parametrize(
    "name, last_name, email, password, repeat_password, expected_error",
    [
        ("", "Tester", "valid@mail.com", "Qwerty123!", "Qwerty123!", "Name required"),
        ("1q", "Tester", "valid@mail.com", "Qwerty123!", "Qwerty123!", "Name is invalid"),
        ("1", "Tester", "valid@mail.com", "Qwerty123!", "Qwerty123!", "Name has to be from 2 to 20 characters long"),
        ("Alex", "", "valid@mail.com", "Qwerty123!", "Qwerty123!", "Last name required"),
        ("Alex", "2q", "valid@mail.com", "Qwerty123!", "Qwerty123!", "Last name is invalid"),
        ("Alex", "2", "valid@mail.com", "Qwerty123!", "Qwerty123!", "Last name has to be from 2 to 20 characters long"),
        ("Alex", "Tester", "", "Qwerty123!", "Qwerty123!", "Email required"),
        ("Alex", "Tester", "invalid_email", "Qwerty123!", "Qwerty123!", "Email is incorrect"),
        ("Alex", "Tester", "valid@mail.com", "", "Qwerty123!", "Password required"),
        ("Alex", "Tester", "valid@mail.com", "q", "Qwerty123!", "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"),
        ("Alex", "Tester", "valid@mail.com", "Qwerty12", "Qwerty123", "Passwords do not match"),
        ("Alex", "Tester", "valid@mail.com", "Qwerty123", "Qwerty12", "Passwords do not match"),
        ("Alex", "Tester", "valid@mail.com", "Qwerty12", "", "Re-enter password required"),
        ("Alex", "Tester", "valid@mail.com", "Qwerty123!", "q", "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter")
    ]
)
def test_registration_invalid_user(driver, main_page, name, last_name, email, password, repeat_password, expected_error):
    registration_form = main_page.open_registration_form()
    registration_form.register_invalid_user(name, last_name, email, password, repeat_password)
    assert registration_form.is_error_visible(expected_error)
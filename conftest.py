import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import main_page_url
from locator.auth_form import AuthFormLoc
from locator.main_page import MainPageLoc
from selenium.webdriver.support import expected_conditions as ec
from data import EMAIL, PASSWORD


auth_form_loc = AuthFormLoc
main_page_loc = MainPageLoc


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(main_page_url)
    yield driver
    driver.quit()


@pytest.fixture
def auto_auth(driver):
    """Фикстура автоматической аутентификации пользователя."""
    login_url = 'https://stellarburgers.nomoreparties.site/login'
    driver.get(login_url)

    driver.find_element(*auth_form_loc.placeholder_email).clear()
    driver.find_element(*auth_form_loc.placeholder_email).send_keys(EMAIL)

    driver.find_element(*auth_form_loc.placeholder_password).clear()
    driver.find_element(*auth_form_loc.placeholder_password).send_keys(PASSWORD)

    WebDriverWait(driver, 15).until(ec.invisibility_of_element_located(auth_form_loc.first_overley))
    WebDriverWait(driver, 15).until(ec.invisibility_of_element_located(auth_form_loc.second_overley))
    driver.find_element(*auth_form_loc.button_enter).click()
    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(main_page_loc.check_text_constr))

    return driver

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import main_page_url
from locator.auth_form import AuthFormLoc
from locator.main_page import MainPageLoc
from selenium.webdriver.support import expected_conditions as ec
from data import EMAIL, PASSWORD, login_url
from pages.base_page import BasePage


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
    base_page = BasePage(driver)
    base_page.go_to_url(login_url)

    base_page.find_element_and_clear(auth_form_loc.placeholder_email)
    base_page.find_element_and_send_keys(auth_form_loc.placeholder_email, EMAIL)

    base_page.find_element_and_clear(auth_form_loc.placeholder_password)
    base_page.find_element_and_send_keys(auth_form_loc.placeholder_password, PASSWORD)

    base_page.invisible_element(auth_form_loc.first_overley)
    base_page.invisible_element(auth_form_loc.second_overley)
    base_page.click_by_element(auth_form_loc.button_enter)
    base_page.download_wait_by_visible(main_page_loc.check_text_constr)

    return driver

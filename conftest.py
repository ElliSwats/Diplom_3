import pytest
from selenium import webdriver
from data import main_page_url
from pages.login_page import LoginPage


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
    login_page = LoginPage(driver)
    login_page.go_to_login_url()
    login_page.get_email()
    login_page.get_password()
    login_page.push_log_in()

    return driver

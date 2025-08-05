import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть на элемент')
    def click_by_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Ожидание видимости элемента")
    def download_wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(ec.presence_of_element_located(locator))

    @allure.step('Получить текст элемента')
    def get_text_by_element(self, locator):
        self.download_wait_by_visible(locator)
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Ожидание видимости элемента')
    def download_wait_by_visible(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def download_wait_by_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator))

    @allure.step('Получение URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        source_loc = self.download_wait_by_visible(source)
        target_loc = self.download_wait_by_visible(target)
        drag_and_drop(self.driver, source=source_loc, target=target_loc)

    @allure.step('Элемент больше не находится в видимости')
    def invisible_element(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.invisibility_of_element_located(locator))

    @allure.step("Ожидание пока номер заказа станет не равным 9999")
    def wait_and_find_element_9999(self, locator):
        return WebDriverWait(self.driver, 15).until(
                   lambda driver: driver.find_element(*locator).text != "9999")

    @allure.step("Ожидание пока появится номер заказа вместо 'Все текущие заказы готовы!'")
    def wait_and_find_element_all_order_ready(self, locator):
        return WebDriverWait(self.driver, 15).until(
            lambda driver: driver.find_element(*locator).text != "Все текущие заказы готовы!")

    @allure.step("Ожидание пока появится номер заказа в созданном заказе")
    def find_and_wait_until_text_changes(self, locator):
        WebDriverWait(self.driver, 20).until(
            lambda _: self.get_text_by_element(locator) != "9999")
        return self.get_text_by_element(locator)

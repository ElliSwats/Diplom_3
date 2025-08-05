import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locator.main_page import MainPageLoc
from data import (order_feed_url, expected_text_constr,
                  expected_tex_window_ingr)


class TestBasicFunc:

    @allure.title('тест успешный переход в ленту заказов через кнопку "Лента заказов"')
    def test_switch_to_order_feed_success(self, driver):
        main_page = MainPage(driver)
        main_page.switch_to_order()
        with allure.step('Сравнение ожидаемого URL с фактическим'):
            assert main_page.get_url() == order_feed_url

    @allure.title('тест успешный переход в конструктор через кнопку "Конструктор"')
    def test_switch_to_constr_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page_loc = MainPageLoc()
        main_page.switch_to_order()
        order_page.return_to_constructor()
        with allure.step('Получение текста "Соберите бургер" на странице "Конструктор"'):
            actual_text = main_page.get_text_by_element(main_page_loc.check_text_constr)
        with allure.step('Сравнение ожидаемого текста с фактическим'):
            assert actual_text == expected_text_constr

    @allure.title('Тест успешного открытия окна с деталями ингридиента через клик по ингридиенту')
    def test_click_to_ingredient_open_window_success(self, driver):
        main_page = MainPage(driver)
        main_page_loc = MainPageLoc()
        main_page.click_to_ingredient_open_window()
        with allure.step('Получение текста окна с деталями ингридиента'):
            actual_text = main_page.get_text_by_element(main_page_loc.ingredient_details)
        with allure.step('Сравнение ожидаемого текста с фактическим'):
            assert expected_tex_window_ingr == actual_text

    @allure.title('Тест успешного открытия и закрытия окна с деталями ингридиента')
    def test_open_close_ingr_window(self, driver):
        main_page = MainPage(driver)
        main_page_loc = MainPageLoc()
        main_page.open_close_ingredient_window()
        with allure.step('Проверка: после закрытия, окно больше не отображается'):
            assert main_page.invisible_element(main_page_loc.window_ingredient)

    @allure.title('Тест увелечение счетчика ингридиента при добавлении в корзину')
    def test_current_totalizer_basket_ingr(self, driver):
        main_page = MainPage(driver)
        main_page_loc = MainPageLoc()
        main_page.filling_basket_with_ingredients()
        current = main_page.get_text_by_element(main_page_loc.totalizer_fluorescent_bun)
        with allure.step('Сравнение ожидаемой цифры счетчика ингридиента с фактической'):
            assert current == '2'

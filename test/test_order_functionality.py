import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderFunc:
    @allure.title('Тест на увеличение счетчика "Выполнено за все время" при создании заказа')
    def test_increasing_counter_all_time(self, auto_auth):
        main_page = MainPage(auto_auth)
        order_page = OrderPage(auto_auth)
        with allure.step('Получаем количество заказов счетчика "Выполнено за все время"'):
            count_before_order = order_page.switch_to_order_feed_get_number_all_time()
        with allure.step('Возвращаемся главную страницу и создаем заказ'):
            order_page.return_to_constructor()
            main_page.create_order()
            main_page.close_order_window()
        with allure.step('Переходим на страницу "Лента заказов", '
                         'получаем количество заказов счетчика "Выполнено за все время"'):
            count_after_order = order_page.switch_to_order_feed_get_number_all_time()
        with allure.step('Сравниваем данные счетчика "Выполнено за все время" до создания заказа и после'):
            assert (int(count_before_order) + 1) == int(count_after_order)

    @allure.title('Тест на увеличение счетчика "Выполнено за сегодня" при создании заказа')
    def test_increasing_counter_today(self, auto_auth):
        main_page = MainPage(auto_auth)
        order_page = OrderPage(auto_auth)
        with allure.step('Получаем количество заказов счетчика "Выполнено за сегодня"'):
            count_before_order = order_page.switch_to_order_feed_get_number_today()
        with allure.step('Возвращаемся главную страницу и создаем заказ'):
            order_page.return_to_constructor()
            main_page.create_order()
            main_page.close_order_window()
        with allure.step('Переходим на страницу "Лента заказов", '
                         'получаем количество заказов счетчика "Выполнено за сегодня"'):
            count_after_order = order_page.switch_to_order_feed_get_number_today()
        with allure.step('Сравниваем данные счетчика "Выполнено за сегодня" до создания заказа и после'):
            assert (int(count_before_order) + 1) == int(count_after_order), 'Счетчик не увеличился'

    @allure.title('Тест: номер созданного заказа появлется в разделе "В работе"')
    def test_order_number_listed_in_progress(self, auto_auth):
        main_page = MainPage(auto_auth)
        order_page = OrderPage(auto_auth)
        with allure.step('Создаем заказ'):
            main_page.create_order()
        with allure.step('Получаем номер созданного заказа'):
            expect_number = main_page.get_order_number()
            main_page.close_order_window()
        with allure.step('Переходим на страницу "Лента заказов", '
                         'получаем номер заказа "В работе"'):
            actual_number = order_page.get_number_in_progress()
        with allure.step('Сравниваем номер созданного заказа с номером заказа в работе'):
            assert '0' + expect_number == actual_number, 'номер заказа отсутствует в разделе "В работе"'

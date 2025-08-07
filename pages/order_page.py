import allure
from locator.main_page import MainPageLoc
from locator.order_page_feed import OrderFeedPageLoc
from pages.base_page import BasePage


main_page_loc = MainPageLoc
order_feed_loc = OrderFeedPageLoc


class OrderPage(BasePage):

    @allure.step('переход в ленту заказов и получение данных счетчика "За все время"')
    def switch_to_order_feed_get_number_all_time(self):
        self.download_wait_by_visible(main_page_loc.order_feed)
        self.download_wait_by_clickable(main_page_loc.order_feed)
        self.click_by_element(main_page_loc.order_feed)
        self.download_wait_by_visible(order_feed_loc.completed_in_all_time)
        return self.get_text_by_element(order_feed_loc.completed_in_all_time)

    @allure.step('переход в "Конструктор"')
    def return_to_constructor(self):
        self.click_by_element(main_page_loc.constructor_button)
        self.download_wait_by_visible(main_page_loc.check_text_constr)

    @allure.step('переход в ленту заказов и получение данных счетчика "За сегодня"')
    def switch_to_order_feed_get_number_today(self):
        self.click_by_element(main_page_loc.order_feed)
        self.wait_and_find_element_all_order_ready(order_feed_loc.completed_today)
        return self.get_text_by_element(order_feed_loc.completed_today)

    @allure.step('переход в ленту заказов и получение номера заказа" в работе"')
    def get_number_in_progress(self):
        self.click_by_element(main_page_loc.order_feed)
        self.download_wait_by_visible(order_feed_loc.number_order_in_progress)
        return self.get_text_by_element(order_feed_loc.number_order_in_progress)

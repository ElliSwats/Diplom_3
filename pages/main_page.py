import allure
from locator.main_page import MainPageLoc
from locator.order_page_feed import OrderFeedPageLoc
from pages.base_page import BasePage


main_page_loc = MainPageLoc
order_feed_loc = OrderFeedPageLoc


class MainPage(BasePage):
    @allure.step('переход на "Ленту заказов"')
    def switch_to_order(self):
        self.click_by_element(main_page_loc.order_feed)
        self.download_wait_by_visible(order_feed_loc.completed_in_all_time)

    @allure.step('клик на ингредиент открывает окно с деталями ингридиента')
    def click_to_ingredient_open_window(self):
        self.click_by_element(main_page_loc.fluorescent_bun)
        self.download_wait_by_clickable(main_page_loc.close_ingredient_details)

    @allure.step('открытие и закрытие окна с деталями ингридиента')
    def open_close_ingredient_window(self):
        self.click_by_element(main_page_loc.fluorescent_bun)
        self.download_wait_by_clickable(main_page_loc.close_ingredient_details)
        self.click_by_element(main_page_loc.close_ingredient_details)

    @allure.step('наполнение корзины ингридиентами')
    def filling_basket_with_ingredients(self):
        self.drag_and_drop_element(source=main_page_loc.fluorescent_bun, target=main_page_loc.basket_top)
        self.download_wait_by_visible(main_page_loc.fluorescent_bun_in_basket)

    @allure.step('Создаем заказ')
    def create_order(self):
        self.drag_and_drop_element(source=main_page_loc.fluorescent_bun, target=main_page_loc.basket_top)
        self.download_wait_by_visible(main_page_loc.fluorescent_bun_in_basket)
        self.click_by_element(main_page_loc.button_create_order)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_and_find_element_9999(main_page_loc.number_order)
        return self.find_and_wait_until_text_changes(main_page_loc.number_order)

    @allure.step('закрыть окно заказа')
    def close_order_window(self):
        self.wait_and_find_element_9999(main_page_loc.number_order)
        self.find_and_wait_until_text_changes(main_page_loc.number_order)
        self.click_by_element(main_page_loc.button_close_window)
        self.invisible_element(main_page_loc.first_overley)
        self.invisible_element(main_page_loc.second_overley)

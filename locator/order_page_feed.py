from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class OrderFeedPageLoc:
    completed_in_all_time = [By.XPATH,
                             "//div[p[text()='Выполнено за все время:']]/p[contains(@class, 'OrderFeed_number')]"]

    completed_today = [By.XPATH,
                       "//div[p[text()='Выполнено за сегодня:']]/p[contains(@class, 'OrderFeed_number')]"]

    number_order_in_progress = [By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[@class='text text_type_digits-default mb-2']"]
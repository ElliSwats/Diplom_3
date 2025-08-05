from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class AuthFormLoc:
    # локатор кнопки "Войти" на странице авторизации
    button_enter = [By.XPATH, "//button[contains(@class, 'button_size_medium__3zxIa')]"]
    # локатор плейсхолдера Email
    placeholder_email = [By.XPATH, "//label[text()='Email']/following-sibling::input"]
    # локатор плейсхолдера Пароль
    placeholder_password = [By.XPATH, "//input[@name='Пароль']"]
    # первый оверлей
    first_overley = [By.XPATH, "//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']"]
    # второй оверлей
    second_overley = [By.XPATH, "//div[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']"]

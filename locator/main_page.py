from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class MainPageLoc:
    # локатор кнопки "Конструктор" в header
    constructor_button = [By.XPATH, "//p[text()='Конструктор']"]
    # локатор текста "Соберите бургер"
    check_text_constr = [By.XPATH, "//h1[text()='Соберите бургер']"]
    # локатор кнопки "лента заказов" в header
    order_feed = [By.XPATH, "//*[text() = 'Лента Заказов']"]
    # локатор Флюоресцентной булки в ленте ингридиентов
    fluorescent_bun = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
    # локатор текста "Детали ингредиента" в окне с деталями
    ingredient_details = [By.XPATH, "//*[text()='Детали ингредиента']"]
    # локатро кнопки крестик для закрытия окна с деталями
    close_ingredient_details = [By.XPATH,
        "//section[contains(@class,'opened__3ISw4')]//button[@type='button']//*[name()='svg']//*[name()='path'and contains(@fill-rule,'evenodd')]"]
    # локатор открытого окна с ингридиентами
    window_ingredient = [By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    # Ваш заказ начали готовить
    order_is_preparing = [By.XPATH, "//p[@class='undefined text text_type_main-small mb-2']"]
    # Локатор счетчика ингридиента Флюоресцентная булка
    totalizer_fluorescent_bun = [By.XPATH,
        "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//div[contains(@class, 'default__28sqi')]//p[contains(@class, 'num__3nue1')]"]
    # Перетяните булочку сюда (верх)
    basket_top = [By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']"]
    # Флюоресцентная булка в корзине
    fluorescent_bun_in_basket =[By.XPATH,
                "//span[@class='constructor-element__text' and text()='Флюоресцентная булка R2-D3 (низ)']"]
    # Кнопка оформить заказ
    button_create_order = [By.XPATH, "//button[contains(text(), 'Оформить заказ')]"]
    # Крестик окна индентификатор заказа
    button_close_window = [By.XPATH, "//button[@type='button']//*[name()='svg']"]
    # Номер созданного заказа
    number_order = [By.XPATH, "//h2[contains(@class, 'type_digits-large mb-8')]"]
    # Первый пекрывающий элемент
    first_overley = [By.XPATH, "//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']"]
    # Второй перекрывающий элемент
    second_overley = [By.XPATH, "//div[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']"]

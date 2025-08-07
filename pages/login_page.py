import allure
from pages.base_page import BasePage
from data import EMAIL, PASSWORD, login_url
from locator.auth_form import AuthFormLoc
from locator.main_page import MainPageLoc

main_page_loc = MainPageLoc
auth_form_loc = AuthFormLoc


class LoginPage(BasePage):

    @allure.step('Переход на страницу авторизации')
    def go_to_login_url(self):
        self.go_to_url(login_url)

    @allure.step('Ввод email')
    def get_email(self):
        self.find_element_and_clear(auth_form_loc.placeholder_email)
        self.find_element_and_send_keys(locator=auth_form_loc.placeholder_email, key=EMAIL)

    @allure.step('Ввод пароля')
    def get_password(self):
        self.find_element_and_clear(auth_form_loc.placeholder_password)
        self.find_element_and_send_keys(locator=auth_form_loc.placeholder_password, key=PASSWORD)

    @allure.step('Нажатие кнопки "войти" на странице авторизации')
    def push_log_in(self):
        self.invisible_element(auth_form_loc.first_overley)
        self.invisible_element(auth_form_loc.second_overley)
        self.click_by_element(auth_form_loc.button_enter)
        self.download_wait_by_visible(main_page_loc.check_text_constr)

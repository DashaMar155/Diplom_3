import logging
import allure
from data.data import LOGIN_URL
from locators.account_page_locators import AccountPageLocators
from .base_page import BasePage

logger = logging.getLogger(__name__)


class AccountPage(BasePage):

    @allure.step("Нажимаем на кнопку 'Личный кабинет'")
    def click_account_button(self):
        logger.info("Кликаем по кнопке 'Личный кабинет'")
        self.wait_for_element_visible(AccountPageLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_when_clickable(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("Нажимаем на кнопку 'История заказов'")
    def click_order_history_button(self):
        logger.info("Кликаем по кнопке 'История заказов'")
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Нажимаем на кнопку 'Выход'")
    def click_logout_button(self):
        logger.info("Кликаем по кнопке 'Выход'")
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверяем, что кнопка 'Выход' отображается")
    def is_logout_button_visible(self) -> bool:
        visible = self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)
        logger.info(f"Кнопка 'Выход' видима: {visible}")
        return visible

    @allure.step("Проверяем, что заказ выполнен")
    def is_order_completed(self) -> bool:
        status = self.get_text_from_element(AccountPageLocators.ORDER_COMPLETED)
        completed = status == "Выполнен"
        logger.info(f"Статус заказа: '{status}', выполнен: {completed}")
        return completed

    @allure.step("Проверяем, что после выхода отображается кнопка 'Вход'")
    def is_login_button_visible_after_logout(self) -> bool:
        text = self.get_text_from_element(AccountPageLocators.LOGIN_AFTER_LOGOUT)
        visible = text == "Вход"
        logger.info(f"Кнопка 'Вход' после выхода отображается: {visible}")
        return visible

    @allure.step("Открываем страницу логина")
    def open_login_page(self):
        logger.info(f"Переход на страницу логина: {LOGIN_URL}")
        self.navigate_to(LOGIN_URL)

    @allure.step("Выполняем логин с email: {email}")
    def login(self, email: str, password: str):
        logger.info(f"Выполняем логин для пользователя: {email}")
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)
        self.click_with_js(AccountPageLocators.LOGIN_BUTTON)

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    #  Действия
    @allure.step("Нажимаем на кнопку 'Конструктор'")
    def click_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажимаем на кнопку 'Лента заказов'")
    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.PLACE_AN_ORDER)

    @allure.step("Открываем детали ингредиента")
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step("Закрываем окно деталей ингредиента")
    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step("Добавляем ингредиент в заказ")
    def add_ingredient_to_order(self):
        self.click_to_element(MainPageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_and_drop_ingredient(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_R2D3_BUN,
            MainPageLocators.ORDER_TARGET_TOP
        )

    #  Проверки
    @allure.step("Проверяем, что конструктор бургеров отображается")
    def is_burger_constructor_visible(self):
        return self.wait_for_section_visible(MainPageLocators.BURGER_CONSTRUCTOR_SECTION)

    @allure.step("Проверяем, что счётчик заказов отображается")
    def is_order_feed_counter_visible(self):
        return self.wait_for_section_visible(MainPageLocators.COMPLETED_ORDERS)

    @allure.step("Проверяем, что окно деталей ингредиента отображается")
    def is_ingredient_details_visible(self):
        return self.is_element_displayed(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    #  Получение данных
    @allure.step("Получаем значение счётчика ингредиента")
    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Получаем сообщение об успешном оформлении заказа")
    def get_order_success_message(self):
        return self.get_text_from_element(MainPageLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step("Ожидаем исчезновение overlay")
    def wait_for_overlay_to_disappear(self, timeout=10):
        return self.wait_for_element_invisible(MainPageLocators.OVERLAY, timeout)

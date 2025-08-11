import logging
import allure
from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from data.data import FEED_URL

logger = logging.getLogger(__name__)

class OrderFeedPage(BasePage):

    @allure.step("Открываем страницу ленты заказов")
    def open_feed_page(self):
        logger.info("Переход на страницу ленты заказов: %s", FEED_URL)
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TITLE)

    @allure.step("Нажимаем на последний заказ в ленте")
    def click_last_order(self):
        logger.debug("Клик по последнему заказу в ленте")
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step("Получаем содержимое деталей заказа")
    def get_order_details_content(self):
        logger.debug("Получение содержимого деталей заказа")
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    @allure.step("Получаем общее количество заказов")
    def get_total_orders_counter(self):
        logger.debug("Чтение счетчика общего числа заказов")
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получаем количество заказов, выполненных сегодня")
    def get_today_completed_counter(self):
        logger.debug("Чтение счетчика заказов за сегодня")
        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())

    @allure.step("Закрываем окно деталей заказа")
    def click_close_order_details(self):
        logger.debug("Закрытие окна деталей заказа")
        self.click_when_clickable(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step("Получаем ID заказа из деталей")
    def get_order_id_from_details(self):
        logger.debug("Получение ID заказа из деталей")
        self.find_and_wait_until_text_changes(OrderFeedPageLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)

    @allure.step("Проверяем, что заказ с ID {order_id} отображается в ленте")
    def is_order_id_in_feed(self, order_id):
        logger.debug("Проверка наличия заказа %s в ленте", order_id)
        formatted_id = f"{int(order_id):07d}"
        locator = (
            OrderFeedPageLocators.ORDER_ID_IN_FEED[0],
            OrderFeedPageLocators.ORDER_ID_IN_FEED[1].format(formatted_id)
        )
        return self.find_element_with_wait(locator)

    @allure.step("Проверяем, что заказ с номером {order_id} находится в процессе")
    def is_order_number_in_progress(self, order_id):
        logger.debug("Проверка, что заказ %s в процессе", order_id)
        formatted_id = f"{int(order_id):07d}"
        locator = (
            OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR[0],
            OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR[1].format(formatted_id)
        )
        self.find_element_with_wait(locator)
        return True

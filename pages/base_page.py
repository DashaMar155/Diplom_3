import logging
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage:
    DEFAULT_WAIT = 10
    LONG_WAIT = 25

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Ожидаем видимость элемента: {locator}")
    def find_element_with_wait(self, locator: Tuple[str, str], timeout: int = DEFAULT_WAIT) -> WebElement:
        logger.info(f"Ожидание видимости элемента {locator} в течение {timeout} секунд")
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Кликаем по элементу: {locator}")
    def click_to_element(self, locator: Tuple[str, str], timeout: int = LONG_WAIT):
        logger.info(f"Кликаем по элементу {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step("Вводим текст '{text}' в элемент: {locator}")
    def add_text_to_element(self, locator: Tuple[str, str], text: str):
        logger.info(f"Ввод текста '{text}' в элемент {locator}")
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст из элемента: {locator}")
    def get_text_from_element(self, locator: Tuple[str, str]) -> str:
        element = self.find_element_with_wait(locator)
        text = element.text
        logger.info(f"Получен текст из элемента {locator}: {text}")
        return text

    @allure.step("Проверяем, что элемент видим: {locator}")
    def is_element_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_WAIT) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Элемент {locator} видим")
            return True
        except TimeoutException:
            logger.warning(f"Элемент {locator} не видим после {timeout} секунд")
            return False

    @allure.step("Кликаем по элементу через JS: {locator}")
    def click_with_js(self, locator: Tuple[str, str], timeout: int = LONG_WAIT):
        logger.info(f"Кликаем по элементу через JS: {locator}")
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Перетаскиваем элемент: {source_locator} → {target_locator}")
    def drag_and_drop(self, source_locator: Tuple[str, str], target_locator: Tuple[str, str]):
        logger.info(f"Перетаскиваем элемент {source_locator} на {target_locator}")
        element_from = self.find_element_with_wait(source_locator)
        element_to = self.find_element_with_wait(target_locator)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()

    @allure.step("Переходим по URL: {url}")
    def navigate_to(self, url: str):
        logger.info(f"Переход по URL: {url}")
        self.driver.get(url)

    @allure.step("Ждем пока элемент станет невидимым: {locator}")
    def wait_for_element_invisible(self, locator: Tuple[str, str], timeout: int = DEFAULT_WAIT) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Элемент {locator} стал невидимым")
            return True
        except TimeoutException:
            logger.warning(f"Элемент {locator} не стал невидимым за {timeout} секунд")
            return False

    def format_locator(self, locator: Tuple[str, str], value) -> Tuple[str, str]:
        method, locator_str = locator
        formatted_locator = locator_str.format(value)
        logger.debug(f"Отформатирован локатор: {formatted_locator}")
        return method, formatted_locator

    @allure.step("Ищем элемент по форматированному локатору: {locator} с параметром {dynamic_value}")
    def find_and_format_locator(self, locator: Tuple[str, str], dynamic_value) -> WebElement:
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step("Ожидаем появления секции: {locator}")
    def wait_for_section_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_WAIT, scroll: bool = True) -> bool:
        try:
            if scroll:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", self.find_element_with_wait(locator))
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.info(f"Секция {locator} видима")
            return True
        except TimeoutException:
            logger.warning(f"Секция {locator} не появилась за {timeout} секунд")
            return False

    @allure.step("Ожидаем, пока текст элемента {locator} изменится")
    def find_and_wait_until_text_changes(self, locator: Tuple[str, str], initial_text: str, timeout: int = DEFAULT_WAIT) -> WebElement:
        logger.info(f"Ждем изменения текста в элементе {locator}")
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_text_from_element(locator) != initial_text
        )
        return self.find_element_with_wait(locator)

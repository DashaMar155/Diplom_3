import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидаем элемент: {locator}")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step("Кликаем по элементу: {locator}")
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Вводим текст '{text}' в элемент: {locator}")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получаем текст из элемента: {locator}")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Скроллим к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locator(self, locator, num):
        method, locator_str = locator
        locator_str = locator_str.format(num)
        return method, locator_str

    @allure.step("Кликаем по элементу, когда он станет кликабельным: {locator}")
    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step("Проверяем, что элемент видим: {locator}")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Кликаем по элементу через JS: {locator}")
    def click_with_js(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидаем появления элемента: {locator}")
    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Перетаскиваем элемент: {source_locator} → {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Проверяем, отображается ли элемент: {locator}")
    def is_element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step("Переходим по URL: {url}")
    def navigate_to(self, url):
        self.driver.get(url)

    def wait_until_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Ожидаем, пока текст элемента {locator} изменится")
    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step("Ищем элемент по форматированному локатору: {locator} с параметром {dynamic_value}")
    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step("Получаем значение атрибута '{attribute_name}' у элемента: {locator}")
    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)

    @allure.step("Ожидаем появления секции: {locator}")
    def wait_for_section_visible(self, locator, timeout=10, scroll=True):
        try:
            if scroll:
                self.scroll_to_element(locator)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидаем, что элемент исчезнет: {locator}")
    def wait_for_element_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

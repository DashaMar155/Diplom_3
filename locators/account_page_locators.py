from selenium.webdriver.common.by import By

class AccountPageLocators:

    #  Авторизация
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0")
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
    LOGIN_AFTER_LOGOUT_BURGER = (
        By.XPATH,
        "//h1[@class='text text_type_main-large mb-5 mt-10']"
    )

    #  Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

    #  История заказов
    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[contains(@class, 'Account_link__2ETsJ')]"
    )
    ORDER_COMPLETED = (
        By.XPATH,
        "//p[contains(@class, 'OrderHistory_visible__19YMB')]"
    )

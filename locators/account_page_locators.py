from selenium.webdriver.common.by import By

class AccountPageLocators:

    # Авторизация
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
    LOGIN_AFTER_LOGOUT_BURGER = (
        By.XPATH,
        "//h1[contains(@class,'text_type_main-large') and contains(text(),'Соберите бургер')]"
    )

    # Личный кабинет
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")

    # История заказов
    ORDER_HISTORY_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'История заказов')]"
    )
    ORDER_COMPLETED = (
        By.XPATH,
        "//p[contains(text(),'Выполнен')]"
    )

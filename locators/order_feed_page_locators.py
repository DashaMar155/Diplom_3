from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    # Верхнее меню
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента заказов')]")
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(@href, '/account/order-history')]")

    # Лента заказов
    LAST_ORDER = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_list')]/li[1]//div[contains(@class,'OrderCard')]"
    )
    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList')]//li"
    )
    FEED_TITLE = (
        By.XPATH,
        "//h1[contains(text(),'Лента заказов')]"
    )

    # Счётчики
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(@class,'OrderFeed_number')][1]"
    )
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//section[contains(., 'Выполнено за сегодня')]//p[contains(@class,'OrderFeed_number')]"
    )

    # Детали заказа
    ORDER_DETAILS_CONTENT = (
        By.XPATH,
        "//p[contains(@class,'text_type_main-medium') and contains(text(),'Состав')]"
    )
    ORDER_ID = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]"
    )
    ORDER_ID_IN_FEED = (
        By.XPATH,
        "//*[contains(text(), '{0}')]"
    )
    ORDER_PREPARING_MESSAGE = (
        By.XPATH,
        "//p[contains(text(),'Готовится')]"
    )
    CLOSE_ORDER_DETAILS_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    # Модальные окна
    ORDER_LOADING_MODAL = (
        By.XPATH,
        "//div[contains(@class,'Modal_modal_opened')]"
    )

    # После входа
    LOGIN_AFTER_LOGOUT_BURGER = (
        By.XPATH,
        "//h1[contains(text(),'Соберите бургер')]"
    )

    # Кнопка оформления заказа
    PLACE_AN_ORDER = (
        By.XPATH,
        "//button[contains(text(),'Оформить заказ')]"
    )

from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    #  Верхнее меню
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ')]")

    #  Лента заказов
    LAST_ORDER = (
        By.XPATH,
        "//ul[@class='OrderFeed_list__OLh59']/li[1]/a[1]/div[1]"
    )
    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]"
    )
    FEED_TITLE = (
        By.XPATH,
        "//h1[contains(@class, 'text_type_main-large')]"
    )

    #  Счётчики
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//div[@class='undefined mb-15']//p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    )

    #  Детали заказа
    ORDER_DETAILS_CONTENT = (
        By.XPATH,
        "//p[@class='text text_type_main-medium mb-8']"
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
        "//p[@class='undefined text text_type_main-small mb-2']"
    )
    CLOSE_ORDER_DETAILS_BUTTON = (
        By.XPATH,
        "//button[@type='button']//*[name()='svg']"
    )

    #  Модальные окна
    ORDER_LOADING_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_opened__3ISw4')]//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]"
    )

    #  После входа
    LOGIN_AFTER_LOGOUT_BURGER = (
        By.XPATH,
        "//h1[@class='text text_type_main-large mb-5 mt-10']"
    )

    #  Кнопка оформления заказа
    PLACE_AN_ORDER = (
        By.XPATH,
        "//button[contains(@class, 'button_button_type_primary__1O7Bx')]"
    )

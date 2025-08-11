from selenium.webdriver.common.by import By

class MainPageLocators:

    # Верхнее меню
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента заказов')]")

    # Конструктор бургера
    BURGER_CONSTRUCTOR_SECTION = (
        By.XPATH,
        "//section[contains(@class,'BurgerIngredients_ingredients')]"
    )
    INGREDIENT_R2D3_BUN = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']"
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[contains(@class,'counter_counter__num')]"
    )
    ORDER_TARGET_TOP = (
        By.XPATH,
        "//img[contains(@alt,'булочку сюда') and contains(@alt,'верх')]"
    )
    PLACE_AN_ORDER = (
        By.XPATH,
        "//button[contains(text(),'Оформить заказ')]"
    )

    # Детали ингредиента
    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]"
    )
    CLOSE_INGREDIENT_DETAILS_BUTTON = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened')]//button[@type='button']//*[name()='svg']"
    )

    # Лента заказов
    COMPLETED_ORDERS = (
        By.XPATH,
        "//p[contains(text(),'Готовы')]"
    )
    COMPLETED_ORDERS_COUNTER = (
        By.XPATH,
        "//section[contains(., 'Готовы')]/p[contains(@class,'OrderFeed_number')]"
    )
    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady')]//li//*[contains(text(), '{0}')]"
    )

    # Успешное оформление заказа
    ORDER_SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(text(),'готовится')]"
    )

    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay")

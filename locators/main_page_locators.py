from selenium.webdriver.common.by import By

class MainPageLocators:

    #  Верхнее меню
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")

    #  Конструктор бургера
    BURGER_CONSTRUCTOR_SECTION = (
        By.XPATH,
        "//section[@class='BurgerIngredients_ingredients__1N8v2']"
    )
    INGREDIENT_R2D3_BUN = (
        By.XPATH,
        "//img[@alt='Флюоресцентная булка R2-D3']"
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[@class='counter_counter__num__3nue1']"
    )
    ORDER_TARGET_TOP = (
        By.XPATH,
        "//img[@alt='Перетяните булочку сюда (верх)']"
    )
    PLACE_AN_ORDER = (
        By.XPATH,
        "//button[contains(@class, 'button_button_type_primary__1O7Bx')]"
    )

    #  Детали ингредиента
    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//h2[contains(@class, 'Modal_modal__title')]"
    )
    CLOSE_INGREDIENT_DETAILS_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]"
    )

    #  Лента заказов
    COMPLETED_ORDERS = (
        By.XPATH,
        "//p[contains(text(),'Готовы:')]"
    )
    COMPLETED_ORDERS_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='153072']"
    )
    ORDER_IN_PROGRESS_LOCATOR = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li[1]//*[contains(text(), '{0}')]"
    )

    #  Успешное оформление заказа
    ORDER_SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(@class, 'text_type_main-small') and contains(text(), 'готовится')]"
    )

    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
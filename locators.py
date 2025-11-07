from selenium.webdriver.common.by import By

class LocatorResetPassword:
    RESET_PASSWORD = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    RESET_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='name']")
    BUTTON_EYE = (By.CSS_SELECTOR, '.input__icon-action svg')
    BLOCK_PASSWORD_ACTIVE = (By.CSS_SELECTOR, '.input_status_active input[name="Введите новый пароль"]')

class LocatorPersonalAccount:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and text()='Личный Кабинет']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")
    PERSONAL_ACCOUNT_BUTTON_AUTH = (By.CSS_SELECTOR, "a[href='/account']")
    HISTORY_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
    ORDER_HISTORY_BLOCK = (By.CSS_SELECTOR, "div.OrderHistory_orderHistory__qy1VB")
    LOGIN_TEXT = (By.XPATH, "//h2[text()='Вход']")

class LocatorMainFunc:
    TEXT_BUILD_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")
    FEED_ORDERS = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")
    POPUP_FEED_ORDER = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 .Modal_modal__close_modified__3V5XS")
    COUNTER_INGREDIENT = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")
    BLOCK_INGREDIENTS = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6")
    SELECTED_INGREDIENTS_BOXS = (By.CSS_SELECTOR, "ul.BurgerConstructor_basket__list__l9dp_")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Оформить заказ']")
    POPUP_ORDER_ID_LARGE = (By.CSS_SELECTOR, "h2.text_type_digits-large")
    POPUP_ORDER_ID = (By.CSS_SELECTOR, '.Modal_orderBox__1xWdi .text_type_digits-default')
    ORDER_IDS = (By.CSS_SELECTOR, "p.text_type_digits-default")
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a.AppHeader_header__link__3D_hX[href='/']")
    BUTTON_CLOSE_POPUP = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 button.Modal_modal__close_modified__3V5XS")
    ORDER_FEED_NUMBER_ALL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    ORDER_FEED_NUMBER_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDER_IN_WORK = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text_type_digits-default")
    ORDERS_READY = (By.CSS_SELECTOR, ".OrderFeed_orderList__cBvyi:not(.OrderFeed_orderListReady__1YFem) .text_type_digits-default")
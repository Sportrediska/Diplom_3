import allure
from pages.login_page import LoginPage
from pages.main_func_page import MainFuncPage


class TestMainFunc:
    @allure.title("Проверка клика на конструктор")
    @allure.description("Тест проверяет работу кнопки конструктора")
    def test_click_constructor(self, driver):
        with allure.step("Создать экземпляр главной страницы"):
            main_func = MainFuncPage(driver)

        with allure.step("Кликнуть на конструктор и проверить успешность"):
            assert main_func.click_constructor()

    @allure.title("Проверка клика на ленту заказов")
    @allure.description("Тест проверяет работу кнопки ленты заказов")
    def test_click_feed_orders(self, driver):
        with allure.step("Создать экземпляр главной страницы"):
            main_func = MainFuncPage(driver)

        with allure.step("Кликнуть на ленту заказов и проверить успешность"):
            assert main_func.click_feed_orders()

    @allure.title("Проверка открытия и закрытия попапа заказа")
    @allure.description("Тест проверяет открытие и закрытие попапа с деталями заказа")
    def test_feed_orders_popup(self, driver):
        with allure.step("Создать экземпляр главной страницы"):
            main_func = MainFuncPage(driver)

        with allure.step("Открыть попап заказа и проверить успешность"):
            assert main_func.check_click_feed_orders_open_popup()

        with allure.step("Закрыть попап заказа и проверить успешность"):
            assert main_func.close_feed_orders_open_popup()

    @allure.title("Проверка добавления ингредиента в заказ")
    @allure.description("Тест проверяет добавление ингредиента в конструктор бургера")
    def test_add_ingredient_order(self, driver):
        with allure.step("Создать экземпляр главной страницы"):
            main_func = MainFuncPage(driver)

        with allure.step("Перейти в конструктор"):
            main_func.click_constructor()

        with allure.step("Перетащить ингредиент в конструктор"):
            main_func.drag_ingredient_to_constructor()

        with allure.step("Проверить, что счетчик ингредиента изменился"):
            assert main_func.get_ingredient_counter() != 0

    @allure.title("Проверка создания заказа авторизованным пользователем")
    @allure.description("Тест проверяет создание заказа авторизованным пользователем")
    def test_authorized_user_creates_order(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            main_func = MainFuncPage(driver)
            login = LoginPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Создать заказ и проверить успешность"):
            assert main_func.make_order()
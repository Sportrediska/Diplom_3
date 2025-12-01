import allure
from pages.login_page import LoginPage
from pages.main_func_page import MainFuncPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestFeedOrder:
    @allure.title("Проверка открытия деталей заказа по клику")
    @allure.description("Тест проверяет, что клик на заказ открывает попап с деталями")
    def test_click_order_opens_details(self, driver):
        with allure.step("Создать экземпляры страниц"):
            order_feed_page = OrderFeedPage(driver)
            main_func_page = MainFuncPage(driver)

        with allure.step("Перейти в ленту заказов"):
            main_func_page.click_feed_orders()

        with allure.step("Кликнуть на заказ и проверить открытие деталей"):
            assert order_feed_page.click_order()

    @allure.title("Проверка отображения заказа в истории и ленте")
    @allure.description("Тест проверяет, что созданный заказ отображается в истории заказов и в ленте")
    def test_order_in_history_and_feed(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            login = LoginPage(driver)
            personal_account = PersonalAccountPage(driver)
            main_func_page = MainFuncPage(driver)
            order_feed_page = OrderFeedPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Создать заказ"):
            main_func_page.make_order()

        with allure.step("Закрыть попап создания заказа"):
            main_func_page.close_feed_orders_open_popup()

        with allure.step("Перейти в личный кабинет"):
            personal_account.click_personal_account()

        with allure.step("Открыть историю заказов"):
            personal_account.open_history_page()

        with allure.step("Получить ID последнего заказа из истории"):
            order_id_in_history = personal_account.get_last_order_id()

        with allure.step("Перейти в ленту заказов"):
            main_func_page.click_feed_orders()

        with allure.step("Получить список ID заказов в ленте"):
            order_ids_in_feed = order_feed_page.get_order_ids()

        with allure.step("Проверить, что ID заказа из истории есть в ленте"):
            assert order_id_in_history in order_ids_in_feed

    @allure.title("Проверка изменения счетчиков заказов")
    @allure.description("Тест проверяет увеличение счетчиков выполненных заказов после создания нового заказа")
    def test_change_counter_orders(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            login = LoginPage(driver)
            main_func_page = MainFuncPage(driver)
            order_feed_page = OrderFeedPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Перейти в ленту заказов"):
            main_func_page.click_feed_orders()

        with allure.step("Получить начальные значения счетчиков"):
            count_before_all = order_feed_page.get_number_complete_all()
            count_before_today = order_feed_page.get_number_complete_today()

        with allure.step("Создать заказ"):
            main_func_page.make_order()

        with allure.step("Получить ID созданного заказа"):
            order_id = main_func_page.get_order_id_from_popup_order_created()

        with allure.step("Закрыть попап создания заказа"):
            main_func_page.close_feed_orders_open_popup()

        with allure.step("Снова перейти в ленту заказов"):
            main_func_page.click_feed_orders()

        with allure.step("Дождаться готовности заказа"):
            main_func_page.wait_order_ready(order_id)

        with allure.step("Получить конечные значения счетчиков"):
            count_after_all = order_feed_page.get_number_complete_all()
            count_after_today = order_feed_page.get_number_complete_today()

        with allure.step("Проверить увеличение счетчика всех заказов"):
            assert count_before_all < count_after_all

        with allure.step("Проверить увеличение счетчика заказов за сегодня"):
            assert count_before_today < count_after_today

    @allure.title("Проверка отображения заказа 'в работе'")
    @allure.description("Тест проверяет, что созданный заказ отображается в разделе 'в работе'")
    def test_order_in_work(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            login = LoginPage(driver)
            main_func_page = MainFuncPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Создать заказ"):
            main_func_page.make_order()

        with allure.step("Получить ID созданного заказа"):
            order_id = main_func_page.get_order_id_from_popup_order_created()

        with allure.step("Закрыть попап создания заказа"):
            main_func_page.close_feed_orders_open_popup()

        with allure.step("Перейти в ленту заказов"):
            main_func_page.click_feed_orders()

        with allure.step("Проверить, что заказ отображается в работе"):
            assert main_func_page.wait_order_in_work(order_id)
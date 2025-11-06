from pages.login_page import LoginPage
from pages.main_func_page import MainFuncPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage
from test_data import VALID_EMAIL, VALID_PASSWORD


class TestFeedOrder:
    def test_click_order_opens_details(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_func_page = MainFuncPage(driver)
        main_func_page.click_feed_orders()
        assert order_feed_page.click_order()

    def test_order_in_history_and_feed(self, driver):
        login = LoginPage(driver)
        personal_account = PersonalAccountPage(driver)
        main_func_page = MainFuncPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login.authorize_user(VALID_EMAIL, VALID_PASSWORD)
        main_func_page.make_order()
        main_func_page.close_feed_orders_open_popup()
        personal_account.click_personal_account()
        personal_account.open_history_page()
        order_id_in_history = personal_account.get_last_order_id()
        main_func_page.click_feed_orders()
        order_ids_in_feed = order_feed_page.get_order_ids()
        assert order_id_in_history in order_ids_in_feed

    def test_change_counter_orders(self, driver):
        login = LoginPage(driver)
        main_func_page = MainFuncPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login.authorize_user(VALID_EMAIL, VALID_PASSWORD)
        main_func_page.click_feed_orders()
        count_before_all = order_feed_page.get_number_complete_all()
        count_before_today = order_feed_page.get_number_complete_today()
        main_func_page.make_order()
        main_func_page.close_feed_orders_open_popup()
        main_func_page.click_feed_orders()
        count_after_all = order_feed_page.get_number_complete_all()
        count_after_today = order_feed_page.get_number_complete_today()

        assert count_before_all < count_after_all
        assert count_before_today < count_after_today

    def test_order_in_work(self, driver):
        login = LoginPage(driver)
        main_func_page = MainFuncPage(driver)
        login.authorize_user(VALID_EMAIL, VALID_PASSWORD)
        main_func_page.make_order()
        order_id = main_func_page.get_order_id_from_popup_order_created()
        main_func_page.close_feed_orders_open_popup()
        main_func_page.click_feed_orders()

        assert main_func_page.check_order_in_work(order_id)

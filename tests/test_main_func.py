from pages.login_page import LoginPage
from pages.main_func_page import MainFuncPage


class TestMainFunc:
    def test_click_constructor(self, driver):
        main_func = MainFuncPage(driver)
        assert main_func.click_constructor()

    def test_click_feed_orders(self, driver):
        main_func = MainFuncPage(driver)
        assert main_func.click_feed_orders()

    def test_feed_orders_popup(self, driver):
        main_func = MainFuncPage(driver)
        assert main_func.check_click_feed_orders_open_popup()
        assert main_func.close_feed_orders_open_popup()

    def test_add_ingredient_order(self, driver):
        main_func = MainFuncPage(driver)
        main_func.click_constructor()
        main_func.drag_ingredient_to_constructor()
        assert main_func.get_ingredient_counter() != 0

    def test_authorized_user_creates_order(self, driver, new_user):
        main_func = MainFuncPage(driver)
        login = LoginPage(driver)
        login.authorize_user(new_user['email'], new_user['password'])
        assert main_func.make_order()
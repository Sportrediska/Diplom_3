from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    def test_open_personal_account(self, driver, new_user):
        login = LoginPage(driver)
        login.authorize_user(new_user['email'], new_user['password'])
        personal_account = PersonalAccountPage(driver)
        assert personal_account.click_personal_account()

    def test_open_order_history(self, driver, new_user):
        login = LoginPage(driver)
        login.authorize_user(new_user['email'], new_user['password'])
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        assert personal_account.open_history_page()

    def test_logout(self, driver, new_user):
        login = LoginPage(driver)
        login.authorize_user(new_user['email'], new_user['password'])
        personal_account = PersonalAccountPage(driver)
        personal_account.click_personal_account()
        assert personal_account.click_logout()

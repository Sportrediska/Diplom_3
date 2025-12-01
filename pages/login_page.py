from time import sleep
from locators import LocatorResetPassword, LocatorPersonalAccount, LocatorMainFunc
from pages.base_page import BasePage

class LoginPage(BasePage):
    def authorize_user(self, email, password):
        self.open('/login')
        self.wait_visibility_element(LocatorResetPassword.INPUT_EMAIL)
        sleep(1)  # сделано, т.к. в firefox появляется невидимая модалка, которая перекрывает элемент для клика
        self.click_element(LocatorResetPassword.INPUT_EMAIL)
        self.fill_field(LocatorResetPassword.INPUT_EMAIL, email)
        self.click_element(LocatorPersonalAccount.INPUT_PASSWORD)
        self.fill_field(LocatorPersonalAccount.INPUT_PASSWORD, password)
        self.click_element(LocatorPersonalAccount.LOGIN_BUTTON)
        self.wait_visibility_element(LocatorMainFunc.TEXT_BUILD_BURGER)

from locators import LocatorPersonalAccount, LocatorMainFunc
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def click_personal_account(self):
        self.click_element(LocatorPersonalAccount.PERSONAL_ACCOUNT_BUTTON)
        return self.wait_visibility_element(LocatorPersonalAccount.HISTORY_ORDER_BUTTON)

    def open_history_page(self):
        self.click_element(LocatorPersonalAccount.HISTORY_ORDER_BUTTON)
        return self.wait_presence_element(LocatorPersonalAccount.ORDER_HISTORY_BLOCK)
#d
    def click_logout(self):
        self.click_element(LocatorPersonalAccount.LOGOUT_BUTTON)
        return self.wait_visibility_element(LocatorPersonalAccount.LOGIN_TEXT)

    def get_last_order_id(self):
        return self.find_last_element(LocatorMainFunc.ORDER_IDS).text
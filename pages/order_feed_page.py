from pages.base_page import BasePage
from locators import LocatorMainFunc

class OrderFeedPage(BasePage):
    def click_order(self):
        self.find_element(LocatorMainFunc.FEED_ORDERS).click()
        return self.wait_visibility_element(LocatorMainFunc.POPUP_ORDER_ID)

    def get_order_ids(self):
        elements = self.find_elements(LocatorMainFunc.ORDER_IDS)
        return [el.text for el in elements]

    def get_number_complete_all(self):
        return self.find_element(LocatorMainFunc.ORDER_FEED_NUMBER_ALL).text

    def get_number_complete_today(self):
        return self.find_element(LocatorMainFunc.ORDER_FEED_NUMBER_TODAY).text


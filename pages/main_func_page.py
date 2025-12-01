from time import sleep

from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators import LocatorMainFunc

class MainFuncPage(BasePage):

    def click_constructor(self):
        self.click_element(LocatorMainFunc.CONSTRUCTOR_BUTTON)
        return self.wait_visibility_element(LocatorMainFunc.TEXT_BUILD_BURGER)

    def click_feed_orders(self):
        self.click_element(LocatorMainFunc.ORDER_FEED_BUTTON)
        return self.wait_visibility_element(LocatorMainFunc.FEED_ORDERS)

    def check_click_feed_orders_open_popup(self):
        self.click_feed_orders()
        self.click_element(LocatorMainFunc.FEED_ORDERS)
        return self.wait_visibility_element(LocatorMainFunc.POPUP_FEED_ORDER)

    def close_feed_orders_open_popup(self):
        self.click_element(LocatorMainFunc.BUTTON_CLOSE_POPUP)
        return self.wait_invisibility_element(LocatorMainFunc.BUTTON_CLOSE_POPUP)

    def drag_ingredient_to_constructor(self):
        ingredient = self.find_element(LocatorMainFunc.BLOCK_INGREDIENTS)
        target = self.find_element(LocatorMainFunc.SELECTED_INGREDIENTS_BOXS)
        ActionChains(self.driver).drag_and_drop(ingredient, target).perform()

    def get_ingredient_counter(self):
        element = self.find_element(LocatorMainFunc.COUNTER_INGREDIENT)
        return int(element.text)

    def click_create_order(self):
        self.click_element(LocatorMainFunc.CREATE_ORDER_BUTTON)
        self.wait_visibility_element(LocatorMainFunc.POPUP_ORDER_ID_LARGE)
        return self.wait_element_change_text(LocatorMainFunc.POPUP_ORDER_ID_LARGE, '9999')

    def make_order(self):
        self.click_constructor()
        self.drag_ingredient_to_constructor()
        return self.click_create_order()

    def get_order_id_from_popup_order_created(self):
        return self.find_element(LocatorMainFunc.POPUP_ORDER_ID_LARGE).text

    def wait_order_in_work(self, order_id):
        self.wait_visibility_element(LocatorMainFunc.ORDER_IN_WORK)
        return self.wait_element_text_will_be(LocatorMainFunc.ORDER_IN_WORK, "0" + order_id)

    def wait_order_ready(self, order_id):
        self.wait_visibility_element(LocatorMainFunc.ORDER_IN_WORK)
        return self.wait_element_text_will_be(LocatorMainFunc.ORDERS_READY, "0" + order_id)
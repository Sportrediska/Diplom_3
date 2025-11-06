from pages.base_page import BasePage
from locators import LocatorResetPassword
from time import sleep


class ResetPasswordPage(BasePage):
    def open_reset_password_form(self):
        self.open('/login')
        self.wait_visibility_element(LocatorResetPassword.RESET_PASSWORD)
        sleep(1) # сделано, т.к. в firefox появляется невидимая модалка, которая перекрывает элемент для клика
        self.click_element(LocatorResetPassword.RESET_PASSWORD)
        self.wait_visibility_element(LocatorResetPassword.RESET_PASSWORD_BUTTON)

    def fill_email_and_go_next(self, email):
        self.fill_field(LocatorResetPassword.INPUT_EMAIL, email)
        self.click_element(LocatorResetPassword.RESET_PASSWORD_BUTTON)
        self.wait_visibility_element(LocatorResetPassword.BUTTON_EYE)

    def check_click_eye_change_border_color(self):
        self.click_element(LocatorResetPassword.BUTTON_EYE)
        return self.wait_visibility_element(LocatorResetPassword.BLOCK_PASSWORD_ACTIVE)
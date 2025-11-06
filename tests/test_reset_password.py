from pages.reset_password_page import ResetPasswordPage
from test_data import VALID_EMAIL


class TestResetPassword:
    def test_eye_change_border(self, driver):
        reset_pass = ResetPasswordPage(driver)
        reset_pass.open_reset_password_form()
        reset_pass.fill_email_and_go_next(VALID_EMAIL)
        assert reset_pass.check_click_eye_change_border_color()
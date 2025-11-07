from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:
    def test_eye_change_border(self, driver, random_user_payload_for_create):
        reset_pass = ResetPasswordPage(driver)
        reset_pass.open_reset_password_form()
        reset_pass.fill_email_and_go_next(random_user_payload_for_create['email'])
        assert reset_pass.check_click_eye_change_border_color()
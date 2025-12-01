import allure
from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:
    @allure.title("Проверка изменения видимости пароля при клике на иконку глаза")
    @allure.description("Тест проверяет, что при клике на иконку глаза меняется видимость пароля")
    def test_eye_change_border(self, driver, random_user_payload_for_create):
        with allure.step("Создать экземпляр страницы сброса пароля"):
            reset_pass = ResetPasswordPage(driver)

        with allure.step("Открыть форму сброса пароля"):
            reset_pass.open_reset_password_form()

        with allure.step("Заполнить email и перейти к следующему шагу"):
            reset_pass.fill_email_and_go_next(random_user_payload_for_create['email'])

        with allure.step("Проверить, что клик на иконку глаза меняет border color"):
            assert reset_pass.check_click_eye_change_border_color()
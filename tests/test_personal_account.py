import allure
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    @allure.title("Проверка открытия личного кабинета")
    @allure.description("Тест проверяет возможность открытия личного кабинета авторизованным пользователем")
    def test_open_personal_account(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            login = LoginPage(driver)
            personal_account = PersonalAccountPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Перейти в личный кабинет и проверить успешность"):
            assert personal_account.click_personal_account()

    @allure.title("Проверка открытия истории заказов")
    @allure.description("Тест проверяет возможность открытия истории заказов из личного кабинета")
    def test_open_order_history(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            login = LoginPage(driver)
            personal_account = PersonalAccountPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Перейти в личный кабинет"):
            personal_account.click_personal_account()

        with allure.step("Открыть историю заказов и проверить успешность"):
            assert personal_account.open_history_page()

    @allure.title("Проверка выхода из аккаунта")
    @allure.description("Тест проверяет возможность выхода из аккаунта через личный кабинет")
    def test_logout(self, driver, new_user):
        with allure.step("Создать экземпляры страниц"):
            login = LoginPage(driver)
            personal_account = PersonalAccountPage(driver)

        with allure.step("Авторизоваться пользователем"):
            login.authorize_user(new_user['email'], new_user['password'])

        with allure.step("Перейти в личный кабинет"):
            personal_account.click_personal_account()

        with allure.step("Выйти из аккаунта и проверить успешность"):
            assert personal_account.click_logout()
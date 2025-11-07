from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
from selenium import webdriver
from base_url import BASE_URL

from faker import Faker
from api.create_user import CreateUser
from api.login_user import LoginUser
from api.delete_user import DeleteUser

@pytest.fixture
def delete_user_api():
    return DeleteUser()

@pytest.fixture
def create_user_api():
    return CreateUser()

@pytest.fixture
def login_user_api():
    return LoginUser()

@pytest.fixture
def random_user_payload_for_create():
    fake = Faker('ru_RU')
    return {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.user_name()
    }

@pytest.fixture
def new_user(random_user_payload_for_create, create_user_api, login_user_api, delete_user_api):
    create_user_api.create_user(random_user_payload_for_create)
    yield random_user_payload_for_create
    login_user_api.login_user(random_user_payload_for_create)
    delete_user_api.delete_user(login_user_api.token)

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    options = FirefoxOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--disable-extensions")
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Ошибка браузера: {request.param}")

    driver.get(BASE_URL)
    yield driver
    driver.quit()
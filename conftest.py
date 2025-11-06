from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
from selenium import webdriver
from base_url import BASE_URL


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
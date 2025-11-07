from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_url import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
#
    def open(self, path=""):
        self.driver.get(f"{BASE_URL}{path}")
#
    def wait_visibility_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_element_change_text(self, locator, initial_text):
        element = self.find_element(locator)
        return self.wait.until(lambda driver: element.text != initial_text)

    def wait_element_text_will_be(self, locator, text):
        element = self.find_element(locator)
        return self.wait.until(lambda driver: element.text == text)

    def wait_invisibility_element(self, locator):
        return self.wait.until(EC.invisibility_of_element(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_last_element(self, locator):
        return self.driver.find_elements(*locator)[-1]

    def click_element(self, locator):
        self.find_element(locator).click()

    def fill_field(self, locator, text):
        self.find_element(locator).send_keys(text)

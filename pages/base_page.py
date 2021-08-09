from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Открыть www.yandex.ru")
    def open(self):
        self.driver.get(self.url)

    def find_elements(self, by, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located((by, locator)))
        except TimeoutException:
            return []

    def is_element_present(self, by, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

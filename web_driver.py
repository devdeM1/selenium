from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class WebDriver:
    DEFAULT_TIMEOUT = 5

    def __init__(self,driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def get_visible_element(self, locator, timeout=DEFAULT_TIMEOUT):
        self.scroll_to_element(self.get_present_element(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_present_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

from abc import ABC

from utils.web_driver_utils import WebDriverUtils


class BasePage(ABC):
    web_driver = WebDriverUtils()

    def __init__(self, driver):
        self.driver = driver

    def page_is_successfully_open(self, locator):
        try:
            self.web_driver.get_present_element(self.driver, locator)
            return True
        except Exception:
            return False

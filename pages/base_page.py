from abc import ABC

from web_driver_utils import WebDriverUtils


class BasePage(ABC):
    web_driver = WebDriverUtils()

    def __init__(self, driver):
        self.driver = driver

    def page_is_successfully_open(self, driver, locator):
        try:
            self.web_driver.get_present_element(driver, locator)
            return True
        except Exception:
            return False

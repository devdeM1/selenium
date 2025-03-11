from abc import ABC

from web_driver import WebDriver


class BasePage(ABC):
    def __init__(self):
        self.web_driver = WebDriver()

    def page_is_successfully_open(self, locator):
        try:
            self.web_driver.get_present_element(locator)
            return True
        except Exception:
            return False

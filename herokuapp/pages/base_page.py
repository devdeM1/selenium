from abc import ABC
from utils.web_driver_utils import WebDriverUtils
from selenium.common.exceptions import TimeoutException


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

    def open(self):
        raise NotImplementedError("Subclasses must implement open method.")

    def get_alert_text(self):
        self.web_driver.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def input_text_to_prompt(self, input_text):
        self.web_driver.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        alert.send_keys(input_text)

    def verify_alert_closed(self, timeout=5):
        try:
            self.web_driver.wait_for_alert(self.driver, timeout)
            return False
        except TimeoutException:
            return True

    def go_to_previous_page(self):
        self.driver.back()

    def switch_to_new_window(self):
        self.web_driver.switch_to_new_window(self.driver)

    def switch_to_first_window(self):
        self.web_driver.switch_to_first_window(self.driver)

    def close_window_by_title(self, title):
        self.web_driver.close_window_by_title(self.driver, title)

    def get_title(self):
        return self.driver.title

    def get_window_count(self):
        return self.web_driver.get_window_count(self.driver)

    def reload(self):
        self.driver.refresh()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

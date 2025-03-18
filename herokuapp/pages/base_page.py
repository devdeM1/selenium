from abc import ABC

from web_driver_utils import WebDriverUtils


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

    def handle_simple_alert(self):
        self.web_driver.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def handle_confirmation_alert(self):
        self.web_driver.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def handle_prompt_alert(self, input_text):
        self.web_driver.wait_for_alert(self.driver)
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.send_keys(input_text)
        alert.accept()
        return alert_text

from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    BUTTON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")
    url = "https://theinternet.herokuapp.com/javascript_alerts"

    def open(self):
        self.driver.get(self.url)

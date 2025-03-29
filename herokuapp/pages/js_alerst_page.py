from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    TITLE_AFTER_CLOSE_ALERT = (By.XPATH, "//p[@id='result']")
    BUTTON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    def open(self):
        self.driver.get(self.URL)

    def click_button_js_alert(self):
        self.web_driver.get_present_element(self.driver, JavaScriptAlertsPage.BUTTON_JS_ALERT).click()

    def click_button_js_confirm(self):
        self.web_driver.get_present_element(self.driver, JavaScriptAlertsPage.BUTTON_JS_CONFIRM).click()

    def click_button_js_prompt(self):
        self.web_driver.get_present_element(self.driver, JavaScriptAlertsPage.BUTTON_JS_PROMPT).click()

    def get_result_output(self):
        return self.web_driver.get_present_element(self.driver, JavaScriptAlertsPage.TITLE_AFTER_CLOSE_ALERT).text

    def trigger_js_alert(self):
        self.driver.execute_script("jsAlert();")

    def trigger_js_confirm(self):
        self.driver.execute_script("jsConfirm();")

    def trigger_js_prompt(self):
        self.driver.execute_script("jsPrompt();")

from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class BasicAuthPage(BasePage):
    TITLE = (By.XPATH, "//p[contains(text(), 'Congratulations! You must have the proper credentials')]")
    url = "http://the-internet.herokuapp.com/basic_auth"

    def open(self):
        self.driver.get(self.url)

    def authorize(self, username, password):
        url = "http://{}:{}@the-internet.herokuapp.com/basic_auth".format(username, password)
        self.driver.get(url)

    def is_auth_successful(self):
        try:
            self.web_driver.get_present_element(self.driver, BasicAuthPage.TITLE)
            return True
        except Exception:
            return False

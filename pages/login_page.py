from locators.login_page_locators import LoginPageLocators
from web_driver import WebDriver


class LoginPage(WebDriver):
    locators = LoginPageLocators()

    def fill_all_fields_and_click_submit(self, login, password):
        self.get_visible_element(self.locators.LOGIN).send_keys(login)
        self.get_visible_element(self.locators.PASSWORD).send_keys(password)
        self.get_visible_element(self.locators.SUBMIT).click()

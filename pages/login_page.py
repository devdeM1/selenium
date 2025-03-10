from locators.login_page_locators import LoginPageLocators
from web_driver import WebDriver


class LoginPage:
    locators = LoginPageLocators()

    def fill_all_fields_and_click_submit(self, web_driver, login, password):
        web_driver.get_visible_element(self.locators.LOGIN).send_keys(login)
        web_driver.get_visible_element(self.locators.PASSWORD).send_keys(password)
        web_driver.get_visible_element(self.locators.SUBMIT).click()

from locators.main_page_locators import MainPageLocators
from web_driver import WebDriver


class MainPage(WebDriver):
    locators = MainPageLocators()

    def click_on_login_button(self):
        self.get_visible_element(self.locators.LOGIN_BUTTON).click()

    def page_is_successfully_open(self):
        try:
            self.get_present_element(self.locators.TITLE)
            return True
        except Exception:
            return False
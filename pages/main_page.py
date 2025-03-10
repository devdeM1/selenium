from locators.main_page_locators import MainPageLocators
from web_driver import WebDriver


class MainPage(WebDriver):
    locators = MainPageLocators()

    def click_on_login_button(self):
        self.get_visible_element(self.locators.LOGIN_BUTTON).click()

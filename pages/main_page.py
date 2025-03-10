from locators.main_page_locators import MainPageLocators
from web_driver import WebDriver


class MainPage:
    locators = MainPageLocators()

    def click_on_login_button(self, web_driver):
        web_driver.get_visible_element(self.locators.LOGIN_BUTTON).click()

from locators.main_page_locators import MainPageLocators


class MainPage:
    locators = MainPageLocators()

    def click_on_login_button(self, web_driver):
        web_driver.get_visible_element(self.locators.LOGIN_BUTTON).click()

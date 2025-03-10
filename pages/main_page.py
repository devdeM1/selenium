from locators.main_page_locators import LOGIN_BUTTON

class MainPage:

    @staticmethod
    def click_on_login_button(web_driver):
        web_driver.get_visible_element(LOGIN_BUTTON).click()

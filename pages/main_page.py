from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//a[@class='global_action_link' and contains(@href, 'login')]")
    TITLE = (By.XPATH, "//title[contains(text(), 'Welcome to Steam')]")
    @staticmethod
    def click_on_login_button(web_driver):
        web_driver.get_visible_element(MainPage.LOGIN_BUTTON).click()

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//a[@class='global_action_link' and contains(@href, 'login')]")
    TITLE = (By.XPATH, "//title[contains(text(), 'Welcome to Steam')]")


    def click_on_login_button(self):
        self.web_driver.get_visible_element(MainPage.LOGIN_BUTTON).click()

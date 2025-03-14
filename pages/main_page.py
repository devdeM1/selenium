from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, "//a[@class='global_action_link' and contains(@href, 'login')]")
    SEARCH_INPUT_BOX = (By.XPATH, "//div[@class='searchbox']/input")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='searchbox']/a/img")

    def click_on_login_button(self):
        self.web_driver.get_present_element(self.driver, MainPage.LOGIN_BUTTON).click()

    def find_a_game_by_name(self, game_name):
        self.web_driver.get_present_element(self.driver, MainPage.SEARCH_INPUT_BOX).send_keys(game_name)
        self.web_driver.get_present_element(self.driver, MainPage.SEARCH_BUTTON).click()

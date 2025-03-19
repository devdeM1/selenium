from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from herokuapp.pages.base_page import BasePage


class ContexMenuPage(BasePage):
    CONTEX_MENU = (By.XPATH, "//div[@oncontextmenu='displayMessage()']")
    url = "https://the-internet.herokuapp.com/context_menu"

    def open(self):
        self.driver.get(self.url)

    def right_click_context_menu(self):
        context_menu_element = self.web_driver.get_present_element(self.driver, ContexMenuPage.CONTEX_MENU)
        actions = ActionChains(self.driver)
        actions.context_click(context_menu_element).perform()
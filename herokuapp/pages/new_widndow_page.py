from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class NewWindowPage(BasePage):
    TEXT_PAGE = (By.XPATH, "//div[@class='example']/h3")

    def get_new_window_text(self):
        return self.web_driver.get_present_element(self.driver, self.TEXT_PAGE).text

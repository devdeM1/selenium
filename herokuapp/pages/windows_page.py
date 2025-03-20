from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class WindowsPage(BasePage):
    HREF_NEW_WINDOW = (By.XPATH, "//div[@class='example']/a")
    url = "https://the-internet.herokuapp.com/windows"

    def open(self):
        self.driver.get(self.url)

    def click_on_href_new_window(self):
        self.web_driver.get_present_element(self.driver, self.HREF_NEW_WINDOW).click()


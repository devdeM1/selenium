from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    PARAGRAPHS = (By.XPATH, "//div[@class='jscroll-inner']//div")
    url = "https://the-internet.herokuapp.com/infinite_scroll"

    def open(self):
        self.driver.get(self.url)

    def get_paragraph_count(self):
        elements = self.web_driver.get_present_elements(self.driver, self.PARAGRAPHS)
        return len(elements)

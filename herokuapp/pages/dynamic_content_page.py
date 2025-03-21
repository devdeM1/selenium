from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class DynamicContentPage(BasePage):
    HREF = (By.XPATH, "//a[contains(@href, 'github.com/tourdedave')]")
    USER_IMAGES = (By.XPATH, "//div[@class='example']//img")
    url = "https://the-internet.herokuapp.com/dynamic_content"

    def open(self):
        self.driver.get(self.url)

    def get_user_images(self):
        elements = self.web_driver.get_present_elements(self.driver, self.USER_IMAGES)
        return [element.get_attribute('src') for element in elements]

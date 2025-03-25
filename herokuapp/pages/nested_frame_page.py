from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class NestedFramePage(BasePage):
    PARENT_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    CHILD_FRAME = (By.XPATH, "//iframe")
    TEXT_IN_PARENT_FRAME = (By.XPATH, "//body[text()='Parent frame']")
    TEXT_IN_CHILD_FRAME = (By.XPATH, "//p[text()='Child Iframe']")
    URL = "https://demoqa.com/nestedframes"

    def open(self):
        self.driver.get(self.URL)

    def get_text_from_child_frame(self):
        self.switch_to_frame(self.PARENT_FRAME)
        text = self.get_text_from_frame(self.CHILD_FRAME, self.TEXT_IN_CHILD_FRAME)
        self.driver.switch_to.parent_frame()
        return text
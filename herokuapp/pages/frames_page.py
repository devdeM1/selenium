from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class FramesPage(BasePage):
    URL = "https://demoqa.com/frames"
    BIG_FRAME = (By.XPATH, "//iframe[@id='frame1']")
    SMALL_FRAME = (By.XPATH, "//iframe[@id='frame2']")
    TEXT_FRAME = (By.XPATH, "//h1")
    NESTED_FRAMES_LINK = (By.XPATH, "//div[@class='element-group'][3]//li[4]")

    def open(self):
        self.driver.get(self.URL)

    def click_nested_frames_link(self):
        self.scroll_to_element(self.NESTED_FRAMES_LINK)
        self.web_driver.get_present_element(self.driver, self.NESTED_FRAMES_LINK).click()

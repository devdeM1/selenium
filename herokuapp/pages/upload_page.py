from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class UploadPage(BasePage):
    FILE_NAME_ON_DRAG_DROP = (By.XPATH, "//div[contains(@class,'success-mark')]//div[@class='dz-filename']/span")
    TICK_SYMBOL = (By.XPATH, "//div[contains(@class,'success-mark')]//div[@class='dz-success-mark']/span")
    DRAG_DROP_AREA = (By.XPATH, "//div[@id='drag-drop-upload']")
    INPUT_FOR_DRAG_DROP_AREA = (By.XPATH, "//input[@class='dz-hidden-input']")
    INPUT_BUTTON = (By.XPATH, "//div[@class='example']//input[@id='file-upload']")
    UPLOAD_BUTTON = (By.XPATH, "//div[@class='example']//input[@id='file-submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='example']/h3")
    FILE_NAME = (By.XPATH, "//div[@class='example']/div")

    URL = "https://the-internet.herokuapp.com/upload"

    def open(self):
        self.driver.get(self.URL)

    def upload_file(self, file_path):
        self.web_driver.get_present_element(self.driver, self.INPUT_BUTTON).send_keys(file_path)

    def submit_upload(self):
        self.web_driver.get_present_element(self.driver, self.UPLOAD_BUTTON).click()

    def is_file_name_displayed(self, file_name):
        return self.web_driver.get_present_element(self.driver, self.FILE_NAME).text == file_name

    def click_on_drag_drop_area(self):
        self.web_driver.get_present_element(self.driver, self.DRAG_DROP_AREA).click()

    def is_file_name_displayed_on_drag_drop_area(self, file_name):
        return self.web_driver.get_present_element(self.driver, self.FILE_NAME_ON_DRAG_DROP).text == file_name

    def is_tick_symbol_displayed(self):
        try:
            return self.web_driver.get_present_element(self.driver, self.TICK_SYMBOL).is_displayed()
        except Exception:
            return False

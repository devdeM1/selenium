from selenium.webdriver.common.by import By

from herokuapp.pages.base_page import BasePage


class UploadPage(BasePage):
    INPUT_BUTTON = (By.XPATH, "//div[@class='example']//input[@id='file-upload']")
    UPLOAD_BUTTON = (By.XPATH, "//div[@class='example']//input[@id='file-submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='example']/h3")
    FILE_NAME = (By.XPATH, "//div[@class='example']/div")

    URL = "https://the-internet.herokuapp.com/upload"

    def open(self):
        self.driver.get(self.URL)

    def upload_file(self, file_path):
        input_element = self.web_driver.get_present_element(self.driver, self.INPUT_BUTTON)
        input_element.send_keys(file_path)

    def submit_upload(self):
        self.web_driver.get_present_element(self.driver, self.UPLOAD_BUTTON).click()

    def is_file_name_displayed(self, file_name):
        return self.web_driver.get_present_element(self.driver, self.FILE_NAME).text == file_name

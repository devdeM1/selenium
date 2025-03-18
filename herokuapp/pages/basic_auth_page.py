from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://the-internet.herokuapp.com/basic_auth"

    def open(self):
        self.driver.get(self.url)

    def authorize(self, username, password):
        url = "http://{}:{}@the-internet.herokuapp.com/basic_auth".format(username, password)
        self.driver.get(url)

    def is_auth_successful(self):
        try:
            wait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//p[contains(text(), 'Congratulations! You must have the proper credentials')]"))
            )
            return True
        except TimeoutException:
            return False

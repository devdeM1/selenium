from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.XPATH, "//div[@data-featuretarget='login']//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    def fill_all_fields_and_click_submit(self, login, password):
        self.web_driver.get_visible_element(LoginPage.LOGIN).send_keys(login)
        self.web_driver.get_visible_element(LoginPage.PASSWORD).send_keys(password)
        self.web_driver.get_visible_element(LoginPage.SUBMIT).click()

from selenium.webdriver.common.by import By

from steam.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.XPATH, "//div[@data-featuretarget='login']//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    DISABLED_SUBMIT = (By.XPATH, "//button[@type='submit' and @disabled]")
    LABEL_UNDER_SUBMIT = (By.XPATH, "//button[@type='submit' and @disabled]/div")

    def fill_all_fields_and_click_submit(self, login, password):
        self.web_driver.get_present_element(self.driver, LoginPage.LOGIN).send_keys(login)
        self.web_driver.get_present_element(self.driver, LoginPage.PASSWORD).send_keys(password)
        self.web_driver.get_present_element(self.driver, LoginPage.SUBMIT).click()

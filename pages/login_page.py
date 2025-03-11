from selenium.webdriver.common.by import By

class LoginPage:
    LOGIN = (By.XPATH, "//div[@data-featuretarget='login']//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    @staticmethod
    def fill_all_fields_and_click_submit(web_driver, login, password):
        web_driver.get_visible_element(LoginPage.LOGIN).send_keys(login)
        web_driver.get_visible_element(LoginPage.PASSWORD).send_keys(password)
        web_driver.get_visible_element(LoginPage.SUBMIT).click()

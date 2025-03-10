from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN = (By.XPATH, "//div[@data-featuretarget='login']//input[@type='text']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

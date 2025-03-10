from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[@class='global_action_link' and contains(@href, 'login')]")
    TITLE = (By.XPATH, "//title[contains(text(), 'Welcome to Steam')]")
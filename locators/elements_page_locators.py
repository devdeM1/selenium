from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    LOGIN = (By.XPATH, "//input[@class='_2GBWeup5cttgbTw8FM3tfx' and @type='text']")
    PASSWORD = (By.XPATH, "//input[@class='_2GBWeup5cttgbTw8FM3tfx' and @type='password']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

class ButtonLoginLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[@class='global_action_link']")

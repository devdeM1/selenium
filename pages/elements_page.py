from locators.elements_page_locators import TextBoxPageLocators, ButtonLoginLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.LOGIN).send_keys('makd1232255')
        self.element_is_visible(self.locators.PASSWORD).send_keys('11111111')
        self.element_is_visible(self.locators.SUBMIT).click()


class ButtonLogin(BasePage):
    locators = ButtonLoginLocators()

    def click_on_button(self):
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()

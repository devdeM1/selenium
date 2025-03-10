from faker import Faker

from conftest import browser
from pages.login_page import LoginPage
from pages.main_page import MainPage
from web_driver import WebDriver


class TestLogin:
    MAIN_URL = 'https://store.steampowered.com'

    def setup_method(self, browser):
        self.fake = Faker()

    def test_login_on_main_page(self, browser):
        web_driver = WebDriver(browser, self.MAIN_URL)
        main_page = MainPage()
        web_driver.open()
        assert web_driver.page_is_successfully_open(main_page.locators.TITLE), 'The page is not opened correctly'
        main_page.click_on_login_button(web_driver)
        login_page = LoginPage()
        assert web_driver.page_is_successfully_open(login_page.locators.PASSWORD), 'The page is not opened correctly'
        user_name = self.fake.user_name()
        password = self.fake.password()
        login_page.fill_all_fields_and_click_submit(web_driver, user_name, password)

from faker import Faker

from conftest import driver
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLogin:
    MAIN_URL = 'https://store.steampowered.com'

    def setup_method(self):
        self.fake = Faker()

    def test_login_on_main_page(self, driver):
        main_page = MainPage(driver, self.MAIN_URL)
        main_page.open()
        assert main_page.page_is_successfully_open(main_page.locators.TITLE), 'The page is not opened correctly'
        main_page.click_on_login_button()
        login_page = LoginPage(driver, driver.current_url)
        assert login_page.page_is_successfully_open(login_page.locators.PASSWORD), 'The page is not opened correctly'
        user_name = self.fake.user_name()
        password = self.fake.password()
        login_page.fill_all_fields_and_click_submit(user_name, password)

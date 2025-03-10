<<<<<<< HEAD
import time

from conftest import driver
from pages.elements_page import TextBoxPage, ButtonLogin


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, 'https://store.steampowered.com/login/?redir=%3Fsnr%3D1_4_4__global-responsive-menu&redir_ssl=1&snr=1_4_4__global-header')
    text_box_page.open()
    text_box_page.fill_all_fields()
    time.sleep(5)

def test_button_login(driver):
    main_page = ButtonLogin(driver, 'https://store.steampowered.com')
    main_page.open()
    main_page.click_on_button()
    time.sleep(5)

=======
from faker import Faker
from faker.contrib.pytest.plugin import faker

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
        assert main_page.page_is_successfully_open(), 'The page is not opened correctly'
        main_page.click_on_login_button()
        login_page = LoginPage(driver, driver.current_url)
        assert login_page.page_is_successfully_open(), 'The page is not opened correctly'
        user_name = self.fake.user_name()
        password = self.fake.password()
        login_page.fill_all_fields_and_click_submit(user_name, password)
>>>>>>> origin/dev

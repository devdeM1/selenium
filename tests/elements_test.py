import pytest
from faker import Faker

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from conftest import driver


class TestLogin:

    def setup_method(self):
        self.fake = Faker()

    def test_login_on_main_page(self, driver):
        main_page = MainPage()
        assert main_page.page_is_successfully_open(driver, main_page.LOGIN_BUTTON), 'The page is not opened correctly'
        main_page.click_on_login_button(driver)
        login_page = LoginPage()
        assert login_page.page_is_successfully_open(driver, login_page.PASSWORD), 'The page is not opened correctly'
        user_name = self.fake.user_name()
        password = self.fake.password()
        login_page.fill_all_fields_and_click_submit(driver, user_name, password)

    @pytest.mark.parametrize('game_name, count', [
        ('The Witcher', 10),
        ('Fallout', 20)
    ])
    def test_take_games_list(self, driver, game_name, count):
        main_page = MainPage()
        assert main_page.page_is_successfully_open(driver,
                                                   main_page.SEARCH_INPUT_BOX), 'The page is not opened correctly'
        main_page.find_a_game_by_name(driver, game_name)
        search_page = SearchPage()
        assert search_page.page_is_successfully_open(driver, search_page.DROPDOWN_BOX_SORT_BY), \
            'The page is not opened correctly'
        initial_prices = search_page.take_prices_of_games(driver, count)
        search_page.click_on_drop_box_sort_by(driver)
        search_page.sort_by_price_desc(driver)
        search_page.wait_update_data(driver, initial_prices, search_page, count)
        prices = search_page.take_prices_of_games(driver, count)
        assert prices == sorted(prices, reverse=True), \
            'Sorting prices in descending order does not work correctly'

import pytest
from faker import Faker

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from conftest import driver
from utils import Utils


class TestLogin:

    def setup_method(self):
        self.fake = Faker()

    def test_login_on_main_page(self, driver):
        main_page = MainPage(driver)
        assert main_page.page_is_successfully_open(main_page.LOGIN_BUTTON), 'The page is not opened correctly'
        main_page.click_on_login_button()
        login_page = LoginPage(driver)
        assert login_page.page_is_successfully_open(login_page.PASSWORD), 'The page is not opened correctly'
        user_name = self.fake.user_name()
        password = self.fake.password()
        login_page.fill_all_fields_and_click_submit(user_name, password)
        assert login_page.page_is_successfully_open(login_page.DISABLED_SUBMIT),\
            'Input verification has not started'
        assert login_page.page_is_successfully_open(login_page.LABEL_UNDER_SUBMIT),\
            'Input verification has not started'

    @pytest.mark.parametrize('game_name, count', [
        ('The Witcher', 10),
        ('Fallout', 20)
    ])
    def test_take_games_list(self, driver, game_name, count):
        main_page = MainPage(driver)
        assert main_page.page_is_successfully_open(main_page.SEARCH_INPUT_BOX), 'The page is not opened correctly'
        main_page.find_a_game_by_name(game_name)
        search_page = SearchPage(driver)
        assert search_page.page_is_successfully_open(search_page.DROPDOWN_BOX_SORT_BY), \
            'The page is not opened correctly'
        initial_prices = search_page.take_prices_of_games(count)
        search_page.click_on_drop_box_sort_by()
        search_page.sort_by_price_desc()
        search_page.wait_update_data(initial_prices, count)
        prices = search_page.take_prices_of_games(count)
        prices = Utils.extract_prices(prices)
        assert prices == sorted(prices, reverse=True), \
            'Sorting prices in descending order does not work correctly'

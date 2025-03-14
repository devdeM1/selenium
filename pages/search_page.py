from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    DROPDOWN_BOX_SORT_BY = (By.XPATH, "//div[contains(@id, 'sort_by')]/a[@class='trigger']")
    DROPDOWN_SORT_DESCENDING_PRICE = (By.XPATH, "//div[contains(@class, 'dropcontainer')]//a[@id='Price_DESC']")
    PRICES_OF_GAMES = (By.XPATH, "//div[contains(@class, 'search_price') or contains(@class, 'discount_final_price')]")

    def click_on_drop_box_sort_by(self):
        self.web_driver.get_present_element(self.driver, SearchPage.DROPDOWN_BOX_SORT_BY).click()

    def sort_by_price_desc(self):
        self.web_driver.get_present_element(self.driver, SearchPage.DROPDOWN_SORT_DESCENDING_PRICE).click()

    def take_prices_of_games(self, count_games):
        prices_of_games = self.web_driver.get_present_elements(self.driver, SearchPage.PRICES_OF_GAMES)
        prices = [price.text for price in prices_of_games[:count_games]]
        return prices

    def wait_update_data(self, initial_prices, count):
        self.web_driver.wait_update_data(self.driver, initial_prices, self, count)

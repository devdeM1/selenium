from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from steam.conftest import driver


class WebDriverUtils:
    DEFAULT_TIMEOUT = 5

    @staticmethod
    def get_present_element(driver, locator, timeout=DEFAULT_TIMEOUT):
        return wait(driver, timeout).until(EC.presence_of_element_located(locator))

    @staticmethod
    def get_present_elements(driver, locator, timeout=DEFAULT_TIMEOUT):
        return wait(driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @staticmethod
    def wait_update_data(driver, initial_prices, search_page, count, timeout=DEFAULT_TIMEOUT):
        wait(driver, timeout).until(lambda d: initial_prices != search_page.take_prices_of_games(count))

    @staticmethod
    def wait_for_alert(driver, timeout=DEFAULT_TIMEOUT):
        return wait(driver, timeout).until(EC.alert_is_present())

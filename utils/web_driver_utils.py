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

    @staticmethod
    def switch_to_new_window(driver, timeout=DEFAULT_TIMEOUT):
        original_window = driver.current_window_handle
        wait(driver, timeout).until(lambda d: len(d.window_handles) > 1)
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

    @staticmethod
    def switch_to_first_window(driver):
        if len(driver.window_handles) > 0:
            driver.switch_to.window(driver.window_handles[0])
        else:
            raise Exception("No windows available to switch to.")

    @staticmethod
    def close_window_by_title(driver, title):
        for window_handle in driver.window_handles:
            driver.switch_to.window(window_handle)
            if driver.title == title:
                driver.close()
                if driver.window_handles:
                    driver.switch_to.window(driver.window_handles[0])
                break
        else:
            raise Exception("Window with title '{}' not found.".format(title))

    @staticmethod
    def get_window_count(driver):
        return len(driver.window_handles)
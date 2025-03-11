import pytest

from web_driver import WebDriver


@pytest.fixture(scope="function")
def driver():
    web_driver = WebDriver()
    web_driver.open('https://store.steampowered.com')
    yield
    web_driver.quit()

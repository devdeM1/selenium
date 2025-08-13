import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", params=["en", "ru"])
def driver(request):
    lang = request.param
    chrome_options = Options()
    chrome_options.add_argument(f"--lang={lang}")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://store.steampowered.com')
    yield driver
    driver.quit()

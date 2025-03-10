import pytest
from selenium import webdriver
<<<<<<< HEAD
=======
from selenium.webdriver.chrome.options import Options
>>>>>>> origin/dev


@pytest.fixture(scope="function")
def driver():
<<<<<<< HEAD
    driver = webdriver.Chrome()
=======
    chrome_options = Options()
    chrome_options.add_argument("--lang=en")
    driver = webdriver.Chrome(options=chrome_options)
>>>>>>> origin/dev
    driver.maximize_window()
    yield driver
    driver.quit()

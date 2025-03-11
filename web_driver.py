from selenium.webdriver.common.devtools.v85.network import WebSocketRequest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class WebDriver(metaclass=Singleton):
    DEFAULT_TIMEOUT = 5
    __driver = None

    def __init__(self):
        if not self.__driver:
            chrome_options = Options()
            chrome_options.add_argument("--lang=en")
            chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=chrome_options)
            self.__driver = driver

    def open(self, url):
        self.__driver.get(url)

    def get_visible_element(self, locator, timeout=DEFAULT_TIMEOUT):
        self.scroll_to_element(self.get_present_element(locator))
        return wait(self.__driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_present_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return wait(self.__driver, timeout).until(EC.presence_of_element_located(locator))

    def quit(self):
        if self.__driver:
            self.__driver.quit()

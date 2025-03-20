from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from herokuapp.pages.base_page import BasePage


class HoversPage(BasePage):
    USER_IMAGES = (By.XPATH, "//div[@class='example']/div/img")
    USER_NAMES = (By.XPATH, "//div[@class='example']/div/div/h5")
    USER_PROFILE_LINKS = (By.XPATH, "//div[@class='example']/div/div/a")

    TITLE_PROFILE = (By.XPATH, "//h1[text()='Not Found']")
    url = "https://the-internet.herokuapp.com/hovers"

    def open(self):
        self.driver.get(self.url)

    def hover_on_user(self, index):
        user_images = self.web_driver.get_present_elements(self.driver, self.USER_IMAGES)
        action = ActionChains(self.driver)
        action.move_to_element(user_images[index]).perform()

    def get_user_name(self, index):
        user_names = self.web_driver.get_present_elements(self.driver, self.USER_NAMES)
        return user_names[index].text

    def click_user_profile_link(self, index):
        user_profile_links = self.web_driver.get_present_elements(self.driver, self.USER_PROFILE_LINKS)
        user_profile_links[index].click()

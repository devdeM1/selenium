from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from herokuapp.pages.base_page import BasePage


class HorizontalSliderPage(BasePage):
    HORIZONTAL_SLIDER = (By.XPATH, "//div[@class='sliderContainer']/input")
    SLIDER_VALUE_DISPLAY = (By.XPATH, "//div[@class='sliderContainer']/span")
    url = "https://the-internet.herokuapp.com/horizontal_slider"

    def open(self):
        self.driver.get(self.url)

    def get_slider_properties(self):
        slider = self.web_driver.get_present_element(self.driver, self.HORIZONTAL_SLIDER)
        min_value = float(slider.get_attribute("min"))
        max_value = float(slider.get_attribute("max"))
        step = float(slider.get_attribute("step"))
        return min_value, max_value, step

    def set_slider_value(self, value):
        min_value, max_value, step = self.get_slider_properties()
        if value < min_value or value > max_value:
            raise ValueError(f"The value must be in the range from {min_value} to {max_value}")
        slider = self.web_driver.get_present_element(self.driver, self.HORIZONTAL_SLIDER)
        self.driver.execute_script("arguments[0].focus();", slider)
        step_count = int((value - min_value) / step)
        actions = ActionChains(self.driver)
        for _ in range(step_count):
            actions.send_keys(Keys.ARROW_RIGHT)
            actions.perform()

    def get_slider_value(self):
        return float(self.web_driver.get_present_element(self.driver, self.SLIDER_VALUE_DISPLAY).text)

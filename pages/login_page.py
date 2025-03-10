from locators.login_page_locators import LOGIN, PASSWORD, SUBMIT


class LoginPage:

    @staticmethod
    def fill_all_fields_and_click_submit(web_driver, login, password):
        web_driver.get_visible_element(LOGIN).send_keys(login)
        web_driver.get_visible_element(PASSWORD).send_keys(password)
        web_driver.get_visible_element(SUBMIT).click()

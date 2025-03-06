import time

from conftest import driver
from pages.elements_page import TextBoxPage, ButtonLogin


def test_text_box(driver):
    text_box_page = TextBoxPage(driver, 'https://store.steampowered.com/login/?redir=%3Fsnr%3D1_4_4__global-responsive-menu&redir_ssl=1&snr=1_4_4__global-header')
    text_box_page.open()
    text_box_page.fill_all_fields()
    time.sleep(5)

def test_button_login(driver):
    main_page = ButtonLogin(driver, 'https://store.steampowered.com')
    main_page.open()
    main_page.click_on_button()
    time.sleep(5)


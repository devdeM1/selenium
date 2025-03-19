from faker import Faker

from herokuapp.pages.basic_auth_page import BasicAuthPage
from herokuapp.conftest import driver
from herokuapp.pages.contex_menu_page import ContexMenuPage
from herokuapp.pages.js_alerst_page import JavaScriptAlertsPage


def test_basic_auth(driver):
    auth_page = BasicAuthPage(driver)
    auth_page.open()
    auth_page.authorize('admin', 'admin')
    assert auth_page.is_auth_successful(), "Authorization failed."


def test_javascript_alert(driver):
    js_alerts_page = JavaScriptAlertsPage(driver)
    js_alerts_page.open()
    assert js_alerts_page.page_is_successfully_open(js_alerts_page.BUTTON_JS_ALERT), "The page is not opened correctly"
    js_alerts_page.click_button_js_alert()
    alert_text = js_alerts_page.get_and_accept_simple_alert()
    assert alert_text == "I am a JS Alert", "Unexpected alert text!"
    assert js_alerts_page.get_result_output() == "You successfully clicked an alert", \
        "Something is wrong with the alert"
    js_alerts_page.click_button_js_confirm()
    alert_text = js_alerts_page.get_and_accept_confirmation_alert()
    assert alert_text == "I am a JS Confirm", "Unexpected alert text!"
    assert js_alerts_page.get_result_output() == "You clicked: Ok", "Something is wrong with the alert"
    js_alerts_page.click_button_js_prompt()
    random_text = Faker().sentence()
    alert_text = js_alerts_page.get_and_accept_prompt_alert(random_text)
    assert alert_text == "I am a JS prompt", "Unexpected alert text!"
    assert js_alerts_page.get_result_output() == f"You entered: {random_text}", \
        "Prompt input was not processed correctly"


def test_contex_menu_page(driver):
    context_menu_page = ContexMenuPage(driver)
    context_menu_page.open()
    assert context_menu_page.page_is_successfully_open(
        context_menu_page.CONTEX_MENU), "The page is not opened correctly"
    context_menu_page.right_click_context_menu()
    alert_text = context_menu_page.get_and_accept_simple_alert()
    assert alert_text == "You selected a context menu", "Unexpected alert text!"

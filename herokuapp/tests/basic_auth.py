from faker import Faker

from herokuapp.pages.basic_auth_page import BasicAuthPage
from herokuapp.conftest import driver
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
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "I am a JS Alert", "Unexpected alert text!"
    alert.accept()
    assert js_alerts_page.get_result_output() == "You successfully clicked an alert", \
        "Something is wrong with the alert"
    js_alerts_page.click_button_js_confirm()
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "I am a JS Confirm", "Unexpected alert text!"
    alert.accept()
    assert js_alerts_page.get_result_output() == "You clicked: Ok", "Something is wrong with the alert"
    js_alerts_page.click_button_js_prompt()
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "I am a JS prompt", "Unexpected alert text!"
    fake = Faker()
    random_text = fake.sentence()
    alert.send_keys(random_text)
    alert.accept()
    assert js_alerts_page.get_result_output() == f"You entered: {random_text}", \
        "Prompt input was not processed correctly"

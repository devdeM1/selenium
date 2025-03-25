import time
import pyautogui
import pytest

from faker import Faker

from herokuapp.pages.basic_auth_page import BasicAuthPage
from herokuapp.conftest import driver
from herokuapp.pages.contex_menu_page import ContexMenuPage
from herokuapp.pages.dynamic_content_page import DynamicContentPage
from herokuapp.pages.frames_page import FramesPage
from herokuapp.pages.horizontal_slider_page import HorizontalSliderPage
from herokuapp.pages.hovers_page import HoversPage
from herokuapp.pages.infinite_scroll_page import InfiniteScrollPage
from herokuapp.pages.js_alerst_page import JavaScriptAlertsPage
from herokuapp.pages.nested_frame_page import NestedFramePage
from herokuapp.pages.new_widndow_page import NewWindowPage
from herokuapp.pages.upload_page import UploadPage
from herokuapp.pages.windows_page import WindowsPage
from utils.images_utils import find_matching_images
from utils.path_utils import get_file_path, file_exists
from utils.random_utils import get_random_slider_value


def test_basic_auth(driver):
    auth_page = BasicAuthPage(driver)
    auth_page.open()
    auth_page.authorize('admin', 'admin')
    assert auth_page.is_auth_successful(), "Authorization failed."


def test_alert(driver):
    js_alerts_page = JavaScriptAlertsPage(driver)
    js_alerts_page.open()
    assert js_alerts_page.page_is_successfully_open(js_alerts_page.BUTTON_JS_ALERT), "The page is not opened correctly"

    js_alerts_page.click_button_js_alert()
    assert js_alerts_page.get_alert_text() == "I am a JS Alert", "Unexpected alert text!"
    js_alerts_page.accept_alert()
    assert js_alerts_page.verify_alert_closed(), "The alert was not closed successfully!"
    assert js_alerts_page.get_result_output() == "You successfully clicked an alert", \
        "Something is wrong with the alert"

    js_alerts_page.click_button_js_confirm()
    assert js_alerts_page.get_alert_text() == "I am a JS Confirm", "Unexpected alert text!"
    js_alerts_page.accept_alert()
    assert js_alerts_page.verify_alert_closed(), "The alert was not closed successfully!"
    assert js_alerts_page.get_result_output() == "You clicked: Ok", "Something is wrong with the alert"

    js_alerts_page.click_button_js_prompt()
    assert js_alerts_page.get_alert_text() == "I am a JS prompt", "Unexpected alert text!"
    random_text = Faker().sentence()
    js_alerts_page.input_text_to_prompt(random_text)
    js_alerts_page.accept_alert()
    assert js_alerts_page.get_result_output() == f"You entered: {random_text}", \
        "Prompt input was not processed correctly"


def test_alert_with_js(driver):
    js_alerts_page = JavaScriptAlertsPage(driver)
    js_alerts_page.open()
    assert js_alerts_page.page_is_successfully_open(js_alerts_page.BUTTON_JS_ALERT), "The page is not opened correctly"
    js_alerts_page.trigger_js_alert()
    assert js_alerts_page.get_alert_text() == "I am a JS Alert", "Unexpected alert text!"
    js_alerts_page.accept_alert()
    assert js_alerts_page.verify_alert_closed(), "The alert was not closed successfully!"
    assert js_alerts_page.get_result_output() == "You successfully clicked an alert", \
        "Something is wrong with the alert"

    js_alerts_page.trigger_js_confirm()
    assert js_alerts_page.get_alert_text() == "I am a JS Confirm", "Unexpected alert text!"
    js_alerts_page.accept_alert()
    assert js_alerts_page.verify_alert_closed(), "The alert was not closed successfully!"
    assert js_alerts_page.get_result_output() == "You clicked: Ok", "Something is wrong with the alert"

    js_alerts_page.trigger_js_prompt()
    assert js_alerts_page.get_alert_text() == "I am a JS prompt", "Unexpected alert text!"
    random_text = Faker().sentence()
    js_alerts_page.input_text_to_prompt(random_text)
    js_alerts_page.accept_alert()
    assert js_alerts_page.get_result_output() == f"You entered: {random_text}", \
        "Prompt input was not processed correctly"


def test_contex_menu_page(driver):
    context_menu_page = ContexMenuPage(driver)
    context_menu_page.open()
    assert context_menu_page.page_is_successfully_open(
        context_menu_page.CONTEX_MENU), "The page is not opened correctly"

    context_menu_page.right_click_context_menu()
    alert_text = context_menu_page.get_alert_text()
    assert alert_text == "You selected a context menu", "Unexpected alert text!"
    context_menu_page.accept_alert()
    assert context_menu_page.verify_alert_closed(), "The context menu alert was not closed successfully!"


def test_horizontal_slider_page(driver):
    horizontal_slider_page = HorizontalSliderPage(driver)
    horizontal_slider_page.open()
    assert horizontal_slider_page.page_is_successfully_open(horizontal_slider_page.HORIZONTAL_SLIDER), \
        "The page is not opened correctly"
    min_value, max_value, step = horizontal_slider_page.get_slider_properties()
    random_value = get_random_slider_value(min_value, max_value, step)
    horizontal_slider_page.set_slider_value(random_value)
    displayed_value = horizontal_slider_page.get_slider_value()
    assert displayed_value == random_value, "The slider value does not match the set value"


def test_hovers_page(driver):
    hovers_page = HoversPage(driver)
    hovers_page.open()
    assert hovers_page.page_is_successfully_open(hovers_page.USER_IMAGES), "The page is not opened correctly"
    user_count = 3
    for i in range(user_count):
        hovers_page.hover_on_user(i)
        user_name = hovers_page.get_user_name(i)
        assert user_name == f"name: user{i + 1}", f"Expected 'name: user{i + 1}', but got '{user_name}'"
        hovers_page.click_user_profile_link(i)
        assert hovers_page.page_is_successfully_open(hovers_page.TITLE_PROFILE), "The page is not opened correctly"
        hovers_page.go_to_previous_page()
        assert hovers_page.page_is_successfully_open(hovers_page.USER_IMAGES), "Returning to the previous page failed"


def test_windows_page(driver):
    windows_page = WindowsPage(driver)
    windows_page.open()
    assert windows_page.page_is_successfully_open(windows_page.HREF_NEW_WINDOW), "The page is not opened correctly"

    windows_page.click_on_href_new_window()
    windows_page.switch_to_new_window()
    new_window_page = NewWindowPage(driver)
    assert new_window_page.get_title() == "New Window", "Not correct TITLE of page"
    assert new_window_page.get_new_window_text() == "New Window", "Not correct text on new window page"

    windows_page.switch_to_first_window()
    assert windows_page.page_is_successfully_open(windows_page.HREF_NEW_WINDOW), "The page is not opened correctly"

    windows_page.click_on_href_new_window()
    windows_page.switch_to_new_window()
    assert new_window_page.get_title() == "New Window", "Not correct TITLE of page"
    assert new_window_page.get_new_window_text() == "New Window", "Not correct text on new window page"

    windows_page.switch_to_first_window()
    assert windows_page.page_is_successfully_open(windows_page.HREF_NEW_WINDOW), "The main page is not opened correctly"

    windows_page.close_window_by_title("New Window")
    assert windows_page.get_window_count() == 2, "Expected 2 windows after closing the first new window"
    windows_page.close_window_by_title("New Window")
    assert windows_page.get_window_count() == 1, "Expected 1 window after closing the second new window."


MAX_RELOAD_ATTEMPTS = 10


@pytest.mark.timeout(15)
def test_dynamic_content_page(driver):
    dynamic_content_page = DynamicContentPage(driver)
    dynamic_content_page.open()
    assert dynamic_content_page.page_is_successfully_open(dynamic_content_page.HREF), "The page is not opened correctly"
    found_matching_images = find_matching_images(dynamic_content_page)
    assert found_matching_images, "No matching images found after reloading."


EXPECTED_PARAGRAPH_COUNT = 23


def test_infinite_scroll_page(driver):
    infinite_scroll_page = InfiniteScrollPage(driver)
    infinite_scroll_page.open()
    assert infinite_scroll_page.page_is_successfully_open(infinite_scroll_page.PARAGRAPHS), \
        "The page is not opened correctly"
    infinite_scroll_page.scroll_until_paragraphs_loaded(EXPECTED_PARAGRAPH_COUNT)
    assert infinite_scroll_page.get_paragraph_count() == EXPECTED_PARAGRAPH_COUNT, \
        f"The number of paragraphs should be {EXPECTED_PARAGRAPH_COUNT},\
         but found {infinite_scroll_page.get_paragraph_count()}."


FILE_NAME = "bsuir.png"


def test_file_upload_page_with_send_keys(driver):
    upload_page = UploadPage(driver)
    upload_page.open()
    assert upload_page.page_is_successfully_open(upload_page.UPLOAD_BUTTON), "The page is not opened correctly."
    file_path = get_file_path(FILE_NAME)
    assert file_exists(file_path), f"File not found: {file_path}"
    upload_page.upload_file(file_path)
    upload_page.submit_upload()
    assert upload_page.page_is_successfully_open(upload_page.SUCCESS_MESSAGE), "The file was not uploaded successfully."
    assert upload_page.is_file_name_displayed(
        FILE_NAME), f"The file '{FILE_NAME}' was not displayed on the page."


def test_file_upload_with_dialog_window_write_path(driver):
    upload_page = UploadPage(driver)
    upload_page.open()
    assert upload_page.page_is_successfully_open(upload_page.DRAG_DROP_AREA), "The page is not opened correctly."
    upload_page.click_on_drag_drop_area()
    file_path = get_file_path(FILE_NAME)
    assert file_exists(file_path), f"File not found: {file_path}"
    time.sleep(1)
    pyautogui.write(file_path)
    pyautogui.press('enter')
    assert upload_page.is_tick_symbol_displayed(), "Tick symbol was not displayed after upload."
    assert upload_page.is_file_name_displayed_on_drag_drop_area(
        FILE_NAME), f"The file '{FILE_NAME}' was not displayed on the page."


def test_frames_page(driver):
    frames_page = FramesPage(driver)
    frames_page.open()
    assert frames_page.page_is_successfully_open(frames_page.BIG_FRAME), "The page is not opened correctly."
    assert frames_page.get_text_from_frame(frames_page.BIG_FRAME, frames_page.TEXT_FRAME) == "This is a sample page", \
        "Text in the big frame does not match expected value."
    assert frames_page.get_text_from_frame(frames_page.SMALL_FRAME,

                                           frames_page.TEXT_FRAME) == "This is a sample page", \
        "Text in the small frame does not match expected value."
    frames_page.click_nested_frames_link()
    nested_frame_page = NestedFramePage(driver)
    assert nested_frame_page.page_is_successfully_open(nested_frame_page.PARENT_FRAME), \
        "The page is not opened correctly."
    assert nested_frame_page.get_text_from_frame(nested_frame_page.PARENT_FRAME,
                                                 nested_frame_page.TEXT_IN_PARENT_FRAME) == "Parent frame", \
        "Text in the parent frame does not match expected value."
    assert nested_frame_page.get_text_from_child_frame() == "Child Iframe", \
        "Text in the child frame does not match expected value."

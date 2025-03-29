import time
import pyautogui
import pytest
import allure

from faker import Faker

from herokuapp.pages.basic_auth_page import BasicAuthPage
from herokuapp.tests.conftest import driver
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


@allure.title("Basic Authorization Test")
def test_basic_auth(driver):
    with allure.step("Open login page"):
        auth_page = BasicAuthPage(driver)
        auth_page.open()
    with allure.step("Enter valid credentials (admin/admin)"):
        auth_page.authorize('admin', 'admin')
    with allure.step("Verify user is logged in"):
        assert auth_page.is_auth_successful(), "Login failed"
        allure.attach(
            driver.get_screenshot_as_png(),
            name="post_login_screen",
            attachment_type=allure.attachment_type.PNG
        )

@allure.title("Test JavaScript Alerts functionality. Click with web-element")
@allure.story("JavaScript Interactions")
def test_alert(driver):
    js_alerts_page = JavaScriptAlertsPage(driver)

    with allure.step("Open page"):
        js_alerts_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="initial_state",
            attachment_type=allure.attachment_type.PNG
        )

    try:
        with allure.step("Test JS Alert"):
            js_alerts_page.click_button_js_alert()
            assert js_alerts_page.get_alert_text() == "I am a JS Alert"
            js_alerts_page.accept_alert()

        with allure.step("Test JS Confirm"):
            js_alerts_page.click_button_js_confirm()
            js_alerts_page.accept_alert()

        with allure.step("Test JS Prompt"):
            random_text = Faker().sentence()
            js_alerts_page.click_button_js_prompt()
            js_alerts_page.input_text_to_prompt(random_text)
            js_alerts_page.accept_alert()
            assert js_alerts_page.get_result_output() == f"You entered: {random_text}"

    except AssertionError as e:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="failure",
            attachment_type=allure.attachment_type.PNG
        )
        raise e


@allure.title("Test JavaScript alerts functionality. Click with execute_script()")
@allure.story("JavaScript Interactions")
def test_alert_with_js(driver):
    js_alerts_page = JavaScriptAlertsPage(driver)
    fake = Faker()

    with allure.step("1. Open JavaScript Alerts page"):
        js_alerts_page.open()
        assert js_alerts_page.page_is_successfully_open(js_alerts_page.BUTTON_JS_ALERT), \
            "The page is not opened correctly"
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_loaded",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("2. Test JS Alert"):
        js_alerts_page.trigger_js_alert()
        assert js_alerts_page.get_alert_text() == "I am a JS Alert", "Unexpected alert text!"
        js_alerts_page.accept_alert()
        assert js_alerts_page.verify_alert_closed(), "The alert was not closed successfully!"
        assert js_alerts_page.get_result_output() == "You successfully clicked an alert", \
            "Alert result text mismatch"
        allure.attach(
            js_alerts_page.get_result_output(),
            name="alert_result_text",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("3. Test JS Confirm"):
        js_alerts_page.trigger_js_confirm()
        assert js_alerts_page.get_alert_text() == "1I am a JS Confirm", "Unexpected confirm text!"
        js_alerts_page.accept_alert()
        assert js_alerts_page.verify_alert_closed(), "Confirm was not closed successfully!"
        assert js_alerts_page.get_result_output() == "You clicked: Ok", \
            "Confirm result text mismatch"
        allure.attach(
            driver.get_screenshot_as_png(),
            name="confirm_result",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("4. Test JS Prompt"):
        js_alerts_page.trigger_js_prompt()
        assert js_alerts_page.get_alert_text() == "I am a JS prompt", "Unexpected prompt text!"
        random_text = fake.sentence()
        js_alerts_page.input_text_to_prompt(random_text)
        js_alerts_page.accept_alert()
        result = js_alerts_page.get_result_output()
        assert result == f"You entered: {random_text}", \
            f"Prompt result mismatch. Expected: 'You entered: {random_text}', Actual: '{result}'"
        allure.attach(
            f"Input text: {random_text}\nResult text: {result}",
            name="prompt_details",
            attachment_type=allure.attachment_type.TEXT
        )


@allure.title("Context Menu Test")
@allure.story("Mouse Interactions")
def test_contex_menu_page(driver):
    with allure.step("Open context menu page"):
        context_menu_page = ContexMenuPage(driver)
        context_menu_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert context_menu_page.page_is_successfully_open(
            context_menu_page.CONTEX_MENU), "The page is not opened correctly"

    with allure.step("Right click on context menu area"):
        context_menu_page.right_click_context_menu()
        alert_text = context_menu_page.get_alert_text()
        allure.attach(
            f"Alert text: {alert_text}",
            name="alert_text",
            attachment_type=allure.attachment_type.TEXT
        )
        assert alert_text == "You selected a context menu", "Unexpected alert text!"

    with allure.step("Accept alert"):
        context_menu_page.accept_alert()
        assert context_menu_page.verify_alert_closed(), "The context menu alert was not closed successfully!"


@allure.title("Horizontal Slider Test")
@allure.story("UI Elements")
def test_horizontal_slider_page(driver):
    with allure.step("Open horizontal slider page"):
        horizontal_slider_page = HorizontalSliderPage(driver)
        horizontal_slider_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert horizontal_slider_page.page_is_successfully_open(
            horizontal_slider_page.HORIZONTAL_SLIDER), "The page is not opened correctly"

    with allure.step("Get slider properties"):
        min_value, max_value, step = horizontal_slider_page.get_slider_properties()
        allure.attach(
            f"Min: {min_value}, Max: {max_value}, Step: {step}",
            name="slider_properties",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Set random slider value"):
        random_value = get_random_slider_value(min_value, max_value, step)
        horizontal_slider_page.set_slider_value(random_value)
        displayed_value = horizontal_slider_page.get_slider_value()
        allure.attach(
            f"Set value: {random_value}, Displayed value: {displayed_value}",
            name="slider_values",
            attachment_type=allure.attachment_type.TEXT
        )
        assert displayed_value == random_value, "The slider value does not match the set value"


@allure.title("Hover Test")
@allure.story("Mouse Interactions")
def test_hovers_page(driver):
    with allure.step("Open hovers page"):
        hovers_page = HoversPage(driver)
        hovers_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert hovers_page.page_is_successfully_open(
            hovers_page.USER_IMAGES), "The page is not opened correctly"

    user_count = 3
    for i in range(user_count):
        with allure.step(f"Hover over user {i + 1}"):
            hovers_page.hover_on_user(i)
            user_name = hovers_page.get_user_name(i)
            allure.attach(
                f"User name: {user_name}",
                name=f"user_{i + 1}_name",
                attachment_type=allure.attachment_type.TEXT
            )
            assert user_name == f"name: user{i + 1}", f"Expected 'name: user{i + 1}', but got '{user_name}'"

        with allure.step(f"Click profile link for user {i + 1}"):
            hovers_page.click_user_profile_link(i)
            assert hovers_page.page_is_successfully_open(
                hovers_page.TITLE_PROFILE), "The page is not opened correctly"
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"profile_page_{i + 1}",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step(f"Return to main page from user {i + 1}"):
            hovers_page.go_to_previous_page()
            assert hovers_page.page_is_successfully_open(
                hovers_page.USER_IMAGES), "Returning to the previous page failed"


@allure.title("Window Management Test")
@allure.story("Browser Interactions")
def test_windows_page(driver):
    with allure.step("Open windows page"):
        windows_page = WindowsPage(driver)
        windows_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert windows_page.page_is_successfully_open(
            windows_page.HREF_NEW_WINDOW), "The page is not opened correctly"

    with allure.step("Open first new window"):
        windows_page.click_on_href_new_window()
        windows_page.switch_to_new_window()
        new_window_page = NewWindowPage(driver)
        assert new_window_page.get_title() == "New Window", "Not correct TITLE of page"
        assert new_window_page.get_new_window_text() == "New Window", "Not correct text on new window page"
        allure.attach(
            driver.get_screenshot_as_png(),
            name="first_new_window",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Return to main window"):
        windows_page.switch_to_first_window()
        assert windows_page.page_is_successfully_open(
            windows_page.HREF_NEW_WINDOW), "The page is not opened correctly"

    with allure.step("Open second new window"):
        windows_page.click_on_href_new_window()
        windows_page.switch_to_new_window()
        assert new_window_page.get_title() == "New Window", "Not correct TITLE of page"
        assert new_window_page.get_new_window_text() == "New Window", "Not correct text on new window page"
        allure.attach(
            driver.get_screenshot_as_png(),
            name="second_new_window",
            attachment_type=allure.attachment_type.PNG
        )

    with allure.step("Close windows and verify count"):
        windows_page.switch_to_first_window()
        assert windows_page.page_is_successfully_open(
            windows_page.HREF_NEW_WINDOW), "The main page is not opened correctly"

        windows_page.close_window_by_title("New Window")
        assert windows_page.get_window_count() == 2, "Expected 2 windows after closing the first new window"
        windows_page.close_window_by_title("New Window")
        assert windows_page.get_window_count() == 1, "Expected 1 window after closing the second new window."


@allure.title("Dynamic Content Test")
@allure.story("Content Loading")
@pytest.mark.timeout(15)
def test_dynamic_content_page(driver):
    with allure.step("Open dynamic content page"):
        dynamic_content_page = DynamicContentPage(driver)
        dynamic_content_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert dynamic_content_page.page_is_successfully_open(
            dynamic_content_page.HREF), "The page is not opened correctly"

    with allure.step("Find matching images after reload"):
        found_matching_images = find_matching_images(dynamic_content_page)
        allure.attach(
            f"Matching images found: {found_matching_images}",
            name="matching_images",
            attachment_type=allure.attachment_type.TEXT
        )
        assert found_matching_images, "No matching images found after reloading."


EXPECTED_PARAGRAPH_COUNT = 23

@allure.title("Infinite Scroll Test")
@allure.story("Content Loading")
def test_infinite_scroll_page(driver):
    with allure.step("Open infinite scroll page"):
        infinite_scroll_page = InfiniteScrollPage(driver)
        infinite_scroll_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert infinite_scroll_page.page_is_successfully_open(
            infinite_scroll_page.PARAGRAPHS), "The page is not opened correctly"

    with allure.step(f"Scroll until {EXPECTED_PARAGRAPH_COUNT} paragraphs loaded"):
        infinite_scroll_page.scroll_until_paragraphs_loaded(EXPECTED_PARAGRAPH_COUNT)
        paragraph_count = infinite_scroll_page.get_paragraph_count()
        allure.attach(
            f"Expected: {EXPECTED_PARAGRAPH_COUNT}, Actual: {paragraph_count}",
            name="paragraph_count",
            attachment_type=allure.attachment_type.TEXT
        )
        assert paragraph_count == EXPECTED_PARAGRAPH_COUNT, \
            f"The number of paragraphs should be {EXPECTED_PARAGRAPH_COUNT}, but found {paragraph_count}."

FILE_NAME = "bsuir.png"

@allure.title("File Upload Test (send_keys)")
@allure.story("File Operations")
def test_file_upload_page_with_send_keys(driver):
    with allure.step("Open upload page"):
        upload_page = UploadPage(driver)
        upload_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert upload_page.page_is_successfully_open(
            upload_page.UPLOAD_BUTTON), "The page is not opened correctly."

    with allure.step("Verify test file exists"):
        file_path = get_file_path(FILE_NAME)
        assert file_exists(file_path), f"File not found: {file_path}"
        allure.attach(
            f"File path: {file_path}",
            name="file_path",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Upload file and verify"):
        upload_page.upload_file(file_path)
        upload_page.submit_upload()
        assert upload_page.page_is_successfully_open(
            upload_page.SUCCESS_MESSAGE), "The file was not uploaded successfully."
        assert upload_page.is_file_name_displayed(
            FILE_NAME), f"The file '{FILE_NAME}' was not displayed on the page."
        allure.attach(
            driver.get_screenshot_as_png(),
            name="upload_success",
            attachment_type=allure.attachment_type.PNG
        )


@allure.title("File Upload Test (dialog window)")
@allure.story("File Operations")
def test_file_upload_with_dialog_window_write_path(driver):
    with allure.step("Open upload page"):
        upload_page = UploadPage(driver)
        upload_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert upload_page.page_is_successfully_open(
            upload_page.DRAG_DROP_AREA), "The page is not opened correctly."

    with allure.step("Verify test file exists"):
        file_path = get_file_path(FILE_NAME)
        assert file_exists(file_path), f"File not found: {file_path}"
        allure.attach(
            f"File path: {file_path}",
            name="file_path",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Upload file via dialog window"):
        upload_page.click_on_drag_drop_area()
        time.sleep(1)
        pyautogui.write(file_path)
        pyautogui.press('enter')
        assert upload_page.is_tick_symbol_displayed(), "Tick symbol was not displayed after upload."
        assert upload_page.is_file_name_displayed_on_drag_drop_area(
            FILE_NAME), f"The file '{FILE_NAME}' was not displayed on the page."
        allure.attach(
            driver.get_screenshot_as_png(),
            name="upload_success",
            attachment_type=allure.attachment_type.PNG
        )


@allure.title("Frames Test")
@allure.story("Page Structure")
def test_frames_page(driver):
    with allure.step("Open frames page"):
        frames_page = FramesPage(driver)
        frames_page.open()
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_opened",
            attachment_type=allure.attachment_type.PNG
        )
        assert frames_page.page_is_successfully_open(
            frames_page.BIG_FRAME), "The page is not opened correctly."

    with allure.step("Verify big frame content"):
        big_frame_text = frames_page.get_text_from_frame(
            frames_page.BIG_FRAME, frames_page.TEXT_FRAME)
        allure.attach(
            f"Big frame text: {big_frame_text}",
            name="big_frame_text",
            attachment_type=allure.attachment_type.TEXT
        )
        assert big_frame_text == "This is a sample page", \
            "Text in the big frame does not match expected value."

    with allure.step("Verify small frame content"):
        small_frame_text = frames_page.get_text_from_frame(
            frames_page.SMALL_FRAME, frames_page.TEXT_FRAME)
        allure.attach(
            f"Small frame text: {small_frame_text}",
            name="small_frame_text",
            attachment_type=allure.attachment_type.TEXT
        )
        assert small_frame_text == "This is a sample page", \
            "Text in the small frame does not match expected value."

    with allure.step("Test nested frames"):
        frames_page.click_nested_frames_link()
        nested_frame_page = NestedFramePage(driver)
        assert nested_frame_page.page_is_successfully_open(
            nested_frame_page.PARENT_FRAME), "The page is not opened correctly."

        parent_frame_text = nested_frame_page.get_text_from_frame(
            nested_frame_page.PARENT_FRAME, nested_frame_page.TEXT_IN_PARENT_FRAME)
        allure.attach(
            f"Parent frame text: {parent_frame_text}",
            name="parent_frame_text",
            attachment_type=allure.attachment_type.TEXT
        )
        assert parent_frame_text == "Parent frame", \
            "Text in the parent frame does not match expected value."

        child_frame_text = nested_frame_page.get_text_from_child_frame()
        allure.attach(
            f"Child frame text: {child_frame_text}",
            name="child_frame_text",
            attachment_type=allure.attachment_type.TEXT
        )
        assert child_frame_text == "Child Iframe", \
            "Text in the child frame does not match expected value."
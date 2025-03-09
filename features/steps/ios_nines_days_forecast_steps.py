from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
import time
@given("User open the app")
def step_impl(context):
    assert hasattr(context, 'app'), "context 中缺少 app 属性"

@then('User should see ios_nextwork_access page')
def step_impl(context):
    try:
        context.app.ios_nextwork_access.verify_page_loaded()

    except NoSuchElementException as e:
        print("Failed", e)

@when('User set up ios_nextwork_access page')
def step_impl(context):
    try:
        context.app.ios_nextwork_access.click_wifi_and_data_option()

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see ios_language_setup page')
def step_impl(context):
    try:
        context.app.ios_language_setup.verify_page_loaded()
        print("User is redirected to the Privacy Policy Statements page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User set up ios_language_setup page')
def step_impl(context):
    try:
        context.app.ios_language_setup.click_english_option()

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see ios_location_access page')
def step_impl(context):
    try:
        context.app.ios_location_access.verify_page_loaded()

    except NoSuchElementException as e:
        print("Failed", e)


@when('User set up ios_language_setup page')
def step_impl(context):
    try:
        context.app.ios_location_access.verify_popup_loaded()
        context.app.ios_location_access.click_while_using_the_app_option()

        context.app.ios_location_access.verify_page_loaded()
        context.app.ios_location_access.click_next_btn()

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see ios_notification_access page')
def step_impl(context):
    try:
        context.app.ios_notification_access.verify_popup_loaded()

    except NoSuchElementException as e:
        print("Failed", e)


@when('User set up ios_notification_access page')
def step_impl(context):
    try:
        context.app.ios_notification_access.verify_popup_loaded()
        context.app.ios_notification_access.click_allow_option()
        context.app.ios_notification_access.click_agree_option()
        context.app.ios_notification_access.click_next_btn()

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see ios_loc_based_notification page')
def step_impl(context):
    try:
        context.app.ios_loc_based_notification.verify_page_loaded()

    except NoSuchElementException as e:
        print("Failed", e)


@when('User setup ios_loc_based_notification page')
def step_impl(context):
    try:
        context.app.ios_loc_based_notification.verify_popup_loaded()
        context.app.ios_loc_based_notification.click_always_allow_option()
        context.app.ios_loc_based_notification.click_next_btn()

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see ios_color_theme page')
def step_impl(context):
    try:
        context.app.ios_color_theme.verify_page_loaded()

    except NoSuchElementException as e:
        print("Failed", e)

@when('User set up ios_color_theme page')
def step_impl(context):
    try:
        context.app.ios_color_theme.verify_popup_loaded()
        context.app.ios_color_theme.click_day_theme_color()
        context.app.ios_color_theme.click_night_theme_color()
        context.app.ios_color_theme.click_next_btn()

    except NoSuchElementException as e:
        print("Failed", e)

@then('User should see the Whats new page')
def in_whats_new_page1(context):
    try:
        context.app.ios_whats_new.verify_sub_page1_loaded()
        print("User is redirected to the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the next button in whats new page')
def clicks_next_in_whats_new_page1(context):
    try:
        context.app.ios_whats_new.click_next_btn()
        print("User click next in the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User is redirected to the 2nd sub page of whats new page')
def in_whats_new_page2(context):
    try:
        context.app.ios_whats_new.verify_sub_page2_loaded()
        print("User is redirected to the 2nd sub page of whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the close button in the 2nd sub page of whats new page')
def clicks_next_in_whats_new_page2(context):
    try:
        context.app.ios_whats_new.click_not_show_btn()
        print("User clicks the close button in the 2nd sub page of whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the Home page')
def in_home_page(context):
    try:
        # context.app.ios_home.go()
        context.app.ios_home.verify_page_loaded()
        print("User is redirected to the Home page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the header ham menu bar')
def clicks_menu_bar(context):
    try:
        context.app.ios_home.open_header_ham_menu_btn()
        print("the header ham menu bar is opened")

    except NoSuchElementException as e:
        print("Failed", e)

@then('User should see dropdown options of header ham menu')
def in_home_page(context):
    try:
        # context.app.ios_home.go()
        context.app.ios_home_header_ham_menu.verify_page_loaded()
        print("User should see dropdown options of header ham menu")

    except NoSuchElementException as e:
        print("Failed", e)

@when('User open the Forecast and Warning service and clicks the 9-Day Forecast option')
def scroll_down_menu_bar_and_click_nine_days_forecast(context):
    try:
        context.app.ios_home_header_ham_menu.open_forecast_warning_service_dropdownlist()
        context.app.ios_home_header_ham_menu.select_nine_days_forecast()
        print("User selects the 9 Days Forecast")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the "9-Day Forecast" page')
def in_nine_days_forecast(context):
    try:
        context.app.ios_nine_days_forecast.verify_page_loaded()
        print("User is in the 9 Days Forecast page")
    except NoSuchElementException as e:
        print("Failed", e)

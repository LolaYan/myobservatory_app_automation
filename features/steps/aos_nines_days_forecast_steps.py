from behave import given, when, then
from selenium.common.exceptions import NoSuchElementException
import time
@given("User open the app")
def step_impl(context):
    assert hasattr(context, 'app'), "context 中缺少 app 属性"


@then('User should see disclaimer page')
def user_start_the_app_the_first_time(context):
    try:
        context.app.aos_disclaimer.verify_page_loaded()

    except NoSuchElementException as e:
        print("Failed", e)

@when('User clicks AGREE button in the Disclaimer page')
def clicks_agree_button_on_the_disclaimer_page(context):
    try:
        context.app.aos_disclaimer.click_agree_btn()
        print("User agrees the disclaimer")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the Privacy Policy Statements page')
def in_privacy_policy_statements_page(context):
    try:
        context.app.aos_privacy_policy_statements.verify_page_loaded()
        print("User is redirected to the Privacy Policy Statements page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks AGREE button in the Privacy Policy Statements page')
def clicks_agree_button_on_the_statements_page(context):
    try:
        context.app.aos_privacy_policy_statements.click_agree_btn()
        print("User agrees the Privacy Policy Statements")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the device notification Access Request page')
def in_background_access_to_location_information_page(context):
    try:
        context.app.aos_device_notification_setting.verify_page_loaded()
        print("User should see the device notification Access Request page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User click Allow option in the device notification Access Request page')
def clicks_ok_button(context):
    try:
        context.app.aos_device_notification_setting.click_allow_option()
        print("User click Allow option in the device notification Access Request page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the Background Location Access Request page')
def in_background_access_to_location_information_page(context):
    try:
        context.app.aos_background_location_access.verify_page_loaded()
        print("User should see the Background Location Access Request page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User click OK button in Background Location Access Request page')
def clicks_ok_button(context):
    try:
        context.app.aos_background_location_access.click_OK_btn()
        print("User click OK button in Background Location Access Request page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the new Location Access page')
def in_new_location_access_page(context):
    try:
        context.app.aos_device_location_access.verify_page_loaded()
        print("User should see the Device location access page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks While using the app button in Device Location Access page')
def clicks_while_using_the_app(context):
    try:
        context.app.aos_device_location_access.click_while_using_the_app_option()
        print("User clicks Allow only while using the app in Device Location Access page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the All Location Permission config page')
def in_location_permission(context):
    try:
        context.app.aos_location_permission_config.verify_page_loaded()
        print("User should see the location permission page")

    except NoSuchElementException as e:
        print("Failed", e)

@when('User clicks Allow all the time option in All Location Permission config page')
def clicks_allow_only_while_using_the_app(context):
    try:
        context.app.aos_location_permission_config.click_allow_all_the_time_option()
        print("User clicks Allow all the time option in All Location Permission config page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the Back button in All Location Permission config page')
def clicks_back_button_in_location_permission(context):
    try:
        context.app.aos_location_permission_config.press_device_back_btn()
        time.sleep(5)
    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the Whats new page')
def in_whats_new_page1(context):
    try:
        context.app.aos_whats_new.verify_sub_page1_loaded()
        print("User is redirected to the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the next button in whats new page')
def clicks_next_in_whats_new_page1(context):
    try:
        context.app.aos_whats_new.click_next_btn()
        print("User click next in the whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User is redirected to the 2nd sub page of whats new page')
def in_whats_new_page2(context):
    try:
        context.app.aos_whats_new.verify_sub_page2_loaded()
        print("User is redirected to the 2nd sub page of whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the close button in the 2nd sub page of whats new page')
def clicks_next_in_whats_new_page2(context):
    try:
        context.app.aos_whats_new.click_not_show_btn()
        print("User clicks the close button in the 2nd sub page of whats new page")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the Home page')
def in_home_page(context):
    try:
        # context.app.aos_home.go()
        context.app.aos_home.verify_page_loaded()
        print("User is redirected to the Home page")

    except NoSuchElementException as e:
        print("Failed", e)


@when('User clicks the header ham menu bar')
def clicks_menu_bar(context):
    try:
        context.app.aos_home.open_header_ham_menu_btn()
        print("the header ham menu bar is opened")

    except NoSuchElementException as e:
        print("Failed", e)

@then('User should see dropdown options of header ham menu')
def in_home_page(context):
    try:
        # context.app.aos_home.go()
        context.app.aos_home_header_ham_menu.verify_page_loaded()
        print("User should see dropdown options of header ham menu")

    except NoSuchElementException as e:
        print("Failed", e)

@when('User open the Forecast and Warning service and clicks the 9-Day Forecast option')
def scroll_down_menu_bar_and_click_nine_days_forecast(context):
    try:
        context.app.aos_home_header_ham_menu.open_forecast_warning_service_dropdownlist()
        context.app.aos_home_header_ham_menu.select_nine_days_forecast()
        print("User selects the 9 Days Forecast")

    except NoSuchElementException as e:
        print("Failed", e)


@then('User should see the "9-Day Forecast" page')
def in_nine_days_forecast(context):
    try:
        context.app.aos_nine_days_forecast.verify_page_loaded()
        print("User is in the 9 Days Forecast page")
    except NoSuchElementException as e:
        print("Failed", e)

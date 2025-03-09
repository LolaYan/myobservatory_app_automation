from time import sleep
from pages import Pages
import allure
import pytest

@pytest.mark.android
def test_android_app(pages: Pages):
    ####### Android device Set up  #############  
    # Scenario 1 - disclaimer page
    pages.aos_disclaimer.verify_page_loaded()
    pages.aos_disclaimer.click_agree_btn()

    # Scenario 2 - privacy_policy_statements page
    pages.aos_privacy_policy_statements.verify_page_loaded()
    pages.aos_privacy_policy_statements.click_agree_btn()

    # Scenario 3 - device_notification_setting page
    # In some android version, notification won't pop up
    noti_locator = pages.aos_device_notification_setting.NOTIFICATION_POPUP_TITLE
    noti_element = pages.aos_device_notification_setting.find_element(noti_locator)
    if noti_element :
        pages.aos_device_notification_setting.verify_page_loaded()
        pages.aos_device_notification_setting.click_allow_option()

    # Scenario 4 - background_location_access page
    pages.aos_background_location_access.verify_page_loaded()
    pages.aos_background_location_access.click_OK_btn()

    # Scenario 5 - device_location_access page
    pages.aos_device_location_access.verify_page_loaded()
    pages.aos_device_location_access.click_while_using_the_app_option()

    # Scenario 6 - location_permission_config page
    pages.aos_location_permission_config.verify_page_loaded()
    pages.aos_location_permission_config.click_allow_all_the_time_option()
    # pages.location_permission_config.click_back_btn()
    pages.aos_location_permission_config.press_device_back_btn()
    # Need to wait here for app to save the permission and retriving location info
    sleep(3)

    # Scenario 7 - whats_new page
    # In some android version, whats_new page won't display like android 15
    whats_new_locator = pages.aos_whats_new.NEXT_BUTTON
    whats_new_element = pages.aos_whats_new.find_element(whats_new_locator)
    if whats_new_element :
        pages.aos_whats_new.verify_sub_page1_loaded()
        pages.aos_whats_new.click_next_btn()
        pages.aos_whats_new.verify_sub_page2_loaded()
        pages.aos_whats_new.click_not_show_btn()

    ####### App Features Scenario  #############  
    # Scenario 8 - home page
    pages.aos_home.verify_page_loaded()
    pages.aos_home.open_header_ham_menu_btn()
    pages.aos_home_header_ham_menu.verify_page_loaded()

    # Scenario 8 - home_header_ham_menu page
    pages.aos_home_header_ham_menu.open_forecast_warning_service_dropdownlist()
    sleep(3) # wait 3s for the dropdowm open UI stable before clicking
    pages.aos_home_header_ham_menu.select_nine_days_forecast()

    # Scenario 9 - nine_days_forecast page
    pages.aos_nine_days_forecast.verify_page_loaded()
        
@pytest.mark.ios
def test_android_app(pages: Pages):
    assert True
from time import sleep
from pages import Pages
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    try: 
        noti_element = WebDriverWait(pages.aos_device_notification_setting.driver, 10).until(EC.visibility_of_element_located(noti_locator))
        pages.aos_device_notification_setting.verify_page_loaded()
        pages.aos_device_notification_setting.click_allow_option()
    except Exception as e:  
        print("We could not find the element in 10s, skip related tests and move on with rest test steps.")

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
    try: 
        whats_new_element = WebDriverWait(pages.aos_whats_new.driver, 10).until(EC.visibility_of_element_located(whats_new_locator))
        pages.aos_whats_new.verify_sub_page1_loaded()
        pages.aos_whats_new.click_next_btn()
        pages.aos_whats_new.verify_sub_page2_loaded()
        pages.aos_whats_new.click_not_show_btn()
    except Exception as e:  
        print("We could not find the element in 10s, skip related tests and move on with rest test steps.")
        
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
def test_ios_app(pages: Pages):
    assert True
    ####### IOS device Set up  #############  
    pages.ios_nextwork_access.verify_page_loaded()
    pages.ios_nextwork_access.click_wifi_and_data_option()

    pages.ios_language_setup.verify_page_loaded()
    pages.ios_language_setup.click_english_option()

    pages.ios_location_access.verify_popup_loaded()
    pages.ios_location_access.click_while_using_the_app_option()

    pages.ios_location_access.verify_page_loaded()
    pages.ios_location_access.click_next_btn()

    pages.ios_notification_access.verify_popup_loaded()
    pages.ios_notification_access.click_allow_option()
    pages.ios_notification_access.click_agree_option()
    pages.ios_notification_access.click_next_btn()

    pages.ios_loc_based_notification.verify_popup_loaded()
    pages.ios_loc_based_notification.click_always_allow_option()
    pages.ios_loc_based_notification.click_next_btn()

    pages.ios_color_theme.verify_popup_loaded()
    pages.ios_color_theme.click_day_theme_color()
    pages.ios_color_theme.click_night_theme_color()
    pages.ios_color_theme.click_next_btn()

    pages.ios_finish_setting.click_finish_btn()

    ####### App Features Scenario  #############  
    pages.ios_home.verify_page_loaded()
    pages.ios_home.open_header_ham_menu_btn()
    pages.ios_home_header_ham_menu.verify_page_loaded()

    pages.ios_home_header_ham_menu.open_forecast_warning_service_dropdownlist()
    sleep(3) # wait 3s for the dropdowm open UI stable before clicking
    pages.ios_home_header_ham_menu.select_nine_days_forecast()

    pages.ios_nine_days_forecast.verify_page_loaded()

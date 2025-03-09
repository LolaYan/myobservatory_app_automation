from pages.AOS_home_page import HomePage
from hamcrest import assert_that


class iOSHomePage(HomePage):
    # iOS elements locator
    # header eles
    HEADER_HAM_BTN = ('xpath', '')
    HEADER_TITLE = ('xpath', '')
    HEADER_REFRESH_BTN = ('xpath', '')
    HEADER_MORE_OPTIONS_BTN = ('xpath', '')

    HEADER_LOCAL_WEATHER_BTN = ('ACCESSIBILITY_ID', 'local_weather_btn')
    HEADER_REGIONAL_WEATHER_BTN = ('ACCESSIBILITY_ID', 'district_btn')

    # Body eles
    BODY_HEADER_CHATBOT_BTN = ('ACCESSIBILITY_ID', 'homepage_shortcut_chatbot')
    BODY_HEADER_DATE_TEXT = ('ACCESSIBILITY_ID', 'date')
    BODY_HEADER_TIME_TEXT = ('ACCESSIBILITY_ID', 'time')
    BODY_HEADER_GBA_BTN = ('ACCESSIBILITY_ID', 'homepage_shortcut_gba')


    # HEADER_HAM_BTN eles 
    NINE_DAYS_FORECAST = ('xpath', '')
    MENU_CONTAINER = ('xpath', '')


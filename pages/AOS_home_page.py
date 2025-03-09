from pages.base_page import BasePage
from hamcrest import assert_that


class HomePage(BasePage):
    # AOS element locators
    # header eles
    HEADER_HAM_BTN = ('xpath', '//android.widget.ImageButton[@content-desc="Navigate up"]')
    HEADER_TITLE = ('xpath', '//*[contains(@text, "MyObservatory")]')
    HEADER_REFRESH_BTN = ('xpath', '//android.widget.Button[@content-desc="Refresh"]')
    HEADER_MORE_OPTIONS_BTN = ('xpath', '//android.widget.ImageView[@content-desc="More options"]')

    HEADER_LOCAL_WEATHER_BTN = ('id', 'local_weather_btn')
    HEADER_REGIONAL_WEATHER_BTN = ('id', 'district_btn')

    # Body eles
    BODY_HEADER_CHATBOT_BTN = ('id', 'homepage_shortcut_chatbot')
    BODY_HEADER_DATE_TEXT = ('id', 'date')
    BODY_HEADER_TIME_TEXT = ('id', 'time')
    BODY_HEADER_GBA_BTN = ('id', 'homepage_shortcut_gba')


    # HEADER_HAM_BTN eles 
    NINE_DAYS_FORECAST = ('xpath', '//*[contains(@text, "9-Day Forecast")]')
    MENU_CONTAINER = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.HEADER_HAM_BTN), "Failed to go to the Home page")

    def open_header_ham_menu_btn(self):
        self.click(self.HEADER_HAM_BTN)

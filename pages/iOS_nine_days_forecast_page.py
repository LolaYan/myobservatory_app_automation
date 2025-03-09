from hamcrest import assert_that
from pages.AOS_nine_days_forecast_page import NineDaysForecastPage


class iOSNineDaysForecastPage(NineDaysForecastPage):

    # HEADER_HAM_BTN eles 
    NINE_DAYS_FORECAST_MENU_TAB = ('xpath', '//*[contains(@text, "9-Day Forecast")]')
    MENU_CONTAINER = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout')

    # body eles
    BODY_DESC = ('id', 'mainAppSevenDayGenSit')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.NINE_DAYS_FORECAST_MENU_TAB), "Failed to go to the Home page")

    # scrolling page to view the whole page


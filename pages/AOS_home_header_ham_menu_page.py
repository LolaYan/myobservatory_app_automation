from pages.base_page import BasePage
from hamcrest import assert_that


class HomeHeaderHamMenuPage(BasePage):

    # HEADER_HAM_BTN LV1 Options 
    FORECAST_WARNING_SERVICE_DROPDOWN_LIST = ('xpath', '//*[contains(@text, "Forecast & Warning Services")]')
    WEATHER_MONITORING_IMAGERY_DROPDOWN_LIST = ('xpath', '//*[contains(@text, "Weather Monitoring Imagery")]')
    
    # FORECAST_WARNING_SERVICE_DROPDOWN_LIST eles
    WEATHER_TIPS = ('xpath', '//*[contains(@text, "Weather Tips")]')
    TODAY_FORECAST = ('xpath', '//*[contains(@text, "Today\'s Weather Warnings")]')
    LOCAL_FORECAST = ('xpath', '//*[contains(@text, "Local Forecast")]')
    NINE_DAYS_FORECAST = ('xpath', '//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and @text="9-Day Forecast"]')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.FORECAST_WARNING_SERVICE_DROPDOWN_LIST), "Failed to go to the Home page")

    def open_forecast_warning_service_dropdownlist(self):
        self.click(self.FORECAST_WARNING_SERVICE_DROPDOWN_LIST)

    def select_nine_days_forecast(self):
        self.click(self.NINE_DAYS_FORECAST)
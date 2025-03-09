from pages.AOS_home_header_ham_menu_page import HomeHeaderHamMenuPage
from hamcrest import assert_that


class iOSHomeHeaderHamMenuPage(HomeHeaderHamMenuPage):
    # iOS elements locator
    # HEADER_HAM_BTN LV1 Options 
    FORECAST_WARNING_SERVICE_DROPDOWN_LIST = ('xpath', '')
    WEATHER_MONITORING_IMAGERY_DROPDOWN_LIST = ('xpath', '')
    
    # FORECAST_WARNING_SERVICE_DROPDOWN_LIST eles
    WEATHER_TIPS = ('xpath', '')
    TODAY_FORECAST = ('xpath', '')
    LOCAL_FORECAST = ('xpath', '')
    NINE_DAYS_FORECAST = ('xpath', '')

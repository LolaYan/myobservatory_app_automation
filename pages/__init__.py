from pages.AOS_set_up.disclaimer_page import DisclaimerPage
from pages.AOS_set_up.privacy_policy_statements_page import PrivacyPolicyStatementPage
from pages.AOS_set_up.device_notification_setting_page import DeviceNotificationSettingPage
from pages.AOS_set_up.background_location_access_statement_page import BackgroundLocationAccessStatementPage
from pages.AOS_set_up.device_location_access_page import DeviceLocationAccessPage
from pages.AOS_set_up.location_permission_config_page import LocationPermissionConfigPage

from pages.iOS_set_up.iOS_color_theme_page import IOSColorThemePage
from pages.iOS_set_up.iOS_finish_setting_page import IOSFinishSettingPage
from pages.iOS_set_up.iOS_language_setup_page import iOSLanguageSetupPage
from pages.iOS_set_up.iOS_loc_based_notification_page import IOSLocBasedNotificationPage
from pages.iOS_set_up.iOS_location_access_page import IOSLocationAccessPage
from pages.iOS_set_up.iOS_nextwork_access_page import iOSNextworkAccessPage
from pages.iOS_set_up.iOS_notification_access_page import IOSNotificationAccessPage

from pages.AOS_whats_new_page import WhatsNewPage
from pages.AOS_home_page import HomePage
from pages.AOS_home_header_ham_menu_page import HomeHeaderHamMenuPage
from pages.AOS_nine_days_forecast_page import NineDaysForecastPage


class Pages:
    def __init__(self, driver):
        self._driver = driver

        self.aos_disclaimer = DisclaimerPage(self._driver)
        self.aos_privacy_policy_statements = PrivacyPolicyStatementPage(self._driver)
        self.aos_device_notification_setting = DeviceNotificationSettingPage(self._driver)
        self.aos_background_location_access = BackgroundLocationAccessStatementPage(self._driver)
        self.aos_device_location_access = DeviceLocationAccessPage(self._driver)
        self.aos_location_permission_config = LocationPermissionConfigPage(self._driver)

        self.ios_color_theme = IOSColorThemePage(self._driver)
        self.ios_finish_setting = IOSFinishSettingPage(self._driver)
        self.ios_language_setup = iOSLanguageSetupPage(self._driver)
        self.ios_location_access = IOSLocationAccessPage(self._driver)
        self.ios_loc_based_notification = IOSLocBasedNotificationPage(self._driver)
        self.ios_nextwork_access = iOSNextworkAccessPage(self._driver)
        self.ios_notification_access = IOSNotificationAccessPage(self._driver)

        self.aos_whats_new = WhatsNewPage(self._driver)
        self.aos_home = HomePage(self._driver)
        self.aos_home_header_ham_menu = HomeHeaderHamMenuPage(self._driver)
        self.aos_nine_days_forecast = NineDaysForecastPage(self._driver)


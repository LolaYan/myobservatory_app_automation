from pages.base_page import BasePage
from hamcrest import assert_that


class iOSNextworkAccessPage(BasePage):

    # Usign inspector to get ACCESSIBILITY_ID of eles below
    WIFI_AND_DATA_OPTION = ('ACCESSIBILITY_ID', '')
    ONLY_WIFI_OPTION = ('ACCESSIBILITY_ID', '')
    DONT_ALLOW_OPTION = ('ACCESSIBILITY_ID', '')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.WIFI_AND_DATA_OPTION), "Failed to go to page")

    def click_wifi_and_data_option(self):
        self.click(self.WIFI_AND_DATA_OPTION)

    def click_only_wifi_option(self):
        self.click(self.ONLY_WIFI_OPTION)

    def click_dont_allow_option(self):
        self.click(self.DONT_ALLOW_OPTION)

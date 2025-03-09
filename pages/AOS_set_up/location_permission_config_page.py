from pages.base_page import BasePage
from hamcrest import assert_that

class LocationPermissionConfigPage(BasePage):
    # header eles
    BACK = ('xpath', '//android.widget.ImageButton[@content-desc="Back"]')

    # body eles
    MOB_TITLE = ('id', 'com.android.permissioncontroller:id/entity_header_title')
    ALLOW_ALL_THE_TIME_OPTION = ('id', 'com.android.permissioncontroller:id/allow_always_radio_button')
    WHILE_USING_THE_APP_OPTION= ('id', 'com.android.permissioncontroller:id/allow_foreground_only_radio_button')
    ASK_EVERY_TIME_OPTION = ('id', 'com.android.permissioncontroller:id/ask_radio_button')
    DONT_ALLOW_OPTION = ('id', 'com.android.permissioncontroller:id/deny_radio_button')
    LOCATION_ACCURACY_SWITCH = ('id', 'com.android.permissioncontroller:id/location_accuracy_switch')

    # footer links
    ALL_MOB_PERMISSIONS_LINK = ('xpath', '//*[contains(@text, "See all MyObservatory permissions")]')
    ALL_APPS_WITH_THIS_PERMISSION_LINK = ('xpath', '//*[contains(@text, "See all apps with this permission")]')


    def verify_page_loaded(self):
        assert_that(self.is_visible(self.ALLOW_ALL_THE_TIME_OPTION), "Failed to go to page")

    def click_allow_all_the_time_option(self):
        self.click(self.ALLOW_ALL_THE_TIME_OPTION)

    def click_while_using_the_app_option(self):
        self.click(self.WHILE_USING_THE_APP_OPTION)

    def click_ask_every_time_option(self):
        self.click(self.ASK_EVERY_TIME_OPTION)

    def click_dont_allow_option(self):
        self.click(self.DONT_ALLOW_OPTION)

    def click_back_btn(self):
        self.click(self.BACK)
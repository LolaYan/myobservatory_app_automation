from pages.base_page import BasePage
from hamcrest import assert_that


class DeviceLocationAccessPage(BasePage):

    LOCATION_PERMISSION_POPUP_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    PRECISE_LOCATION_RADIOBUTTON = ('id', 'com.android.permissioncontroller:id/permission_location_accuracy_radio_fine')
    COARSE_LOCATION_RADIOBUTTON = ('id', 'com.android.permissioncontroller:id/permission_location_accuracy_radio_coarse')
    WHILE_USING_THE_APP_OPTION = ('id', 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
    ONLY_THIS_TIME_OPTION = ('id', 'com.android.permissioncontroller:id/permission_allow_one_time_button')
    DONT_ALLOW_OPTION = ('id', 'com.android.permissioncontroller:id/permission_deny_button')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.WHILE_USING_THE_APP_OPTION), "Failed to go to page")

    def click_while_using_the_app_option(self):
        self.click(self.WHILE_USING_THE_APP_OPTION)

    def click_only_this_time_option(self):
        self.click(self.ONLY_THIS_TIME_OPTION)

    def click_dont_allow_option(self):
        self.click(self.DONT_ALLOW_OPTION)

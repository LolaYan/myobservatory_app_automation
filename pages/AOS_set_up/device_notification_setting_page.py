from pages.base_page import BasePage
from hamcrest import assert_that

class DeviceNotificationSettingPage(BasePage):

    NOTIFICATION_POPUP_TITLE = ('id', 'com.android.permissioncontroller:id/permission_message')
    ALLOW_OPTION = ('id', 'com.android.permissioncontroller:id/permission_allow_button')
    DONT_ALLOW_OPTION = ('id', 'com.android.permissioncontroller:id/permission_deny_button')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.NOTIFICATION_POPUP_TITLE), "Failed to go to page")

    def click_allow_option(self):
        self.click(self.ALLOW_OPTION)

    def click_dont_allow_option(self):
        self.click(self.DONT_ALLOW_OPTION)

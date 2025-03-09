from pages.base_page import BasePage
from hamcrest import assert_that


class IOSLocBasedNotificationPage(BasePage):

    # Native iOS pop up elements
    WHILE_USING_THE_APP_OPTION = ('ACCESSIBILITY_ID', '')
    ALWAYS_ALLOW_OPTION = ('ACCESSIBILITY_ID', '')

    # Page elements
    NEXT_BTN = ('ACCESSIBILITY_ID', '')
    NOT1_SWITCHBOX = ('ACCESSIBILITY_ID', '')
    NOT2_SWITCHBOX = ('ACCESSIBILITY_ID', '')


    def verify_popup_loaded(self):
        assert_that(self.is_visible(self.WHILE_USING_THE_APP_OPTION), "Failed to open location access pop up")

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.NEXT_BTN), "Failed to open location access pop up")

    def click_while_using_the_app_option(self):
        self.click(self.WHILE_USING_THE_APP_OPTION)

    def click_always_allow_option(self):
        self.click(self.ALWAYS_ALLOW_OPTION)

    def click_next_btn(self):
        self.click(self.NEXT_BTN)
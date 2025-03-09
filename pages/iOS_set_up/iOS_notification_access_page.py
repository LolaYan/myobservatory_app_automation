from pages.base_page import BasePage
from hamcrest import assert_that


class IOSNotificationAccessPage(BasePage):

    # Native iOS pop up elements
    ALLOW_OPTION = ('ACCESSIBILITY_ID', '')
    DONT_ALLOW_OPTION = ('ACCESSIBILITY_ID', '')

    # Notificaiton terms and con page element
    AGREE_OPTION = ('ACCESSIBILITY_ID', '')
    DISAGREE_OPTION = ('ACCESSIBILITY_ID', '')

    # Location page elements
    NEXT_BTN = ('ACCESSIBILITY_ID', '')
    NOTIFICATION_SWITCHBOX = ('ACCESSIBILITY_ID', '')

    # native pop up functions       
    def verify_popup_loaded(self):
        assert_that(self.is_visible(self.ALLOW_OPTION), "Failed to open pop up")

    def click_allow_option(self):
        self.click(self.ALLOW_OPTION)

    def click_dont_allow_option(self):
        self.click(self.DONT_ALLOW_OPTION)

    # Notificaiton terms and con page functions
    def click_agree_option(self):
        self.click(self.AGREE_OPTION)

    # Notificaiton page functions
    def verify_page_loaded(self):
        assert_that(self.is_visible(self.NEXT_BTN), "Failed to open page")

    def click_next_btn(self):
        self.click(self.NEXT_BTN)
from pages.base_page import BasePage
from hamcrest import assert_that


class IOSFinishSettingPage(BasePage):
    
    # Location page elements
    FINISH_BTN = ('ACCESSIBILITY_ID', '')

    def click_finish_btn(self):
        self.click(self.FINISH_BTN)
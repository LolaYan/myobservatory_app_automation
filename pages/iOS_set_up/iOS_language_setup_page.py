from pages.base_page import BasePage
from hamcrest import assert_that


class iOSLanguageSetupPage(BasePage):

    # Usign inspector to get ACCESSIBILITY_ID of eles below
    COMPLEX_CHINESE_OPTION = ('ACCESSIBILITY_ID', '')
    SIMPLE_CHINESE_OPTION = ('ACCESSIBILITY_ID', '')
    ENGLISH_OPTION = ('ACCESSIBILITY_ID', '')

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.COMPLEX_CHINESE_OPTION), "Failed to go to page")

    def click_complex_chinese_option(self):
        self.click(self.COMPLEX_CHINESE_OPTION)

    def click_simple_chinese_option(self):
        self.click(self.SIMPLE_CHINESE_OPTION)

    def click_english_option(self):
        self.click(self.ENGLISH_OPTION)

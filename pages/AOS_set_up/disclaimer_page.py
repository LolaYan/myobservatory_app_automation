from pages.base_page import BasePage
from hamcrest import assert_that

class DisclaimerPage(BasePage):
    
    DISCLAIMER_TITLE = ('id', 'txt_title')
    DISCLAIMER_CONTENT = ('id', 'txt_content')
    AGREE_BUTTON = ('id', 'btn_agree')
    DISAGREE_BUTTON = ('id', 'btn_not_agree')

    def click_agree_btn(self):
        self.click(self.AGREE_BUTTON)

    def click_disagree_btn(self):
        self.click(self.DISAGREE_BUTTON)

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.DISCLAIMER_TITLE), "Failed to go to the Disclaimer page")
        assert_that(self.is_visible(self.AGREE_BUTTON), "Failed to go to the Disclaimer page")
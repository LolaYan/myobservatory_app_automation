from pages.base_page import BasePage
from hamcrest import assert_that

class PrivacyPolicyStatementPage(BasePage):

    PPS_TITLE = ('id', 'txt_title')
    PPS_CONTENT = ('id', 'txt_content')
    AGREE_BUTTON = ('id', 'btn_agree')
    DISAGREE_BUTTON = ('id', 'btn_not_agree')

    def click_agree_btn(self):
        self.click(self.AGREE_BUTTON)

    def click_disagree_btn(self):
        self.click(self.DISAGREE_BUTTON)

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.PPS_TITLE), "Failed to go to the PrivacyPolicyStatement Page")
        assert_that(self.is_visible(self.AGREE_BUTTON), "Failed to go to the PrivacyPolicyStatement Page")
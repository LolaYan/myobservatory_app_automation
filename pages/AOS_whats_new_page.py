from pages.base_page import BasePage
from hamcrest import assert_that

class WhatsNewPage(BasePage):

    # There should be 2 sliding pages in this page
    # exit_btn in sub-page-1 means "next", means "close" in sub-page-2
    NEXT_BUTTON = ('id', 'exit_btn')
    CLOSE_BUTTON = ('id', 'exit_btn')
    DO_NOT_SHOW_AGAIN_BUTTON = ('id', 'do_not_show_again_btn')

    # ele in sub-page-1 
    WHATS_NEW_IMAGE = ('id', 'img_view')

    # ele in sub-page-2
    WHATS_NEW_TITLE = ('id', 'whatsNewTitle')
    WHATS_NEW_CONTENT = ('id', 'whatsNewContent')


    def verify_sub_page1_loaded(self):
        assert_that(self.is_visible(self.WHATS_NEW_IMAGE), "Failed to go to the page")

    def verify_sub_page2_loaded(self):
        assert_that(self.is_visible(self.WHATS_NEW_CONTENT), "Failed to go to the page")

    def click_next_btn(self):
        self.click(self.NEXT_BUTTON)

    def click_close_btn(self):
        self.click(self.CLOSE_BUTTON)

    def click_not_show_btn(self):
        self.click(self.DO_NOT_SHOW_AGAIN_BUTTON)
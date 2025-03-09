from hamcrest import assert_that

from pages.base_page import BasePage


class BackgroundLocationAccessStatementPage(BasePage):
    
    BLAS_TITLE = ('id', 'alertTitle')
    BLAS_CONTENT = ('id', 'android:id/message')
    OK_BUTTON = ('id', 'android:id/button1')

    def click_OK_btn(self):
        self.click(self.OK_BUTTON)

    def verify_page_loaded(self):
        assert_that(self.is_visible(self.BLAS_TITLE), "Failed to go to the BackgroundLocationAccessStatement Page")
        assert_that(self.is_visible(self.OK_BUTTON), "Failed to go to the BackgroundLocationAccessStatement Page")
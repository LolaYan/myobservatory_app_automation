from pages.base_page import BasePage
from hamcrest import assert_that


class IOSColorThemePage(BasePage):

    # Page elements
    DAY_THEME_BLACK = ('ACCESSIBILITY_ID', '')
    DAY_THEME_WHITE = ('ACCESSIBILITY_ID', '')
    DAY_THEME_GREEN = ('ACCESSIBILITY_ID', '')
    DAY_THEME_YELLOW = ('ACCESSIBILITY_ID', '')
    DAY_THEME_RED = ('ACCESSIBILITY_ID', '')

    NIGHT_THEME_BLACK = ('ACCESSIBILITY_ID', '')
    NIGHT_THEME_WHITE = ('ACCESSIBILITY_ID', '')
    NIGHT_THEME_GREEN = ('ACCESSIBILITY_ID', '')
    NIGHT_THEME_YELLOW = ('ACCESSIBILITY_ID', '')
    NIGHT_THEME_RED = ('ACCESSIBILITY_ID', '')

    NEXT_BTN = ('ACCESSIBILITY_ID', '')

    # native pop up functions       
    def verify_popup_loaded(self):
        assert_that(self.is_visible(self.NEXT_BTN), "Failed to open page")

    # Parameterise the color input 
    def click_day_theme_color(self):
        self.click(self.DAY_THEME_YELLOW)

    def click_night_theme_color(self):
        self.click(self.DAY_THEME_YELLOW)

    def click_next_btn(self):
        self.click(self.NEXT_BTN)
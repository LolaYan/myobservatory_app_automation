
import time
from typing import Optional, Tuple
from appium.webdriver import WebElement
from appium.webdriver.extensions.android.nativekey import AndroidKey
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging


class BasePage:
    # To do: DEFAULT_TIMEOUT should read from config file 
    DEFAULT_TIMEOUT = 300
    current_day = time.strftime("%Y%m%d")
    

    def __init__(self, driver):
        self.driver = driver

    # explicit wait to find the element
    def find_element(self, locator: Tuple[str, str], timeout: Optional[int] = None,
              expected_condition: EC = EC.visibility_of_element_located, ) -> WebElement:
        current_time = time.strftime("%Y%m%d_%H%M%S")
        if not timeout:
            timeout = self.DEFAULT_TIMEOUT
        try: 
            return WebDriverWait(self.driver, timeout).until(expected_condition(locator))
        except Exception as e:  
            self.driver.save_screenshot(path=f"screenshots/{self.current_day}/error_{current_time}.png", full_page=True)
            logging.error(f"Failed to locate the element: {locator}")  
            raise e  

    def is_visible(self, locator) -> bool:
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
        time.sleep(0.5)

    def clear(self, locator):
        self.find_element(locator).clear()

    def press_device_back_btn(self):
        self.driver.press_keycode(AndroidKey.BACK)

    def validate_element_with_timeout(self, locator, timeout=5):
        current_time = time.strftime("%Y%m%d_%H%M%S")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            logging.info(f"Element {locator} is returned，please go on test the element feature")
            return element 
        except TimeoutException:
            logging.warning(f"Wait for {timeout}s element not found : {locator}")
            self.driver.save_screenshot(path=f"screenshots/{self.current_day}/error_{current_time}.png", full_page=True)
            return None

#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

import logging
import os
import time
import uuid

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOGGER.setLevel(logging.WARNING)


class SdetWebDriver():
    def __init__(self):
        self.web_driver = webdriver
        self.timeout = 10
        self.short_timeout = 2
        self.screenshot_path = os.getcwd() + '/screenshot/'

    def sdet_open_browser(self, width=None, height=None):
        logging.debug('sdet_open_browser')
        chrome_options = self._get_chrome_options()
        self.web_driver = webdriver.Chrome(options=chrome_options)

        if width != None and height != None:
            self.web_driver.set_window_size(width, height)
        else:
            self.web_driver.maximize_window()

        self.web_driver.implicitly_wait(self.timeout)

        return self.web_driver

    def _get_chrome_options(self):
        chrome_options = Options()
        # chrome_options.add_experimental_option(
        #     'prefs', {'safebrowsing.enabled': True, 'download.default_directory': f"{TEST_DATA_DIR}"})
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
        # Disable sandbox mode. Resolve error when DevToolsActivePort file does not exist
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resources [for Linux only]
        # chrome_options.add_argument('--remote-debugging-port=9222')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('blink-settings=imagesEnabled=false')
        return chrome_options

    def sdet_save_screenshot(self, filename):
        logging.debug(f'sdet_save_screenshot: {filename}')
        self.web_driver.save_screenshot(self.screenshot_path + filename + '.png')

    def sdet_click_element(self, locator, timeout=None, is_screenshot=False):
        time.sleep(self.short_timeout)
        _status = 'Failed'
        if timeout is None:
            timeout = self.timeout
        try:
            element = WebDriverWait(self.web_driver, timeout, 1).until(
                EC.element_to_be_clickable((By.XPATH, locator))
            )
            element = WebDriverWait(self.web_driver, timeout, 1).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
            element.click()
            _status = 'Success'
        except TimeoutException as ex:
            if is_screenshot:
                file_name = uuid.uuid4().hex
                self.web_driver.save_screenshot(self.screenshot_path + file_name + '.png')
        finally:
            logging.debug('sdet_click_locator: %s, status: %s' % (locator, _status))

    def sdet_get_num_of_items(self, locator, class_name):
        logging.debug('this locator %s' % locator)
        result = 0
        try:
            items_element = self.web_driver.find_element(By.XPATH, locator).find_elements(By.CLASS_NAME, class_name)
            result = len(items_element)
        finally:
            logging.debug('sdet_get_num_of_items, number of items: %s' % result)
        return result

    def sdet_check_element_exists(self, locator, timeout=10):
        result = False
        try:
            element = WebDriverWait(self.web_driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except TimeoutException as ex:
            result = False
        else:
            result = True
        finally:
            logging.debug('sdet_check_element_exists, locator: %s, exists: %s' % (locator, result))
        return result

    def sdet_scroll_to(self, locator):
        element = self.web_driver.find_element(By.XPATH, locator)
        self.web_driver.execute_script("arguments[0].scrollIntoView();", element)
        logging.debug('sdet_scroll_to element: %s' % locator)
        time.sleep(2)


if __name__ == "__main__":
    logging.debug('sdet_common')
    # browser = 'chrome'
    # driver_instance = SdetWebDriver(browser)
    # driver_instance.web_driver.get('https://www.google.com')
    # driver_instance.web_driver.close()

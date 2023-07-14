#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

# execute command: python3 ui_automation/cathay_homework.py
import logging
import time

from lib.SDET_COMMON import SdetWebDriver
from lib.SDET_ELEMENT import get_element_locator

BASIC_FORMAT = "%(levelname)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=BASIC_FORMAT)


sdet_elements = get_element_locator
base_url = "https://www.cathaybk.com.tw/cathaybk"
sdet_web_driver = SdetWebDriver()
sdet_web_driver.sdet_open_browser(width=390, height=844)

logging.info("[Step 1] 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。")
sdet_web_driver.web_driver.get(base_url)
sdet_web_driver.sdet_save_screenshot("screenshot1")

logging.info("[Step 2] 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡介紹，需計算有幾個項目並將畫面截圖。")
mobile_menu = sdet_elements('mobile_layout')
sdet_web_driver.sdet_click_element(mobile_menu['menu'])
sdet_web_driver.sdet_click_element(mobile_menu['menu_product_intro'])
sdet_web_driver.sdet_click_element(mobile_menu['menu_product_intro_creditcard'])
time.sleep(1)
sdet_web_driver.sdet_save_screenshot("screenshot2")

class_name = "cubre-a-menuLink"
sdet_web_driver.sdet_check_element_exists(mobile_menu['menu_product_intro_creditcard_content'])
items_number = sdet_web_driver.sdet_get_num_of_items(mobile_menu['menu_product_intro_creditcard_content'], class_name)
logging.info(f"[Step 2][項目數量]: {items_number}")
# assert (items_number == 8, "The Number of items should be 8 but failed.")

logging.info("[Step 3] 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖。")
sdet_web_driver.sdet_click_element(mobile_menu['menu_product_intro_creditcard_info'])

creditcard_page = sdet_elements('cathaybk_personal_product_credit-card_cards')
class_name = "cubre-o-slide__item"

stop_issuing_section = creditcard_page['stop_issuing_content']
sdet_web_driver.sdet_check_element_exists(stop_issuing_section)
sdet_web_driver.sdet_scroll_to(stop_issuing_section)

items_number = sdet_web_driver.sdet_get_num_of_items(stop_issuing_section, class_name)
logging.info(f"[Step 3][停發數量]: {items_number}")
# assert (items_number == 11, "Number of stop issuing cards should be 11 but failed.")

sdet_web_driver.sdet_save_screenshot("screenshot3")

sdet_web_driver.web_driver.quit()

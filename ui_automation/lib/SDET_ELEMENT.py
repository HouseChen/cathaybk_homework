#!/usr/bin/env python3
# -*-  coding: utf-8 -*-

def get_element_locator(page, locator=None):
    result = {}
    if page == 'cathaybk':
        result = {

        }
    elif page == 'mobile_layout':
        result = {
            "menu": "//header[@class='cubre-o-header']//div[@class='cubre-o-header__burger']/a",
            "menu_product_intro": "//header[@class='cubre-o-header']//div[@class='cubre-o-nav__content']//div[@class='cubre-o-menu__item'][1]//div[@class='cubre-a-menuSortBtn -l1']",
            "menu_product_intro_creditcard": "//header[@class='cubre-o-header']//div[@class='cubre-o-nav__content']//div[@class='cubre-o-menu__item is-L1open']/div[@class='cubre-o-menu__content']/div[1]/div[1]",
            "menu_product_intro_creditcard_content": "//header[@class='cubre-o-header']//div[@class='cubre-o-nav__content']//div[@class='cubre-o-menu__item is-L1open']/div[@class='cubre-o-menu__content']//div[@class='cubre-o-menuLinkList__item is-L2open']/div[@class='cubre-o-menuLinkList__content']",
            "menu_product_intro_creditcard_info": "//div[@class='cubre-o-nav__content']//div[@class='cubre-o-menu__item is-L1open']/div[@class='cubre-o-menu__content']/div[1]/div[1]/div[@class='cubre-o-menuLinkList__content']//a[1]"
        }
    elif page == 'cathaybk_personal_product_credit-card_cards':
        result = {
            "stop_issuing_content": "//section[@data-anchor-block='blockname06']//div[@class='cubre-o-block__component']"
        }
    if not locator:
        return result
    else:
        return result[locator]


def get_page_url(page):
    page_list = {
        "cathaybk": "/cathaybk",
    }
    return page_list[page]

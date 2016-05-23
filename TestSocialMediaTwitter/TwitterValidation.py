# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


def validate_twitter_highlighted_buffer(driver):

    """ Validation for twitter highlighted layer """

    try:
        twitter_highlight_graphic_layer = driver.find_element_by_id("twitterHighlightGraphicLayer_layer")
        if twitter_highlight_graphic_layer.is_displayed():
            return True
    except Exception:
        return False


def validate_twitter_buffer(driver):

    """ Validation for twitter buffer on map """

    try:
        validate_twitter_buffer = driver.find_element_by_id("twitterBufferLayer_layer")
        if validate_twitter_buffer.is_displayed():
            return True
    except Exception:
        return False
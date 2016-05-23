# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


def validate_youtube_buffer(driver):

    """ Validation for youtube buffer on map """

    try:
        validate_youtube_buffer = driver.find_element_by_id("youtubeBufferLayer_layer")
        if validate_youtube_buffer.is_displayed():
            return True
    except Exception:
        return False


def validate_youtube_highlighted_buffer(driver):

    """ Validation for youtube highlighted layer """

    try:
        twitter_highlight_graphic_layer = driver.find_element_by_id("youtubeHighlightGraphicLayer_layer")
        if twitter_highlight_graphic_layer.is_displayed():
            return True
    except Exception:
        return False
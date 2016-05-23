# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


def validate_flickr_buffer(driver):

    """ Validation for flickr buffer on map """

    try:
        validate_flickr_buffer = driver.find_element_by_id("flickrBufferLayer_layer")
        if validate_flickr_buffer.is_displayed():
            return True
    except Exception:
        return False


def validate_flickr_highlighted_buffer(driver):

    """ Validation for flickr highlighted layer """

    try:
        flickr_highlight_graphic_layer = driver.find_element_by_id("flickrHighlightGraphicLayer_layer")
        if flickr_highlight_graphic_layer.is_displayed():
            return True
    except Exception:
        return False
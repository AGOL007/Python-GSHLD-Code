# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


def validate_social_media_highlighted_buffer(driver):

    """ Validation for social media highlighted layer """

    try:
        flickr_highlight_graphic_layer = driver.find_element_by_id("socialMediaHighlightGraphicLayer_layer")
        if flickr_highlight_graphic_layer.is_displayed():
            return True
    except Exception:
        return False


def validate_social_media_buffer(driver):

    """ Validation for social media buffer on map """

    try:
        validate_social_media = driver.find_element_by_id("socialMediaBufferLayer_layer")
        if validate_social_media.is_displayed():
            return True
    except Exception:
        return False
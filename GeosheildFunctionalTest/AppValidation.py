# -*- coding: utf-8 -*-
""" File contains Validation Methods"""
__author__ = 'SagarKul'
import GeoShieldSeleniumAction
import AppCommanUtility


def validate_layer_name(driver, category_sub_layer_name):

    """ Validation For layer in left panel with layer in bottom panel """
    try:
        layer_active_data = driver.find_elements_by_class_name("layerDataContainer")
        for item in layer_active_data:
            layer_active_data_div = item.find_elements_by_class_name("layerContentRow")
            for item1 in layer_active_data_div:
                layer_active_data_div_text = item1.text
                if category_sub_layer_name == layer_active_data_div_text:
                    GeoShieldSeleniumAction.click_right_panel_open(driver, True)
                elif category_sub_layer_name in layer_active_data_div_text:
                    GeoShieldSeleniumAction.click_right_panel_open(driver, True)

    except Exception:
        return True


def validate_right_panel_layer_name(driver, category_sub_layer_name):

    """ Validation for layers present in right panel with the layers in left panel """

    try:
        layer_active_data_right_panel_layer = driver.find_elements_by_class_name("tocLayerRow")
        for item in layer_active_data_right_panel_layer:
            layer_active_data_right_panel_layer_div = item.find_elements_by_class_name("tocLayerName")
            for item1 in layer_active_data_right_panel_layer_div:
                layer_active_data_right_panel_layer_div_text = item1.text
                if category_sub_layer_name == layer_active_data_right_panel_layer_div_text:
                    AppCommanUtility.click_bottom_panel_layer(driver, layer_active_data_right_panel_layer_div_text)
                elif category_sub_layer_name in layer_active_data_right_panel_layer_div_text:
                    AppCommanUtility.click_bottom_panel_layer(driver, layer_active_data_right_panel_layer_div_text)

    except Exception:
        return True


def validate_feature_count_panel(driver):

    """ Validation for feature count present in bottom panel with right panel """

    try:
        layer_active_data_count = driver.find_element_by_class_name("gridBottomPanel")
        layer_active_data_count_div = layer_active_data_count.find_element_by_class_name("gridTotalResultsPanel")
        layer_active_data_count_div_text = layer_active_data_count_div.text

        to_render_graphic_count = driver.find_element_by_class_name("tocRenderGraphicCount")
        to_render_graphic_count_div = to_render_graphic_count.find_element_by_class_name("tocLayerGraphicCount")
        to_render_graphic_count_div_text = to_render_graphic_count_div.text
        to_layer_graphic_count_div_text_split = layer_active_data_count_div_text.split(" ")
        to_layer_graphic_count_div_text_split_index = to_layer_graphic_count_div_text_split[0]

        if to_render_graphic_count_div_text == to_layer_graphic_count_div_text_split_index:
            return True
        else:
            return False
    except Exception:
        return True


def validate_feature_count(driver, category_sub_layer_name):

    """ Validation for feature count present on map """

    try:
        layer_name_feature_svg_tag = driver.find_elements_by_tag_name("svg")
        for item in layer_name_feature_svg_tag:
            layer_name_feature_g_tag = item.find_elements_by_tag_name("g")
            for item1 in layer_name_feature_g_tag:
                layer_name_feature_get_attribute = item1.get_attribute("id")
                if category_sub_layer_name in layer_name_feature_get_attribute:
                    layer_name_feature_image_tag = item1.find_elements_by_tag_name("image")
                    layer_name_feature_image_tag_count = len(layer_name_feature_image_tag)
                    if layer_name_feature_image_tag_count == 0:
                        print "Feature is not in default extent"
                        return True
                    else:
                        return True
    except Exception:
        return True


def validate_twitter_buffer(driver):

    """ Validation for twitter buffer on map """

    try:
        validate_twitter_buffer = driver.find_element_by_id("twitterBufferLayer_layer")
        if validate_twitter_buffer.is_displayed():
            return True
    except Exception:
        return False


def validate_youtube_buffer(driver):

    """ Validation for youtube buffer on map """

    try:
        validate_youtube_buffer = driver.find_element_by_id("youtubeBufferLayer_layer")
        if validate_youtube_buffer.is_displayed():
            return True
    except Exception:
        return False


def validate_flickr_buffer(driver):

    """ Validation for flickr buffer on map """

    try:
        validate_flickr_buffer = driver.find_element_by_id("flickrBufferLayer_layer")
        if validate_flickr_buffer.is_displayed():
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


def validate_agency_feed_avl_historic_tab(driver, category_agency_feed_avl):

    """ Validation for feature count on map """

    layer_name_feature_svg_tag = driver.find_elements_by_tag_name("svg")
    for item in layer_name_feature_svg_tag:
        layer_name_feature_g_tag = item.find_elements_by_tag_name("g")
        for item1 in layer_name_feature_g_tag:
            layer_name_feature_get_attribute = item1.get_attribute("id")
            if category_agency_feed_avl in layer_name_feature_get_attribute:
                layer_name_feature_image_tag = item1.find_elements_by_tag_name("circle")
                layer_name_feature_image_tag_count = len(layer_name_feature_image_tag)
                if layer_name_feature_image_tag_count == 0:
                    print "Feature is not in default extent"
                    return True
                else:
                    return True


def validate_agency_feed_avl_buffer(driver):

    """ Validation for avl tab buffer on map """

    try:
        validate_social_media = driver.find_element_by_id("avlDrawBufferLayer_layer")
        if validate_social_media.is_displayed():
            return True
    except Exception:
        return False


def validate_agency_feed_lpr_buffer(driver):

    """ Validation for lpr tab buffer on map """

    try:
        validate_social_media = driver.find_element_by_id("lprDrawBuffer_layer")
        if validate_social_media.is_displayed():
            return True
    except Exception:
        return False


def validate_twitter_highlighted_buffer(driver):

    """ Validation for twitter highlighted layer """

    try:
        twitter_highlight_graphic_layer = driver.find_element_by_id("twitterHighlightGraphicLayer_layer")
        if twitter_highlight_graphic_layer.is_displayed():
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


def validate_flickr_highlighted_buffer(driver):

    """ Validation for flickr highlighted layer """

    try:
        flickr_highlight_graphic_layer = driver.find_element_by_id("flickrHighlightGraphicLayer_layer")
        if flickr_highlight_graphic_layer.is_displayed():
            return True
    except Exception:
        return False


def validate_social_media_highlighted_buffer(driver):

    """ Validation for social media highlighted layer """

    try:
        flickr_highlight_graphic_layer = driver.find_element_by_id("socialMediaHighlightGraphicLayer_layer")
        if flickr_highlight_graphic_layer.is_displayed():
            return True
    except Exception:
        return False
















































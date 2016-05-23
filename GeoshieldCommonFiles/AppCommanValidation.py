# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import AppCommanUtility
from GeoshieldCommonFiles import TestLog, TestFailScreenShots


def validate_layer_name(driver, category_sub_layer_name, tool_name, index, ws_index, boolean_value):

    """ Validation For layer in left panel with layer in bottom panel """
    count=0

    try:
        layer_active_data = driver.find_elements_by_class_name("layerDataContainer")
        for item in layer_active_data:
            layer_active_data_div = item.find_elements_by_class_name("layerContentRow")
            for item1 in layer_active_data_div:
                layer_active_data_div_text = item1.text
                if category_sub_layer_name == layer_active_data_div_text:
                    count=count+1
                    AppCommanUtility.click_right_panel_open(driver, tool_name, index, boolean_value, ws_index)
#                    TestLog.create_result_validation_right_panel_layer(category_sub_layer_name)
                elif category_sub_layer_name in layer_active_data_div_text:
                    count=count+1
                    AppCommanUtility.click_right_panel_open(driver, tool_name, index, boolean_value, ws_index)
#                    TestLog.create_result_validation_right_panel_layer(category_sub_layer_name)
        if count == 0:
            return False
    except Exception:
        return False


def validate_right_panel_layer_name(driver, category_sub_layer_name, tool_name, index, ws_index):

    """ Validation for layers present in right panel with the layers in left panel """
    count=0
    try:
        layer_active_data_right_panel_layer = driver.find_elements_by_class_name("tocLayerRow")
        for item in layer_active_data_right_panel_layer:
            layer_active_data_right_panel_layer_div = item.find_elements_by_class_name("tocLayerName")
            for item1 in layer_active_data_right_panel_layer_div:
                layer_active_data_right_panel_layer_div_text = item1.text
                if category_sub_layer_name == layer_active_data_right_panel_layer_div_text:
                    AppCommanUtility.click_bottom_panel_layer(driver, layer_active_data_right_panel_layer_div_text, tool_name, index, ws_index)
                   # TestLog.create_result_validation_right_panel_layer(category_sub_layer_name)
                elif category_sub_layer_name in layer_active_data_right_panel_layer_div_text:
                    AppCommanUtility.click_bottom_panel_layer(driver, layer_active_data_right_panel_layer_div_text, tool_name, index, ws_index)
                    #TestLog.create_result_validation_right_panel_layer(category_sub_layer_name)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "validate_right_panel_layer_name")
        TestLog.log_creation(tool_name, "validate_right_panel_layer_name", index, ws_index)


def validate_feature_count_panel(driver, tool_name, index, ws_index):

    """ Validation for feature count present in bottom panel with right panel """

    try:
        layer_active_data_count = driver.find_element_by_class_name("gridBottomPanel")
        layer_active_data_count_div = layer_active_data_count.find_element_by_class_name("gridTotalResultsPanel")
        layer_active_data_count_div_text = layer_active_data_count_div.text

        to_render_graphic_count = driver.find_elements_by_class_name("tocRenderGraphicCount")
        for item in to_render_graphic_count:
            to_render_graphic_count_div = item.find_element_by_class_name("tocLayerGraphicCount")
            to_render_graphic_count_div_text = to_render_graphic_count_div.text
            to_layer_graphic_count_div_text_split = layer_active_data_count_div_text.split(" ")
            to_layer_graphic_count_div_text_split_index = to_layer_graphic_count_div_text_split[0]

            if to_render_graphic_count_div_text == to_layer_graphic_count_div_text_split_index:
                return True
            else:
                continue
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "validate_feature_count_panel")
        TestLog.log_creation(tool_name, "validate_feature_count_panel", index, ws_index)


def validate_feature_count(driver, category_sub_layer_name, tool_name, index, ws_index):

    """ Validation for feature count present on map """
#    try:
    layer_name_feature_svg_tag = driver.find_elements_by_tag_name("svg")
    for item in layer_name_feature_svg_tag:
        layer_name_feature_g_tag = item.find_elements_by_tag_name("g")
        for item1 in layer_name_feature_g_tag:
            layer_name_feature_get_attribute = item1.get_attribute("id")
            if category_sub_layer_name in layer_name_feature_get_attribute:
                layer_name_feature_image_tag = item1.find_elements_by_tag_name("image")
                layer_name_feature_image_tag_count = len(layer_name_feature_image_tag)
                if layer_name_feature_image_tag_count == 0:
                    TestLog.log_creation(tool_name, "validate_feature_count", index, ws_index)
                else:
                    return True

#    except Exception:
#        TestFailScreenShots.get_screenshots(driver, tool_name, "validate_feature_count")
#        TestLog.log_creation(tool_name, "validate_feature_count", index, ws_index)


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
                    return False
                else:
                    return True


def validate_feature_circle_count(driver, category_sub_layer_name, tool_name, index, ws_index):

    """ Validation for feature count present on map """
#    try:
    layer_name_feature_svg_tag = driver.find_elements_by_tag_name("svg")
    for item in layer_name_feature_svg_tag:
        layer_name_feature_g_tag = item.find_elements_by_tag_name("g")
        for item1 in layer_name_feature_g_tag:
            layer_name_feature_get_attribute = item1.get_attribute("id")
            if category_sub_layer_name in layer_name_feature_get_attribute:
                layer_name_feature_image_tag = item1.find_elements_by_tag_name("circle")
                layer_name_feature_image_tag_count = len(layer_name_feature_image_tag)
                if layer_name_feature_image_tag_count == 0:
                    TestLog.log_creation(tool_name, "validate_feature_count", index, ws_index)
                else:
                    return True
# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
from GeoshieldCommonFiles import AppCommanUtility, AppCommanValidation, TestResults, TestLog, TestFailScreenShots


def click_widget_icon(driver, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to click on widget"""
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_coordinates_item, "click_widget_icon")
        TestLog.log_creation(tools_navigation_find_coordinates_item, "click_widget_icon", index, ws_index)


def click_advanced_search_item_find_coordinate(driver, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to click on tool find coordinate"""

    AppCommanUtility.click_widget_items(driver, tools_navigation_find_coordinates_item, index, ws_index)


def fill_data_navigation_find_coordinates(driver, ddl_tool_find_coordinates, ddl_select_coordinate_system_item, find_coordinates_textbox_longitude_text, find_coordinates_textbox_latitude_text, find_coordinates_textbox_long_min_text, find_coordinates_textbox_lat_min_text, find_coordinates_textbox_long_sec, find_coordinates_textbox_lat_sec, find_coordinate_textbox_UTM_zone_text, find_coordinate_textbox_easting_text, find_coordinate_textbox_northing_text, find_coordinate_textbox_zone_text, find_coordinate_textbox_zdl_text, find_coordinate_textbox_letter_text, find_coordinate_textbox_EN_text, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to fill the data in find coordinates tool """

    fill_data_find_coordinate_tool(driver, ddl_tool_find_coordinates, tools_navigation_find_coordinates_item, index, ws_index)
    select_ddl_item_find_coordinate(driver, ddl_select_coordinate_system_item, tools_navigation_find_coordinates_item, index, ws_index)

    if ddl_select_coordinate_system_item == "DD":
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. -100", find_coordinates_textbox_longitude_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 35", find_coordinates_textbox_latitude_text)
        click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index)

    elif ddl_select_coordinate_system_item == "Deg. Min.":
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. -106", find_coordinates_textbox_longitude_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 39", find_coordinates_textbox_latitude_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 24", find_coordinates_textbox_long_min_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 12", find_coordinates_textbox_lat_min_text)
        click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index)

    elif ddl_select_coordinate_system_item == "DMS":
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. -108", find_coordinates_textbox_longitude_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 41", find_coordinates_textbox_latitude_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 7", find_coordinates_textbox_long_min_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 17", find_coordinates_textbox_lat_min_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 3", find_coordinates_textbox_long_sec)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 32", find_coordinates_textbox_lat_sec)
        click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index)

    elif ddl_select_coordinate_system_item == "UTM":

        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 12", find_coordinate_textbox_UTM_zone_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 386003", find_coordinate_textbox_easting_text)
        AppCommanUtility.fill_data_tools_fields(driver, "Eg. 3552725", find_coordinate_textbox_northing_text)
        click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index)

    elif ddl_select_coordinate_system_item == "MGRS":

        find_coordinates_content(driver, "findCordMGRSCoordinateSystem", "Zone", find_coordinate_textbox_zone_text, tools_navigation_find_coordinates_item, index, ws_index)
        find_coordinates_content(driver, "findCordMGRSCoordinateSystem", "ZDL", find_coordinate_textbox_zdl_text, tools_navigation_find_coordinates_item, index, ws_index)
        find_coordinates_content(driver, "findCordMGRSCoordinateSystem", "2-Letters", find_coordinate_textbox_letter_text, tools_navigation_find_coordinates_item, index, ws_index)
        find_coordinates_content(driver, "findCordMGRSCoordinateSystem", "E-N", find_coordinate_textbox_EN_text, tools_navigation_find_coordinates_item, index, ws_index)
        click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index)

    elif ddl_select_coordinate_system_item == "USNG":

        find_coordinates_content(driver, "findCordUSNGCoordinateSystem", "Zone", find_coordinate_textbox_zone_text, tools_navigation_find_coordinates_item, index, ws_index)
        find_coordinates_content(driver, "findCordUSNGCoordinateSystem", "ZDL", find_coordinate_textbox_zdl_text, tools_navigation_find_coordinates_item, index, ws_index)
        find_coordinates_content(driver, "findCordUSNGCoordinateSystem", "2-Letters", find_coordinate_textbox_letter_text, tools_navigation_find_coordinates_item, index, ws_index)
        find_coordinates_content(driver, "findCordUSNGCoordinateSystem", "E-N", find_coordinate_textbox_EN_text, tools_navigation_find_coordinates_item, index, ws_index)
        click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index)

    AppCommanUtility.widget_close_icon(driver, tools_navigation_find_coordinates_item, index, ws_index)


def fill_data_find_coordinate_tool(driver, find_coordinate_item, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to fill the data in find direction tool """
    try:
        find_cord_system_container = driver.find_elements_by_class_name("findCordSystemContainer")
        for item in find_cord_system_container:
            cord_system_label = item.find_element_by_class_name("cordSystemLabel")
            if cord_system_label.text == find_coordinate_item:
                dijit_arrow_button_container = item.find_element_by_class_name("dijitArrowButtonContainer")
                dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitArrowButtonInner")
                dijit_arrow_button_inner.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_coordinates_item, "fill_data_find_coordinate_tool")
        TestLog.log_creation(tools_navigation_find_coordinates_item, "fill_data_find_coordinate_tool", index, ws_index)


def fill_data_find_coordinate_tool_textbox(driver, find_coordinate_item, find_coordinate_item_text):

    """ Method to fill the data in textboxes of find direction tool """

    find_cord_system_container = driver.find_elements_by_class_name("findCordSystemContainer")
    for item in find_cord_system_container:
        cord_system_label = item.find_element_by_class_name("cordSystemLabel")
        if cord_system_label.text == find_coordinate_item:
            dijit_arrow_button_container = item.find_element_by_class_name("dijitInputContainer")
            dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitInputInner")
            dijit_arrow_button_inner.clear()
            dijit_arrow_button_inner.send_keys()
            time.sleep(1)
            break


def find_coordinates_content(driver, attribute_text, find_coordinate_item, tool_field_text_box_text, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to fill the data in find coordinates tool """
    try:
        find_coordinates_content = driver.find_element_by_class_name("findCoordinatesContent")
        find_coordinates_content_div = find_coordinates_content.find_elements_by_tag_name("div")
        for item in find_coordinates_content_div:
            find_coordinates_content_div_attribute = item.get_attribute("data-dojo-attach-point")
            if find_coordinates_content_div_attribute == attribute_text:
                find_Coordinates_Elements = item.find_elements_by_class_name("findCoordinatesElements")
                for item1 in find_Coordinates_Elements:
                    if find_coordinate_item in item1.text:
                        dijit_input_container = item1.find_element_by_class_name("dijitInputContainer")
                        dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
                        dijit_input_inner.clear()
                        dijit_input_inner.send_keys(tool_field_text_box_text)
                        break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_coordinates_item, "find_coordinates_content")
        TestLog.log_creation(tools_navigation_find_coordinates_item, "find_coordinates_content", index, ws_index)


def click_ok_btn(driver, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to click on OK button of find coordinates tool"""
    try:
        find_button = driver.find_element_by_class_name("findButton")
        find_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_coordinates_item, "click_ok_btn")
        TestLog.log_creation(tools_navigation_find_coordinates_item, "click_ok_btn", index, ws_index)


def find_coordinates_tool_validation(driver, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to validate the tool find coordinates """

    AppCommanUtility.click_down_panel(driver, tools_navigation_find_coordinates_item, index, ws_index)
    AppCommanUtility.click_select_layer_label_container(driver, tools_navigation_find_coordinates_item, index, ws_index)
    AppCommanUtility.click_right_panel_open(driver, False, tools_navigation_find_coordinates_item, index, ws_index)
    AppCommanUtility.click_graphics_tab(driver, tools_navigation_find_coordinates_item, index, ws_index)
    AppCommanValidation.validate_right_panel_layer_name(driver, tools_navigation_find_coordinates_item, tools_navigation_find_coordinates_item, index, ws_index)

    AppCommanUtility.click_bottom_panel_layer(driver, tools_navigation_find_coordinates_item, tools_navigation_find_coordinates_item, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tools_navigation_find_coordinates_item, index, ws_index)
    AppCommanValidation.validate_feature_circle_count(driver, "findCoordinates", tools_navigation_find_coordinates_item, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)


def select_ddl_item_find_coordinate(driver, ddl_item_text, tools_navigation_find_coordinates_item, index, ws_index):

    """ Method to select the drop down item of find coordinate tool """
    try:
        dijit_menu_item = driver.find_elements_by_class_name("dijitMenuItem")
        for item in dijit_menu_item:
            if item.text == ddl_item_text:
                item.click()
                time.sleep(1)
                return True
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_coordinates_item,  "select_ddl_item_find_coordinate")
        TestLog.log_creation(tools_navigation_find_coordinates_item, "select_ddl_item_find_coordinate", index, ws_index)
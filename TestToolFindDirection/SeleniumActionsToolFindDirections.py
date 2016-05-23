# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time

import ToolValidation
from GeoshieldCommonFiles import AppCommanUtility, TestFailScreenShots, TestLog, TestResults


def click_widget_icon(driver, tools_navigation_find_direction_item, index, ws_index):

    """ Method to click on widget tool """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_direction_item, "click_widget_icon")
        TestLog.log_creation(tools_navigation_find_direction_item, "click_widget_icon", index, ws_index)


def click_advanced_search_item_find_direction(driver, tools_navigation_find_direction_item, find_direction_from_address, find_direction_to_address, tools_navigation_find_direction_item_widget_text, travel_mode_find_direction, index, ws_index):

    """ Method to fill the data in find direction tool """

    AppCommanUtility.click_widget_items(driver, tools_navigation_find_direction_item, index, ws_index)

    enter_address_find_direction(driver, "esri_dijit_Geocoder_1_input", find_direction_from_address, tools_navigation_find_direction_item, index, ws_index)
    enter_address_find_direction(driver, "esri_dijit_Geocoder_2_input", find_direction_to_address, tools_navigation_find_direction_item, index, ws_index)
#    select_find_direction_travel_mode(driver, travel_mode_find_direction, tools_navigation_find_direction_item, index, ws_index)
    time.sleep(0.5)

    click_btn_find_direction(driver, "Get Directions")
    time.sleep(1)

    AppCommanUtility.click_popup_close_icon(driver, tools_navigation_find_direction_item_widget_text)
    AppCommanUtility.widget_close_icon(driver, tools_navigation_find_direction_item_widget_text, index, ws_index)

    ToolValidation.validate_route_find_direction_tool(driver)

    TestResults.open_py_excel_pass(index, ws_index)


def enter_address_find_direction(driver, attribute_text, address_text, tools_navigation_find_direction_item, index, ws_index):

    """ Method to enter the address in find direction fields """
    try:
        time.sleep(2)
        directions_input_container = driver.find_elements_by_class_name("directionsInputContainer")
        for item in directions_input_container:
            find_direction_content_div = item.find_elements_by_tag_name("input")
            for item1 in find_direction_content_div:
                find_direction_content_div_get_attribute = item1.get_attribute("id")
                if find_direction_content_div_get_attribute == attribute_text:
                    item1.clear()
                    item1.send_keys(address_text)
                    time.sleep(1)
                    break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_direction_item, "enter_address_find_direction")
        TestLog.log_creation(tools_navigation_find_direction_item, "enter_address_find_direction", index, ws_index)


def click_btn_find_direction(driver, find_direction_btn_text):

    """ Method to perform click action on find direction button """

    try:
        esri_stops_get_directions = driver.find_element_by_class_name("esriStopsGetDirectionsContainer")
        esri_stops_get_directions_div = esri_stops_get_directions.find_elements_by_tag_name("div")
        for item in esri_stops_get_directions_div:
            if item.text == find_direction_btn_text:
                item.click()
                break
    except Exception:
        return True


def select_find_direction_travel_mode(driver, travel_mode_find_direction, tools_navigation_find_direction_item, index, ws_index):

    """ Method to perform to select the travel mode """
    try:
        time.sleep(2)
        esri_travel_modes_container = driver.find_element_by_class_name("esriTravelModesContainer")
        esri_directions_button = esri_travel_modes_container.find_elements_by_class_name("esriDirectionsButton")
        for item in esri_directions_button:
            if item.text == travel_mode_find_direction:
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_find_direction_item, "select_find_direction_travel_mode")
        TestLog.log_creation(tools_navigation_find_direction_item, "select_find_direction_travel_mode", index, ws_index)


# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

from GeoshieldCommonFiles import AppCommanUtility, AppCommanValidation, TestFailScreenShots, TestLog, TestResults
import time


def click_widget_icon(driver, tools_navigation_show_coordinates_item, index, ws_index):

    """ Method to click on widget icon"""
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_show_coordinates_item, "click_widget_icon")
        TestLog.log_creation(tools_navigation_show_coordinates_item, "click_widget_icon", index, ws_index)


def click_advanced_search_item_search_coordinate(driver, tools_navigation_show_coordinates_item, index, ws_index):

    """ Method to click on tool search coordinate """

    AppCommanUtility.click_widget_items(driver, tools_navigation_show_coordinates_item, index, ws_index)


def fill_data_navigation_show_coordinates_tool(driver, show_coordinate_lable, tools_navigation_show_coordinates_item, index, ws_index):

    """ Method to fill the data in tool show coordinates"""

    select_coordinate_system(driver, show_coordinate_lable, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanUtility.click_on_map(driver, tools_navigation_show_coordinates_item, index, ws_index)

    AppCommanUtility.widget_close_icon(driver, tools_navigation_show_coordinates_item, index, ws_index)


def select_coordinate_system(driver, show_coordinate_label, tools_navigation_show_coordinates_item, index, ws_index):

    """ Method to select the coordinate system """
    try:
        show_cords_item_place_holder = driver.find_elements_by_class_name("showCordsItemPlaceHolder")
        for item in show_cords_item_place_holder:
            show_cord_label = item.find_element_by_class_name("showCordLabel")
            if show_cord_label.text == show_coordinate_label:
                show_cord_checkbox_container = item.find_element_by_class_name("showCordCheckboxContainer")
                show_cord_checkbox_container.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_navigation_show_coordinates_item, "select_coordinate_system")
        TestLog.log_creation(tools_navigation_show_coordinates_item, "select_coordinate_system", index, ws_index)


def search_coordinates_tool_validation(driver, tools_navigation_show_coordinates_item, index, ws_index):

    """ Method to validate the tool search coordinates """

    AppCommanUtility.click_down_panel(driver, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanUtility.click_select_layer_label_container(driver, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanUtility.click_right_panel_open(driver, False, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanUtility.click_graphics_tab(driver, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanValidation.validate_right_panel_layer_name(driver, tools_navigation_show_coordinates_item, tools_navigation_show_coordinates_item, index, ws_index)

    AppCommanUtility.click_bottom_panel_layer(driver, tools_navigation_show_coordinates_item, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tools_navigation_show_coordinates_item, index, ws_index)
    AppCommanValidation.validate_feature_circle_count(driver, "showCoordinates", tools_navigation_show_coordinates_item, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)







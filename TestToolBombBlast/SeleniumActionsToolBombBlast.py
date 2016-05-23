# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
from GeoshieldCommonFiles import AppCommanUtility, TestLogBombBlast, TestLog, TestFailScreenShots
from GeoshieldCommonFiles import AppCommanValidation
import traceback


def click_widget_icon(driver, tools_utilities_bomb_blast_item, index, ws_index):

    """ Method to perform click action on widget tool"""
    #//div[@class='iconContainer']/div[@id='tools_img']
    try:
        time.sleep(2)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_bomb_blast_item, "click_widget_icon")
        TestLog.log_creation(tools_utilities_bomb_blast_item, "click_widget_icon", index, ws_index)


def click_bomb_blast_item_selection(driver, tools_utilities_bomb_blast_item, tool_bomb_blast_bomb_type, tool_bomb_blast_widget_name, index, ws_index):

    """ Method to perform click action on bomb blast item """

    AppCommanUtility.click_widget_items(driver, tools_utilities_bomb_blast_item, index, ws_index)
    time.sleep(0.5)
    select_bomb_item(driver, tool_bomb_blast_bomb_type, tools_utilities_bomb_blast_item, index, ws_index, class_name="bombThreatIconElement")
    AppCommanUtility.click_on_map(driver, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanUtility.widget_close_icon(driver, tool_bomb_blast_widget_name, index, ws_index)


def select_bomb_item(driver, tool_bomb_blast_bomb_type, tools_utilities_bomb_blast_item, index, ws_index, class_name):

    """ Method to perform selection of bomb blast item  """
    count = 0
    try:
        bomb_threat_icon_element = driver.find_elements_by_class_name(class_name)
        for item in bomb_threat_icon_element:
            bomb_threat_icon_element_title = item.get_attribute("title")
            if bomb_threat_icon_element_title == tool_bomb_blast_bomb_type:
                count = count + 1
                bomb_threat_icon_element_title_div = item.find_element_by_tag_name("div")
                bomb_threat_icon_element_title_div.click()
                time.sleep(1)
                break
        if count == 0:
            TestLog.log_creation(tools_utilities_bomb_blast_item, "select_bomb_item", index)
    except Exception:
        TestLog.log_creation(tools_utilities_bomb_blast_item, "select_bomb_item", index)


def tool_bomb_blast_validation(driver,index, tool_bomb_blast_widget_name, tools_utilities_bomb_blast_item, ws_index):

    """ Method to perform validation of tool bomb blast """

    AppCommanUtility.click_down_panel(driver, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanUtility.click_select_layer_label_container(driver, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanUtility.click_right_panel_open(driver, tools_utilities_bomb_blast_item, index, boolean_value=False, ws_index=7)
    AppCommanUtility.click_graphics_tab(driver, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanValidation.validate_right_panel_layer_name(driver, tool_bomb_blast_widget_name, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanUtility.click_bottom_panel_layer(driver, tool_bomb_blast_widget_name, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tools_utilities_bomb_blast_item, index, ws_index)
    AppCommanValidation.validate_feature_count(driver, tool_bomb_blast_widget_name, tools_utilities_bomb_blast_item, index, ws_index)
    TestLogBombBlast.open_py_excel_pass(index, ws_index)



# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
from GeoshieldCommonFiles import AppCommanUtility
from  GeoshieldCommonFiles import AppCommanValidation, TestLog, TestFailScreenShots, TestLogBombBlast


def click_widget_icon(driver, tool_name, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='basicDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_widget_icon")
        TestLog.log_creation(tool_name, "click_widget_icon", index, ws_index)


def click_select_date_value(driver, tool_name, index, ws_index):

    """ Method to perform to select date"""
    try:
        time.sleep(3)
        select_date_value = driver.find_element_by_class_name("selectedDateValue")
        select_date_value.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_select_date_value")
        TestLog.log_creation(tool_name, "click_select_date_value", index, ws_index)


def click_predefined_daterange_tab(driver, tool_name, index, ws_index):

    """ Method to perform actions on daterange and predefined tab """
    try:
        predefined_tab = driver.find_element_by_class_name("state-selected")
        predefined_tab.click()

        select_predefined_tab_type(driver,tool_name, index, ws_index, class_name="layerContentRow")

        date_range_tab_content = driver.find_element_by_class_name("removeRightBorder")
        date_range_tab_content.click()

        from_date_select_data_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_0']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
        from_date_select_data_range.click()

        select_from_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_0_popup']/tbody/tr[1]/td[4]")
        select_from_date.click()

        to_date_select_date_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_1']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
        to_date_select_date_range.click()

        time.sleep(2)
        select_to_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_1_popup']/tbody/tr[5]/td[1]")
        select_to_date.click()
        time.sleep(2)
        browse_ok_cancel_btn(driver, tool_name, index, ws_index)

    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_predefined_daterange_tab")
        TestLog.log_creation(tool_name, "click_predefined_daterange_tab", index, ws_index)


def select_predefined_tab_type(driver, tool_name, index, ws_index, class_name):

    """ Method to select the type of predefined tab"""
    try:
        predefined_tab_content = driver.find_elements_by_class_name(class_name)
        for item in predefined_tab_content:
            if item.text == "Last 4 days":
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "select_predefined_tab_type")
        TestLog.log_creation(tool_name, "select_predefined_tab_type", index, ws_index)


def browse_ok_cancel_btn(driver, tool_name, index, ws_index):

    """ Common Method to perform action on Ok button """
    try:
        click_ok_button = driver.find_element_by_class_name("okBtn")
        click_ok_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "browse_ok_cancel_btn")
        TestLog.log_creation(tool_name, "browse_ok_cancel_btn", index, ws_index)


def click_browse_container(driver, browse_tab_container_name, category_main_layer_name, category_sub_layer_name, tool_name, index, ws_index):

    """ Method to click on container of browse widget"""

    AppCommanUtility.click_browse_tab_item(driver, browse_tab_container_name, tool_name, index, ws_index)

    select_layer_browse_widget(driver, category_main_layer_name, category_sub_layer_name, tool_name, index, ws_index)


def select_layer_browse_widget(driver, category_main_layer_name, category_sub_layer_name, tool_name, index, ws_index):

    """ Method to select the layer"""

    AppCommanUtility.click_expand_button_div(driver, category_main_layer_name, tool_name, index, ws_index)
    AppCommanUtility.click_toggel_btn(driver, category_sub_layer_name, tool_name, index, ws_index)
    AppCommanUtility.click_expand_button_div(driver, category_main_layer_name, tool_name, index, ws_index)

    click_down_panel_div(driver, tool_name, index, ws_index)


def click_down_panel_div(driver, tool_name, index, ws_index):

    """ Method to click on down panel"""

    AppCommanUtility.click_down_panel(driver, tool_name, index, ws_index)
    click_select_layer_container(driver, tool_name, index, ws_index)
    click_right_panel_open(driver, tool_name, index, ws_index)


def click_select_layer_container(driver, tool_name, index, ws_index):

    """ Method to click on select layer container """

    AppCommanUtility.click_select_layer_label_container(driver, tool_name, index, ws_index)


def click_right_panel_open(driver, tool_name, index, ws_index):

    """ Method to click on right panel """

    AppCommanUtility.click_right_panel_open(driver,tool_name,index, boolean_value=True, ws_index=11)


def validate_browse_widget(driver, category_sub_layer_name, tool_name, index, ws_index):

    AppCommanValidation.validate_right_panel_layer_name(driver, category_sub_layer_name, tool_name, index, ws_index)
   # click_bottom_panel_layer_name(driver, tool_name, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tool_name, index, ws_index)
    AppCommanValidation.validate_feature_count(driver, category_sub_layer_name, tool_name, index, ws_index)
    TestLogBombBlast.open_py_excel_pass(index, ws_index)


def click_bottom_panel_layer_name(driver, tool_name, index, ws_index):

    """ Method to perfrom click action on bottom panel layer """
    try:
        layer_content_row = driver.find_elements_by_class_name("layerContentRow")
        for item in layer_content_row:
            if item.is_displayed():
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_bottom_panel_layer_name")
        TestLog.log_creation(tool_name, "click_bottom_panel_layer_name", index, ws_index)

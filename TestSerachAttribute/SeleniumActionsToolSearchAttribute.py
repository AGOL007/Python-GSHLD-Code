# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time

from GeoshieldCommonFiles import AppCommanValidation, AppCommanUtility, TestLog, TestFailScreenShots, TestResults


def click_widget_icon(driver, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_advanced_search_search_attribute_item, "click_widget_icon")
        TestLog.log_creation(tools_advanced_search_search_attribute_item, "click_widget_icon", index, ws_index)


def click_advanced_search_item_search_attribute(driver, advanced_search_item_search_attribute, index, ws_index):

    """ Method to perform click action on search attribute tool  """

    AppCommanUtility.click_widget_items(driver, advanced_search_item_search_attribute, index, ws_index)


def fill_data_search_attribute_new_query(driver, search_attribute_select_layer_textbox_text, search_attribute_textbox_Field_text, search_attribute_textbox_Operaror_text, search_attribute_textbox_Value_text, query_name, search_attribute_tool_name, search_attribute_sub_layer_name, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perform fill data in new query tool """

    fill_data_advanced_search_attribure_query(driver, "Select Layer", search_attribute_select_layer_textbox_text)

    fill_data_advanced_serach_attribute_query_ddl(driver, "Select Field", tools_advanced_search_search_attribute_item, index, ws_index)
    AppCommanUtility.select_ddl_item(driver, search_attribute_textbox_Field_text, tools_advanced_search_search_attribute_item, index, ws_index)

    fill_data_advanced_serach_attribute_query_ddl(driver, "Select Operator", tools_advanced_search_search_attribute_item, index, ws_index)
    AppCommanUtility.select_ddl_item(driver, search_attribute_textbox_Operaror_text, tools_advanced_search_search_attribute_item, index, ws_index)

    AppCommanUtility.fill_data_tools_fields(driver, "Eg: 10", search_attribute_textbox_Value_text)
    select_query_title(driver, query_name, tools_advanced_search_search_attribute_item, index, ws_index)

    attribute_query_savequery_button = driver.find_element_by_class_name("attributeQuerySaveQueryButton")
    attribute_query_savequery_button.click()
    time.sleep(1)

    AppCommanUtility.click_popup_close_icon(driver, search_attribute_tool_name)

    attribute_query_search_button = driver.find_element_by_class_name("attributeQuerySearchButton")
    attribute_query_search_button.click()
    time.sleep(1)

    AppCommanUtility.click_popup_close_icon(driver, search_attribute_tool_name)


def click_right_sub_panel_prior_query(driver, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perform click action on prior query """

    click_right_sub_panel(driver, "Prior Query", tools_advanced_search_search_attribute_item, index, ws_index)


def fill_data_search_attribute_prior_query(driver, query_name, search_attribute_tool_name, index, ws_index):

    """ Method to perform fill data in prior query """

    AppCommanUtility.fill_data_tools_fields(driver, "Select title", query_name)

    click_priority_ok_btn(driver, "OK", search_attribute_tool_name, index, ws_index)
    time.sleep(1)


def app_validation(driver, search_attribute_tool_name, search_attribute_select_layer_textbox_text, search_attribute_sub_layer_name, index, ws_index):

    """  Method to perform close action on popup """
    count = 0
    try:
        dijit_dialog_title_Bar = driver.find_elements_by_class_name("dijitDialogTitleBar")
        for item in dijit_dialog_title_Bar:
            dijit_dialog_title = item.find_element_by_class_name("dijitDialogTitle")
            dijit_dialog_close_icon = item.find_element_by_class_name("dijitDialogCloseIcon")
            if dijit_dialog_close_icon.is_displayed():
                if dijit_dialog_title.text == search_attribute_tool_name:
                    count = count + 1
                    dijit_dialog_close_icon.click()
                    time.sleep(2)
                    AppCommanUtility.widget_close_icon(driver, search_attribute_tool_name, index, ws_index)
                    break
        if count == 0:
            AppCommanUtility.widget_close_icon(driver, search_attribute_tool_name, index, ws_index)
            tool_search_attribute_validation(driver, search_attribute_select_layer_textbox_text, search_attribute_sub_layer_name, search_attribute_tool_name, index, ws_index)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, search_attribute_tool_name, "app_validation")
        TestLog.log_creation(search_attribute_tool_name, "app_validation", index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)


def tool_search_attribute_validation(driver, search_attribute_select_layer_textbox_text, search_attribute_sub_layer_name, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perfrom validation of search attribute """

    AppCommanUtility.click_down_panel(driver, tools_advanced_search_search_attribute_item, index, ws_index)
    AppCommanUtility.click_select_layer_label_container(driver, tools_advanced_search_search_attribute_item, index, ws_index)
    AppCommanUtility.click_right_panel_open(driver, tools_advanced_search_search_attribute_item, index, True, ws_index)
    AppCommanValidation.validate_right_panel_layer_name(driver, search_attribute_select_layer_textbox_text, tools_advanced_search_search_attribute_item, index, ws_index)
    click_bottom_panel_layer_name(driver, tools_advanced_search_search_attribute_item, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tools_advanced_search_search_attribute_item, index, ws_index)
    AppCommanValidation.validate_feature_count(driver, search_attribute_select_layer_textbox_text, tools_advanced_search_search_attribute_item, index, ws_index)


def fill_data_advanced_search_attribure_query(driver, search_attribute_item, search_attribute_text_box_text):

    """ Method to fill the data in search attribute  """

    attribute_query_row = driver.find_elements_by_class_name("attributeQueryRow")
    for item in attribute_query_row:
        attribute_query_cell_label = item.find_element_by_class_name("attributeQueryCellLabel")
        if attribute_query_cell_label.text == search_attribute_item:
            try:
                dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
                dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
                dijit_input_inner.clear()
                dijit_input_inner.send_keys(search_attribute_text_box_text)
                break
            except Exception:
                continue


def fill_data_advanced_serach_attribute_query_ddl(driver, agency_feed_place_holder_text, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perfrom click action on dropdown """
    try:
        search_finder_div_text_box = driver.find_elements_by_class_name("dijitValidationTextBox")
        for item in search_finder_div_text_box:
            search_finder_div_text_box_one = item.find_element_by_class_name("dijitInputContainer")
            search_finder_div_text_box_one_placeholder = search_finder_div_text_box_one.find_element_by_class_name("dijitPlaceHolder")
            if search_finder_div_text_box_one_placeholder.text == agency_feed_place_holder_text:
                dijit_arrow_button_container = item.find_element_by_class_name("dijitArrowButtonContainer")
                dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitArrowButtonInner")
                dijit_arrow_button_inner.click()
                time.sleep(1)
                return True
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_advanced_search_search_attribute_item, "fill_data_advanced_serach_attribute_query_ddl")
        TestLog.log_creation(tools_advanced_search_search_attribute_item, "fill_data_advanced_serach_attribute_query_ddl", index, ws_index)


def select_query_title(driver, query_name, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to select the query name """
    try:
        save_query_div = driver.find_element_by_class_name("saveQueryDiv")
        dijit_textBox = save_query_div.find_element_by_class_name("dijitInputContainer")
        dijit_input_inner = dijit_textBox.find_element_by_class_name("dijitInputInner")
        dijit_input_inner.send_keys(query_name)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_advanced_search_search_attribute_item, "select_query_title")
        TestLog.log_creation(tools_advanced_search_search_attribute_item, "select_query_title", index, ws_index)


def click_right_sub_panel(driver, right_panel_name, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to click on right sub panel """
    try:
        remove_right_border = driver.find_elements_by_class_name("removeRightBorder")
        for item in remove_right_border:
            if item.text == right_panel_name:
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_advanced_search_search_attribute_item, "click_right_sub_panel")
        TestLog.log_creation(tools_advanced_search_search_attribute_item, "click_right_sub_panel", index, ws_index)


def click_priority_ok_btn(driver, priority_btn_text, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perfrom click action on New query OK button """
    try:
        attribute_query_prior_query_button = driver.find_elements_by_class_name("attributeQueryPriorQueryButton")
        for item in attribute_query_prior_query_button:
            if item.text == priority_btn_text:
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_advanced_search_search_attribute_item, "click_priority_ok_btn")
        TestLog.log_creation(tools_advanced_search_search_attribute_item, "click_priority_ok_btn", index, ws_index)


def click_bottom_panel_layer_name(driver, tools_advanced_search_search_attribute_item, index, ws_index):

    """ Method to perfrom click action on bottom panel layer """
    try:
        layer_content_row = driver.find_elements_by_class_name("layerContentRow")
        for item in layer_content_row:
            if item.is_displayed():
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_advanced_search_search_attribute_item, "click_bottom_panel_layer_name")
        TestLog.log_creation(tools_advanced_search_search_attribute_item, "click_bottom_panel_layer_name", index, ws_index)

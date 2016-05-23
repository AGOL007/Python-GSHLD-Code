# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


import time
from GeoshieldCommonFiles import AppCommanValidation, AppCommanUtility, TestFailScreenShots, TestLog, TestResults


def select_browse_tab_layer(driver, main_layer_name, sub_layer_name, tools_utilities_selection_item, index, ws_index):

    """ Method to select the layer from browse tab """

    AppCommanUtility.click_expand_button_div(driver, main_layer_name, tools_utilities_selection_item, index, ws_index)
    AppCommanUtility.click_toggel_btn(driver, sub_layer_name, tools_utilities_selection_item, index, ws_index)


def click_widget_icon(driver, tools_utilities_selection_item, index, ws_index):

    """ Method to click on widget tool """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_selection_item, "click_widget_icon")
        TestLog.log_creation(tools_utilities_selection_item, "click_widget_icon", index, ws_index)


def click_utilities_item_selection(driver, tools_utilities_selection_item, sub_layer_name, tool_selection_textbox_distance_text, index, ws_index):

    """ Method to select the tool Selection and fill the data in buffer tab of selection"""

    AppCommanUtility.click_widget_items(driver, tools_utilities_selection_item, index, ws_index)

    utilities_selection_ddl_list(driver, "Select Layer", tools_utilities_selection_item, index, ws_index, class_name="selectBufferRow", class_name_label="selectBufferCellLabel")
    AppCommanUtility.select_ddl_item(driver, sub_layer_name, tools_utilities_selection_item, index, ws_index)

    fill_data_utilities_selection(driver, "Distance", tool_selection_textbox_distance_text, tools_utilities_selection_item, index, ws_index, class_name="selectBufferRow", class_name_label="selectBufferCellLabel")

    utilities_selection_ddl_list(driver, "Unit", tools_utilities_selection_item, index, ws_index, class_name="selectBufferRow", class_name_label="selectBufferCellLabel")
    AppCommanUtility.select_ddl_item(driver, "Miles", tools_utilities_selection_item, index, ws_index)

    AppCommanUtility.select_buffer_graphic_icons(driver, "Draw Point")

    AppCommanUtility.click_on_map(driver, tools_utilities_selection_item, index, ws_index)

    tool_selection_click_ok_btn(driver, class_name="proximityButton", index=0)

    AppCommanUtility.click_minimize_btn(driver, tools_utilities_selection_item, index, ws_index)


def click_utilities_item_selection_proximity(driver, tools_utilities_selection_item, sub_layer_name, tool_selection_textbox_distance_text, index, ws_index):

    """ Method to select the tab proximity and fill data in proximity """

    AppCommanUtility.click_maximize_btn(driver, tools_utilities_selection_item, index, ws_index)

    AppCommanUtility.select_sub_tool(driver, "Proximity", index, ws_index, class_name="removeRightBorder")

    utilities_selection_ddl_list(driver, "Primary Objects Layer", tools_utilities_selection_item, index, ws_index, class_name="proximityRowContainer", class_name_label="proximityLabelText")
    AppCommanUtility.select_ddl_item(driver, sub_layer_name, tools_utilities_selection_item, index, ws_index)

    fill_data_utilities_selection(driver, "Distance", tool_selection_textbox_distance_text, tools_utilities_selection_item, index, ws_index, class_name="proximityRowContainer", class_name_label="proximityLabelText")

    utilities_selection_ddl_list(driver, "Unit", tools_utilities_selection_item, index, ws_index, class_name="proximityRowContainer", class_name_label="proximityLabelText")
    AppCommanUtility.select_ddl_item(driver, "Miles", tools_utilities_selection_item, index, ws_index)

    utilities_selection_ddl_list(driver, "Nearby Objects Layer", tools_utilities_selection_item, index, ws_index, class_name="proximityRowContainer", class_name_label="proximityLabelText")
    AppCommanUtility.select_ddl_item(driver, sub_layer_name, tools_utilities_selection_item, index, ws_index)

    tool_selection_click_ok_btn(driver, class_name="proximityButton", index=1)
    time.sleep(1)


def utilities_selection_ddl_list(driver, selection_text_box, tools_utilities_selection_item, index, ws_index, class_name, class_name_label):

    """ Method to perform selection of drop down list """
    try:
        selection_tab_content = driver.find_elements_by_class_name(class_name)
        for item in selection_tab_content:
            selection_label_elements = item.find_element_by_class_name(class_name_label)
            if selection_label_elements.text == selection_text_box:
                dijit_arrow_button_container = item.find_element_by_class_name("dijitArrowButtonContainer")
                dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitArrowButtonInner")
                dijit_arrow_button_inner.click()
                time.sleep(1)
                return True
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_selection_item, "utilities_selection_ddl_list")
        TestLog.log_creation(tools_utilities_selection_item, "utilities_selection_ddl_list", index, ws_index)


def fill_data_utilities_selection(driver, selection_text_box, tools_utilities_selection_item, index, ws_index, selection_text_box_text, class_name, class_name_label):

    """ Method to fill data in fields of selection tool """
    try:
        selection_tab_content = driver.find_elements_by_class_name(class_name)
        for item in selection_tab_content:
            selection_label_elements = item.find_element_by_class_name(class_name_label)
            if selection_label_elements.text == selection_text_box:
                dijit_arrow_button_container = item.find_element_by_class_name("dijitInputContainer")
                dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitInputInner")
                dijit_arrow_button_inner.clear()
                dijit_arrow_button_inner.send_keys(selection_text_box_text)
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_selection_item, "fill_data_utilities_selection")
        TestLog.log_creation(tools_utilities_selection_item, "fill_data_utilities_selection", index, ws_index)


def tool_selection_buffer_validation(driver, tools_utilities_selection_item, index, ws_index):

    """ Method to validate buffer tab"""

    AppCommanUtility.click_down_panel(driver, tools_utilities_selection_item, index, ws_index)
    AppCommanUtility.click_select_layer_label_container(driver, tools_utilities_selection_item, index, ws_index)
    AppCommanUtility.click_right_panel_open(driver, True, tools_utilities_selection_item, index, ws_index)
#    AppCommanUtility.click_graphics_tab(driver)
    AppCommanValidation.validate_right_panel_layer_name(driver, tools_utilities_selection_item, tools_utilities_selection_item, index, ws_index)
    AppCommanUtility.click_bottom_panel_layer(driver, "Select Buffer Results", tools_utilities_selection_item, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tools_utilities_selection_item, index, ws_index)
    AppCommanValidation.validate_feature_count(driver, "proximityResultLayer", tools_utilities_selection_item, index, ws_index)


def tool_selection_proximity_validation(driver, tools_utilities_selection_item, index, ws_index):

    """ Method to validate proximity tab """

    AppCommanUtility.widget_close_icon(driver, tools_utilities_selection_item, index, ws_index)
    AppCommanUtility.click_select_layer_label_container(driver, tools_utilities_selection_item, index, ws_index)
    AppCommanValidation.validate_right_panel_layer_name(driver, tools_utilities_selection_item, tools_utilities_selection_item, index, ws_index)
    AppCommanUtility.click_bottom_panel_layer(driver, "Proximity Results", tools_utilities_selection_item, index, ws_index)
    AppCommanValidation.validate_feature_count_panel(driver, tools_utilities_selection_item, index, ws_index)
    AppCommanValidation.validate_feature_count(driver, "proximityResultLayer", tools_utilities_selection_item, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)


def tool_selection_click_ok_btn(driver, class_name, index):

    """ Method to click on OK button of tool selection """

    proximity_button = driver.find_elements_by_class_name(class_name)
    proximity_button[index].click()
    time.sleep(2)










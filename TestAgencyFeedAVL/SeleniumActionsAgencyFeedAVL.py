# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
from GeoshieldCommonFiles import TestLog, TestFailScreenShots, AppCommanUtility, AppCommanValidation, TestResults


def click_widget_icon(driver, agency_feed_avl, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_avl, "click_widget_icon")
        TestLog.log_creation(agency_feed_avl, "click_widget_icon", index, ws_index)


def click_agency_feed_avl(driver, agency_feed_avl, index, ws_index):

    AppCommanUtility.click_widget_items(driver, agency_feed_avl, index, ws_index)

    click_avl_live_select_all_checkbox(driver, agency_feed_avl, index, ws_index)

    click_okbtn_avl_live_tab(driver, agency_feed_avl, index, ws_index)


def click_avl_live_select_all_checkbox(driver, agency_feed_avl, index, ws_index):
    count = 0
    avl_live_section = driver.find_elements_by_class_name("avlLiveSection")
    for item in avl_live_section:
        try:
            avl_live_section_div = item.find_element_by_class_name("liveSectionItemCheckBox")
            avl_live_section_div.click()
            count = count + 1
            time.sleep(1)
        except Exception:
            continue
    if count == 0:
        TestFailScreenShots.get_screenshots(driver, agency_feed_avl, "click_avl_live_select_all_checkbox")
        TestLog.log_creation(agency_feed_avl, "click_avl_live_select_all_checkbox", index, ws_index)


def click_okbtn_avl_live_tab(driver, agency_feed_avl, index, ws_index):
    try:
        avl_ok_content = driver.find_element_by_class_name("avlOkContent")
        avl_ok_content.click()
        time.sleep(2)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_avl, "click_okbtn_avl_live_tab")
        TestLog.log_creation(agency_feed_avl, "click_okbtn_avl_live_tab", index, ws_index)


def validate_avl_live_tab(driver, agency_feed_avl, avl_live_layer_name, index, ws_index):

    try:
        avl_live_layer = driver.find_element_by_id("avlLive_layer")
        if avl_live_layer.is_displayed():
            AppCommanUtility.click_minimize_btn(driver, agency_feed_avl, index, ws_index)

            AppCommanUtility.click_down_panel(driver, agency_feed_avl, index, ws_index)

            AppCommanUtility.click_select_layer_label_container(driver, agency_feed_avl, index, ws_index)

            AppCommanValidation.validate_layer_name(driver, avl_live_layer_name, agency_feed_avl, index, ws_index, boolean_value=True)

            AppCommanUtility.click_live_tab(driver, agency_feed_avl, index, ws_index)

            AppCommanValidation.validate_right_panel_layer_name(driver, avl_live_layer_name, agency_feed_avl, index, ws_index)

            AppCommanValidation.validate_feature_count(driver, "avlLive", agency_feed_avl, index, ws_index)

            AppCommanUtility.click_maximize_btn(driver, agency_feed_avl, index, ws_index)

            TestResults.open_py_excel_pass(index, ws_index)

        else:
            AppCommanUtility.click_popup_close_icon(driver, agency_feed_avl)

    except Exception:

        AppCommanUtility.click_popup_close_icon(driver, agency_feed_avl)


def click_right_tab_historic(driver, agency_feed_item_avl_unitid_text, agency_feed_avl, index, ws_index):

    AppCommanUtility.select_sub_tool(driver, "Historic", index, ws_index, class_name="removeRightBorder")

    agency_feed_avl_fill_data(driver, "Unit Id", agency_feed_avl, index, ws_index)

    agency_feed_date_fill_date(driver, "Select by Unit")

    fill_data_select_date(driver)

    click_okbtn_historic_select_by_unit_tab(driver, agency_feed_avl, index, ws_index)


def agency_feed_avl_fill_data(driver, agency_feed_avl_item, agency_feed_avl_textbox_text, index, ws_index):

    """ Common method to perform actions in AVL tab of agency feed """
    try:
        avl_tab_content = driver.find_elements_by_class_name("avlTabContent")
        for item in avl_tab_content:
            avl_live_textbox = item.find_element_by_class_name("avlLiveTextBox")
            if avl_live_textbox.text == agency_feed_avl_item:
                dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
                dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
                dijit_input_inner.clear()
                dijit_input_inner.send_keys(agency_feed_avl_textbox_text)

    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_avl_item, "agency_feed_avl_fill_data")
        TestLog.log_creation(agency_feed_avl_item, "agency_feed_avl_fill_data", index, ws_index)


def agency_feed_date_fill_date(driver, avl_date_text):

    """ Method to perform fill date in agency feed """

    avl_round_container = driver.find_elements_by_class_name("avlRoundContainer")
    for item in avl_round_container:
        avl_live_textBox = driver.find_elements_by_class_name("avlRadioButtonLabel")
        for item1 in avl_live_textBox:
            dijit_input_container = item.find_elements_by_class_name("dijitInputContainer")
            for item2 in dijit_input_container:
                if item1.text == avl_date_text:
                    dijit_input_inner = item2.find_element_by_class_name("dijitInputInner")
                    dijit_input_inner.clear()
                    dijit_input_inner.send_keys("12/21/2011")
                    return True


def fill_data_select_date(driver):

    to_date_select_date_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_3']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
    to_date_select_date_range.click()

    dijit_calendar_year_label = driver.find_element_by_xpath(".//*[@id='dijit_form_DateTextBox_3_popup']/tfoot/tr/td/div/span[1]")
    dijit_calendar_year_label.click()

    time.sleep(2)
    select_to_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_3_popup']/tbody/tr[5]/td[1]")
    select_to_date.click()


def click_okbtn_historic_select_by_unit_tab(driver, agency_feed_avl, index, ws_index):
    try:
        avl_ok_content = driver.find_elements_by_class_name("avlOkContent")
        avl_ok_content[1].click()
        time.sleep(2)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_avl, "click_okbtn_historic_select_by_unit_tab")
        TestLog.log_creation(agency_feed_avl, "click_okbtn_historic_select_by_unit_tab", index, ws_index)
    try:
        avl_historic_layer = driver.find_element_by_id("avlHistoricLayer_layer")
        if avl_historic_layer.is_displayed():
            AppCommanUtility.click_minimize_btn(driver, agency_feed_avl, index, ws_index)

            AppCommanUtility.click_down_panel(driver, agency_feed_avl, index, ws_index)

            AppCommanUtility.click_select_layer_label_container(driver, agency_feed_avl, index, ws_index)

            AppCommanValidation.validate_layer_name(driver, "AVL Historic Layer", agency_feed_avl, index, ws_index, boolean_value=True)

            AppCommanValidation.validate_right_panel_layer_name(driver, "AVL Historic Layer", agency_feed_avl, index, ws_index)

            AppCommanValidation.validate_agency_feed_avl_historic_tab(driver, "avlHistoricLayer")

            AppCommanUtility.click_maximize_btn(driver, agency_feed_avl, index, ws_index)

    except Exception:
        AppCommanUtility.click_popup_close_icon(driver, agency_feed_avl)


def click_historic_select_by_area_tab(driver, agency_feed_avl_distance_textbox, agency_feed_avl, index, ws_index):

    #"avlDeactiveRadioButton"

    avl_deactive_radio_button = driver.find_element_by_class_name("avlDeactiveRadioButton")
    avl_deactive_radio_button.click()

    select_geometry_tab(driver)

    AppCommanUtility.click_on_map(driver, agency_feed_avl, index, ws_index)

    agency_feed_avl_fill_data(driver, "Distance", agency_feed_avl_distance_textbox, index, ws_index)

#    agency_feed_date_fill_date(driver, "Select by Area")

    click_okbtn_select_by_area(driver)

    AppCommanUtility.click_popup_close_icon(driver, agency_feed_avl)

    AppCommanUtility.widget_close_icon(driver, agency_feed_avl, index, ws_index)

    validate_select_by_area_buffer(driver)


def select_geometry_tab(driver):

    """ Method to select geometry of AVL tab of agency feed """

    avl_live_textBox = driver.find_elements_by_class_name("simpleDrawGraphicsElements")
    for item in avl_live_textBox:
        try:
            simple_draw_point = item.find_element_by_class_name("simpleDrawPoint")
            simple_draw_point.click()
            time.sleep(2)
        except Exception:
            continue


def click_okbtn_select_by_area(driver):
    avl_ok_content = driver.find_elements_by_class_name("avlOkContent")
    avl_ok_content[2].click()
    time.sleep(2)


def validate_select_by_area_buffer(driver):

    try:
        avlDraw_buffer_layer = driver.find_element_by_id("avlDrawBufferLayer_layer")
        if avlDraw_buffer_layer.is_dispalyed():
            return True
        else:
            return False
    except Exception:
        return False
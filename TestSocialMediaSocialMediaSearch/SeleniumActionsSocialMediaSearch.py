# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


import time
import SocialMediaSearchValidation
from GeoshieldCommonFiles import AppCommanValidation, AppCommanUtility, TestLog, TestFailScreenShots, TestResults


def click_widget_icon(driver, social_media_social_media_search, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_social_media_search, "click_widget_icon")
        TestLog.log_creation(social_media_social_media_search, "click_widget_icon", index, ws_index)


def click_social_media_item_social_media_search(driver, social_media_social_media_search, social_media_search_distance_textbox_text, social_media_search_keyword_textbox_text, social_media_search_refreshtime_textbox_text, index, ws_index):

    AppCommanUtility.click_widget_items(driver, social_media_social_media_search, index, ws_index)

    fill_data_social_media_search_textbox(driver, "Distance", social_media_search_distance_textbox_text, social_media_social_media_search, index, ws_index, class_name="tableCellLabel")
    fill_data_social_media_search_textbox(driver, "Keyword", social_media_search_keyword_textbox_text, social_media_social_media_search, index, ws_index, class_name="tableCellLabel")
    check_box_social_media_search(driver, "Twitter", social_media_social_media_search, index, ws_index,)
    check_box_social_media_search(driver, "Youtube", social_media_social_media_search, index, ws_index,)

    fill_data_select_date(driver, social_media_social_media_search, index, ws_index)

    select_geometry_social_media_search(driver, social_media_social_media_search, index, ws_index)


def fill_data_social_media_search_textbox(driver, social_media_search_textbox, social_media_search_textbox_text, social_media_social_media_search, index, ws_index, class_name):

    """ Common method to perform actions in social media search """
    try:
        search_social_media_search_div = driver.find_elements_by_class_name("rowContainer")
        for item in search_social_media_search_div:
            search_social_media_label = item.find_elements_by_class_name(class_name)
            for item1 in search_social_media_label:
                if item1.text == social_media_search_textbox:
                    search_social_media_search_div_textbox_one = item.find_element_by_class_name("dijitInputInner")
                    search_social_media_search_div_textbox_one.clear()
                    search_social_media_search_div_textbox_one.send_keys(social_media_search_textbox_text)
                    time.sleep(1)
                    break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_social_media_search, "fill_data_social_media_search_textbox")
        TestLog.log_creation(social_media_social_media_search, "fill_data_social_media_search_textbox", index, ws_index)


def check_box_social_media_search(driver, social_media_item_checkbox, social_media_social_media_search, index, ws_index):

    """ Method to perform click action on chrckboxes in social media """
    try:
        social_media_option = driver.find_elements_by_class_name("socialMediaOptions")
        for item in social_media_option:
            social_media_checkbox_container = item.find_element_by_class_name("socialMediaCheckboxContainer")
            social_media_item_attribute = social_media_checkbox_container.get_attribute("title")
            if social_media_item_attribute == social_media_item_checkbox:
                social_media_checkbox_container.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_social_media_search, "check_box_social_media_search")
        TestLog.log_creation(social_media_social_media_search, "check_box_social_media_search", index, ws_index)


def fill_data_select_date(driver, social_media_social_media_search, index, ws_index):
    try:
        from_date_select_data_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_2']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
        from_date_select_data_range.click()

        select_from_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_2_popup']/tbody/tr[1]/td[4]")
        select_from_date.click()

        to_date_select_date_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_3']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
        to_date_select_date_range.click()

        time.sleep(2)
        select_to_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_3_popup']/tbody/tr[5]/td[1]")
        select_to_date.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_social_media_search, "fill_data_select_date")
        TestLog.log_creation(social_media_social_media_search, "fill_data_select_date", index, ws_index)


def select_geometry_social_media_search(driver, social_media_social_media_search, index, ws_index):

    select_geometry_container = driver.find_element_by_class_name("selectGeometryContainer")
    select_geometry_container_div = select_geometry_container.find_element_by_class_name("selectPointGeometry")
    select_geometry_container_div.click()

    AppCommanUtility.click_minimize_btn(driver, social_media_social_media_search, index, ws_index)

    AppCommanUtility.click_on_map(driver, social_media_social_media_search, index, ws_index)

    AppCommanUtility.click_maximize_btn(driver, social_media_social_media_search, index, ws_index)

    click_social_media_search_ok_btn(driver, social_media_social_media_search, index, ws_index)


def click_social_media_search_ok_btn(driver, social_media_social_media_search, index, ws_index):
    try:
        social_media_Ok_button = driver.find_element_by_class_name("socialMediaOkButton")
        social_media_Ok_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_social_media_search, "click_social_media_search_ok_btn")
        TestLog.log_creation(social_media_social_media_search, "click_social_media_search_ok_btn", index, ws_index)


def click_select_source_dropdown(driver, source_drop_down_item, social_media_social_media_search, index, ws_index):
    try:
        drop_down_main_container = driver.find_element_by_class_name("dropDownMainContainer")
        social_media_search_drop_down_label = drop_down_main_container.find_element_by_class_name("socialMediaSearchDropDownLabel")
        if social_media_search_drop_down_label.text == source_drop_down_item:
            dijit_arrow_button_container = drop_down_main_container.find_element_by_class_name("dijitArrowButtonContainer")
            dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitArrowButtonInner")
            dijit_arrow_button_inner.click()
    except Exception:
        return True


def social_media_search_validation(driver, social_media_social_media_search, social_media_search_select_source_item, social_media_search_layer_name, social_media_sub_layer, index, ws_index):

    click_select_source_dropdown(driver, "Select Source", social_media_social_media_search, index, ws_index)
    AppCommanUtility.select_ddl_item(driver, social_media_search_select_source_item, social_media_social_media_search, index, ws_index)

    try:
        social_media_row_container = driver.find_elements_by_class_name("socialMediaRowContainer")
        for item in social_media_row_container:
            if item.is_displayed():
                item.click()
                break
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_social_media_search, index, ws_index)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_social_media_search, index, ws_index)

    SocialMediaSearchValidation.validate_social_media_highlighted_buffer(driver)

    AppCommanUtility.widget_close_icon(driver, social_media_social_media_search, index, ws_index)

    SocialMediaSearchValidation.validate_social_media_buffer(driver)

    AppCommanUtility.click_down_panel(driver, social_media_social_media_search, index, ws_index)

    AppCommanUtility.click_select_layer_label_container(driver, social_media_social_media_search, index, ws_index)

    AppCommanValidation.validate_layer_name(driver, social_media_search_layer_name, social_media_social_media_search, index, ws_index, boolean_value=True)

    AppCommanValidation.validate_right_panel_layer_name(driver, social_media_search_layer_name, social_media_social_media_search, index, ws_index)

    AppCommanValidation.validate_feature_count_panel(driver, social_media_social_media_search, index, ws_index)

    AppCommanValidation.validate_feature_count(driver, social_media_sub_layer, social_media_social_media_search, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)


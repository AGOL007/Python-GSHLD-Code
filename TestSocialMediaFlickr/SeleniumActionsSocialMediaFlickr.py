# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
from GeoshieldCommonFiles import AppCommanUtility
from GeoshieldCommonFiles import AppCommanValidation, TestFailScreenShots, TestLog, TestResults
import FlickrValidation


def click_widget_icon(driver, social_media_flickr, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_flickr, "click_widget_icon")
        TestLog.log_creation(social_media_flickr, "click_widget_icon", index, ws_index)


def click_social_media_item_flickr(driver, social_media_flickr, flickr_distance_textbox_text, flickr_keyword_textbox_text, flickr_refreshtime_textbox_text, flickr_unit, index, ws_index):

    AppCommanUtility.click_widget_items(driver, social_media_flickr, index, ws_index)
    fill_data_flickr_textbox(driver, "Distance", flickr_distance_textbox_text, social_media_flickr, index, ws_index)
    fill_data_flickr_textbox(driver, "Keyword", flickr_keyword_textbox_text, social_media_flickr, index, ws_index)
    fill_data_flickr_textbox(driver, "Refresh Time (in Seconds)", flickr_refreshtime_textbox_text, social_media_flickr, index, ws_index)

    fill_data_flickr_ddl_item(driver, "Unit", social_media_flickr, index, ws_index)
    AppCommanUtility.select_ddl_item(driver, flickr_unit)

    fill_data_select_date(driver, social_media_flickr, index, ws_index)

    select_geometry_flickr_item(driver, social_media_flickr, index, ws_index)

    AppCommanUtility.click_on_map(driver, social_media_flickr, index, ws_index)

    select_flickr_submit_button(driver, social_media_flickr, index, ws_index)


def fill_data_flickr_textbox(driver, flickr_textbox, flickr_textbox_text, social_media_flickr, index, ws_index):

    """ Common method to perform actions in flickr widget """
    try:
        search_flickr_div = driver.find_elements_by_class_name("searchFlickrDiv")
        for item in search_flickr_div:
            search_flickr_label = item.find_element_by_class_name("flickLeftPanelLabel")
            if search_flickr_label.text == flickr_textbox:
                search_flickr_div_textbox = item.find_element_by_class_name("dijitInputContainer")
                search_flickr_div_text_box_one = search_flickr_div_textbox.find_element_by_class_name("dijitInputInner")
                search_flickr_div_text_box_one.clear()
                search_flickr_div_text_box_one.send_keys(flickr_textbox_text)
                time.sleep(1)

    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_flickr, "fill_data_flickr_textbox")
        TestLog.log_creation(social_media_flickr, "fill_data_flickr_textbox", index, ws_index)


def fill_data_flickr_ddl_item(driver, flickr_textbox, social_media_flickr, index, ws_index):

    try:
        search_flickr_div = driver.find_elements_by_class_name("searchFlickrDiv")
        for item in search_flickr_div:
            search_flickr_label = item.find_element_by_class_name("flickLeftPanelLabel")
            if search_flickr_label.text == flickr_textbox:
                search_flickr_div_textbox = item.find_element_by_class_name("dijitArrowButtonContainer")
                search_flickr_div_text_box_one = search_flickr_div_textbox.find_element_by_class_name("dijitArrowButtonInner")
                search_flickr_div_text_box_one.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_flickr, "fill_data_flickr_ddl_item")
        TestLog.log_creation(social_media_flickr, "fill_data_flickr_ddl_item", index, ws_index)


def fill_data_select_date(driver, social_media_flickr, index, ws_index):
    try:
        from_date_select_data_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_4']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
        from_date_select_data_range.click()

        select_from_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_4_popup']/tbody/tr[1]/td[4]")
        select_from_date.click()

        to_date_select_date_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_5']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
        to_date_select_date_range.click()

        time.sleep(2)
        select_to_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_5_popup']/tbody/tr[5]/td[1]")
        select_to_date.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_flickr, "fill_data_select_date")
        TestLog.log_creation(social_media_flickr, "fill_data_select_date", index, ws_index)


def select_geometry_flickr_item(driver, social_media_flickr, index, ws_index):

    """ Method to select geometry flickr widget """
    try:
        flickr_inactive_rect_button = driver.find_element_by_class_name("flickrDeactivePointButton")
        flickr_inactive_rect_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_flickr, "select_geometry_flickr_item")
        TestLog.log_creation(social_media_flickr, "select_geometry_flickr_item", index, ws_index)


def select_flickr_submit_button(driver, social_media_flickr, index, ws_index):

    """ Method to click on submit button of flickr """
    try:
        flickr_search_submit_button = driver.find_element_by_class_name("flickrSearchSubmitButton")
        flickr_search_submit_button.click()
        time.sleep(2)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_flickr, "select_flickr_submit_button")
        TestLog.log_creation(social_media_flickr, "select_flickr_submit_button", index, ws_index)


def validate_social_media_flickr(driver, social_media_flickr, flickr_layer, index, ws_index):

    """ Method to validate the twitter social media item """
    try:
        row_tweet_container = driver.find_elements_by_class_name("rowflickrContainer")
        row_tweet_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_flickr, index, ws_index)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_flickr, index, ws_index)

    FlickrValidation.validate_flickr_buffer(driver)

    AppCommanUtility.widget_close_icon(driver, social_media_flickr, index, ws_index)

    FlickrValidation.validate_flickr_highlighted_buffer(driver)

    AppCommanUtility.click_down_panel(driver, social_media_flickr, index, ws_index)

    AppCommanUtility.click_select_layer_label_container(driver, social_media_flickr, index, ws_index)

    AppCommanValidation.validate_layer_name(driver, flickr_layer, social_media_flickr, index, ws_index, boolean_value=True)

    AppCommanValidation.validate_right_panel_layer_name(driver, flickr_layer, social_media_flickr, index, ws_index)

    AppCommanValidation.validate_feature_count_panel(driver, social_media_flickr, index, ws_index)

    AppCommanValidation.validate_feature_count(driver, "flickrResultFeatureLayer", social_media_flickr, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)
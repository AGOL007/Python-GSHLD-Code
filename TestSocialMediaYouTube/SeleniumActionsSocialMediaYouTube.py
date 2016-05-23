# -*- coding: utf-8 -*-
""" Unit test file """
from unittest.test.test_case import Test

__author__ = 'SagarKul'

import time
from GeoshieldCommonFiles import AppCommanUtility
from GeoshieldCommonFiles import AppCommanValidation, TestLog, TestFailScreenShots, TestResults
import YouTubeValidation


def click_widget_icon(driver, social_media_youtube, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_youtube, "click_widget_icon")
        TestLog.log_creation(social_media_youtube, "click_widget_icon", index, ws_index)


def click_social_media_item_you_tube(driver, social_media_youtube, youtube_distance_textbox_text, youtube_keyword_textbox_text, youtube_refreshtime_textbox_text, youtube_units, index, ws_index):

    """ Method to click on social media item youtube """

    AppCommanUtility.click_widget_items(driver, social_media_youtube, index, ws_index)
    fill_data_youtube_textbox(driver, "Distance", youtube_distance_textbox_text, social_media_youtube, index, ws_index)
    fill_data_youtube_textbox(driver, "Keyword", youtube_keyword_textbox_text, social_media_youtube, index, ws_index)
    fill_data_youtube_textbox(driver, "Refresh Time (in Seconds)", youtube_refreshtime_textbox_text, social_media_youtube, index, ws_index)

    fill_data_select_date(driver, social_media_youtube, index, ws_index)

    fill_data_youtube_ddl_item(driver, "Units", social_media_youtube, index, ws_index)
    AppCommanUtility.select_ddl_item(driver, youtube_units)

    click_point_geometry(driver, social_media_youtube, index, ws_index, class_name="youtubePointGeometry")

    AppCommanUtility.click_on_map(driver, social_media_youtube, index, ws_index)

    click_youtube_submit_button(driver,social_media_youtube, index, ws_index, class_name="youtubeSubmitButton")


def fill_data_youtube_textbox(driver, you_tube_tsxt_box, you_tube_tsxt_box_text, social_media_youtube, index, ws_index):

    """ Common method to perform actions in youtube widget """
    try:
        search_youtube_div = driver.find_elements_by_class_name("searchYoutubeDiv")
        for item in search_youtube_div:
            search_you_tube_label = item.find_element_by_class_name("youtubeLeftPanelLabel")
            if search_you_tube_label.text == you_tube_tsxt_box:
                search_you_tube_div_text_box = item.find_element_by_class_name("dijitInputContainer")
                search_you_tube_div_text_box_one = search_you_tube_div_text_box.find_element_by_class_name("dijitInputInner")
                search_you_tube_div_text_box_one.clear()
                search_you_tube_div_text_box_one.send_keys(you_tube_tsxt_box_text)
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_youtube, "fill_data_youtube_textbox")
        TestLog.log_creation(social_media_youtube, "fill_data_youtube_textbox", index, ws_index)


def fill_data_youtube_ddl_item(driver, you_tube_tsxt_box, social_media_youtube, index, ws_index):
    try:
        search_youtube_div = driver.find_elements_by_class_name("searchYoutubeDiv")
        for item in search_youtube_div:
            search_you_tube_label = item.find_element_by_class_name("youtubeLeftPanelLabel")
            if search_you_tube_label.text == you_tube_tsxt_box:
                search_you_tube_div_text_box = item.find_element_by_class_name("dijitArrowButtonContainer")
                search_you_tube_div_text_box_one = search_you_tube_div_text_box.find_element_by_class_name("dijitArrowButtonInner")
                search_you_tube_div_text_box_one.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_youtube, "fill_data_youtube_ddl_item")
        TestLog.log_creation(social_media_youtube, "fill_data_youtube_ddl_item", index, ws_index)


def fill_data_select_date(driver, social_media_youtube, index, ws_index):
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
        TestFailScreenShots.get_screenshots(driver, social_media_youtube, "fill_data_select_date")
        TestLog.log_creation(social_media_youtube, "fill_data_select_date", index, ws_index)


def click_point_geometry(driver, social_media_youtube, index, ws_index, class_name):

    """ Method to click on geometry """
    try:
        youtube_point_button = driver.find_element_by_class_name(class_name)
        youtube_point_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_youtube, "click_point_geometry")
        TestLog.log_creation(social_media_youtube, "click_point_geometry", index, ws_index)


def click_youtube_submit_button(driver,social_media_youtube, index, ws_index, class_name):

    """ Method to click on you tube submit button """
    try:
        you_tube_submit_button = driver.find_element_by_class_name(class_name)
        you_tube_submit_button.click()
        time.sleep(2)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_youtube, "click_youtube_submit_button")
        TestLog.log_creation(social_media_youtube, "click_youtube_submit_button", index, ws_index)


def validate_social_media_youtube(driver, social_media_youtube, youtube_layer_name, index, ws_index):

    """ Method to validate the twitter social media item """
    try:
        row_tweet_container = driver.find_elements_by_class_name("rowYoutubeContainer")
        row_tweet_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_youtube, index, ws_index)
        TestResults.open_py_excel_pass(index, ws_index)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_youtube, index, ws_index)

    YouTubeValidation.validate_youtube_highlighted_buffer(driver)

    AppCommanUtility.widget_close_icon(driver, social_media_youtube, index, ws_index)

    YouTubeValidation.validate_youtube_buffer(driver)

    AppCommanUtility.click_down_panel(driver, social_media_youtube, index, ws_index)

    AppCommanUtility.click_select_layer_label_container(driver, social_media_youtube, index, ws_index)

    AppCommanValidation.validate_layer_name(driver, youtube_layer_name, social_media_youtube, index, ws_index, boolean_value=True)

    AppCommanValidation.validate_right_panel_layer_name(driver, youtube_layer_name, social_media_youtube, index, ws_index)

    AppCommanValidation.validate_feature_count_panel(driver, social_media_youtube, index, ws_index)

    AppCommanValidation.validate_feature_count(driver, "youtubeResultFeatureLayer", social_media_youtube, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)
# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
from  GeoshieldCommonFiles import AppCommanValidation, AppCommanUtility, TestLog, TestFailScreenShots, TestResults
import TwitterValidation


def click_widget_icon(driver, social_media_twitter, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_twitter, "click_widget_icon")
        TestLog.log_creation(social_media_twitter, "click_widget_icon", index, ws_index)


def click_social_media_item_twitter(driver, social_media_twitter, twitter_keyword_textbox_text, twitter_distance_textbox_text, twitter_refreshtime_textbox_text, index, ws_index):

    AppCommanUtility.click_widget_items(driver, social_media_twitter, index, ws_index)

    fill_data_twitter_text_box(driver, "Keyword", twitter_keyword_textbox_text,social_media_twitter, index, ws_index)
    fill_data_twitter_text_box(driver, "Distance (in Miles)", twitter_distance_textbox_text, social_media_twitter, index, ws_index)
    fill_data_twitter_text_box(driver, "Refresh Time (in Seconds)", twitter_refreshtime_textbox_text, social_media_twitter, index, ws_index)

    select_point_geometry(driver,social_media_twitter, index, ws_index)

    AppCommanUtility.click_minimize_btn(driver, social_media_twitter, index, ws_index)

    AppCommanUtility.click_on_map(driver,social_media_twitter, index, ws_index)

    AppCommanUtility.click_maximize_btn(driver, social_media_twitter, index, ws_index)

    click_ok_button(driver, social_media_twitter, index, ws_index)


def fill_data_twitter_text_box(driver, twitter_text_box, twitter_text_box_text,social_media_twitter, index, ws_index):

    """ Common method to perform actions in twitter tab """
    try:
        search_tweet_div = driver.find_elements_by_class_name("searchTweetDiv")
        for item in search_tweet_div:
            search_tweet_div_label = item.find_element_by_class_name("leftPanelLabel")
            if search_tweet_div_label.text == twitter_text_box:
                search_tweet_div_text_box = item.find_element_by_class_name("dijitInputContainer")
                search_tweet_div_text_box_one = search_tweet_div_text_box.find_element_by_class_name("dijitInputInner")
                search_tweet_div_text_box_one.clear()
                search_tweet_div_text_box_one.send_keys(twitter_text_box_text)
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_twitter, "fill_data_twitter_text_box")
        TestLog.log_creation(social_media_twitter, "fill_data_twitter_text_box", index, ws_index)


def select_point_geometry(driver, social_media_twitter, index, ws_index):

    """ Method to select the geometry"""
    try:
        time.sleep(1)
        search_point_geometry = driver.find_element_by_class_name("searchPointGeometry")
        search_point_geometry.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_twitter, "select_point_geometry")
        TestLog.log_creation(social_media_twitter, "select_point_geometry", index, ws_index)


def click_ok_button(driver,social_media_twitter, index, ws_index):

    """ Method to click on OK button """
    try:
        click_ok_btn = driver.find_elements_by_class_name("searchSubmitButton")
        for item in click_ok_btn:
            if item.text == 'OK':
                item.click()
                break
        time.sleep(2)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_twitter, "click_ok_button")
        TestLog.log_creation(social_media_twitter, "click_ok_button", index, ws_index)


def validate_social_media_twitter(driver, social_media_twitter, twitter_layer, index, ws_index):

    """ Method to validate the twitter social media item """
    try:
        row_tweet_container = driver.find_elements_by_class_name("rowTweetContainer")
        row_tweet_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_twitter, index, ws_index)
        TestResults.open_py_excel_pass(index, ws_index)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_twitter, index, ws_index)

    TwitterValidation.validate_twitter_highlighted_buffer(driver)

    AppCommanUtility.widget_close_icon(driver, social_media_twitter, index, ws_index)

    TwitterValidation.validate_twitter_buffer(driver)

    AppCommanUtility.click_down_panel(driver,social_media_twitter, index, ws_index)

    AppCommanUtility.click_select_layer_label_container(driver, social_media_twitter, index, ws_index)

    AppCommanValidation.validate_layer_name(driver, twitter_layer, social_media_twitter, index, ws_index, boolean_value=True)

    AppCommanValidation.validate_right_panel_layer_name(driver, twitter_layer, social_media_twitter, index, ws_index)

    AppCommanValidation.validate_feature_count_panel(driver, social_media_twitter, index, ws_index)

    AppCommanValidation.validate_feature_count(driver, "twitterResultFeatureLayer", social_media_twitter, index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)




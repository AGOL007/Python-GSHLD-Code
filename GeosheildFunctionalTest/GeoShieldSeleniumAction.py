# -*- coding: utf-8 -*-
""" File contains the method to perform different selenium action"""
__author__ = 'SagarKul'

import time
import AppCommanUtility
import AppValidation


def click_left_panel_open(driver):

    """ Method to perform click action on left panel """
    time.sleep(3)
    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "panelOpenCloseContainer")
    panel_open_close_container = driver.find_element_by_class_name("panelOpenCloseContainer")
    panel_open_close_container.click()


def click_select_date_value(driver):

    """ Method to perform to select date"""

    time.sleep(3)
    select_date_value = driver.find_element_by_class_name("selectedDateValue")
    select_date_value.click()


def click_predefined_daterange_tab(driver):

    """ Method to perform actions on daterange and predefined tab """

    predefined_tab = driver.find_element_by_class_name("state-selected")
    predefined_tab.click()

    predefined_tab_content = driver.find_elements_by_class_name("layerContentRow")
    for item in predefined_tab_content:
        if item.text == "Last 4 days":
            item.click()

    date_range_tab_content = driver.find_element_by_class_name("removeRightBorder")
    date_range_tab_content.click()

    from_date_select_data_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_0']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
    from_date_select_data_range.click()

    select_from_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_0_popup']/tbody/tr[1]/td[4]")
    select_from_date.click()

    to_date_select_date_range = driver.find_element_by_xpath("//div[@id='widget_dijit_form_DateTextBox_1']/div[@class='dijitReset dijitRight dijitButtonNode dijitArrowButton dijitDownArrowButton dijitArrowButtonContainer']")
    to_date_select_date_range.click()

    #calendar_select_data_range = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_1_popup']/tfoot/tr/td/div/span[3]")
    #calendar_select_data_range.click()

    time.sleep(2)
    select_to_date = driver.find_element_by_xpath("//table[@id='dijit_form_DateTextBox_1_popup']/tbody/tr[5]/td[1]")
    select_to_date.click()
    time.sleep(2)
    AppCommanUtility.browse_ok_cancel_btn(driver)


def click_events_rms_browse_tab(driver, category_main_layer_name, category_sub_layer_name):

    """ Method to perform selection of different layers """

    AppCommanUtility.click_browse_tab_item(driver, "Events")
    AppCommanUtility.click_expand_button_div(driver, category_main_layer_name)
    AppCommanUtility.click_toggel_btn(driver, category_sub_layer_name)
    AppCommanUtility.click_expand_button_div(driver, category_main_layer_name)

def click_down_panel(driver, flag):

    """Method to perfrom click action on down panel"""
    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "layerDataGridPanelOpenCloseContanier")
    panal_open_close_container = driver.find_element_by_class_name("layerDataGridPanelOpenCloseContanier")
    panal_open_close_container.click()
    if flag:
        click_select_layer_label_container(driver)

def click_select_layer_label_container(driver):

    """ Method to perform click on layer label container"""

    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "selectLayerLabelConatiner")
    select_layer_container = driver.find_element_by_class_name("selectLayerLabelConatiner")
    select_layer_container.click()

def click_right_panel_open(driver, flag):

    """ Method to perform click action on right panel """
    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "rightPanelOpenCloseContanier")
    panel_open_close_container = driver.find_element_by_class_name("rightPanelOpenCloseContanier")
    panel_open_close_container.click()
    if flag:
        click_active_data_tab(driver)

def click_active_data_tab(driver):

    """ Method to perform click action on tab of active data """

    active_data = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='activeData_button_title']")
    active_data.click()


def click_social_media_item_twitter(driver, social_media_item_twitter, twitter_text_box_keyword_text, twitter_text_box_distance_text, twitter_text_box_refresh_time):

    """ Method to perfrom actions in twitter widget """

    time.sleep(2)
    tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@class='toolImage advancedDataQueriesIcon']")
    tab_item_div.click()

    AppCommanUtility.click_social_media_items(driver, social_media_item_twitter)
    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "searchPointGeometry")
    AppCommanUtility.fill_data_twitter_text_box(driver, "Keyword", twitter_text_box_keyword_text)
    AppCommanUtility.fill_data_twitter_text_box(driver, "Distance (in Miles)", twitter_text_box_distance_text)
    AppCommanUtility.fill_data_twitter_text_box(driver, "Refresh Time (in Seconds)", twitter_text_box_refresh_time)

    search_point_geometry = driver.find_element_by_class_name("searchPointGeometry")
    search_point_geometry.click()
    click_on_map = driver.find_element_by_id("mapContainer")
    click_on_map.click()
    time.sleep(2)

    click_ok_btn = driver.find_elements_by_class_name("searchSubmitButton")
    for item in click_ok_btn:
        if item.text == 'OK':
            item.click()
            break
    time.sleep(2)

    try:
        row_tweet_container = driver.find_elements_by_class_name("rowTweetContainer")
        row_tweet_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_item_twitter)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_item_twitter)
    AppValidation.validate_feature_count(driver, "twitterResultFeatureLayer")
    AppValidation.validate_twitter_highlighted_buffer(driver)
    AppCommanUtility.widget_close_icon(driver, social_media_item_twitter)
    AppValidation.validate_twitter_buffer(driver)

    click_down_panel(driver, True)
#    AppCommanUtility.click_bottom_panel_layer(driver, "Twitter Layer")
    AppValidation.validate_layer_name(driver, "Twitter Layer")
    AppValidation.validate_right_panel_layer_name(driver, "Twitter Layer")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


def click_social_media_item_youtube(driver, social_media_item_you_tube, you_tube_tsxt_box_distance_text, you_tube_tsxt_box_keyword_text, you_tube_tsxt_box_refresh_time_text):

    """ Method to perfrom actions in youtube widget """

    AppCommanUtility.click_social_media_items(driver, social_media_item_you_tube)
    AppCommanUtility.fill_data_youtube_textbox(driver, "Distance", you_tube_tsxt_box_distance_text)
    AppCommanUtility.fill_data_youtube_textbox(driver, "Keyword", you_tube_tsxt_box_keyword_text)
    AppCommanUtility.fill_data_youtube_textbox(driver, "Refresh Time (in Seconds)", you_tube_tsxt_box_refresh_time_text)

    youtube_point_button = driver.find_element_by_class_name("youtubePointGeometry")
    youtube_point_button.click()

    click_on_map = driver.find_element_by_id("mapContainer_root")
    click_on_map.click()
    time.sleep(2)

    you_tube_submit_button = driver.find_element_by_class_name("youtubeSubmitButton")
    you_tube_submit_button.click()
    time.sleep(2)

    try:
        row_youtube_container = driver.find_elements_by_class_name("rowYoutubeContainer")
        row_youtube_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_item_you_tube)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_item_you_tube)
    AppValidation.validate_feature_count(driver, "youtubeResultFeatureLayer")
    AppValidation.validate_youtube_highlighted_buffer(driver)
    AppCommanUtility.widget_close_icon(driver, social_media_item_you_tube)
    AppValidation.validate_youtube_buffer(driver)

    click_down_panel(driver, True)
    AppValidation.validate_layer_name(driver, "YouTube Layer")
    AppValidation.validate_right_panel_layer_name(driver, "YouTube Layer")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


def click_social_media_item_flickr(driver, social_media_item_flickr, flickr_tsxt_box_distance_text, flickr_tsxt_box_keyword_text, flickr_tsxt_box_refresh_time_text):

    """ Method to perform actions in Flickr widget """

    AppCommanUtility.click_social_media_items(driver, social_media_item_flickr)
    AppCommanUtility.fill_data_flickr_textbox(driver, "Distance", flickr_tsxt_box_distance_text)
    AppCommanUtility.fill_data_flickr_textbox(driver, "Keyword", flickr_tsxt_box_keyword_text)
    AppCommanUtility.fill_data_flickr_textbox(driver, "Refresh Time (in Seconds)", flickr_tsxt_box_refresh_time_text)

    flickr_inactive_rect_button = driver.find_element_by_class_name("flickrDeactivePointButton")
    flickr_inactive_rect_button.click()

    click_on_map = driver.find_element_by_id("mapContainer")
    click_on_map.click()
    time.sleep(2)

    flickr_search_submit_button = driver.find_element_by_class_name("flickrSearchSubmitButton")
    flickr_search_submit_button.click()
    time.sleep(2)

    try:
        row_flickr_container = driver.find_elements_by_class_name("rowflickrContainer")
        row_flickr_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_item_flickr)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_item_flickr)
    AppValidation.validate_feature_count(driver, "flickrResultFeatureLayer")
    AppValidation.validate_flickr_highlighted_buffer(driver)
    AppCommanUtility.widget_close_icon(driver, social_media_item_flickr)
    AppValidation.validate_flickr_buffer(driver)

    click_down_panel(driver, True)
    AppValidation.validate_layer_name(driver, "Flickr Layer")
    AppValidation.validate_right_panel_layer_name(driver, "Flickr Layer")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


def click_social_media_item_social_media_search(driver, social_media_item_social_media_search, social_media_search_tsxt_box_distance_text, social_media_search_tsxt_box_keyword_text, social_media_search_tsxt_box_refresh_time_text):

    """ Method to perform actions in social media search widget """

    AppCommanUtility.click_social_media_items(driver, social_media_item_social_media_search)
    AppCommanUtility.fill_data_social_media_search_textbox(driver, "Distance", social_media_search_tsxt_box_distance_text)
    AppCommanUtility.fill_data_social_media_search_textbox(driver, "Keyword", social_media_search_tsxt_box_keyword_text)
    AppCommanUtility.check_box_social_media_search(driver, "Twitter")
    AppCommanUtility.check_box_social_media_search(driver, "Youtube")
    select_geometry_container = driver.find_element_by_class_name("selectGeometryContainer")
    select_geometry_container_div = select_geometry_container.find_element_by_class_name("selectPointGeometry")
    select_geometry_container_div.click()
    AppCommanUtility.click_minimize_btn(driver, "Social Media Search")

    click_on_map = driver.find_element_by_id("mapContainer_root")
    click_on_map.click()
    time.sleep(3)

    AppCommanUtility.click_maximize_btn(driver, "Social Media Search")
    social_media_Ok_button = driver.find_element_by_class_name("socialMediaOkButton")
    social_media_Ok_button.click()

    try:
        AppCommanUtility.wait_to_load_webelement(driver, "class_name", "socialMediaExportToCSVButton")
        social_media_row_container = driver.find_elements_by_class_name("socialMediaRowContainer")
        social_media_row_container[0].click()
    except Exception:
        AppCommanUtility.widget_close_icon(driver, social_media_item_social_media_search)
        return True

    AppCommanUtility.click_minimize_btn(driver, social_media_item_social_media_search)
    AppValidation.validate_feature_count(driver, "socialMediaTwitterFeatureLayer")
    AppValidation.validate_social_media_highlighted_buffer(driver)
    AppCommanUtility.widget_close_icon(driver, social_media_item_social_media_search)
    AppValidation.validate_flickr_buffer(driver)
    click_down_panel(driver, True)
    AppValidation.validate_layer_name(driver, "Social Media Twitter Layer")
    AppValidation.validate_right_panel_layer_name(driver, "Social Media Twitter Layer")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


def click_agency_feed_item_live_cads(driver, agency_feed_item_current_call_for_services):

    """ Method to perform actions in live cads widget """

    AppCommanUtility.click_social_media_items(driver, agency_feed_item_current_call_for_services)
    live_CAD_section = driver.find_elements_by_class_name("liveCADSection")
    for item in live_CAD_section:
        try:
            live_CAD_section_div = item.find_element_by_class_name("liveSectionItemCheckBox")
            live_CAD_section_div.click()
        except Exception:
            continue

    live_CAD_button = driver.find_element_by_class_name("liveCADButton")
    live_CAD_button.click()

    AppValidation.validate_feature_count(driver, "LiveCAD")
    AppCommanUtility.click_popup_close_icon(driver, "Live CAD")
    AppCommanUtility.widget_close_icon(driver, "Live CAD")
    click_down_panel(driver, True)
    AppValidation.validate_layer_name(driver, "Live CAD")
    live_data_tab = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='live_button_title']")
    live_data_tab.click()

    AppValidation.validate_right_panel_layer_name(driver, "Live CAD")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


def click_agency_feed_item_avl(driver, agency_feed_item_avl, agency_feed_item_avl_unitid_text, agency_feed_item_avl_distance_text):

    """ Method to perfrom actions in AVL widget """

    AppCommanUtility.click_social_media_items(driver, agency_feed_item_avl)

    avl_live_section = driver.find_elements_by_class_name("avlLiveSection")
    for item in avl_live_section:
        try:
            avl_live_section_div = item.find_element_by_class_name("liveSectionItemCheckBox")
            avl_live_section_div.click()
            time.sleep(1)
        except Exception:
            continue

    avl_Ok_Content = driver.find_element_by_class_name("avlOkContent")
    avl_Ok_Content.click()
    time.sleep(2)

    AppCommanUtility.click_popup_close_icon(driver, "AVL")
    AppCommanUtility.open_right_panel(driver, "Historic")
    AppCommanUtility.agency_feed_avl_fill_data(driver, "Unit Id", agency_feed_item_avl_unitid_text)
    AppCommanUtility.agency_feed_date_fill_date(driver, "Select by Unit")

    avl_Ok_content = driver.find_elements_by_class_name("avlOkContent")
    avl_Ok_content[1].click()
    time.sleep(2)

    AppValidation.validate_agency_feed_avl_historic_tab(driver, "avlHistoricLayer")

    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "avlDeactiveRadioButton")
    avl_deactive_radio_button = driver.find_element_by_class_name("avlDeactiveRadioButton")
    avl_deactive_radio_button.click()

    AppCommanUtility.select_geometry_tab(driver)
    click_on_map = driver.find_element_by_id("mapContainer_root")
    click_on_map.click()
    time.sleep(2)

    AppCommanUtility.agency_feed_avl_fill_data(driver, "Distance", agency_feed_item_avl_distance_text)
    avl_Ok_content_btn = driver.find_elements_by_class_name("avlOkContent")
    avl_Ok_content_btn[2].click()
    time.sleep(3)

    AppCommanUtility.click_popup_close_icon(driver, agency_feed_item_avl)
    AppValidation.validate_agency_feed_avl_buffer(driver)
    AppCommanUtility.widget_close_icon(driver, agency_feed_item_avl)

    click_down_panel(driver, True)
    AppValidation.validate_layer_name(driver, "AVL-Live")

    live_data_tab = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='live_button_title']")
    live_data_tab.click()

    AppValidation.validate_right_panel_layer_name(driver, "AVL-Live")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


def click_agency_feed_item_LPR(driver, agency_feed_item_LPR, agency_feed_item_lpr_license_plate_number_text, agency_feed_item_lpr_distance_text):

    """ Method to perform actions in LPR widget """

    AppCommanUtility.click_social_media_items(driver, agency_feed_item_LPR)
    AppCommanUtility.agency_feed_lpr_fill_data(driver, "License Plate Number", agency_feed_item_lpr_license_plate_number_text)

    lpr_Ok_Content = driver.find_elements_by_class_name("lprOkContent")
    lpr_Ok_Content[0].click()
    time.sleep(2)

    AppCommanUtility.click_popup_close_icon(driver, "LPR")

    AppCommanUtility.open_right_panel(driver, "Historic")
    AppCommanUtility.agency_feed_lpr_fill_data(driver, "License Plate Number", agency_feed_item_lpr_license_plate_number_text)
    AppCommanUtility.agency_feed_lpr_ddl_list(driver, "Hits")
    AppCommanUtility.agency_feed_lpr_ddl_item(driver, "Active 1")
    AppCommanUtility.agency_feed_lpr_ddl_list(driver, "Unit")
    AppCommanUtility.agency_feed_lpr_ddl_item(driver, "348 S Beach St")

#    AppCommanUtility.click_agency_feed_lpr_ok_btn(driver)

    lpr_Ok_Content = driver.find_elements_by_class_name("lprOkContent")
    lpr_Ok_Content[1].click()
    time.sleep(2)

    AppCommanUtility.click_popup_close_icon(driver, "LPR")
    AppCommanUtility.wait_to_load_webelement(driver, "class_name", "lprDeactiveRadioButton")
    avl_deactive_radio_button = driver.find_element_by_class_name("lprDeactiveRadioButton")
    avl_deactive_radio_button.click()

    AppCommanUtility.select_geometry_tab(driver)
    click_on_map = driver.find_element_by_id("mapContainer_root")
    click_on_map.click()
    time.sleep(2)

    AppCommanUtility.agency_feed_lpr_fill_data(driver, "Distance", agency_feed_item_lpr_distance_text)

    lpr_Ok_Content = driver.find_elements_by_class_name("lprOkContent")
    lpr_Ok_Content[2].click()
    time.sleep(2)

    AppCommanUtility.click_popup_close_icon(driver, "LPR")
    AppValidation.validate_agency_feed_lpr_buffer(driver)
    AppValidation.validate_feature_count(driver, "historicLayer")
    AppCommanUtility.widget_close_icon(driver, "LPR")

    click_down_panel(driver, True)
    AppValidation.validate_layer_name(driver, "LPN SUSPECT")

    live_data_tab = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='live_button_title']")
    live_data_tab.click()

    AppValidation.validate_right_panel_layer_name(driver, "LPN SUSPECT")
    AppValidation.validate_feature_count_panel(driver)
    click_down_panel(driver, False)


























































































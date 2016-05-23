# -*- coding: utf-8 -*-

""" File Contains the common Methods """
__author__ = 'SagarKul'
import time


def click_browse_tab_item(driver, title_text_node):

    """ Common Method to perform click action on browse tab item """

    browse_tab_item = driver.find_elements_by_class_name("dijitAccordionTitle")
    for item in browse_tab_item:
        browse_tab_item_title = item.find_element_by_class_name("dijitAccordionText")
        if browse_tab_item_title.text == title_text_node:
            browse_tab_item_title.click()
            break


def browse_ok_cancel_btn(driver):

    """ Common Method to perform action on Ok button """

    click_ok_button = driver.find_element_by_class_name("okBtn")
    click_ok_button.click()


def click_expand_button_div(driver, event_rms_or_cad_name):

    """ Common Method to perform action on expand button """

    event_container = driver.find_elements_by_class_name("categoryGroupPanel")
    for item in event_container:
        event_container_div = item.find_element_by_class_name("expandButtonDiv")
        event_container_div_list = item.find_element_by_class_name("groupNameConatiner")
        if event_container_div_list.text == event_rms_or_cad_name:
            event_container_div.click()
            time.sleep(1)
            break


def click_toggel_btn(driver, event_rms_or_cad_name):

    """ Common Method to perform action on toggle button """

    event_container = driver.find_elements_by_class_name("subCategoryDataPanel")
    for item in event_container:
        event_container_div_list = item.find_element_by_class_name("subCategoryLabel")
        toggel_btn_container = item.find_element_by_class_name("toggleButtonBackGroundColor")
        if event_container_div_list.text == event_rms_or_cad_name:
            toggel_btn_container.click()
            time.sleep(1)
            break


def click_social_media_items(driver, social_media_items):

    """ Common Method to perform action on social media items click  """

    social_media_item = driver.find_elements_by_class_name("backGroundToolIcon")
    for item in social_media_item:
        social_media_item_div = item.find_element_by_class_name("iconTool")
        social_media_item_div_attribute = social_media_item_div.get_attribute("title")
        if social_media_item_div_attribute == social_media_items:
            social_media_item_div.click()
            time.sleep(1)
            break


def fill_data_twitter_text_box(driver, twitter_text_box, twitter_text_box_text):

    """ Common method to perform actions in twitter tab """

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


def search_ele_with_attrubite(driver, searche_attribute, search_element):

    if searche_attribute == 'class_name':
        return driver.find_element_by_class_name(search_element)
    elif searche_attribute == 'id':
        return driver.find_element_by_id(search_element)
    elif searche_attribute == 'tagname':
        return driver.find_elements_by_tag_name(search_element)
    elif searche_attribute == 'xpath':
        return driver.find_elements_by_xpath(search_element)


def wait_to_load_webelement(driver, search_element, search_attribute):
    """ Wait to load an element """
    for i in range(0, 30):
        try:
            if search_element == "class_name":
                loading_element = driver.find_element_by_class_name(search_attribute)
            elif search_element == "id":
                loading_element = driver.find_element_by_id(search_attribute)
            elif search_element == "tag_name":
                loading_element = driver.find_elements_by_tag_name(search_attribute)
            if loading_element.is_displayed():
                if loading_element.is_enabled():
                    return True
        except Exception:
            time.sleep(1)
            continue


def widget_close_icon(driver, social_media_items):

    """ Common method to close widgets """

    tool_dialog_title_container = driver.find_elements_by_class_name("customDialogTitleBar")
    for item in tool_dialog_title_container:
        tool_dialog_title_div = item.find_element_by_class_name("toolDialogTitleText")
        tool_dialog_title_div_text = tool_dialog_title_div.text
        custom_dialog_close_icon = item.find_element_by_class_name("customDialogCloseIcon")
        if social_media_items == tool_dialog_title_div_text:
            custom_dialog_close_icon.click()
            time.sleep(2)
            break


def fill_data_youtube_textbox(driver, you_tube_tsxt_box, you_tube_tsxt_box_text):

    """ Common method to perform actions in youtube widget """

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


def fill_data_flickr_textbox(driver, flickr_textbox, flickr_textbox_text):

    """ Common method to perform actions in flickr widget """

    search_flickr_div = driver.find_elements_by_class_name("searchFlickrDiv")
    for item in search_flickr_div:
        search_flickr_label = item.find_element_by_class_name("flickLeftPanelLabel")
        if search_flickr_label.text == flickr_textbox:
            search_flickr_div_textbox = item.find_element_by_class_name("dijitInputContainer")
            search_flickr_div_text_box_one = search_flickr_div_textbox.find_element_by_class_name("dijitInputInner")
            search_flickr_div_text_box_one.clear()
            search_flickr_div_text_box_one.send_keys(flickr_textbox_text)
            time.sleep(1)
            break


def fill_data_social_media_search_textbox(driver, social_media_search_textbox, social_media_search_textbox_text):

    """ Common method to perform actions in social media search """

    search_social_media_search_div = driver.find_elements_by_class_name("rowContainer")
    for item in search_social_media_search_div:
        search_social_media_label = item.find_elements_by_class_name("tableCellLabel")
        for item1 in search_social_media_label:
            search_social_media_search_div_textbox = item.find_elements_by_class_name("dijitInputContainer")
            for item2 in search_social_media_search_div_textbox:
                if item1.text == social_media_search_textbox:
                    search_social_media_search_div_textbox_one = item2.find_element_by_class_name("dijitInputInner")
                    search_social_media_search_div_textbox_one.clear()
                    search_social_media_search_div_textbox_one.send_keys(social_media_search_textbox_text)
                    time.sleep(1)
                    break


def check_box_social_media_search(driver, social_media_item_checkbox):

    """ Method to perform click action on chrckboxes in social media """

    social_media_option = driver.find_elements_by_class_name("socialMediaOptions")
    for item in social_media_option:
        social_media_checkbox_container = item.find_element_by_class_name("socialMediaCheckboxContainer")
        social_media_item_attribute = social_media_checkbox_container.get_attribute("title")
        if social_media_item_attribute == social_media_item_checkbox:
            social_media_checkbox_container.click()
            time.sleep(1)
            break


def click_minimize_btn(driver, tool_dialog_title_text_text):

    """ Method to perform click action on minimize button """

    custom_dialog_titleBar = driver.find_elements_by_class_name("customDialogTitleBar")
    for item in custom_dialog_titleBar:
        tool_dialog_title_text = item.find_element_by_class_name("toolDialogTitleText")
        minimize_btn = item.find_element_by_class_name("minmaxIcon")
        if tool_dialog_title_text.text == tool_dialog_title_text_text:
            minimize_btn.click()
            time.sleep(1)
            break


def click_maximize_btn(driver, tool_dialog_title_text_text):

    """ Method to perform action on maximiz button of widget """

    custom_dialog_titleBar = driver.find_elements_by_class_name("customDialogTitleBar")
    for item in custom_dialog_titleBar:
        tool_dialog_title_text = item.find_element_by_class_name("toolDialogTitleText")
        maximize_btn = item.find_element_by_class_name("minmaxIcon")
        if tool_dialog_title_text.text == tool_dialog_title_text_text:
            maximize_btn.click()
            time.sleep(1)
            break


def click_popup_close_icon(driver, agency_feeds_items):

    """ Common method to perform close action on popup """

    try:
        dijit_dialog_title_Bar = driver.find_elements_by_class_name("dijitDialogTitleBar")
        for item in dijit_dialog_title_Bar:
            dijit_dialog_title = item.find_element_by_class_name("dijitDialogTitle")
            dijit_dialog_close_icon = item.find_element_by_class_name("dijitDialogCloseIcon")
            if dijit_dialog_title.text == agency_feeds_items:
                dijit_dialog_close_icon.click()
                time.sleep(2)
                break
    except Exception:
        return True


def open_right_panel(driver, right_panel_label):

    """ Common method to perform open action on right panel """

    remove_right_border = driver.find_elements_by_class_name("removeRightBorder")
    for item in remove_right_border:
        remove_right_border_label = item.get_attribute("label")
        if remove_right_border_label == right_panel_label:
            item.click()
            time.sleep(2)
            break


def agency_feed_avl_fill_data(driver, agency_feed_avl_item, agency_feed_avl_textbox_text):

    """ Common method to perform actions in AVL tab of agency feed """

    avl_tab_content = driver.find_elements_by_class_name("avlTabContent")
    for item in avl_tab_content:
        avl_live_textBox = item.find_element_by_class_name("avlLiveTextBox")
        if avl_live_textBox.text == agency_feed_avl_item:
            dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
            dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
            dijit_input_inner.clear()
            dijit_input_inner.send_keys(agency_feed_avl_textbox_text)
            break


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


def close_popup_window(driver, popup_window_text):

    """ Common Method to perform action on popup close icon """

    try:
        dijit_dialog_title_bar = driver.find_elements_by_class_name("dijitDialogTitleBar")
        for item in dijit_dialog_title_bar:
            dijit_dialog_title = item.find_elements_by_class_name("dijitDialogTitle")
            dijit_dialog_close_icon = item.find_elements_by_class_name("dijitDialogCloseIcon")
            if dijit_dialog_title.text == popup_window_text:
                dijit_dialog_close_icon.click()
                break
    except Exception:
        return True


def agency_feed_lpr_fill_data(driver, agency_feed_lpr_item, agency_feed_lpr_textbox_text):

    """ Common method to perform actions in LPR tab of agency feed """

    lpr_tab_content = driver.find_elements_by_class_name("lprTabContent")
    for item in lpr_tab_content:
        lpr_live_textBox = item.find_element_by_class_name("lprLiveTextBox")
        if lpr_live_textBox.text == agency_feed_lpr_item:
            dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
            dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
            dijit_input_inner.clear()
            dijit_input_inner.send_keys(agency_feed_lpr_textbox_text)
            break


def agency_feed_lpr_ddl_list(driver, agency_feed_lpr_item):

    """ Common method to perfrom actions in LPR tab of agency feed """

    lpr_tab_content = driver.find_elements_by_class_name("lprTabContent")
    for item in lpr_tab_content:
        lpr_live_textBox = item.find_element_by_class_name("lprLiveTextBox")
        if lpr_live_textBox.text == agency_feed_lpr_item:
            dijit_arrow_button_container = item.find_element_by_class_name("dijitArrowButtonContainer")
            dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitArrowButtonInner")
            dijit_arrow_button_inner.click()
            time.sleep(1)
            break


def agency_feed_lpr_ddl_item(driver, ddl_item_text):

    """ Method to perfrom actions to select DDL item """

    dijit_menu_item = driver.find_elements_by_class_name("dijitMenuItem")
    for item in dijit_menu_item:
        if item.text == ddl_item_text:
            item.click()
            time.sleep(1)
            break


def click_agency_feed_lpr_ok_btn(driver):

    """ Method to perform action on Ok btn of LPR tab of agency feed """

    lpr_live_tab_Content = driver.find_elements_by_class_name("lprLiveTabContent")
    for item in lpr_live_tab_Content:
        lpr_live_textBox = item.find_elements_by_class_name("lprLiveTextBox")
        lpr_Ok_content_btn = item.find_elements_by_class_name("avlOkContent")
        for item1 in lpr_live_textBox:
            for item2 in lpr_Ok_content_btn:
                if item1.text == "Hits":
                    item2.click()
                    break


def click_bottom_panel_layer(driver, layer_name):

    """ Common method to perform action on click action on bottom layers """

    layer_content = driver.find_elements_by_class_name("layerContent")
    for item in layer_content:
        if item.text == layer_name:
            item.click()
            break


























































#        for item1 in search_social_media_label:
#            search_social_media_search_div_textbox = item.find_elements_by_class_name("dijitInputContainer")
#            for item2 in search_social_media_search_div_textbox:
#                if item1.text == social_media_search_textbox:
#                    search_social_media_search_text_box_one = item2.find_element_by_class_name("dijitInputInner")
#                    search_social_media_search_text_box_one.clear()
#                    search_social_media_search_text_box_one.send_keys(social_media_search_textbox_text)
#                    time.sleep(1)
#                    break














































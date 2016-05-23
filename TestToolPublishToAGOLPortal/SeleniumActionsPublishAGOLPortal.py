# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


from GeoshieldCommonFiles import AppCommanUtility, TestFailScreenShots, TestLog, TestResults
import time


def click_widget_icon(driver, tools_utilities_publish_to_AGOL_item, index, ws_index):

    """ Method to perfrom click action on widget tool """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_publish_to_AGOL_item, "click_widget_icon")


def click_advanced_search_item_publish_to_AGOL(driver, tools_utilities_publish_to_AGOL_item, tool_AGOL_publish_textbox_username_text, tool_AGOL_publish_textbox_passward_text, tool_AGOL_publish_textbox_webmaptitle_text, index, ws_index):

    """ Method to click on item publish to AGOL"""

    AppCommanUtility.click_widget_items(driver, tools_utilities_publish_to_AGOL_item, index, ws_index)

    fill_data_publish_to_AGOL_tab(driver, "Username", tool_AGOL_publish_textbox_username_text, tools_utilities_publish_to_AGOL_item, index, ws_index)
    fill_data_publish_to_AGOL_tab(driver, "Password", tool_AGOL_publish_textbox_passward_text, tools_utilities_publish_to_AGOL_item, index, ws_index)
    fill_data_publish_to_AGOL_tab(driver, "Webmap Title", tool_AGOL_publish_textbox_webmaptitle_text, tools_utilities_publish_to_AGOL_item, index, ws_index)

    click_okbtn_publish_to_AGOL_tab(driver, tools_utilities_publish_to_AGOL_item, index, ws_index, class_name="publishMapButton")


def fill_data_publish_to_AGOL_tab(driver, publish_tab_label_text, publish_tab_field_text, tools_utilities_publish_to_AGOL_item, index, ws_index):

    """ Method to fill data in publish to AGOL """
    try:
        custom_dialog_panel = driver.find_element_by_class_name("customDialogPanel")
        web_map_row = custom_dialog_panel.find_elements_by_class_name("webMapRow")
        for item in web_map_row:
            try:
                web_map_row_label = item.find_element_by_class_name("publishColLabel")
            except Exception:
                continue
            if web_map_row_label.text == publish_tab_label_text:
                dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
                dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
                dijit_input_inner.clear()
                dijit_input_inner.send_keys(publish_tab_field_text)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_publish_to_AGOL_item, "fill_data_publish_to_AGOL_tab")
        TestLog.log_creation(tools_utilities_publish_to_AGOL_item, "fill_data_publish_to_AGOL_tab", index, ws_index)


def click_okbtn_publish_to_AGOL_tab(driver,tools_utilities_publish_to_AGOL_item, index, ws_index, class_name):

    """ Method to click OK button of publish to AGOL """
    try:
        publish_map_button = driver.find_element_by_class_name(class_name)
        publish_map_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_publish_to_AGOL_item, "click_okbtn_publish_to_AGOL_tab")
        TestLog.log_creation(tools_utilities_publish_to_AGOL_item, "click_okbtn_publish_to_AGOL_tab", index, ws_index)


def fill_credentils_arcgis_signin(driver):

    """ Method to fill data in arcgis online """

    time.sleep(20)

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)

    driver.switch_to.frame(driver.find_element_by_id("oAuthFrame"))

#    AppCommanUtility.wait_to_load_webelement(driver, "id", "user_username")

    username_field = driver.find_element_by_id("user_username")
    username_field.clear()
    username_field.send_keys("geoshield1")

    passward_field = driver.find_element_by_id("user_password")
    passward_field.clear()
    passward_field.send_keys("cybertech1")

    click_okbtn_arcgis_signin(driver, id="signIn")


def click_okbtn_arcgis_signin(driver, id):

    """ Method to click on sign in button of arcgis online """

    sign_in_btn = driver.find_element_by_id(id)
    sign_in_btn.click()


def tool_publish_to_AGOL_validation(driver, tool_AGOL_publish_textbox_webmaptitle_text, tools_utilities_publish_to_AGOL_item, index, ws_index):

    """ Method to validate the tool publish to AGOL """

    try:
        time.sleep(15)
#        AppCommanUtility.wait_to_load_webelement(driver, "id", "webmap-title-text")
        webmap_title_text = driver.find_element_by_id("webmap-title-text")
        if webmap_title_text.text == tool_AGOL_publish_textbox_webmaptitle_text:
            return True
        else:
            TestFailScreenShots.get_screenshots(driver, tools_utilities_publish_to_AGOL_item, "click_okbtn_publish_to_AGOL_tab")
            TestLog.log_creation(tools_utilities_publish_to_AGOL_item, "click_okbtn_publish_to_AGOL_tab", index, ws_index)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tools_utilities_publish_to_AGOL_item, "click_okbtn_publish_to_AGOL_tab")
        TestLog.log_creation(tools_utilities_publish_to_AGOL_item, "click_okbtn_publish_to_AGOL_tab", index, ws_index)

    TestResults.open_py_excel_pass(index, ws_index)
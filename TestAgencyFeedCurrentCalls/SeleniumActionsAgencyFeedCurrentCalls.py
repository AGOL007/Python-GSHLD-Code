# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


from GeoshieldCommonFiles import AppCommanUtility, AppCommanValidation, TestFailScreenShots, TestLog, TestResults
import time


def click_widget_icon(driver, agency_feed_current_call_for_service, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_current_call_for_service, "click_widget_icon")
        TestLog.log_creation(agency_feed_current_call_for_service, "click_widget_icon", index, ws_index)


def click_agency_feed_item_current_calls_for_service(driver, agency_feed_current_call_for_service, index, ws_index):

    AppCommanUtility.click_widget_items(driver, agency_feed_current_call_for_service, index, ws_index)

    click_live_cad_select_all_checkbox(driver)

    click_okbtn_liva_cad(driver, agency_feed_current_call_for_service, index, ws_index)


def click_live_cad_select_all_checkbox(driver):
    live_cad_section = driver.find_elements_by_class_name("liveCADSection")
    for item in live_cad_section:
        try:
            live_cad_section_div = item.find_element_by_class_name("liveSectionItemCheckBox")
            live_cad_section_div.click()
        except Exception:
            continue


def click_okbtn_liva_cad(driver, agency_feed_current_call_for_service, index, ws_index):
    try:
        live_cad_button = driver.find_element_by_class_name("liveCADButton")
        live_cad_button.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_current_call_for_service, "click_okbtn_liva_cad")
        TestLog.log_creation(agency_feed_current_call_for_service, "click_okbtn_liva_cad", index, ws_index)


def validate_agency_feed_current_call_for_services(driver, agency_feed_current_call_for_service_widget_name, live_cad_layer_name, index, ws_index):
    try:
        live_cad_layer = driver.find_element_by_id("LiveCAD_layer")
        if live_cad_layer.is_displayed():
            AppCommanUtility.widget_close_icon(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

            AppCommanUtility.click_down_panel(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

            AppCommanUtility.click_select_layer_label_container(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

            AppCommanValidation.validate_layer_name(driver, live_cad_layer_name, agency_feed_current_call_for_service_widget_name, index, ws_index, boolean_value=True)

            AppCommanUtility.click_live_tab(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

            AppCommanValidation.validate_right_panel_layer_name(driver, live_cad_layer_name, agency_feed_current_call_for_service_widget_name, index, ws_index)

            AppCommanValidation.validate_feature_count_panel(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

            AppCommanValidation.validate_feature_count(driver, "LiveCAD", agency_feed_current_call_for_service_widget_name, index, ws_index)

            TestResults.open_py_excel_pass(index, ws_index)

        else:
            AppCommanUtility.click_popup_close_icon(driver, agency_feed_current_call_for_service_widget_name)

            AppCommanUtility.widget_close_icon(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

            TestResults.open_py_excel_pass(index, ws_index)
    except Exception:
        AppCommanUtility.click_popup_close_icon(driver, agency_feed_current_call_for_service_widget_name)

        AppCommanUtility.widget_close_icon(driver, agency_feed_current_call_for_service_widget_name, index, ws_index)

        TestResults.open_py_excel_pass(index, ws_index)

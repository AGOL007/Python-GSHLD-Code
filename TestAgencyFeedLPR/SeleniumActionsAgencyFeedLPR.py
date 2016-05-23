import time
from GeoshieldCommonFiles import AppCommanUtility, AppCommanValidation, TestLog, TestFailScreenShots, TestResults


def click_widget_icon(driver, agency_feed_lpr, index, ws_index):

    """ Method to perform click action on widget  """
    try:
        time.sleep(1)
        tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='advancedDataQueries_img']")
        tab_item_div.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_lpr, "click_widget_icon")
        TestLog.log_creation(agency_feed_lpr, "click_widget_icon", index, ws_index)


def click_agency_feed_lpr(driver, agency_feed_lpr, agency_feed_lpr_textbox, index, ws_index):
    AppCommanUtility.click_widget_items(driver, agency_feed_lpr, index, ws_index)

    agency_feed_lpr_fill_data(driver, "License Plate Number", agency_feed_lpr_textbox, index, ws_index)

    click_lpr_live_okbtn(driver, agency_feed_lpr_textbox, index, ws_index)

    validate_agency_feed_lpr_live_tab(driver, agency_feed_lpr_textbox, agency_feed_lpr, index, ws_index)


def agency_feed_lpr_fill_data(driver, agency_feed_lpr_item, agency_feed_lpr_textbox_text, index, ws_index):

    """ Common method to perform actions in LPR tab of agency feed """
    try:
        lpr_tab_content = driver.find_elements_by_class_name("lprTabContent")
        for item in lpr_tab_content:
            lpr_live_textBox = item.find_element_by_class_name("lprLiveTextBox")
            if lpr_live_textBox.text == agency_feed_lpr_item:
                dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
                dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
                dijit_input_inner.clear()
                dijit_input_inner.send_keys(agency_feed_lpr_textbox_text)
                break

    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_lpr_item, "agency_feed_lpr_fill_data")
        TestLog.log_creation(agency_feed_lpr_item, "agency_feed_lpr_fill_data", index, ws_index)


def click_lpr_live_okbtn(driver, agency_feed_lpr_item, index, ws_index):
    try:
        lpr_Ok_Content = driver.find_elements_by_class_name("lprOkContent")
        lpr_Ok_Content[0].click()
        time.sleep(2)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_lpr_item, "agency_feed_lpr_fill_data")
        TestLog.log_creation(agency_feed_lpr_item, "agency_feed_lpr_fill_data", index, ws_index)


def validate_agency_feed_lpr_live_tab(driver, agency_feed_lpr_textbox, agency_feed_lpr_item, index, ws_index):

    try:
        lpr_live_layer = driver.find_element_by_id("lprLive_layer")
        if lpr_live_layer.is_displayed():
            AppCommanUtility.click_minimize_btn(driver, "LPR", index, ws_index)

            AppCommanUtility.click_down_panel(driver, agency_feed_lpr_item, index, ws_index)

            AppCommanUtility.click_select_layer_label_container(driver, agency_feed_lpr_item, index, ws_index)

            AppCommanValidation.validate_layer_name(driver, "LPN SUSPECT", agency_feed_lpr_item, index, ws_index, boolean_value=True)

            AppCommanUtility.click_live_tab(driver, agency_feed_lpr_item, index, ws_index)

            AppCommanValidation.validate_right_panel_layer_name(driver, "LPN SUSPECT", agency_feed_lpr_item, index, ws_index)

            AppCommanValidation.validate_feature_count(driver, "lpnlive", agency_feed_lpr_item, index, ws_index)

            AppCommanUtility.click_maximize_btn(driver, "LPR", index, ws_index)

        else:
            AppCommanUtility.click_popup_close_icon(driver, "LPR")

    except Exception:

            AppCommanUtility.click_popup_close_icon(driver, "LPR")


def click_agency_feed_lpr_historic_select_by_lpn(driver, agency_feed_lpr_textbox, agency_feed_lpr_item, index, ws_index):

    AppCommanUtility.select_sub_tool(driver, "Historic",  index, ws_index, class_name="removeRightBorder")

    agency_feed_lpr_fill_data(driver, "License Plate Number", agency_feed_lpr_textbox, index, ws_index)

    agency_feed_lpr_ddl_list(driver, "Hits", agency_feed_lpr_item, index, ws_index)

    AppCommanUtility.select_ddl_item(driver, "All", agency_feed_lpr_item, index, ws_index)

    agency_feed_lpr_ddl_list(driver, "Unit", agency_feed_lpr_item, index, ws_index)

    AppCommanUtility.select_ddl_item(driver, "ALL", agency_feed_lpr_item, index, ws_index)

    agency_feed_date_fill_date(driver, "Select by LPN")

    click_lpr_select_by_lpn_okbtn(driver, agency_feed_lpr_item, index, ws_index)


def agency_feed_lpr_ddl_list(driver, agency_feed_lpr_item, agency_feed_lpr, index, ws_index):

    """ Common method to perfrom actions in LPR tab of agency feed """
    try:
        lpr_tab_content = driver.find_elements_by_class_name("lprTabContent")
        for item in lpr_tab_content:
            lpr_live_textBox = item.find_element_by_class_name("lprLiveTextBox")
            if lpr_live_textBox.text == agency_feed_lpr_item:
                dijit_arrow_button_container = item.find_element_by_class_name("dijitArrowButtonContainer")
                dijit_arrow_button_inner = dijit_arrow_button_container.find_element_by_class_name("dijitArrowButtonInner")
                dijit_arrow_button_inner.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, agency_feed_lpr_item, "agency_feed_lpr_ddl_list")
        TestLog.log_creation(agency_feed_lpr_item, "agency_feed_lpr_ddl_list", index, ws_index)


def click_lpr_select_by_lpn_okbtn(driver, agency_feed_lpr, index, ws_index):

    lpr_Ok_Content = driver.find_elements_by_class_name("lprOkContent")
    lpr_Ok_Content[1].click()
    time.sleep(2)

    avl_historic_layer = driver.find_element_by_id("historicLayer_layer")
    if avl_historic_layer.is_displayed():
        AppCommanUtility.click_minimize_btn(driver, "LPR", index, ws_index)

        AppCommanUtility.click_down_panel(driver, agency_feed_lpr, index, ws_index)

        AppCommanUtility.click_select_layer_label_container(driver, agency_feed_lpr, index, ws_index)

        AppCommanValidation.validate_layer_name(driver, "LPN Historic Layer", agency_feed_lpr, index, ws_index, boolean_value=True)

        AppCommanValidation.validate_right_panel_layer_name(driver, "LPN Historic Layer", agency_feed_lpr, index, ws_index)

        AppCommanValidation.validate_feature_count(driver, "historicLayer", agency_feed_lpr, index, ws_index)

        AppCommanUtility.click_maximize_btn(driver, "LPR", index, ws_index)

    else:
        AppCommanUtility.click_popup_close_icon(driver, "LPR")


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


def click_historic_select_by_area(driver, agency_feed_lpr_distance_textbox, agency_feed_lpr, index, ws_index):

    avl_deactive_radio_button = driver.find_element_by_class_name("lprDeactiveRadioButton")
    avl_deactive_radio_button.click()

    select_geometry_tab(driver)

    AppCommanUtility.click_on_map(driver, agency_feed_lpr, index, ws_index)

    agency_feed_lpr_fill_data(driver, "Distance", agency_feed_lpr_distance_textbox, index, ws_index)

#    agency_feed_date_fill_date(driver, "Select by Area")

    click_okbtn_lpr_select_by_area(driver)

    AppCommanUtility.click_popup_close_icon(driver, "LPR")

    AppCommanUtility.widget_close_icon(driver, "LPR", index, ws_index)

    validate_select_by_area_buffer(driver)

    TestResults.open_py_excel_pass(index, ws_index)


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


def click_okbtn_lpr_select_by_area(driver):
    lpr_Ok_Content = driver.find_elements_by_class_name("lprOkContent")
    lpr_Ok_Content[2].click()
    time.sleep(2)


def validate_select_by_area_buffer(driver):

    try:
        avlDraw_buffer_layer = driver.find_element_by_id("lprDrawBuffer_layer")
        if avlDraw_buffer_layer.is_dispalyed():
            return True
        else:
            return False
    except Exception:
        return False
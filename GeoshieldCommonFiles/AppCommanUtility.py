# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
import xml.etree.ElementTree as ET
import xlrd
import TestLog
import TestLogBombBlast
import TestFailScreenShots

def getData(fileName, sheet_index):
    myrows = []
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(sheet_index)
    for row_index in range(1, sheet.nrows):
        myrows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
    return myrows


def click_left_panel_open(driver, tool_name, index, ws_index, method_name):

    """ Method to perform click action on left panel """
    try:
        time.sleep(3)
        wait_to_load_webelement(driver, "class_name", "panelOpenCloseContainer")
        panel_open_close_container = driver.find_element_by_class_name("panelOpenCloseContainer")
        panel_open_close_container.click()

    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, method_name)
        TestLog.log_creation(tool_name, "click_left_panel_open", index, ws_index)


def click_left_panel_open_div(driver):

    """ Method to click on left panel div """

    panel_open_close_container = driver.find_element_by_class_name("panelOpenCloseContainer")
    panel_open_close_container_div = panel_open_close_container.find_element_by_class_name("leftSidePanelCollapseOpen")
    panel_open_close_container_div.click()


def click_browse_tab_item(driver, title_text_node, tool_name, index, ws_index):

    """ Common Method to perform click action on browse tab item """
    try:
        browse_tab_item = driver.find_elements_by_class_name("dijitAccordionTitle")
        for item in browse_tab_item:
            browse_tab_item_title = item.find_element_by_class_name("dijitAccordionText")
            if browse_tab_item_title.text == title_text_node:
                browse_tab_item_title.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_browse_tab_item")
        TestLog.log_creation(tool_name, "click_browse_tab_item", index, ws_index)


def wait_to_load_webelement(driver, search_element, search_attribute):

    """ Wait to load an element """

    for i in range(0, 30):
        try:
            if search_element == "class_name":
                loading_element = driver.find_element_by_class_name(search_attribute)
            elif search_element == "id":
                loading_element = driver.find_element_by_id(search_attribute)
            elif search_element == "tag_name":
                loading_element = driver.find_element_by_tag_name(search_attribute)
            if loading_element.is_displayed():
                if loading_element.is_enabled():
                    return True
        except Exception:
            time.sleep(1)
            continue


def click_widget_items(driver, social_media_items, index, ws_index):

    """ Common Method to perform action on social media items click  """
    count = 0
    try:
        widget_item = driver.find_elements_by_class_name("backGroundToolIcon")
        for item in widget_item:
            widget_item_div = item.find_element_by_class_name("iconTool")
            widget_item_attribute = widget_item_div.get_attribute("title")
            if widget_item_attribute == social_media_items:
                count = count + 1
                widget_item_div.click()
                time.sleep(1)
                break
        if count == 0:
            TestFailScreenShots.get_screenshots(driver, social_media_items, "click_widget_items")
            TestLog.log_creation(social_media_items, "click_widget_items", index, ws_index)
    except Exception:
        TestFailScreenShots.get_screenshots(driver, social_media_items, "click_widget_items")
        TestLog.log_creation(social_media_items, "click_widget_items", index, ws_index)


def click_minimize_btn(driver, tool_dialog_title_text_text, index, ws_index):

    """ Method to perform click action on minimize button """
    try:
        custom_dialog_titleBar = driver.find_elements_by_class_name("customDialogTitleBar")
        for item in custom_dialog_titleBar:
            tool_dialog_title_text = item.find_element_by_class_name("toolDialogTitleText")
            minimize_btn = item.find_element_by_class_name("minmaxIcon")
            if tool_dialog_title_text.text == tool_dialog_title_text_text:
                minimize_btn.click()
                time.sleep(1)
                break
    except Exception:
        TestLog.log_creation(tool_dialog_title_text_text, "click_minimize_btn", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_dialog_title_text_text)


def click_maximize_btn(driver, tool_dialog_title_text_text, index, ws_index):

    """ Method to perform action on maximiz button of widget """
    try:
        custom_dialog_titleBar = driver.find_elements_by_class_name("customDialogTitleBar")
        for item in custom_dialog_titleBar:
            tool_dialog_title_text = item.find_element_by_class_name("toolDialogTitleText")
            maximize_btn = item.find_element_by_class_name("minmaxIcon")
            if tool_dialog_title_text.text == tool_dialog_title_text_text:
                maximize_btn.click()
                time.sleep(1)
                break

    except Exception:
        TestLog.log_creation(tool_dialog_title_text_text, "click_maximize_btn", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_dialog_title_text_text)


def widget_close_icon(driver, social_media_items, index, ws_index):

    """ Common method to close widgets """
    count = 0
    try:
        tool_dialog_title_container = driver.find_elements_by_class_name("customDialogTitleBar")
        for item in tool_dialog_title_container:
            tool_dialog_title_div = item.find_element_by_class_name("toolDialogTitleText")
            tool_dialog_title_div_text = tool_dialog_title_div.text
            custom_dialog_close_icon = item.find_element_by_class_name("customDialogCloseIcon")
            if social_media_items == tool_dialog_title_div_text:
                count = count + 1
                custom_dialog_close_icon.click()
                time.sleep(2)
                break
        if count == 0:
            TestLog.log_creation(social_media_items, "widget_close_icon", index, ws_index)
            TestFailScreenShots.get_screenshots(driver, social_media_items)
    except Exception:
        TestLog.log_creation(social_media_items, "widget_close_icon", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, social_media_items)


def click_expand_button_div(driver, event_rms_or_cad_name, tool_name, index, ws_index):

    """ Common Method to perform action on expand button """
    try:
        event_container = driver.find_elements_by_class_name("categoryGroupPanel")
        for item in event_container:
            event_container_div = item.find_element_by_class_name("expandButtonDiv")
            event_container_div_list = item.find_element_by_class_name("groupNameConatiner")
            if event_container_div_list.text == event_rms_or_cad_name:
                event_container_div.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_expand_button_div")
        TestLog.log_creation(tool_name, "", index, ws_index)


def click_toggel_btn(driver, event_rms_or_cad_name, tool_name, index, ws_index):

    """ Common Method to perform action on toggle button """
    try:
        event_container = driver.find_elements_by_class_name("subCategoryDataPanel")
        for item in event_container:
            event_container_div_list = item.find_element_by_class_name("subCategoryLabel")
            toggel_btn_container = item.find_element_by_class_name("toggleButtonBackGroundColor")
            if event_container_div_list.text == event_rms_or_cad_name:
                toggel_btn_container.click()
                time.sleep(1)
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_toggel_btn")
        TestLog.log_creation(tool_name, "click_toggel_btn", index, ws_index)


def click_down_panel(driver, tool_name, index, ws_index):

    """Method to perfrom click action on down panel"""
    try:
        wait_to_load_webelement(driver, "class_name", "layerDataGridPanelOpenCloseContanier")
        panal_open_close_container = driver.find_element_by_class_name("layerDataGridPanelOpenCloseContanier")
        panal_open_close_container.click()
    except Exception:
        TestLog.log_creation(tool_name, "click_down_panel", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_down_panel")


def click_select_layer_label_container(driver, tool_name, index, ws_index):

    """ Method to perform click on layer label container"""
    try:
        wait_to_load_webelement(driver, "class_name", "selectLayerLabelConatiner")
        select_layer_container = driver.find_element_by_class_name("selectLayerLabelConatiner")
        if select_layer_container.is_displayed():
            select_layer_container.click()
        else:
            TestLog.log_creation(tool_name, "click_select_layer_label_container", index, ws_index)
            TestFailScreenShots.get_screenshots(driver, tool_name, "click_select_layer_label_container")
    except Exception:
        TestLog.log_creation(tool_name, "click_select_layer_label_container", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_select_layer_label_container")


def click_right_panel_open(driver, tool_name, index, boolean_value, ws_index):

    """ Method to perform click action on right panel """
    try:
        wait_to_load_webelement(driver, "class_name", "rightPanelOpenCloseContanier")
        panel_open_close_container = driver.find_element_by_class_name("rightPanelOpenCloseContanier")
        panel_open_close_container.click()
        if boolean_value:
            click_active_data_tab(driver)
    except Exception:
        TestLog.log_creation(tool_name, "click_right_panel_open", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_right_panel_open")


def click_active_data_tab(driver):

    """ Method to perform click action on tab of active data """

    active_data = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='activeData_button_title']")
    active_data.click()


def click_bottom_panel_layer(driver, layer_name, tool_name, index, ws_index):

    """ Common method to perform action on click action on bottom layers """
    try:
        layer_content = driver.find_elements_by_class_name("layerContent")
        for item in layer_content:
            if item.text == layer_name:
                item.click()
                time.sleep(2)
                break

    except Exception:
        TestLog.log_creation(tool_name, "click_bottom_panel_layer", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_bottom_panel_layer")


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


def select_ddl_item(driver, ddl_item_text, tool_name, index, ws_index):

    """ Method to perfrom actions to select DDL item """
    try:
        dijit_menu_item = driver.find_elements_by_class_name("dijitMenuItem")
        for item in dijit_menu_item:
            if item.text == ddl_item_text:
                item.click()
                time.sleep(1)
                return True
            elif ddl_item_text in item.text:
                item.click()
                time.sleep(1)
                return True
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "select_ddl_item")
        TestLog.log_creation(tool_name, "select_ddl_item", index, ws_index)


def fill_data_tools_fields(driver, agency_feed_place_holder_text, search_attribute_text_box_text):

    """ Common method to fill the data in fields of different tools """

    search_finder_div_text_box = driver.find_elements_by_class_name("dijitValidationTextBox")
    for item in search_finder_div_text_box:
        search_finder_div_text_box_one = item.find_element_by_class_name("dijitInputContainer")
        search_finder_div_text_box_one_placeholder = search_finder_div_text_box_one.find_element_by_class_name("dijitPlaceHolder")
        if search_finder_div_text_box_one_placeholder.text == agency_feed_place_holder_text:
            dijit_input_container = item.find_element_by_class_name("dijitInputContainer")
            dijit_input_inner = dijit_input_container.find_element_by_class_name("dijitInputInner")
            dijit_input_inner.clear()
            dijit_input_inner.send_keys(search_attribute_text_box_text)
            break


def click_graphics_tab(driver, tool_name, index, ws_index):

    """ Method to click on graphics tab of right panel """
    try:
        time.sleep(1)
        active_data = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='graphicLayers_button_title']")
        active_data.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_graphics_tab")
        TestLog.log_creation(tool_name, "click_graphics_tab", index, ws_index)


def click_live_tab(driver, tool_name, index, ws_index):

    """ Method to click on graphics tab of right panel """
    try:
        time.sleep(1)
        live_tab = driver.find_element_by_xpath("//div[@class='dijitAccordionTitleFocus']/span[@id='live_button_title']")
        live_tab.click()
    except Exception:
        TestFailScreenShots.get_screenshots(driver, tool_name, "click_live_tab")
        TestLog.log_creation(tool_name, "click_live_tab", index, ws_index)


def click_on_map(driver, tool_name, index, ws_index):

    """ Method to click on map"""

    try:
        click_on_map_div = driver.find_element_by_id("mapContainer")
        if click_on_map_div.is_displayed():
            click_on_map_div.click()
            time.sleep(2)
        else:
            TestLog.log_creation(tool_name, "click_on_map", index, ws_index)
            TestFailScreenShots.get_screenshots(driver, tool_name)
    except Exception:
        TestLog.log_creation(tool_name, "click_on_map", index, ws_index)
        TestFailScreenShots.get_screenshots(driver, tool_name)
#        TestExcel.open_py_excel_pass(sheet_index, index)
#        time.sleep(2)
#    else:
#        TestExcel.open_py_excel_fail()


def select_buffer_graphic_icons(driver, geometry_title):

    """ Method to click on buffer graphic icons"""

    select_buffer_graphic_icons_div = driver.find_elements_by_class_name("selectBufferGraphicIcons")
    for item in select_buffer_graphic_icons_div:
        select_buffer_graphic_icons_attribute = item.get_attribute("title")
        if select_buffer_graphic_icons_attribute == geometry_title:
            item.click()
            break


def select_sub_tool(driver, sub_tool_text, index, ws_index, class_name):

    """ Method to click on sub-tool item """
    try:
        remove_right_border = driver.find_elements_by_class_name(class_name)
        for item in remove_right_border:
            if item.text == sub_tool_text:
                item.click()
                break
    except Exception:
        TestFailScreenShots.get_screenshots(driver, sub_tool_text, "select_sub_tool")
        TestLog.log_creation(sub_tool_text, "select_sub_tool", index, ws_index)


def click_tab_control_node(driver, node_text):

    """ Method to click on sub node of the tool """

    tab_control_node = driver.find_elements_by_class_name("tabControlNode")
    for item in tab_control_node:
        if item.is_displayed():
            tab_control_node_div = item.find_elements_by_tag_name("div")
            for item1 in tab_control_node_div:
                if item1.text == node_text:
                    item1.click()
                    break


def wait_to_load_loading_indicator(driver):
    """ Wait to load an element """

    i = 0
    while True:
        try:
            loading_element = driver.find_elements_by_class_name("spanLoadingText")
            for item in loading_element:
                if item.is_displayed():
                    if item.text == "Initializing widgets...":
                        time.sleep(1)
                        i += 1
                        continue
                    elif item.text == "Loading...":
                        time.sleep(1)
                        i += 1
                        continue
                    elif item.text == "Adding...":
                        time.sleep(1)
                        i += 1
        except Exception:
            break


def parse_browse_value():

    """ Method to parse the data """

    tree = ET.parse(r'C:\Users\sagarkul\Desktop\app.xml')
    root = tree.getroot()
    app_config = []

    for browserval in root.iter('add'):
        app_config.append(browserval.attrib)
        for item in app_config:
            if item['key'] == 'Browser':
                browser_name = item['value']

    if browser_name == "Chrome":
        time.sleep(2)


def tearDown(driver):
    driver.close()


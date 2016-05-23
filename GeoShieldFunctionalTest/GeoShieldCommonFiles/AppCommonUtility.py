

import xlrd
import time


def locator_value(driver, locator_type, value):

    """ Method to get the locator type """

    if locator_type == "id":
        webelement = driver.find_element_by_id(value)
    elif locator_type == "name":
        webelement = driver.find_element_by_name(value)
    elif locator_type == "xpath":
        webelement = driver.find_element_by_name(value)
    elif locator_type == "classname":
        webelement = driver.find_element_by_class_name(value)
    elif locator_type == "tagname":
        webelement = driver.find_element_by_tag_name(value)
    elif locator_type == "classnames":
        webelement = driver.find_elements_by_class_name(value)
    return webelement


def locator_value_two(driver, locator_type, value, item):

    """ Method to get the locator type """

    if locator_type == "id":
        webelement = item.find_element_by_id(value)
    elif locator_type == "name":
        webelement = item.find_element_by_name(value)
    elif locator_type == "xpath":
        webelement = item.find_element_by_name(value)
    elif locator_type == "classname":
        webelement = item.find_element_by_class_name(value)
    elif locator_type == "tagname":
        webelement = item.find_element_by_tag_name(value)
    elif locator_type == "classnames":
        webelement = item.find_elements_by_class_name(value)
    return webelement


def get_data_from_spread_sheet(sheet_index):

    """ Method to get the data from excel """

    workbook = xlrd.open_workbook("C:/Users/sagarkul/Desktop/KeywordDriven.xlsx")
    worksheet = workbook.sheet_by_name(sheet_index)
    row_end_index = worksheet.nrows - 1
    col_end_index = worksheet.ncols - 1
    row_start_index = 0
    col_start_index = 0
    data_row = []
    curr_row = row_start_index
    while curr_row <= row_end_index:
            cur_col = col_start_index
            while cur_col <= col_end_index:
                value = worksheet.cell_value(curr_row, cur_col)
                data_row.append(value)
                cur_col += 1
            curr_row += 1
    return data_row


def enter_text(driver, webelement, text):

    """ Method to enter the text"""

    try:
        webelement.send_keys(text)
    except Exception:
        print "No Element found to enter text"


def click_button(driver, webelement):

    """ Method to click on button """

    try:
        webelement.click()
    except Exception:
        print "No such Element"


def click_browse_tab_item(driver, title_text_node, data_row_index1, data_row_index2, data_row_index3, data_row_index4):

    """ Common Method to perform click action on browse tab item """
    browse_tab_item = locator_value(driver, data_row_index1, data_row_index2)
    for item in browse_tab_item:
        browse_tab_item_title = locator_value_two(driver, data_row_index3, data_row_index4, item)
        if browse_tab_item_title.text == title_text_node:
            click_button(driver, browse_tab_item_title)
            break


def click_expand_button_div(driver, event_rms_or_cad_name, data_row_index1, data_row_index2, data_row_index3, data_row_index4, data_row_index5, data_row_index6):

    """ Common Method to perform action on expand button """

    event_container = locator_value(driver, data_row_index1, data_row_index2)
    for item in event_container:
        event_container_div = locator_value_two(driver, data_row_index3, data_row_index4, item)
        event_container_div_list = locator_value_two(driver, data_row_index5, data_row_index6, item)
        if event_container_div_list.text == event_rms_or_cad_name:
            click_button(driver, event_container_div)
            time.sleep(1)
            break


def click_toggel_btn(driver, event_rms_or_cad_name, data_row_index1, data_row_index2, data_row_index3, data_row_index4, data_row_index5, data_row_index6):

    """ Common Method to perform action on toggle button """

    event_container = locator_value(driver, data_row_index1, data_row_index2)
    for item in event_container:
        event_container_div_list = locator_value_two(driver, data_row_index3, data_row_index4, item)
        toggel_btn_container = locator_value_two(driver, data_row_index5, data_row_index6, item)
        if event_container_div_list.text == event_rms_or_cad_name:
            click_button(driver, toggel_btn_container)
            time.sleep(1)
            break






from GeoShieldCommonFiles import AppCommonUtility
import time


def select_predefined_tab_type(driver, class_name):

    """ Method to select the type of predefined tab"""
    for item in class_name:
        if item.text == "Last 4 days":
            item.click()
            break


def step_execution(driver, browse_tab_container_name, category_main_layer_name, category_sub_layer_name):

    """ Method to execute the steps """

    data_row_index = AppCommonUtility.get_data_from_spread_sheet("Keyword")

    for item in data_row_index:
        if item == "click_left_panel":
            time.sleep(3)
            item1 = data_row_index.index(item)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            AppCommonUtility.click_button(driver, web_elemnt)

        elif item == "click_select_date_value":
            item1 = data_row_index.index(item)
            time.sleep(3)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            AppCommonUtility.click_button(driver, web_elemnt)

        elif item == "click_predefined_daterange_tab":
            item1 = data_row_index.index(item)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            AppCommonUtility.click_button(driver, web_elemnt)

        elif item == "select_predefined_tab_type":
            item1 = data_row_index.index(item)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            select_predefined_tab_type(driver, web_elemnt)

        elif item == "browse_ok_cancel_btn":
            item1 = data_row_index.index(item)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            AppCommonUtility.click_button(driver, web_elemnt)

        elif item == "browse_ok_cancel_btn":
            item1 = data_row_index.index(item)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            AppCommonUtility.click_button(driver, web_elemnt)

        elif item == "click_browse_tab_item":
            item1 = data_row_index.index(item)
            AppCommonUtility.click_browse_tab_item(driver, browse_tab_container_name, data_row_index[item1+1], data_row_index[item1+2], data_row_index[item1+3], data_row_index[item1+4] )

        elif item == "click_expand_button_div":
            item1 = data_row_index.index(item)
            AppCommonUtility.click_expand_button_div(driver, category_main_layer_name, data_row_index[item1+1], data_row_index[item1+2], data_row_index[item1+3], data_row_index[item1+4], data_row_index[item1+5], data_row_index[item1+6])

        elif item == "click_toggel_btn":
            item1 = data_row_index.index(item)
            AppCommonUtility.click_toggel_btn(driver, category_sub_layer_name, data_row_index[item1+1], data_row_index[item1+2], data_row_index[item1+3], data_row_index[item1+4], data_row_index[item1+5], data_row_index[item1+6])


def validation_step_execution(driver):

    data_row_index = AppCommonUtility.get_data_from_spread_sheet("Keyword")

    for item in data_row_index:
        if item == "click_down_panel":
            item1 = data_row_index.index(item)
            web_elemnt = AppCommonUtility.locator_value(driver, data_row_index[item1+1], data_row_index[item1+2])
            AppCommonUtility.click_button(driver, web_elemnt)

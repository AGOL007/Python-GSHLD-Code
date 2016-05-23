# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

from GeoshieldCommonFiles import AppCommanUtility


def click_widget_icon(driver):

    """ Method to perform click action on widget tool """

    tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='tools_img']")
    tab_item_div.click()


def click_navigation_item_google_street_view(driver):

    """ Method to click on google street view"""

    AppCommanUtility.click_widget_items(driver, "Google Street View")
    AppCommanUtility.click_on_map(driver)

    driver.switch_to_window(driver.window_handles[1])


def click_minus_btn_google_street_view(driver):

    """ Method to Zoom out the map"""

    for i in range(0, 2):
        btn_minus = driver.find_element_by_class_name("icon-plus")
        btn_minus.click()


def tool_google_street_view_validation(driver):

    """ Method to validate tool google street view """

    google_street_view_logo = driver.find_element_by_class_name("googleStreetViewLogo")
    if google_street_view_logo.is_displayed():
        return True
    else:
        return False


def switch_main_driver(driver):

    """ Method to switch on main driver """

    driver.close()
    driver.switch_to_window(driver.window_handles[0])
# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'


import time


def click_widget_icon(driver):

    """ Method to click on widget tool """

    time.sleep(1)
    tab_item_div = driver.find_element_by_xpath("//div[@class='iconContainer']/div[@id='workflows_img']")
    tab_item_div.click()


def click_workflow_link_text(driver, workflow_links_text):

    """ Method to select the tool Selection and fill the data in buffer tab of selection"""

    work_flows_container = driver.find_elements_by_class_name("hyperlinkContainer")
    for item in work_flows_container:
        work_flows_container_tag_element = item.find_elements_by_tag_name("a")
        for item1 in work_flows_container_tag_element:
            if item1.text == workflow_links_text:
                item1.click()
                break


def switch_to_driver(driver):

    """ Switch to main driver """

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)


def validate_workflow_widget(driver):

    """ switch to main driver and validate the URl """

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)

    driver_current_url = driver.current_url
    driver.close()

    driver.switch_to_window(window_before)

    work_flows_container = driver.find_elements_by_class_name("hyperlinkContainer")
    for item in work_flows_container:
        work_flows_container_tag_element = item.find_elements_by_tag_name("a")
        for item1 in work_flows_container_tag_element:
            if item1.get_attribute("href") == driver_current_url:
                return True
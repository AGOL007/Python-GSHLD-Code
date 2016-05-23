# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest
from ddt import ddt, data, unpack

import SeleniumActionsBrowseWidget
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser
import time

@ddt
class TestToolSearchAttribute(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 11))
    @unpack
    def test_browse_widget(self, index, result, browse_tab_container_name, category_main_layer_name, category_sub_layer_name, tool_name):

        """ Test Method """

        time.sleep(3)
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, tool_name, int(index), ws_index=11, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsBrowseWidget.click_widget_icon(self.driver, tool_name, int(index), ws_index=11)

        # click on predefined date range tab
        SeleniumActionsBrowseWidget.click_select_date_value(self.driver, tool_name, int(index), ws_index=11)

        # click predefined date range tab
        SeleniumActionsBrowseWidget.click_predefined_daterange_tab(self.driver, tool_name, int(index), ws_index=11)

        # click browse container
        SeleniumActionsBrowseWidget.click_browse_container(self.driver, browse_tab_container_name, category_main_layer_name, category_sub_layer_name, tool_name, index, ws_index=11)

        # validate browse widget
        SeleniumActionsBrowseWidget.validate_browse_widget(self.driver, category_sub_layer_name, tool_name, index, ws_index=11)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

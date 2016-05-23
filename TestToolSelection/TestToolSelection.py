# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionTestToolSelection
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestToolSearchCoordinates(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 6))
    @unpack
    def test_search_coordinate_tool(self, index, result, tools_utilities_selection_item, main_layer_name, sub_layer_name, tool_selection_textbox_distance_text):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, tools_utilities_selection_item, int(index), ws_index=6, method_name="click_left_panel_open")

        # select browse tab
        SeleniumActionTestToolSelection.select_browse_tab_layer(self.driver, main_layer_name, sub_layer_name, tools_utilities_selection_item, int(index), ws_index=6)

        # click widget icon
        SeleniumActionTestToolSelection.click_widget_icon(self.driver, tools_utilities_selection_item, int(index), ws_index=6)

        # click utilities item selection
        SeleniumActionTestToolSelection.click_utilities_item_selection(self.driver, tools_utilities_selection_item, sub_layer_name, int(tool_selection_textbox_distance_text), int(index), ws_index=6)

        # tool selection buffer tab validation
        SeleniumActionTestToolSelection.tool_selection_buffer_validation(self.driver, tools_utilities_selection_item, int(index), ws_index=6)

        # click utilities item proximity
        SeleniumActionTestToolSelection.click_utilities_item_selection_proximity(self.driver, tools_utilities_selection_item, sub_layer_name, int(tool_selection_textbox_distance_text), int(index), ws_index=6)

        # tool selection proximity tab validation
        SeleniumActionTestToolSelection.tool_selection_proximity_validation(self.driver, tools_utilities_selection_item, int(index), ws_index=6)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

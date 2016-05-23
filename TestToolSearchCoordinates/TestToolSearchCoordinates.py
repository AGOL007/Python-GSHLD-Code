# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsToolShowCoordinates
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestToolSearchCoordinates(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 4))
    @unpack
    def test_search_coordinate_tool(self, index, result, tools_navigation_show_coordinates_item, show_coordinate_lable):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver,tools_navigation_show_coordinates_item, int(index), ws_index=4, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsToolShowCoordinates.click_widget_icon(self.driver, tools_navigation_show_coordinates_item, int(index), ws_index=4)

        # click tool search coordinates
        SeleniumActionsToolShowCoordinates.click_advanced_search_item_search_coordinate(self.driver, tools_navigation_show_coordinates_item, int(index), ws_index=4)

        # fill data in show coordinates tool
        SeleniumActionsToolShowCoordinates.fill_data_navigation_show_coordinates_tool(self.driver, show_coordinate_lable, tools_navigation_show_coordinates_item, int(index), ws_index=4)

        # tool validation search coordinates
        SeleniumActionsToolShowCoordinates.search_coordinates_tool_validation(self.driver, tools_navigation_show_coordinates_item, int(index), ws_index=4)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

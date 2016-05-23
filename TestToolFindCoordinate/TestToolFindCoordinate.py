# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsToolFindCoordinate
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestToolFindCoordinate(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 3))
    @unpack
    def test_find_coordinate_tool(self, index, result, tools_navigation_find_coordinates_item, ddl_tool_find_coordinates, ddl_select_coordinate_system_item, find_coordinates_textbox_longitude_text, find_coordinates_textbox_latitude_text, find_coordinates_textbox_long_min_text, find_coordinates_textbox_lat_min_text, find_coordinates_textbox_long_sec, find_coordinates_textbox_lat_sec, find_coordinate_textbox_zone_text, find_coordinate_textbox_zdl_text, find_coordinate_textbox_letter_text, find_coordinate_textbox_EN_text, find_coordinate_textbox_UTM_zone_text, find_coordinate_textbox_easting_text, find_coordinate_textbox_northing_text):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, tools_navigation_find_coordinates_item, int(index), ws_index=3, method_name="click_left_panel_open")

        # click widegt icon tool
        SeleniumActionsToolFindCoordinate.click_widget_icon(self.driver, tools_navigation_find_coordinates_item, int(index), ws_index=3)

        # click advanced search item find coordinates
        SeleniumActionsToolFindCoordinate.click_advanced_search_item_find_coordinate(self.driver, tools_navigation_find_coordinates_item, int(index), ws_index=3)

        # fill data in navigation tool find coordinates
        SeleniumActionsToolFindCoordinate.fill_data_navigation_find_coordinates(self.driver, ddl_tool_find_coordinates, ddl_select_coordinate_system_item, find_coordinates_textbox_longitude_text, find_coordinates_textbox_latitude_text, find_coordinates_textbox_long_min_text, find_coordinates_textbox_lat_min_text, find_coordinates_textbox_long_sec, find_coordinates_textbox_lat_sec, find_coordinate_textbox_UTM_zone_text, find_coordinate_textbox_easting_text, find_coordinate_textbox_northing_text, find_coordinate_textbox_zone_text, find_coordinate_textbox_zdl_text, find_coordinate_textbox_letter_text, find_coordinate_textbox_EN_text, tools_navigation_find_coordinates_item, int(index), ws_index=3)

        # tool validation find coordinates
        SeleniumActionsToolFindCoordinate.find_coordinates_tool_validation(self.driver, tools_navigation_find_coordinates_item, int(index), ws_index=3)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

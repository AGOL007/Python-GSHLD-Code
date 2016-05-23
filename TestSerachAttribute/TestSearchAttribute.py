# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsToolSearchAttribute
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestToolSearchAttribute(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 2))
    @unpack
    def test_serach_attribute_tool(self, index, result, tools_advanced_search_search_attribute_item, search_attribute_textbox_search_layer_text, search_attribute_textbox_Field_text, search_attribute_textbox_Operaror_text, search_attribute_textbox_Value_text, query_name, search_attribute_tool_name, search_attribute_sub_layer_name):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, tools_advanced_search_search_attribute_item, int(index), ws_index=2, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsToolSearchAttribute.click_widget_icon(self.driver, tools_advanced_search_search_attribute_item, int(index), ws_index=2)

        # click advanced search item search attribute
        SeleniumActionsToolSearchAttribute.click_advanced_search_item_search_attribute(self.driver, tools_advanced_search_search_attribute_item, int(index), ws_index=2)

        # fill data search attribute new query
        SeleniumActionsToolSearchAttribute.fill_data_search_attribute_new_query(self.driver, search_attribute_textbox_search_layer_text, search_attribute_textbox_Field_text, search_attribute_textbox_Operaror_text, search_attribute_textbox_Value_text, query_name, search_attribute_tool_name, search_attribute_sub_layer_name, tools_advanced_search_search_attribute_item, index, ws_index=2)

        # click right sub panel prior query
        SeleniumActionsToolSearchAttribute.click_right_sub_panel_prior_query(self.driver, tools_advanced_search_search_attribute_item, index, ws_index=2)

        # fill data search attribute prior query
        SeleniumActionsToolSearchAttribute.fill_data_search_attribute_prior_query(self.driver, query_name, search_attribute_tool_name, index, ws_index=2)

        # search attribute tool validation
        SeleniumActionsToolSearchAttribute.app_validation(self.driver, search_attribute_tool_name, search_attribute_textbox_search_layer_text, search_attribute_sub_layer_name, index, ws_index=2)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

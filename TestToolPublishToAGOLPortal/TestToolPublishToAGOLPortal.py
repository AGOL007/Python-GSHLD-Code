# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest
from TestBase.GeoshieldTestBase import set_browser
from GeoshieldCommonFiles import AppCommanUtility
import SeleniumActionsPublishAGOLPortal

from ddt import ddt, data, unpack
import xlrd

@ddt
class TestToolPublishToAGOLPortal(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 9))
    @unpack
    def test_publish_to_AGOL_tool(self, index, result, tools_utilities_publish_to_AGOL_item, tool_AGOL_publish_textbox_username_text, tool_AGOL_publish_textbox_passward_text, tool_AGOL_publish_textbox_webmaptitle_text):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel open
        AppCommanUtility.click_left_panel_open(self.driver, tools_utilities_publish_to_AGOL_item, int(index), ws_index=9, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsPublishAGOLPortal.click_widget_icon(self.driver, tools_utilities_publish_to_AGOL_item, int(index), ws_index=9)

        # click advance search item publish to AGOL
        SeleniumActionsPublishAGOLPortal.click_advanced_search_item_publish_to_AGOL(self.driver, tools_utilities_publish_to_AGOL_item, tool_AGOL_publish_textbox_username_text, tool_AGOL_publish_textbox_passward_text, tool_AGOL_publish_textbox_webmaptitle_text, int(index), ws_index=9)

        # fill data in arcgis signin tab
        SeleniumActionsPublishAGOLPortal.fill_credentils_arcgis_signin(self.driver)

        # tool validation publish to AGOL
        SeleniumActionsPublishAGOLPortal.tool_publish_to_AGOL_validation(self.driver, tool_AGOL_publish_textbox_webmaptitle_text, tools_utilities_publish_to_AGOL_item, int(index), ws_index=9)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

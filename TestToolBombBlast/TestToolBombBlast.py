# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest
from ddt import ddt, data, unpack
import SeleniumActionsToolBombBlast
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser


@ddt
class TestToolBombBlast(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 7))
    @unpack
    def test_search_coordinate_tool(self, index, result, tools_utilities_bomb_blast_item, tool_bomb_blast_bomb_type, tool_bomb_blast_widget_name):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # Click left panel
        AppCommanUtility.click_left_panel_open(self.driver, tool_bomb_blast_bomb_type, int(index), ws_index=7, method_name="click_left_panel_open")

        # Click bomb blast widget icon
        SeleniumActionsToolBombBlast.click_widget_icon(self.driver, tools_utilities_bomb_blast_item, int(index), ws_index=7)

        # Click bomb blast item selection
        SeleniumActionsToolBombBlast.click_bomb_blast_item_selection(self.driver, tools_utilities_bomb_blast_item, tool_bomb_blast_bomb_type, tool_bomb_blast_widget_name, int(index),ws_index=7)

        # tool validation bomb blast
        SeleniumActionsToolBombBlast.tool_bomb_blast_validation(self.driver, int(index), tool_bomb_blast_widget_name, tools_utilities_bomb_blast_item, ws_index=7)

        # result method

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        #time.sleep(2)
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

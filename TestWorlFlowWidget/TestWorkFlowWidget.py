# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsWorkFlowWidget
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser
@ddt
class TestToolSearchCoordinates(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 10))
    @unpack
    def test_search_coordinate_tool(self, workflow_links_text):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver)

        # click widget icon
        SeleniumActionsWorkFlowWidget.click_widget_icon(self.driver)

        # click work flow link text
        SeleniumActionsWorkFlowWidget.click_workflow_link_text(self.driver, workflow_links_text)

        # validate workflow URL
        SeleniumActionsWorkFlowWidget.validate_workflow_widget(self.driver)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

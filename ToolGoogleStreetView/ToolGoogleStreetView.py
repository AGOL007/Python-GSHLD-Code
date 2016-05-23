# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import SeleniumActionsGoogleStreetView
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser


class TestToolGoogleStreetView(unittest.TestCase):

    def test_google_street_view(self):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver)

        # click widget item
        SeleniumActionsGoogleStreetView.click_widget_icon(self.driver)

        # click on google street view
        SeleniumActionsGoogleStreetView.click_navigation_item_google_street_view(self.driver)

        # validate tool google street view
        SeleniumActionsGoogleStreetView.tool_google_street_view_validation(self.driver)

        # switch to main driver
        SeleniumActionsGoogleStreetView.switch_main_driver(self.driver)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

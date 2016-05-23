# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest
from ddt import ddt, data, unpack

import SeleniumActionsAgencyFeedCurrentCalls
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser


@ddt
class TestAgencyFeedCurrentCallForService(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 16))
    @unpack
    def test_agency_feed_current_call_for_service(self, index, result, agency_feed_current_call_for_service, agency_feed_current_call_for_service_widget_name, live_cad_layer_name):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, agency_feed_current_call_for_service, int(index), ws_index=16, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsAgencyFeedCurrentCalls.click_widget_icon(self.driver, agency_feed_current_call_for_service, int(index), ws_index=16)

        # click agency feed item
        SeleniumActionsAgencyFeedCurrentCalls.click_agency_feed_item_current_calls_for_service(self.driver, agency_feed_current_call_for_service, int(index), ws_index=16)

        # validate agency feed live CAD
        SeleniumActionsAgencyFeedCurrentCalls.validate_agency_feed_current_call_for_services(self.driver, agency_feed_current_call_for_service_widget_name, live_cad_layer_name, int(index), ws_index=16)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

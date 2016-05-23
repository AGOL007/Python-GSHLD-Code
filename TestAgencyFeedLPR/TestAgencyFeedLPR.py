# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

from ddt import ddt, data, unpack

import SeleniumActionsAgencyFeedLPR
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestAgencyFeedLPR(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 18))
    @unpack
    def test_agency_feed_current_call_for_service(self, index, result, agency_feed_lpr, agency_feed_lpr_textbox, agency_feed_lpr_distance_textbox):

        """ Test Method """
        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, agency_feed_lpr, int(index), ws_index=18, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsAgencyFeedLPR.click_widget_icon(self.driver, agency_feed_lpr, int(index), ws_index=18)

        SeleniumActionsAgencyFeedLPR.click_agency_feed_lpr(self.driver, agency_feed_lpr, agency_feed_lpr_textbox, int(index), ws_index=18)

        SeleniumActionsAgencyFeedLPR.click_agency_feed_lpr_historic_select_by_lpn(self.driver, agency_feed_lpr_textbox, agency_feed_lpr, int(index), ws_index=18)

        SeleniumActionsAgencyFeedLPR.click_historic_select_by_area(self.driver, int(agency_feed_lpr_distance_textbox), agency_feed_lpr, int(index), ws_index=18)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

#    def tearDown(self):
#        """ Quit browser"""
#        self.driver.close()

if __name__ == '__main__':
    unittest.main()

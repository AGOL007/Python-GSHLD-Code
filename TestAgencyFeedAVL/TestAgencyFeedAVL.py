# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsAgencyFeedAVL
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestAgencyFeedCurrentCallForService(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 17))
    @unpack
    def test_agency_feed_current_call_for_service(self, index, result, agency_feed_avl, agency_feed_avl_unitid_textbox, agency_feed_avl_distance_textbox,  avl_live_layer_name):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, agency_feed_avl, int(index), ws_index=17, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsAgencyFeedAVL.click_widget_icon(self.driver, agency_feed_avl, int(index), ws_index=17)

        # click agency feed item AVL
        SeleniumActionsAgencyFeedAVL.click_agency_feed_avl(self.driver, agency_feed_avl, int(index), ws_index=17)

        # validate AVL tab
        SeleniumActionsAgencyFeedAVL.validate_avl_live_tab(self.driver, agency_feed_avl, avl_live_layer_name, int(index), ws_index=17)

        # click right panel
        SeleniumActionsAgencyFeedAVL.click_right_tab_historic(self.driver, agency_feed_avl_unitid_textbox, agency_feed_avl, int(index), ws_index=17)

        SeleniumActionsAgencyFeedAVL.click_historic_select_by_area_tab(self.driver, int(agency_feed_avl_distance_textbox), agency_feed_avl, int(index), ws_index=17)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

#    def tearDown(self):
#        """ Quit browser"""
#        self.driver.close()

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsSocialMediaSearch
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestSocialMediaSearch(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 15))
    @unpack
    def test_social_media_social_media_search(self, index, result, social_media_social_media_search, social_media_search_distance_textbox_text, social_media_search_keyword_textbox_text, social_media_search_refreshtime_textbox_text, social_media_search_select_source_item, social_media_search_layer_name, social_media_sub_layer):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, social_media_social_media_search, int(index), ws_index=15, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsSocialMediaSearch.click_widget_icon(self.driver, social_media_social_media_search, int(index), ws_index=15)

        # click social media item social media search
        SeleniumActionsSocialMediaSearch.click_social_media_item_social_media_search(self.driver, social_media_social_media_search, int(social_media_search_distance_textbox_text), social_media_search_keyword_textbox_text, int(social_media_search_refreshtime_textbox_text), int(index), ws_index=15)

        # validate social media item social media search
        SeleniumActionsSocialMediaSearch.social_media_search_validation(self.driver, social_media_social_media_search, social_media_search_select_source_item, social_media_search_layer_name, social_media_sub_layer, int(index), ws_index=15)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

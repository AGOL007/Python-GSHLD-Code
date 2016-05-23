# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsSocialMediaFlickr
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestSocialMediaFlickr(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 14))
    @unpack
    def test_social_media_flickr(self, index, result, social_media_flickr, flickr_distance_textbox_text, flickr_keyword_textbox_text, flickr_refreshtime_textbox_text, flickr_unit, flickr_layer):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, social_media_flickr, int(index), ws_index=14, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsSocialMediaFlickr.click_widget_icon(self.driver, social_media_flickr, int(index), ws_index=14)

        # click social media item flickr
        SeleniumActionsSocialMediaFlickr.click_social_media_item_flickr(self.driver, social_media_flickr, int(flickr_distance_textbox_text), flickr_keyword_textbox_text, int(flickr_refreshtime_textbox_text), flickr_unit, int(index), ws_index=14)

        # validate social media item flickr
        SeleniumActionsSocialMediaFlickr.validate_social_media_flickr(self.driver, social_media_flickr, flickr_layer, int(index), ws_index=14)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

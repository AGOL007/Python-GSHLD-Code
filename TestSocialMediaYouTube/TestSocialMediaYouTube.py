# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsSocialMediaYouTube
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestSocialMediaYouTube(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 13))
    @unpack
    def test_social_media_you_tube(self, index, result, social_media_youtube, youtube_distance_textbox_text, youtube_keyword_textbox_text, youtube_refreshtime_textbox_text, youtube_units, youtube_layer_name):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver, social_media_youtube, int(index), ws_index=13, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsSocialMediaYouTube.click_widget_icon(self.driver, social_media_youtube, int(index), ws_index=13)

        # click social media item you tube
        SeleniumActionsSocialMediaYouTube.click_social_media_item_you_tube(self.driver, social_media_youtube, int(youtube_distance_textbox_text), youtube_keyword_textbox_text, int(youtube_refreshtime_textbox_text), youtube_units, int(index), ws_index=13)

        # validate social media you tube
        SeleniumActionsSocialMediaYouTube.validate_social_media_youtube(self.driver, social_media_youtube, youtube_layer_name, int(index), ws_index=13)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

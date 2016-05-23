# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest

import xlrd
from ddt import ddt, data, unpack

import SeleniumActionsSocialMediaTwitter
from GeoshieldCommonFiles import AppCommanUtility
from TestBase.GeoshieldTestBase import set_browser

@ddt
class TestSocialMediaTwitter(unittest.TestCase):

    @data(*AppCommanUtility.getData(r"C:\Users\sagarkul\Desktop\DataSource.xlsx", 12))
    @unpack
    def test_social_media_twitter(self, index, result, social_media_twitter, twitter_keyword_textbox_text, twitter_distance_textbox_text, twitter_refreshtime_textbox_text, twitter_layer):

        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        # click left panel
        AppCommanUtility.click_left_panel_open(self.driver,social_media_twitter, int(index), ws_index=12, method_name="click_left_panel_open")

        # click widget icon
        SeleniumActionsSocialMediaTwitter.click_widget_icon(self.driver, social_media_twitter, int(index), ws_index=12)

        # click social media twitter
        SeleniumActionsSocialMediaTwitter.click_social_media_item_twitter(self.driver, social_media_twitter, twitter_keyword_textbox_text, int(twitter_distance_textbox_text), int(twitter_refreshtime_textbox_text), int(index), ws_index=12)

        # validate social media twitter
        SeleniumActionsSocialMediaTwitter.validate_social_media_twitter(self.driver, social_media_twitter, twitter_layer, int(index), ws_index=12)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    def tearDown(self):
        """ Quit browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

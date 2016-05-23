# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import GeoShieldSeleniumAction
import unittest
from TestBase import set_browser
from ddt import ddt, data, unpack
import xlrd

def getData(fileName):
    myrows = []
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(0)
    for row_index in range(1, sheet.nrows):
        myrows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
    return myrows

@ddt
class MyTestCase(unittest.TestCase):

    @data(*getData(r"C:\Users\sagarkul\Desktop\LiveFeed.xlsx"))
    @unpack
    def test_browse_tab(self, social_media_twitter, twitter_keyword_textbox_text, twitter_distance_textbox_text, twitter_refreshtime_textbox_text, social_media_youtube, youtube_distance_textbox_text, youtube_keyword_textbox_text, youtube_refreshtime_textbox_text, social_media_flickr, flickr_distance_textbox_text, flickr_keyword_textbox_text, flickr_refreshtime_textbox_text, social_media_social_media_search, social_media_search_distance_textbox_text, social_media_search_keyword_textbox_text, social_media_search_refreshtime_textbox_text, agency_feed_current_calls_services, agency_feed_avl, agency_feed_avl_unitid_textbox, agency_feed_avl_date_textbox, agency_feed_avl_distance_textbox, agency_feed_lpr, agency_feed_lpr_textbox, agency_feed_lpr_distance_textbox):
        """ Test Method """
        # categoryname, categorymainlayername, categorysublayername
        # Launch the browser

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        #  Click Left Panel
        GeoShieldSeleniumAction.click_left_panel_open(self.driver)

        # Click Select Date Value
#        GeoShieldSeleniumAction.click_select_date_value(self.driver)

        # Click predefined date range
#        GeoShieldSeleniumAction.click_predefined_daterange_tab(self.driver)

        # Click RMS of browse tab
#        GeoShieldSeleniumAction.click_events_rms_browse_tab(self.driver, categorymainlayername, categorysublayername)

        # Click right panel
#        GeoShieldSeleniumAction.click_down_panel(self.driver)

        # Validate the layer name

#        AppValidation.validate_layer_name(self.driver, categoryname, categorymainlayername, categorysublayername)

#        AppValidation.validate_feature_count(self.driver, categorysublayername)

        # Click Social media item twitter
        GeoShieldSeleniumAction.click_social_media_item_twitter(self.driver, social_media_twitter, str(twitter_keyword_textbox_text), int(twitter_distance_textbox_text), int(twitter_refreshtime_textbox_text))

        # Click Social media item Youtube
        GeoShieldSeleniumAction.click_social_media_item_youtube(self.driver, social_media_youtube, int(youtube_distance_textbox_text), youtube_keyword_textbox_text, int(youtube_refreshtime_textbox_text))

        # Click Social media item Flickr
        GeoShieldSeleniumAction.click_social_media_item_flickr(self.driver, social_media_flickr, int(flickr_distance_textbox_text), flickr_keyword_textbox_text, int(flickr_refreshtime_textbox_text))

        # Click social media item social media search
        GeoShieldSeleniumAction.click_social_media_item_social_media_search(self.driver, social_media_social_media_search, int(social_media_search_distance_textbox_text), social_media_search_keyword_textbox_text, int(social_media_search_refreshtime_textbox_text))

        # Click agency feed item Live cads
        GeoShieldSeleniumAction.click_agency_feed_item_live_cads(self.driver, agency_feed_current_calls_services)

        # Click agency feed item AVL
        GeoShieldSeleniumAction.click_agency_feed_item_avl(self.driver, agency_feed_avl, int(agency_feed_avl_unitid_textbox), int(agency_feed_avl_distance_textbox))

        # Click agency feed item LPR
        GeoShieldSeleniumAction.click_agency_feed_item_LPR(self.driver, agency_feed_lpr, agency_feed_lpr_textbox, int(agency_feed_lpr_distance_textbox))

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    #def tearDown(self):
    #    """ Quit browser"""
    #    self.driver.close()

if __name__ == '__main__':
    unittest.main()

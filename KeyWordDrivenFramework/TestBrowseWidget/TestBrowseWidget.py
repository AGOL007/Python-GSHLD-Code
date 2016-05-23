# -*- coding: utf-8 -*-
""" Unit test file """
from robot.parsing import datarow

__author__ = 'SagarKul'

import unittest
from TestBase import set_browser
import SeleniumActions
import time


class TestAgencyFeedLPR(unittest.TestCase):

    def test_agency_feed_current_call_for_service(self):

        """ Test Method """
        self.driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1")

#        data_row_index = SeleniumActions.get_data_from_spread_sheet()

#        web_elemnt = SeleniumActions.locator_value(self.driver, data_row_index[13], data_row_index[14])
#        SeleniumActions.enter_text(self.driver, web_elemnt, data_row_index[15])

#        web_elemnt = SeleniumActions.locator_value(self.driver, data_row_index[17], data_row_index[18])
#        SeleniumActions.click_button(self.driver, web_elemnt)

#        time.sleep(2)
#        web_elemnt = SeleniumActions.locator_value(self.driver, data_row_index[17], data_row_index[18])
#        SeleniumActions.enter_text(self.driver, web_elemnt, data_row_index[19])

        SeleniumActions.step_execution(self.driver)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

#    def tearDown(self):
#        """ Quit browser"""
#        self.driver.close()

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import unittest
import xlrd
from ddt import ddt, data, unpack
from TestBase.GeoshieldTestBase import set_browser
import SeleniumActions


def getData(fileName, sheet_index):
    myrows = []
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(sheet_index)
    for row_index in range(1, sheet.nrows):
        myrows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
    return myrows


@ddt
class TestToolSearchAttribute(unittest.TestCase):
    @data(*getData(r"C:\Users\sagarkul\Desktop\KeywordDriven.xlsx", 0))
    @unpack
    def test_browse_widget(self, browse_tab_container_name, category_main_layer_name, category_sub_layer_name):
        """ Test Method """

        self.driver.get("http://geoshieldles.usgovcloudapp.net:8080/geoshieldmissionmodule/")

        SeleniumActions.step_execution(self.driver, browse_tab_container_name, category_main_layer_name, category_sub_layer_name)

        SeleniumActions.validation_step_execution(self.driver)

    def setUp(self):
        """ Intiate and maximize the browser """
        self.driver = set_browser()
        self.driver.maximize_window()

    #def tearDown(self):
    #    """ Quit browser"""
    #    self.driver.close()


if __name__ == '__main__':
    unittest.main()

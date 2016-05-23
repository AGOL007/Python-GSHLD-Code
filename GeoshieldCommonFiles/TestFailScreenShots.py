# -*- coding: utf-8 -*-
""" Unit test file """
__author__ = 'SagarKul'

import time
import os


def get_screenshots(driver, tool_name, method_name):

    show_time = time.strftime("%Y_%m_%d %I_%M_%S", time.localtime())
    file_name = r"C:\Users\sagarkul\Desktop\Snapshots"
    file_extention = 'png'

    driver.get_screenshot_as_file(os.path.join(file_name, ''.join([tool_name, method_name, show_time, ".png"])))

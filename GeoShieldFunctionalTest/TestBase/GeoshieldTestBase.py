# -*- coding: utf-8 -*-
""" File contains configuration and browser intiation methods"""
__author__ = 'SagarKul'


from selenium import webdriver
import xml.etree.ElementTree as ET


def set_browser():
    """ this function initiate the provided browser"""

    #   Read values from config file
    tree = ET.parse(r'C:\Users\sagarkul\Desktop\app.xml')
    root = tree.getroot()
    app_config = []

    for browserval in root.iter('add'):
        app_config.append(browserval.attrib)
        for item in app_config:
            if item['key'] == 'Browser':
                browser_name = item['value']
            if item['key'] == 'Path':
                path = item['value']
            if item['key'] == 'AppUrl':
                app_Url = item['value']
                return app_Url

    #   Set the browser

    if browser_name.lower() == "firefox":
        return webdriver.Firefox()
    elif browser_name.lower() == "chrome":
        return webdriver.Chrome(path + "chromedriver.exe")
    elif browser_name.lower() == "ie":
        return webdriver.Ie(path + "IEDriverServer.exe")
    else:
        print "Please pass firefox or chrome to start browser"
        return None


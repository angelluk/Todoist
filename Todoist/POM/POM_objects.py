#-*- coding: utf-8 -*-
# python 2
from unicodedata import *

import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config import *




class Login(unittest.TestCase):
    # data
    #URL = None

    # common locators
    #sidebar = '.cx-sidebar'


    def __init__(self, curdriver):
        self.driver = curdriver


    def login_via_email(self):

       pass
__author__ = 'olukianenko'

from appium import webdriver
from Config import *


class DriverManager:

    def __init__(self):
        self.driver = None



    def get_driver_for_browserstack(self,userName = USER_NAME, accessKey = ACCESS_KEY, build = BUILD, device = DEVICE, app = APP_TODOIST ):

        desired_caps = {
            "build": build,
            "device": device,
            'browserstack.debug': True,
            "app": app
        }

        driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub",
                                  desired_caps)
        self.driver = driver

        return driver


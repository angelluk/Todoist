import unittest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import POM_objects
import Appium_driver
from Config import *



class Tests(unittest.TestCase):

    '''
        simple end to end  Wiki test
    '''

    @unittest.skip("skipping test")
    def test_wiki(self):

        logging.warning('Starting -  test_wiki()')

        try:
            ap_drv = Appium_driver.DriverManager()

            driver = ap_drv.get_driver_for_browserstack(app=APP_WIKI)

            search_element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
            )
            search_element.click()

            search_input = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
            )
            search_input.send_keys("BrowserStack")
            time.sleep(5)

            search_results = driver.find_elements_by_class_name("android.widget.TextView")
            assert (len(search_results) > 0)

        except Exception as e:
            logging.error(e)
        finally:
            driver.quit()
            logging.warning('Finished -  test_wiki()')




    def test_Todoist_login(self):

        logging.warning('Starting -  test_Todoist_login()')

        try:
            ap_drv = Appium_driver.DriverManager()

            driver = ap_drv.get_driver_for_browserstack(app=APP_TODOIST)

            email_in = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ID, "com.todoist:id/btn_welcome_continue_with_email"))
            )
            email_in.click()


            email = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ID, "com.todoist:id/email_exists_input")))
            email.clear()
            email.send_keys("alexeilukyanenko@gmail.com")


            email_in = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ID, "com.todoist:id/btn_continue_with_email")))
            email_in.click()

            password = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ID, "com.todoist:id/log_in_password")))
            password.clear()
            password.send_keys("Lukasus26041")

            log_in = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ID, "com.todoist:id/btn_log_in")))
            log_in.click()


            menu = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Change the current view")))

            assert (menu is not None)


        except Exception as e:
            logging.error(e)
        finally:
            driver.quit()
            logging.warning('Finished -  test_Todoist_login()')


if __name__ == '__main__':
    unittest.main()
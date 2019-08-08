#!/usr/bin/python
# -------------------------------------------------------------------
# Copyright 2019 Jose Angel Gariburo
##
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
##
# http://www.apache.org/licenses/LICENSE-2.0
##
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##
# File : sysdig_python_webui_tests.py
##
# Sample:
# - Test page load: basic test
# python ./sysdig_python_selenium_webui_tests.py --page_url http://app.sysdigcloud.com/
##
# - Test page load: if it takes more than 5 seconds, fail the test. Default timeout is 10 seconds
# python ./sysdig_python_selenium_webui_tests.py --page_url http://app.sysdigcloud.com/ --max_load_seconds 5
##
# - Test page load: after page loading, save screenshot
# python ./sysdig_python_selenium_webui_tests.py --page_url http://app.sysdigcloud.com/ --should_save_screenshot true
##
# -------------------------------------------------------------------
import sys
import argparse
import unittest

from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class SysDigWebUITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page_url_ = 'http://app.sysdigcloud.com/'
        cls.max_load_seconds_ = 10.0
        opts = Options()
        opts.headless = True
        assert opts.headless
        cls.driver = webdriver.Firefox(options=opts)

    def test_aaaloadpage(self):
        self.driver.delete_all_cookies()
        start_clock = time.perf_counter()
        self.driver.get(self.page_url_)
        end_clock = time.perf_counter()
        elapsed_seconds = (end_clock - start_clock)
        self.assertLessEqual(elapsed_seconds, self.max_load_seconds_)

    def test_title(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        self.assertEqual(self.driver.title, 'Login - Sysdig')

    def test_loginbutton(self):
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        self.assertEqual(self.driver.find_element_by_class_name('ember-view simple-btn simple-btn--login').text, 'Log in')

    def test_forgotpass(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        self.assertEqual(self.driver.find_element_by_class_name('login__link').text, 'Forgot your password?')
    
    def test_googlebutton(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        self.assertTrue(self.driver.find_element_by_class_name('block-login__third-party-button'))

    def test_thirdpartybutton(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        self.assertTrue(self.driver.find_element_by_class_name('ember-view block-login__third-party-button'))

    def test_logopos(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        logo = self.driver.find_element_by_class_name('login__logo')
        self.assertEqual(logo.size.width, 520.0)
        self.assertEqual(logo.size.height, 49.0)

    def test_loginpos(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        login = self.driver.find_element_by_class_name('ember-view simple-btn simple-btn--login')
        self.assertEqual(login.size.width, 520.0)
        self.assertEqual(login.size.height, 40.0)
    
    def test_failogin(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        login = self.driver.find_elements_by_class_name('ember-view simple-btn simple-btn--login')
        login.click()
        alert = self.driver.switch_to.alert
        alert = 0
    
    def test_notacustomer(self):        
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, 5)
        titlewait = wait.until(ec.title_is('Login - Sysdig'))
        notcustomer = self.driver.find_element_by_partial_link_text('Not a customer? Try for free')
        notcustomer.click()        

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

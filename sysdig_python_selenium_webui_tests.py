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
# -------------------------------------------------------------------
import unittest

import time
from selenium import webdriver
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

    def test_loadpage(self):
        # Test page loads in less than max_load_seconds_ (10.0 seconds) defined while setting up the class
        self.driver.delete_all_cookies()
        start_clock = time.perf_counter()
        self.driver.get(self.page_url_)
        end_clock = time.perf_counter()
        elapsed_seconds = (end_clock - start_clock)
        self.assertLessEqual(elapsed_seconds, self.max_load_seconds_)

    def test_title(self):
        # Test page title is the one expected
        self.driver.get(self.page_url_)
        WebDriverWait(self.driver, self.max_load_seconds_)
        self.assertEqual(self.driver.title, 'Login - Sysdig')

    def test_loginbutton(self):
        # Test text in Log in button is the one expected
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view simple-btn simple-btn--login')))
        self.assertEqual(wait.text, 'Log in')

    def test_forgotpass(self):
        # Test text in Forgot your password button is the one expected
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'login__link')))
        self.assertEqual(wait.text, 'Forgot your password?')
        self.assertEqual(wait.location['x'], 618.0)
        self.assertEqual(wait.location['y'], 373.0)

    def test_googlebutton(self):
        # Test Google button is in place
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'block-login__third-party-button')))
        self.assertEqual(wait.text, 'Google')
        self.assertEqual(wait.location['x'], 503.0)
        self.assertEqual(wait.location['y'], 481.0)

    def test_thirdpartybutton(self):
        # Test third party buttons are in place
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view block-login__third-party-button')))
        self.assertEqual(wait.size.width, 114.67)
        self.assertEqual(wait.size.height, 50.0)

    def test_logopos(self):
        # Test logo image has expected width and height
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.visibility_of((By.XPATH, '//*[@class="ember-view block-authentication-form"]/div/div/img')))
        self.assertEqual(wait.size.width, 520.0)
        self.assertEqual(wait.size.height, 49.0)

    def test_loginpos(self):
        # Test login button has expected width and height
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view simple-btn simple-btn--login')))
        self.assertEqual(wait.size.width, 520.0)
        self.assertEqual(wait.size.height, 40.0)

    def test_failogin(self):
        # Test that when clicking log in button with empty username and password we see an alert on screen
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view simple-btn simple-btn--login')))
        wait.click()
        alert = self.driver.switch_to.alert
        self.assertNotEqual(alert, 0)

    def test_notacustomer(self):
        # Test that when clicking on not a customer button we are sent to Sign Up page
        self.driver.get(self.page_url_)
        wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'login__link')))
        wait.click()
        wait = WebDriverWait(self.driver, self.max_load_seconds_)
        self.assertEqual(self.driver.title, 'Sign Up | Sysdig')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

# Python & Selenium Web UI Testing

This project is an initial approach on how to test a web UI using python and selenium library for testing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.x
Selenium for python 3.x
```

### Installing

1. Install python

[Python](https://www.python.org/downloads/)

2. Install selenium for python

[Selenium for python](https://docs.python.org/3/installing/index.html)

## Running the tests

There are two options to run the tests:
1. If you have docker: **_sh selenium_gui_test.sh_**
2. If you don't have docker: **_python sysdig_python_selenium_webui_tests.py_**


The output should be something in the same format as this:

```
E...EEEFE.
======================================================================
ERROR: test_failogin (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 102, in test_failogin
    wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view simple-btn simple-btn--login')))
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\wait.py", line 80, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:


======================================================================
ERROR: test_loginbutton (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 59, in test_loginbutton
    wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view simple-btn simple-btn--login')))
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\wait.py", line 80, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:


======================================================================
ERROR: test_loginpos (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 95, in test_loginpos
    wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view simple-btn simple-btn--login')))
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\wait.py", line 80, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:


======================================================================
ERROR: test_logopos (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 88, in test_logopos
    wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.visibility_of((By.XPATH, '//*[@class="ember-view block-authentication-form"]/div/div/img')))
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\wait.py", line 71, in until
    value = method(self._driver)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\expected_conditions.py", line 144, in __call__
    return _element_if_visible(self.element)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\expected_conditions.py", line 148, in _element_if_visible
    return element if element.is_displayed() == visibility else False
AttributeError: 'tuple' object has no attribute 'is_displayed'

======================================================================
ERROR: test_thirdpartybutton (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 81, in test_thirdpartybutton
    wait = WebDriverWait(self.driver, self.max_load_seconds_).until(ec.element_to_be_clickable((By.CLASS_NAME, 'ember-view block-login__third-party-button')))
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\support\wait.py", line 80, in until
    raise TimeoutException(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message:


======================================================================
FAIL: test_notacustomer (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 113, in test_notacustomer
    self.assertEqual(self.driver.title, 'Sign Up | Sysdig')
AssertionError: 'Login - Sysdig' != 'Sign Up | Sysdig'
- Login - Sysdig
+ Sign Up | Sysdig


----------------------------------------------------------------------
Ran 10 tests in 109.757s

FAILED (failures=1, errors=5)
```

## TO-DO

1. Not able to get web ui elements to properly test them. Tried waiting for some conditions but it doesn't work for some elements. Most of the elements ids are dynamically generated.
2. Test when loading web page and clicking on button not working when checking the page title, not yet loaded when asserting the title name.
3. Add more web ui testing about position, sizes and other graphical elements.
4. Add classes for testing other browsers, not only Firefox.

## Author

* **Jose Angel Gariburo Cortes** - *Initial work* - [Carmot](https://github.com/Carmot)

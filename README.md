# Python $ Selenium Web UI Testing

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
FE..EEE.E.
======================================================================
ERROR: test_failogin (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 113, in test_failogin
    login.click()
AttributeError: 'list' object has no attribute 'click'

======================================================================
ERROR: test_loginbutton (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 72, in test_loginbutton
    self.assertEqual(self.driver.find_element_by_class_name('ember-view simple-btn simple-btn--login').text, 'Log in')
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 564, in find_element_by_class_name
    return self.find_element(by=By.CLASS_NAME, value=name)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: .ember-view simple-btn simple-btn--login


======================================================================
ERROR: test_loginpos (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 104, in test_loginpos
    login = self.driver.find_element_by_class_name('ember-view simple-btn simple-btn--login')
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 564, in find_element_by_class_name
    return self.find_element(by=By.CLASS_NAME, value=name)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: .ember-view simple-btn simple-btn--login


======================================================================
ERROR: test_logopos (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 97, in test_logopos
    self.assertEqual(logo.size.width, 520.0)
AttributeError: 'dict' object has no attribute 'width'

======================================================================
ERROR: test_thirdpartybutton (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 90, in test_thirdpartybutton
    self.assertTrue(self.driver.find_element_by_class_name('ember-view block-login__third-party-button'))
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 564, in find_element_by_class_name
    return self.find_element(by=By.CLASS_NAME, value=name)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 978, in find_element
    'value': value})['value']
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "C:\Users\jose.gariburo\AppData\Roaming\Python\Python37\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: .ember-view block-login__third-party-button


======================================================================
FAIL: test_aaaloadpage (__main__.SysDigWebUITest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "sysdig_python_selenium_webui_tests.py", line 60, in test_aaaloadpage
    self.assertLessEqual(elapsed_seconds, self.max_load_seconds_)
AssertionError: 11.864984399999999 not less than or equal to 10.0

----------------------------------------------------------------------
Ran 10 tests in 82.359s

FAILED (failures=1, errors=5)
```

## Author

* **Jose Angel Gariburo Cortes** - *Initial work* - [Carmot](https://github.com/Carmot)

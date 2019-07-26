import calendar
import datetime
import logging
import random
import string
import time
from random import randint
from functools import wraps

from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class Base(object):
    """
    Page class that all page models can inherit from.
    Please, try to save its structure&style and not to change its code without code review/discussion
    with other project users.

    """

    def __init__(self, driver, explicit_wait=10):
        """
        Inits Selenium Driver class with driver
        :param driver: webdriver instance
        :param int explicit_wait: Time you want use as wait time
        :return A SeleniumDriver object

        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def driver(self):
        return self.driver

    def get_driver(self):
        """
        Get the webdriver instance
        :return: webdriver instance

        """
        driver = self.driver
        return driver

    def refresh(self):
        """
        Refresh current pages on the web application

        """
        self.driver.refresh()
        logging.info("The current browser location was refreshed")

    def get_browser_title(self):
        """
        Get title of current pages on the web application
        :return: Title of the current pages

        """
        title = self.driver.title
        logging.info("Title of the current pages is :: " + title)
        return title

    def get_browser_url(self):
        """
        Get URL of current pages on the web application
        :return: Current pages URL

        """
        browser_url = self.driver.current_url
        logging.info("Current browser url is :: " + browser_url)
        return browser_url

    def navigate_browser_back(self):
        """
        Go one pages back

        """
        self.driver.back()

    def navigate_browser_forward(self):
        """
        Go one pages forward

        """
        self.driver.forward()

    def quit_driver(self):
        """
        Quit driver

        """
        if self.driver is not None:
            self.driver.quit()

    def select_checkbox(self, element, info, time_to_wait=0):
        """
        Select Checkbox
        :param WebElement element: Element to check
        :param str info: Information about the element, usually text on the element
        :param int time_to_wait: Time you want to wait after checking the element

        """
        if not element.is_selected():
            element.click()
            logging.info("Element :: '" + info + "' is checked")
            logging.info("Waiting after checking the element for "
                         + str(time_to_wait) + " seconds")
            time.sleep(time_to_wait)
        else:
            logging.info("Element :: '" + info + "' was already checked")

    def unselect_checkbox(self, element, info, time_to_wait=0):
        """
        Deselect Checkbox
        :param WebElement element: Element to uncheck
        :param str info: Information about the element, usually text on the element
        :param int time_to_wait: Time you want to wait after un-checking the element

        """
        if element.is_selected():
            element.click()
            logging.info("Element :: '" + info + "' is unchecked")
            logging.info("Waiting after un-checking the element for "
                         + str(time_to_wait) + " seconds")
            time.sleep(time_to_wait)
        else:
            logging.info("Element :: '" + info + "' was already unchecked")

    def get_element(self, locator):
        """
        Get element for a provided locator
        :param locator: locator of the element to find
        :return: Element Object
        :rtype: WrapWebElement

        """
        try:
            element = self.driver.find_element(*locator)
        except NoSuchElementException:
            raise Exception("There is no such element or its" + str(locator) + " has changed ")
        return WrapWebElement(self.driver, element, locator)

    def get_element_list(self, locator):
        """
        Get elements list for a provided locator
        :param locator: locator of the element list to find
        :return: Element List
        :rtype: list

        """
        time.sleep(3)
        try:
            elements = self.driver.find_elements(*locator)
        except NoSuchElementException:
            raise Exception("There is no such element or its" + str(locator) + " has changed ")
        return list(map(lambda el: WrapWebElement(self.driver, el, locator=locator), elements))

    def wait_for_element(self, locator, wait_type=ec.presence_of_element_located, timeout=10):
        """
        Wait for element to present
        :param wait_type: which condition of the element you are waiting for
        :param locator: locator of the element to find
        :param int timeout: Maximum time you want to wait for the element
        :rtype: WrapWebElement

        """
        start_time = int(round(time.time() * 1000))
        element = None
        try:
            logging.info("Waiting for maximum :: " + str(timeout) +
                         " :: seconds for element to be visible and clickable")
            wait = WebDriverWait(self.driver, timeout,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(wait_type(locator))
            end_time = int(round(time.time() * 1000))
            duration = (end_time - start_time) / 1000.00
            logging.info("Element '"
                         "' appeared on the web pages after :: " + "{0:.2f}".format(duration) + " :: seconds")
        except ElementNotVisibleException:
            logging.error("Element '"
                          "' not appeared on the web pages after :: " + str(timeout) + " :: seconds")
        if isinstance(element, WebElement):
            return WrapWebElement(self.driver, element, locator)
        else:
            return element

    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Wait for element to be clickable
        :param locator: locator of the element to find
        :param int timeout: Maximum time you want to wait for the element
        :rtype: WrapWebElement

        """
        return self.wait_for_element(locator, ec.element_to_be_clickable, timeout)

    def wait_for_element_visible(self, locator, timeout=10):
        """
        Wait for element to be visible
        :param locator: locator of the element to find
        :param int timeout: Maximum time you want to wait for the element
        :rtype: WrapWebElement

        """
        return self.wait_for_element(locator, ec.visibility_of_element_located, timeout)

    def create_random_string(self, size=1, chars=string.ascii_uppercase + string.digits):
        """
        Create random string to use it in name generator
        :param int size: Size of desired random string
        :param string chars: Character set to select randomly from
        :return: Random string
        :rtype: string

        """
        return ''.join(random.choice(chars) for _ in range(size))

    def create_random_integer(self, start=0, finish=10):
        """
        Create random integer to use it in name generator
        :param int start: Starting point for interval
        :param int finish: Endpoint for interval
        :return: Random integer between given interval
        :rtype: int

        """
        return randint(start, finish)

    def generate_campaign_name(self):
        """
        Generator of campaign names which are used in all features of this project
        :return: Campaign name according to current date
        :rtype: string

        """
        i = datetime.datetime.now()
        per_name = "%s%s%s%s%s%s%s%s%s" % ("Sel", i.day, i.month, i.year, i.hour, i.minute, i.second,
                                           "-", self.create_random_string(3))
        return str(per_name.upper())

    def erase_text(self, locator, click=None, clear=None, backspace=None):
        """
        Various ways to erase text from web element.
        :param tuple locator: locator tuple or WebElement instance
        :param bool click: clicks the input field
        :param bool clear: clears the input field
        :param int backspace: how many times to hit backspace
        """
        element = locator
        if not isinstance(element, WebElement):
            element = self.get_element(locator)

        if click:
            element.click()

        if clear:
            element.clear()

        if backspace:
            actions = ActionChains(self.driver)
            for _ in range(backspace):
                actions.send_keys(Keys.BACKSPACE)
            actions.perform()

    class SwitchFrame:
        def __init__(self, driver, element):
            self.driver = driver
            self.element = element

        def __enter__(self):
            self.driver.switch_to.frame(self.element)

        def __exit__(self, type, value, traceback):
            self.driver.switch_to.parent_frame()

    def switch_frame(self, locator):
        """
        Switch to iframe togater 'with' keyword.
        Switches back automatically when operations finished 'with' block.
        :param tuple locator:
        :rtype: SwitchFrame

        """
        return self.SwitchFrame(self.driver, self.wait_for_element(locator))

    def switch_window(self, window_name):
        """
        Switch to  window or tabs
        :param window_name: tab or window name.
        """
        self.driver.switch_to.window(window_name)

    def add_months(self, current_date, months):
        """
        Adds months to current date to get future datetime
        :param current_date: Current date
        :param months: Count of months you want to add to get future datetime
        :return: Future datetime

        """
        month = current_date.month - 1 + months
        year = int(current_date.year + month / 12)
        month = month % 12 + 1
        day = min(current_date.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    def scroll_up(self, locator, time_out=5):
        """
        Scrolls page up to the element
        :param time_out:
        :param locator:
        :return:
        """
        try:
            element = self.get_element(locator)
            element.send_keys(Keys.PAGE_UP)
            self.wait_for_element(locator, time_out)
        except Exception:
            raise Exception("An exception occurred when scrolling up")
        return self


class WrapWebElement(WebElement):
    """
    This class defines the generic interceptor for the methods of wrapped web element references.It also provides
    implementations for methods that acquire web element references

    """
    element = None
    driver = None
    locator = None

    def __init__(self, driver, element, locator=None):
        super().__init__(element.parent, element._id)
        self.element = element
        self.driver = driver
        self.locator = locator

    def find_element(self, *locator):
        """
        Find an element given a By strategy and locator.
        :param locator: locator of the element to find
        :rtype: WrapWebElement

                """
        if isinstance(locator[0], tuple):
            element = self.element.find_element(*locator[0])
            used_locator = locator[0]
        else:
            element = self.element.find_element(*locator)
            used_locator = locator
        return WrapWebElement(self.driver, element, locator=used_locator)

    def find_elements(self, *locator):
        """
        Find elements given locator.
        :param locator: locator of the elements to find
        :rtype: list of elements
        """
        if isinstance(locator[0], tuple):
            elements = self.element.find_elements(*locator[0])
            used_locator = locator[0]
        else:
            elements = self.element.find_elements(*locator)
            used_locator = locator
        return list(map(lambda el: WrapWebElement(self.driver, el, locator=used_locator), elements))

    def wait_visible(self, timeout=10):
        """
        Wait for element to be visible
        :param int timeout: Desired wait time before visibility of element
        :return: Desired visible element
        :rtype: WebElement

        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda _: self.element.is_displayed(), "{} element not visible".format(str(self.locator)))
        return self

    def wait_enable(self, timeout=10):
        """
        Wait for element to be enable
        :param int timeout: Desired wait time before visibility of element
        :return: Desired visible element
        :rtype: WebElement

        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda _: self.element.is_enabled(), "{} element not enable".format(str(self.locator)))
        return self

    def wait_clickable(self, timeout=10):
        """
        Wait for element to be clickable
        :param int timeout: Desired wait time before visibility of element
        :return: Desired visible element
        :rtype: WebElement

        """
        self.wait_visible(timeout=timeout)
        self.wait_enable(timeout=timeout)
        return self

    def double_click(self):
        """
        Double-clicks an element.
        :return: self

        """
        actions = ActionChains(self.driver)
        actions.double_click(self.element).perform()
        return self

    def right_click(self):
        """
        Right clicks an element.
        :return: self

        """
        actions = ActionChains(self.driver)
        actions.context_click(self.element).perform()
        return self

    def focus(self):
        """
        Focus on an an element.
        :return: self

        """
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element).perform()
        self.click()
        return self

    def scroll(self, center=False):
        """
        Scrolls to an element
        :return: self

        """
        if center:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", self.element)
        return self

    def __getattribute__(self, attribute):
        """
        Return getattr(self, name).
        :param attribute: Attribute of the element
        :return: value of attribute

        """
        if attribute not in list(WrapWebElement.__dict__):
            returning_value = object.__getattribute__(self.element, attribute)
        else:
            returning_value = object.__getattribute__(self, attribute)

        @wraps(WebElement)
        def wrapper(*args, **kwargs):
            value = returning_value(*args, **kwargs)
            if (isinstance(value, WebElement) or attribute in (
                    "click", "submit", "clear")) and attribute != 'find_element':
                return self
            else:
                return value

        if callable(returning_value):
            return wrapper
        else:
            return returning_value


    def get_only_product_name(self, product_text):
        """
        Returns stripped product title
        :param product_text: Whole product text
        :return: Title of the product

        """
        return product_text.split('\n')[0]

    def search_title(self, title, word):
        """
        Returns if the word is contained in search title
        :param title: Search title
        :param word: Word to be searched
        :return: Place of word in the title

        """

        return title.find('word')
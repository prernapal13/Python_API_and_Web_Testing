import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Services:
    """
    This class is to maintain the services provided by selenium webdriver
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=20):
        """
        This method is to wait for presence of given element for given time(default timeout = 20 secs.)
        If element does not present in given max time, this will throw timeout exception.
        :param locator: XPATH of given element as string 
        :param timeout: maximum wait timeout as number
        """
        WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, locator)))

    def send_keys(self, locator, txt):
        """
        This method is to type in a given element
        :param locator: XPATH of given element as string
        :param txt: text to be types in the element
        """
        self.wait_for_element(locator)
        self.driver.find_element_by_xpath(locator).send_keys(txt)

    def click(self, locator):
        """
        This method is to click on the web element.
        :param locator: XPATH of given element as string
        """
        self.wait_for_element(locator)
        ele = self.driver.find_element_by_xpath(locator)
        ele.click()

    def get_text_by_xpath(self, locator):
        """
        This method is get the text present within given web element.
        :param locator: XPATH of given element as string 
        :return: text in the web element as string
        """
        self.wait_for_element(locator)
        return self.driver.find_element_by_xpath(locator).text
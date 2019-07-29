import logging

from selenium.webdriver.common.keys import Keys

from utilities.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class HomePage(Services):
    """
    This class is to write functions related to Google home page
    """

    def __init__(self, driver):
        Services.__init__(self, driver)
        self.driver = driver
        self.xpath_search_box = "//input[@name='q']"
        self.xpath_search_btn = "//input[@name='btnK'][2]"

    def get_title(self):
        """
        This method is to get the title of Google home page
        :return: Google home page title as string
        """
        title = self.driver.title
        logging.info("# Title: " + title)
        return title

    def search_action(self, txt):
        """
        This method is to perform a search with given search parameter
        :param txt: search parameter
        """
        logging.info("# Entering search text: " + txt)
        self.send_keys(self.xpath_search_box, txt)
        logging.info("# Clicking Enter")
        self.send_keys(self.xpath_search_box, Keys.ENTER)
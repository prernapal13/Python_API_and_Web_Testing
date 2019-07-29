import logging

from utilities.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class SearchResultPage(Services):
    """
    This class is to write functions related to Google search result page
    """
    def __init__(self, driver):
        Services.__init__(self, driver)
        self.driver = driver
        self.xpath_search_lnks = "//div[@class='r']//a//h3"
        self.xpath_no_result_found = "//p[@role='heading']"
        self.xpath_suggested_text = "//span[text()='Did you mean:']/following-sibling::a//i"

    def get_all_searched_links(self):
        """
        This method is to get the text of all the links returned after performing a search in Google engine
        :return: list of text from all search results
        """
        searched_result_elements = self.driver.find_elements_by_xpath(self.xpath_search_lnks)
        searched_result_links = []
        for ele in searched_result_elements:
            if len(ele.text.strip()) != 0:
                searched_result_links.append(ele.text)
        logging.info("# Searched result links: " + str(searched_result_links))
        return searched_result_links

    def get_suggested_text(self):
        """
        This method is to get the text suggested by Google in case of spelling mistake etc.
        :return: text suggested by Google as string
        """
        suggested_text = self.get_text_by_xpath(self.xpath_suggested_text)
        return suggested_text

    def get_no_result_found_txt(self):
        """
        This method is to get the text from No result found page
        :return: No result found text as string
        """
        result = self.get_text_by_xpath(self.xpath_no_result_found)
        logging.info("# No result found page text: " + result)
        return result

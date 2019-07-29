import logging

from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage
from utilities.drivermanager import DriverManager

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class GoogleSearchTests(DriverManager):
    """
    This class is to write test cases related to Google Search functionality
    """

    def test_google_home_page(self):
        """
        This method is to test the title of Google home page
        """
        home_page = HomePage(self.driver)
        actual_title = home_page.get_title()
        assert actual_title == "Google", "Actual title '{0}' should be same as expected 'Google'".format(actual_title)

    def test_google_search(self):
        """
        This method is to test valid google search. It verifies that all the links returned as searched result contain 
        the searched keyword in it
        """
        search_str = "automation"
        home_page = HomePage(self.driver)
        home_page.search_action(search_str)

        search_result_page = SearchResultPage(self.driver)
        search_result_lst = search_result_page.get_all_searched_links()
        for link in search_result_lst:
            assert search_str.lower() in link.lower(), "search string {0} is not present in link {1}".format(search_str,
                                                                                                             link)

    def test_google_search_did_you_mean(self):
        """
        This method is to test 'did you mean' functionality of Google. It verifies that the corrected word is suggested
        for search.
        """
        search_str = "fortnight"
        home_page = HomePage(self.driver)
        home_page.search_action(search_str)

        search_result_page = SearchResultPage(self.driver)
        actual_suggested_text = search_result_page.get_suggested_text()
        expected_suggested_text = "fortnite"
        assert actual_suggested_text == expected_suggested_text, \
            "actual suggested text {0} is not same as expected suggested text {1}".format(actual_suggested_text,
                                                                                          expected_suggested_text)

    def test_no_result_found(self):
        """
        This method is to verify 'no result found page' functionality of Google. It verified that the given search 
        string appears on no result found page
        """
        search_str = "NO_RE$ULT_FOUND_TE$T_$CENARIO"
        home_page = HomePage(self.driver)
        home_page.search_action(search_str)

        search_result_page = SearchResultPage(self.driver)
        actual_search_result = search_result_page.get_no_result_found_txt()
        assert search_str in actual_search_result, "search string {0} should be present on No result found page.".format(
            search_str)



import pytest
import softest as softest
from tests.webPages.page_duckDuckGo import Search
from tests.webPages.page_searchResults import SearchResultsPage

@pytest.mark.usefixtures("setup")
class TestMichaelJordanSearch(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.index_page = Search(self.driver, self.wait)
        self.search_result_page = SearchResultsPage(self.driver, self.wait)

    def test_challenge(self):

        # Assert title matches PS: for english use 'DuckDuckGo - Privacy, simplified.'
        self.assertEqual("DuckDuckGo — La privacidad, simplificada.", self.driver.title)

        # Search Michal Jordan in DuckDuckGo
        self.index_page.search("Michael Jordan")

        # Assert that the MAIN search result contains an image
        self.assertTrue(self.search_result_page.search_results_contains_image("Michael Jordan"))

        # Assert at least one of all first 10 results ar from the provided pages
        self.assertTrue(self.search_result_page.at_least_one_result_of("Wikipedia"))
        # No results where found in the first page that came from NBA.com
        self.assertTrue(self.search_result_page.at_least_one_result_of("NBA.com"))

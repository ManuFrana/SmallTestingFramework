import time

import pytest
import softest as softest

from tests.webPages.page_AllSettings import AllSettings
from tests.webPages.page_duckDuckGo import Search

@pytest.mark.usefixtures("setup")
class TestChangeLanguage(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.index_page = Search(self.driver, self.wait)
        self.all_settings_page = AllSettings(self.driver, self.wait)

    def test_challenge(self):

        # Assert title matches PS: for english use 'DuckDuckGo - Privacy, simplified.'
        self.assertEqual("DuckDuckGo — La privacidad, simplificada.", self.driver.title)

        self.index_page.click_option_in_side_menu("Todas las configuraciones")


        self.assertEqual("Ajustes de DuckDuckGo", self.driver.title)

        self.all_settings_page.change_language_to("Esperanto", "Lingvo")
import time

import pytest
import unittest

from tests.webPages.page_Themes import ThemesPage
from tests.webPages.page_duckDuckGo import Search


@pytest.mark.usefixtures("setup")
class TestChangeTheme(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.index_page = Search(self.driver, self.wait)
        self.theme_page = ThemesPage(self.driver, self.wait)

    def test_challenge(self):
        # Click an option from the sideBarMenu (Hamburger icon) PS: for english use 'Themes'
        self.index_page.click_option_in_side_menu("Temas")

        # Asert the page is correct: PS: for english use 'DuckDuckGo Settings'
        self.assertEqual('Ajustes de DuckDuckGo', self.driver.title)

        # Change page theme color and validate it actually changes
        self.theme_page.change_theme("Terminal")

        # Clicks Save and Exit button and validiates page is redirected to https://duckduckgo.com/
        self.theme_page.click_save_button()

import pytest
import unittest

from tests.webPages.page_Blog import Blog


@pytest.mark.usefixtures("setup")
class TestGetInTouchForm(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        print("simplemente paso por aca")

    def test_fill_get_in_touch_form_with_valid_data(self):
        self.blog = Blog(self.driver, self.wait)
        first_get_in_touch = self.blog.get_top_get_in_touch_button()
        first_get_in_touch.click()
        form = self.blog.fill_form('manuel', 'manuel@example.org', 'December Labs', 'Hi please, review my application')
        form.click()
        output_text = self.blog.validate_form_submission()
        self.assertEqual(2, len(output_text), msg="Form did not complete...")
        self.assertEqual('Thanks for reaching out!', output_text[0].text)
        self.assertEqual("We’ll be in touch shortly.", output_text[1].text)

    def test_fill_get_in_touch_form_without_name(self):
        self.blog = Blog(self.driver, self.wait)
        first_get_in_touch = self.blog.get_top_get_in_touch_button()
        first_get_in_touch.click()
        form = self.blog.fill_form('', 'manuel@example.org', 'December Labs', 'Hi please, review my application')
        form.click()
        self.assertTrue(self.blog.validate_name_is_required())

    def test_fill_get_in_touch_form_without_email(self):
        self.blog = Blog(self.driver, self.wait)
        first_get_in_touch = self.blog.get_top_get_in_touch_button()
        first_get_in_touch.click()
        form = self.blog.fill_form('manuel', '', 'December Labs', 'Hi please, review my application')
        form.click()
        self.assertTrue(self.blog.validate_email_is_required())

    def test_fill_get_in_touch_form_company_company(self):
        self.blog = Blog(self.driver, self.wait)
        first_get_in_touch = self.blog.get_top_get_in_touch_button()
        first_get_in_touch.click()
        form = self.blog.fill_form('manuel', 'manuel@example.org', '', 'Hi please, review my application')
        form.click()
        self.assertTrue(self.blog.validate_company_is_required())





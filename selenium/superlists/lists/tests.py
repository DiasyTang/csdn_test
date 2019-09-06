from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
import pdb
from django.template.loader import render_to_string


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        pdb.set_trace()
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.endswith('</html>'))
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)
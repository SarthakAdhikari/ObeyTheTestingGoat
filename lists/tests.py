from django.test import TestCase

from .views import home_page

# Create your tests here.

class HomepageTest(TestCase):

    def test_uses_home_page_template(self):
        response =  self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
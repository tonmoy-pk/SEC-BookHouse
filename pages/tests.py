from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

'''
class HomepageTests(SimpleTestCase):
    # inherit from simpletestcase because here don't have model included
    def test_homepage_status_code(self): # the function is have to start with the name test
        response = self.client.get('/') # take home url, check by url
        self.assertEqual(response.status_code, 200) # Http status code for the homepage equals 200 means that it exists

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home')) # calling the URL name
        self.assertEqual(response.status_code,200)  # check the home page http status code by name

    def test_homepage_template(self): # here this method confirms that homepage uses the correct template
        response = self.client.get('/') # get the home url
        self.assertTemplateUsed(response, 'home.html') # check this url use home template or not

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/') # get the home url
        self.assertContains(response, 'Homepage') # in home template there are 'Homepage' html code

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.') # this html code not in home html'''


class HomepageTests(SimpleTestCase):  # here self.response means self.client.get('/')
    def setUp(self):  # this method is same as test_homepage_url_name method
        url = reverse('home') # take the url by name
        self.response = self.client.get(url)  # here self.response means assign home url

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200) # self.response means get the home url('/'),then check status_code 200 or not means it exists and send correct http request

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')  # self.response means the homepage and check with the template

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage') # get the correct url and check whether contains 'Homepage' html or not

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.') # self.response means homepage and it not include this html code

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/') # check this url function name and class based HomePageview function are same or not
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about') # get the 'about' url
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self): # checking http request
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self): # checking valid template or not
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self): # check this code is write in about.html
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should note be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__) # check whether view func name and AboutPageView name

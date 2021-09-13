from django.test import TestCase
from django.contrib.auth import get_user_model
# the good practice is overly descriptive with your unit test names
from django.urls import reverse, resolve
# we're not using CustomUserCreationForm and SignupPageview,for that reason using django allauth so we reomve from here
'''
the update creation of TestCase is setUpTestData,it's added the ability to run tests both within a whole class and for each individual 
test,it allows the creation of initial data at the class level that can be applied to the entire TestCase.This results in much 
faster tests than using setUp().
'''


class CustomUserTests(TestCase):

    def test_create_user(self):  # testing a user
        User = get_user_model()  # set our user model to the variable User
        user = User.objects.create_user(
            # create one via the manager method create_user,create dummy data
            username='azhar',
            email='ibrahimalazhar264@gmail.com',
            password='azhar19971'
        )
        self.assertEqual(user.username, 'azhar')  # check the username
        self.assertEqual(user.email, 'ibrahimalazhar264@gmail.com')
        self.assertTrue(user.is_active)  # check whether the user is active or not
        self.assertFalse(user.is_staff) # staff is only admin(superuser)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model() # set the user model into variable User
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin') # check the username of super user
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff) # superuser is staff
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase): # this class is for testing signup process in django allauth
    username = 'azhar'      # create dummy username and password
    email = 'ibrahimalazhar264@gmail.com'

    def setUp(self):
        url = reverse('account_signup') # setup the url which url name is 'account_signup' given from allauth
        self.response = self.client.get(url) # take the self.response using url

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200) # check http request
        self.assertTemplateUsed(self.response, 'account/signup.html') # checking the current template
        self.assertContains(self.response, 'Sign Up') # in signup template we use html button 'Sign Up'
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email) # create a new user which is azhar
        self.assertEqual(get_user_model().objects.all().count(),1) # there are only user is 'azhar'
        self.assertEqual(get_user_model().objects.all()[0].username, self.username) # check the username azhar
        self.assertEqual(get_user_model().objects.all()[0].email, self.email) # check the email('ibrahimalazhar264..')

'''
class SignupPageTests(TestCase):
    def setUp(self): # setup is not for testing purpose,it erase repeating code
        url = reverse('signup')  # take the url name to url variable
        self.response = self.client.get(url)  # take the url into self.response

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200) # check signup url valid http response or not
        self.assertTemplateUsed(self.response, 'signup.html') # check this url use signup template or not
        self.assertContains(self.response, 'Sign Up') # this 'Sign Up' is use in button in signup.html
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.') # this one not contains in button in signup html file

    def test_signup_form(self): # check the custom user form for signup process
        form = self.response.context.get('form') # take the form
        self.assertIsInstance(form, CustomUserCreationForm) # check the form
        self.assertContains(self.response, 'csrfmiddlewaretoken') # check the form contain middleware token or not

    def test_signup_view(self): # check the view function for signup process
        view = resolve('/accounts/signup/') # take the url in view variable
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
'''
# if you use django allauth then run the test file you show 3 errors because of our own views,forms an urls.
# we use 3rd party packages django-allauth so don't need to test its core functionality



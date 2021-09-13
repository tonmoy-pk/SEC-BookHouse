from django.test import Client, TestCase
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


class BookTests(TestCase):

    def setUp(self): # here add a sample book to test,create dummy data in setup,when we need this data,just call it
        self.user = get_user_model().objects.create_user(  # take the model(django allauth) and create a dummy user,this model hass these attributes build in which is username,email,password
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )
        self.special_permission = Permission.objects.get(codename='special_status') # here add the special_status permission to the setUp method so it is available for all our tests
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )
        self.review = Review.objects.create( # create a object of Review
            book=self.book,  # this is fk,where pk is Book
            author=self.user,  # this one also fk
            review='An excellent review',
        )

    def test_book_listing(self): # check the models value's,checks that both its string representation and content are correct
        self.assertEqual(f'{self.book.title}', 'Harry Potter') # here check the book title using f string
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')
    '''
    def test_book_list_view(self):
        response = self.client.get(reverse('book_list')) # take the book_list url name
        self.assertEqual(response.status_code, 200)  # check the http request
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url()) # get_absolute_url method define the detail of a book, here book is context_object_name of detailview
        no_response = self.client.get('/books/12345/')  # take this url into no_response variable
        self.assertEqual(response.status_code, 200)  # check valid http request,it is good to check dose exist & doesn't
        self.assertEqual(no_response.status_code, 404)  # check get 404 error or not,incorrect page returns a 404
        self.assertContains(response, 'Harry Potter')  # in detail view take 'Harry Potter' header or not
        self.assertContains(response, 'An excellent review')  # in detailview check there contains this review 'An excellent review' or not
        self.assertTemplateUsed(response, 'books/book_detail.html')'''

    def test_book_list_view_for_logged_in_user(self): # check list view using login user
        self.client.login(email='reviewuser@email.com', password='testpass123') # login with dummy email and password
        response = self.client.get(reverse('book_list'))  # response variable take this url
        self.assertEqual(response.status_code, 200)   # return valid httprequest, 200 for success
        self.assertContains(response, 'Harry Potter')  # in html file this title is include or not
        self.assertTemplateUsed(response, 'books/book_list.html') # check using the correct template or not

    def test_book_list_view_for_logged_out_user(self): # check list view using logged out
        self.client.logout()
        response = self.client.get(reverse('book_list'))  # response variable take this url
        self.assertEqual(response.status_code, 302) # 302 status code means redirection and 200 for success
        self.assertRedirects(response, '%s?next=/books/' % (reverse('account_login'))) # after logout then redirect the account_login url
        response = self.client.get('%s?next=/books/' % (reverse('account_login')))  # in response variable stores the account_login url
        self.assertContains(response, 'Log In') # now check with log in page store the html code 'Log In' or not

    def test_book_detail_view_with_permissions(self): # check a user didn't create the post and try to access the detailpage then shows 403 forbidden
        self.client.login(email='reviewuser@email.com', password='testpass123') # login using this email and password
        self.user.user_permissions.add(self.special_permission) # add special_permission which is obj of Permission
        response = self.client.get(self.book.get_absolute_url()) # response variable takes the detailview using get_abs_url in response var
        no_response = self.client.get('/books/12345/')  # this url is no exist in database
        self.assertEqual(response.status_code, 200) # check for http success,it will be true because there is one user who create the book,so he can easily access his book detail page,
        self.assertEqual(no_response.status_code,404) # check 404 error
        self.assertContains(response, 'Harry Potter')  # check title 'Harry Potter' are in response variable or not
        self.assertContains(response, 'An excellent review')  # check review is in response variable or not
        self.assertTemplateUsed(response, 'books/book_detail.html') # check using correct template or not





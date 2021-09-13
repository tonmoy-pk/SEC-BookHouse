from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin ,PermissionRequiredMixin # we add permissionrequiredmixin after loginrequired and before detailview,because permissionrequired check after the user is logged in
)
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q
# import LoginRequiredMixin for if the user are not logged in then he can't access the listview or detailview,he see the login page


class BookListView(LoginRequiredMixin,ListView): # inherit from Django generic ListView
    model = Book # even somehow know the UUID of a specific page you'd be redirected to log in as well
    context_object_name = 'book_list' # we can define context_object_name is 'book_list',build in context_object_name is 'object_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login' # if the user are not logged in and try to access the listview then django shows the login page,traditional django login url name is 'login' and allauth login url name is 'account_login'


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model = Book
    context_object_name = 'book' # here we explicitly define the context_object_name means in template we use 'book' for this item in place of 'object'
    template_name = 'books/book_detail.html'
    login_url = 'account_login' # if the user access the detail view then show login page,for allauth it is 'acc_login'
    permission_required = 'books.special_status' # permisssionrequired works on books(app name) model,if a normal user who is not superuser try to access the detail page of a books which one he didn't create then shows 403 forbidden,but a superuser can access all of detailview of a book


class SearchResultsListView(ListView): # here build a class based view for searching which inherits from ListView
    model = Book  # using book model
    context_object_name = 'book_list'  # here book_list means all list of books related to search
    template_name = 'books/search_results.html'
    # queryset = Book.objects.filter(title__icontains='beginners') # filtering the title for searching purpose,contains is case sensitive and icontains is not case sensitive
    # for basic filtering most of the time built in queryset methods of filter(),all(),get(),exclude() is enough

    def get_queryset(self):  # using Q for search multiple things, | means or,here number of filters grows so seperate out the queryset override via get_queryset() mehtod
        query = self.request.GET.get('q') # added query variable that takes the value of q from the form submission, q is the input name of search from home.html,get the value and store to query variable
        return Book.objects.filter(  # updated our filter to use query on either a title or an author
            Q(title__icontains=query) | Q(author__icontains=query) # icontains is case insensitive,search title or author where take the input name 'q' from html file,, title,author is attributes of Model
        )

'''
the third mixin is 'UserPassesTestMixin' which restricts a view's access only to users who pass a specific test.
Another in large projects is groups,which are Django's way of applying permissions to a category of users,become prominent.There are dedicated Groups
section in admin homepage where they can be added and have permissions set yet.This is far more efiicient than adding permissions
on a per-use basis.
'''

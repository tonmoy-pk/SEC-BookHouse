from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView

urlpatterns = [
    path('', BookListView.as_view(),name='book_list'),
    # django also added a field called id,which is primary key,the pk of first book is 1
    # path('<int:pk>', BookDetailView.as_view(), name='book_detail'), # when we use id as a pk
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),  # here using uuid as a pk in place of int id,
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]




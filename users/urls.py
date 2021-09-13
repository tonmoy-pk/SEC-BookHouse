from django.urls import path
from .views import SignupPageView
# if i use django allauth then we don't need to use signup url and view function,the signup process also include in
# django all auth app as well as include login,logout,password_reset

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'), # the existing url names for login and signup are written within the buil-in django app file django/contrib/auth/urls.py
]

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# if you use the django allauth,then you don't need to create url,view function,form for signup purpose,the django build
# in allauth contains login,logout,password and signup also.


# here we use django allauth,first install this package then set in installed_apps,
# you don't need to create signup view function,django allauth automatically handles login,logout and signup also
class SignupPageView(generic.CreateView): # extends createview for sign up purpose
    form_class = CustomUserCreationForm  # this form is custom user form (extends base form)
    success_url = reverse_lazy('login') # in class based form we have to use revers lazy because here take some times
    template_name = 'signup.html'




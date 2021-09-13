from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView): # using django's templateview so that the only tweak needed is to specify desired temp
    template_name = 'home.html'


class AboutPageView(TemplateView): # this view inherit from django build in templateview
    template_name = 'about.html'


from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(),name='home'), # even if we change the actual route of this page,we can still refeer to it by same home url name
    path('about/', AboutPageView.as_view(), name='about'),
]
'''
# in django.contrib.auth.urls the build in url and name is
accounts/login [name='login']
accounts/logout [name='logout']
accounts/password_change/ [name= 'password_change]
accounts/password_change/done/ [name= 'password_change_done]
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
'''


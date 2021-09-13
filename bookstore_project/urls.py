"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    # here we change the path for admin,because hacker can easily access the admin path
    # if we use django-admin-honeypot(3rd party package),then a hacker can enter the admin page which is fake,then after the login this IP address will be blocked for this site
    path('anything-but-admin',admin.site.urls),
    # path('admin/', admin.site.urls),
    # for accounts/login,logout,password_reset and also signup purpose here we use django allauth's(a third party app)
    # the url is accounts/login,accounts/logout etc,and the url name is 'account_login', 'account_logout' etc(build in)
    path('accounts/', include('allauth.urls')), # here using allauth in place of auth
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# to see media items locally we need add this additional line

if settings.DEBUG:  # if DEBUG is true then the Debug Toolbar is appear,DEBUG is true in local mode not production mode
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)), # when we access debug toolbar this path is shown in command prompt
    ] + urlpatterns



'''
  # here swap out the build in auth app and accounts/signup for django-allauth's own allauth app
  # User Management
  path('accounts/', include('django.contrib.auth.urls')),  # for build in authentication like accounts/login,accounts/logout, accounts/password_change, accounts/password_change/done etc
  # Local apps
  path('accounts/', include('users.urls')), # we can create any route for signup process but it's common to use the same accounts/ one used by the default auth app
  '''


'''
# this url need to template in registration/login, registration/logout .... etc
# Back in the auth/views.py(build in,github) file we can see on line 45 for LoginView that the template_name is 'registration/login.html',if you change the default location we could,we can use overriding which seems like overkill
# the source code of build in login,logout,password_change,password_change_done,password_reset authentication django source code
# you can write these urls in project level urls or don't need to add in urls file,it works fine
# django/contrib/auth/urls.py
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'), # name is refer to it with a template tag in html file
    path('logout/', views.LogoutView.as_view(), name='logout'), #name=logout means refer to it with a template tag as just logout
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
'''
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()  # take the model using get_user_model obj
# this class is using for Users in admin page,in django allauth automatically build in Accounts and Sites, in Accounts
# section shows all registered Email addresses and Sites define a Domain name,you can change this domain name for
# configuring email
# here we don't need to form here,the CustomUserCreation form no longer use here because of django allauth


class CustomUserAdmin(UserAdmin):  # create a CustomUserAdmin class which extend from UserAdmin(build in)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser  # take the current model and store it into variable
    list_display = ['email', 'username',]  # this list display on admin page,we can also add "is_staff" in list display


admin.site.register(CustomUser, CustomUserAdmin) # register CustomUserAdmin in place of CustomUser(general model which inherit from abstract user) in admin page

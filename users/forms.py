from django.contrib.auth import get_user_model  # directly importing CustomUser here,making one single reference
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# we don't need to customUsercreation form anymore,the django-allauth define the form for signup process

class CustomUserCreationForm(UserCreationForm): # extend the base user form where store username,password
    # this class is using for sign up creation form
    class Meta:
        model = get_user_model() # take the model
        fields = ('email', 'username',)  # here the list of fields,you don't need to set password explicitly in fields


class CustomUserChangeForm(UserChangeForm): # extend the base user form UserChangeForm
    class Meta:     # this class using for admin can change this attributes
        model = get_user_model() # take the model
        fields = ('email', 'username',) # admin can change this fields values


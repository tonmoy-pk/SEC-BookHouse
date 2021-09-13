from django.db import models
from django.contrib.auth.models import AbstractUser
# if you wanted to fully rip out the default user system that would means using AbstractBaseUser rather than AbstractUse
# here we use django allauth,, and for sign up and login process we set email in place of username through settings.py file,but in admin.py file here set username as well as email,fully removing the username from the custom user model
# requires the use of AbstractBaseUser,it requires far more coding
# if you use the two same email for sign process like one use gmail and another one use hotmail then the first one user -name set before @ in email and second one username set django allauth automatically


class CustomUser(AbstractUser): # it extends from AbstractUser so the attributes in here is username and password,we can add attribute in this class
    pass

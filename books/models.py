from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model


class Book(models.Model): # importing django class models and then creating a Book model that subclass it which means we
    # automatically have access to everything within django.db.models.Models
    id = models.UUIDField(  # here id field store uuid which is django build in url in place of id=1 or 2..
        primary_key=True, # UUIDField of id is pk
        db_index=True,  # here using indexing for faster searches,for better performance,typically only applied on pk in a model,require additional space
        default= uuid.uuid4, # use uuid4 for encryption,this allows us to use DetailView which requires either a slug or pk field,it won't work with a UUID field without significant modification
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # here blank is True,because already we have 3 data,if we wanted to uploads of a regular file than we use FileField
    # cover = models.ImageField(upload_to='covers/', blank=True) # imagefield comes with some basic image processing validation,uploaded image will be MEDIA_ROOT/covers(the MEDIA_ROOT part is implied based on settings.py file)
    # upload_to ='covers' means when we upload the image from any directory then it auto upload to covers directory

    class Meta: # add a special class that an author can read all books(access to detailview)
        permissions = [ # set a permission name and description which will be visible in the admin
            ('special_status', 'Can read all books'),  # after this then go to a user of admin page then search in user permission box books|book|Can read all books (which means the user can read all books means accessing detailview),click the arrow the save it in admin page
        ]

    def __str__(self): # using dunder string for show title in admin and django shell
        return self.title

    def get_absolute_url(self): # reverse the url name 'book_detail' and passes in the id as a string
        # here pass a dictionary to url where pk is str representation of self.pk
        return reverse('book_detail',kwargs={'pk': str(self.pk)}) # this method is using for when you wants to enter the detailpage after submitting form or clicking the list header,whenever you need individual pages for an object


class Review(models.Model):
    book = models.ForeignKey( # one to many foreign key that links to Book class,and naming it the same linked model
        Book,
        on_delete= models.CASCADE,  # if delete this book then connected review also deleted
        related_name='reviews',   # here this is a foreign key relationship if we find out all reviews of a book then we use book.reviews.all
    )
    review = models.CharField(max_length=255)  # review field contains the actual content which is textfield
    author = models.ForeignKey(  # link to the author field to auto update the current user with review
        get_user_model(),  # get_user_model refers the custom user model
        on_delete=models.CASCADE, # if a author is delete then the related review also remove automatically
    )

    def __str__(self):
        return self.review



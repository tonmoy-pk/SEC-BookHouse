from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):  # here create a class where review is Tabular form
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,  # here set the tabular review inside the BookAdmin for set the review inside the each book
    ]
    list_display = ("title", "author", "price",)  # it specify which fields we also want display


admin.site.register(Book, BookAdmin)  # register the BookAdmin class inside of Book model for display the list and inline review


from django.contrib import admin
from .models import Book,Author
from . import models
# Register your models here.



class BookManger(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'market_price','pub']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['pub']
    list_editable = ['market_price']
admin.site.register(Book, BookManger)

class AuthorManger(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['name']
    list_editable = ['age']
admin.site.register(Author, AuthorManger)

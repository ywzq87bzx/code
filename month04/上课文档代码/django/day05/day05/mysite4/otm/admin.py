from django.contrib import admin
from .models import Publisher, Book


# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']


admin.site.register(Publisher)
admin.site.register(Book, BookManager)

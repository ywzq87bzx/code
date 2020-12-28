from django.contrib import admin
from .models import Author,Book
# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Author)
admin.site.register(Book,BookManager)
from django.contrib import admin
from .models import Book, Author


# Register your models here.

# 添加一个模型管理器类
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    search_fields = ['title']
    list_filter = ['pub']
    list_display_links = ['id', 'title']
    # list_editable = ['market_price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


# 注册模型类和模型管理器类
admin.site.register(Book, BookManager)

admin.site.register(Author, AuthorManager)

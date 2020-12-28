from django.contrib import admin
from .models import *
# Register your models here.
# [10分钟]，在后台界面中添加多对多的管理
# 17:45回来带着写！！


admin.site.register(Author)
admin.site.register(Book)
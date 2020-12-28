"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views
# urlpatterns是一个列表，列表中每一项
# 表示url与视图函数的对应关系，换句话说，
# 用户请求的url过来后，由哪个视图函数去处理
# 这种对应关系会使用path函数
urlpatterns = [
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/page/2003
    path('page/2003',views.page_2003),
    # 127.0.0.1:8000/page/2004
    path('page/2004' ,views.page_2004),
    # 127.0.0.1:8000
    path('',views.default_page),
    path('page/1',views.page_one),
    path('page/<int:num>',views.page_num),
    path('users/<path:name>', views.page_name),
    path('<int:a>/<str:op>/<int:b>',views.math_view),
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})$',
            views.birthday_view),
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})$',
            views.birthday_view),



]

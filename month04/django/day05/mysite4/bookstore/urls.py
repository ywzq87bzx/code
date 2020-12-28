from django.urls import path
from . import views

urlpatterns=[
    path('',views.list_view),
    path('add',views.add_view),
    path('update/<int:bid>',views.update_view),
    path('delete', views.delete_view),
]
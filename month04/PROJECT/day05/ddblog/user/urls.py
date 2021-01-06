from django.urls import path
from . import views
urlpatterns =[
    path('sms', views.sms_view),
    path('<str:username>',views.UsersView.as_view()),
    path('<str:username>/avatar',views.user_avatar)
]
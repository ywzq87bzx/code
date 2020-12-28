from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.user_detail),
    path('update/<int:id>', views.user_update),
]

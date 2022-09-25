from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('new_user', views.new_user_method)
]
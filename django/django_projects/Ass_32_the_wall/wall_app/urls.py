from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('register', views.register),
    path('login/', views.login),
    path('wall', views.show_the_wall),
    path('wall/post_message', views.post_message),
    path('wall/post_comment', views.post_comment),
    path('logout', views.logout)
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('adding_dojo', views.adding_dojo_method),
    path('adding_ninja', views.adding_ninja_method)
]
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.root),
    path('destroy_session',views.destroy_session),
    path('make_add_two',views.make_add_two),
]
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root_method),
    path('blogs', views.index_method),
    path('new', views.new_method),
    path('create', views.create_method),
    path('<int:number>', views.show_method),
    path('<int:number>/edit', views.edit_method),
    path('<int:number>/delete', views.destroy_method),
    path('json',views.title_content_method),
]
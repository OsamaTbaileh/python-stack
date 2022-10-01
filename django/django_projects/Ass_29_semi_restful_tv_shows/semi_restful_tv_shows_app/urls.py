from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.view_all_shows),
    path('shows/new', views.add_new_show),                                  # when press add new show on top right
    path('shows/create', views.create_new_show),                            # when press create on left top
    path('shows/<show_id>', views.view_the_show),                           # when press show on top right
    path('shows/<show_id>/edit', views.go_to_edit_the_show),                # when press on edit on top right or bottom
    path('shows/<show_id>/update', views.update_the_show),                  # wheb press on update on left bottom
    path('shows/<show_id>/destroy', views.delete_the_show),                 # when press on delete on right top and bottom
    path('go_back_to_shows',views.go_back_to_shows)                         #to go back to the main shows page
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.main_page),
    path('books/add_fav_book', views.add_fav_book),#ok
    path('books/<book_id>/add_to_fav', views.add_to_fav),###3still not test
    path('books/<book_id>', views.view_the_book),
    path('books/<book_id>/update', views.update_the_book),
    path('books/<book_id>/delete', views.delete_the_book),
    path('books/<book_id>/unfav_book', views.unfav_book)
]
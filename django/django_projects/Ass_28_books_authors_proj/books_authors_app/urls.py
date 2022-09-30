from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('adding_book', views.adding_book_method),
    path('books/<book_id>', views.view_book_method),
    path('add_author_to_book/<book_id>', views.add_author_to_book_method),
    path('authors', views.authors_main_page_method),
    path('adding_author', views.adding_author_method),
    path('authors/<author_id>', views.view_author_method),
    path('add_book_to_author/<author_id>', views.add_book_to_author_method),
]
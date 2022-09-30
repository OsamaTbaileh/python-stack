from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Book, Author

def root(request):
    context = {
        "all_the_books": Book.objects.all()
    }
    return render(request, "add_a_book.html", context)

def adding_book_method(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def view_book_method(request, book_id ):
    the_book= Book.objects.get(id=book_id)
    context = {
        "the_book_template" : the_book,
        "book_id_template" : book_id,
        "the_book_authors": the_book.authors.all(),
        "all_the_authors": Author.objects.all()
    }    
    return render(request, "book.html", context)

def add_author_to_book_method(request, book_id):
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = request.POST["author"])
    book.authors.add(author)
    return redirect('/books/'+ str (book_id))





def authors_main_page_method(request):
    context = {
        "all_the_Books": Book.objects.all(),
        "all_the_Authors": Author.objects.all()
    }
    return render(request, "add_an_author.html", context)

def adding_author_method(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=first_name, last_name=last_name, notes=notes)
    return redirect('/authors')

def view_author_method(request, author_id ):
    the_author= Author.objects.get(id=author_id)
    context = {
        "the_author_template" : the_author,
        "author_id_template" : author_id,
        "the_author_books": the_author.books.all(),
        "all_the_books": Book.objects.all()
    }    
    return render(request, "author.html", context)

def add_book_to_author_method(request,author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(title= request.POST['book'])
    author.books.add(book)
    return redirect('/authors/' + str(author_id))

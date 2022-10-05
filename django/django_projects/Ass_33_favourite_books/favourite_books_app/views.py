from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

def root(request):
    return render(request, 'login_and_registration.html')


def register(request):
    errors = User.objects.basic_validator_register(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/') 
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)

        request.session['username'] = request.POST['first_name']
        user = User.objects.get(email= request.POST['email'])
        request.session['userid'] = user.id
    return redirect('/books')


def login(request):
    errors = User.objects.basic_validator_login(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/') 
    else:
        user = User.objects.filter(email = request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                request.session['username'] = logged_user.first_name
                request.session['status'] = "logged in"
                return redirect('/books')
        return redirect('/')


def logout(request):
    # del request.session['userid']
    # del request.session['username']
    request.session.clear()
    return redirect('/')


def main_page(request):
    if 'userid' not in request.session:
        return redirect("/")
    the_user = User.objects.get(id = request.session['userid'])
    context = {
        "book_list_liked_by_user" : the_user.liked_books.all(),
        "all_the_books" : Book.objects.all(),
        "all_the_users" : User.objects.all(),
    }
    return render(request, 'favourite_books.html', context )


def add_fav_book(request):
    errors = Book.objects.basic_validator_book(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/') 
    else:
        the_book = Book.objects.create(title = request.POST['title'], desc = request.POST['description'], uploaded_by = User.objects.get(id = request.session['userid']))
        the_user = User.objects.get(id=request.session['userid'])
        the_user.liked_books.add(the_book)
    return redirect('/books')


def add_to_fav(request, book_id):
    the_book = Book.objects.get(id=book_id)
    the_user = User.objects.get(id=request.session['userid'])
    the_user.liked_books.add(the_book)
    return redirect('/books')


def view_the_book(request, book_id):
    the_book = Book.objects.get(id=book_id)
    the_user = User.objects.get(id = request.session['userid'])
    context = {
    "the_book" :Book.objects.get(id=book_id),
    "users_list_liked_the_book" : the_book.users_who_like.all(),
    "liked_books_by_user" : the_user.liked_books.all(),
    "all_the_books" : Book.objects.all(),
    "all_the_users" : User.objects.all(),
    }
    return render(request, 'the_book.html', context)


def update_the_book(request, book_id):
    the_book = Book.objects.get(id= book_id)
    the_book.title = request.POST['title']
    the_book.desc = request.POST['description']
    the_book.save()
    return redirect('/books')


def delete_the_book(request,book_id):
    the_book = Book.objects.get(id= book_id)
    the_book.delete()
    return redirect('/books')


def unfav_book(request, book_id):
    the_book = Book.objects.get(id=book_id)
    the_user = User.objects.get(id=request.session['userid'])
    the_user.liked_books.remove(the_book)
    return redirect('/books')
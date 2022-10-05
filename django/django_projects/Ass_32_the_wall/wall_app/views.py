from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
from models import *
import bcrypt


def root(request):
    return render(request, 'login_and_registration.html')


def register(request):
    errors = User.objects.basic_validator_register(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/') 
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)

    request.session['username'] = request.POST['first_name']
    user = User.objects.get(email= request.POST['email'])
    request.session['userid'] = user.id
    return redirect('/wall')


def login(request):
    errors = User.objects.basic_validator_login(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/') 

    user = User.objects.filter(email = request.POST['email'])
    print(user)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session['username'] = logged_user.first_name
            request.session['status'] = "logged in"
            return redirect('/wall')
    return redirect('/')


def show_the_wall(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user" : User.objects.get(id=request.session['userid']),
        "all_the_users" : User.objects.all(),
        "all_the_messages" : Message.objects.all(),
        "all_the_comments" : Comment.objects.all()
    }
    return render (request, 'the_wall.html', context) 


def post_message(request):
    models.create_post(request)
    return redirect('/wall')


def post_comment(request):
    user = User.objects.get(id = request.session['userid'])
    message = Message.objects.get(id = request.POST['messageid'])
    Comment.objects.create(comment = request.POST['comment'], user = user , message = message)
    return redirect('/wall')


def logout(request):
    del request.session['userid']
    del request.session['username']
    return redirect('/')

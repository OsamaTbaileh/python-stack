from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def root(request):
    return render(request, 'login_and_registration.html')


def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/') 
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # print(pw_hash)
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
    request.session['username'] = request.POST['first_name']
    request.session['status'] = "Registered"
    # print(request.session['username'])
    return redirect('/success')


def login(request):
    user = User.objects.filter(email = request.POST['email'])
    print(user)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # request.session['userid'] = logged_user.id
            request.session['username'] = logged_user.first_name
            request.session['status'] = "logged in"
            return redirect('/success')
    return redirect('/')


def success(request):
    if 'username' not in request.session:
        return redirect("/")
    return render (request, 'success.html')    


def logout(request):
    # del request.session['userid']
    del request.session['username']
    return redirect('/')





from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import User

def root(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request, "index.html", context)
    

def new_user_method(request):
    new_user = User.objects.create(
    first_name=request.POST['first_name'], 
    last_name = request.POST['last_name'], 
    email_address=request.POST['email'],
    age=request.POST['age'])
    print(new_user)
    return redirect('/')

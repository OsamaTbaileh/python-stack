from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Dojo, Ninja

def root(request):
    context = {
        "all_the_Dojos": Dojo.objects.all(),
        "all_the_Ninjas": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def adding_dojo_method(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(name=name, city=city, state=state, desc="OK")
    return redirect('/')

def adding_ninja_method(request):
    print(request.POST['dojo'])
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = Dojo.objects.get(name= request.POST['dojo'])
    Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')
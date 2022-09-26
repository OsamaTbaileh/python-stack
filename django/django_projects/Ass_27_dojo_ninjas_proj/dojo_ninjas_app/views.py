from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Dojo, Ninja

def root(request):
    context = {
        "all_the_Dojos": Dojo.objects.all(),
        "all_the_Ninjas": Ninja.objects.all()
    }
    print (context)
    return render(request, "index.html", context)

def adding_dojo_method(request):
    name = request.Post['name']
    city = request.Post['city']
    state = request.Post['state']
    Dojo.objects.create(name=name, city=city, state=state, desc="OK")
    return redirect('/')

def adding_ninja_method(request):
    first_name = request.Post['first_name']
    last_name = request.Post['last_name']
    dojo = Dojo.objects.get(name= request.POST['dojo'])
    Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/')
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    # if request.method == "GET":
    #     print("a GET request is being made to this route")
    #     return render(request, "counter.html")
    # if request.method == "POST":
    #     print("a POST request is being made to this route")


    if 'count' not in request.session:  
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request,"counter.html")

def destroy_session(request):
    del request.session['count']		
    return render(request, "result.html")

def make_add_two(request):
    request.session['count'] += 1
    return redirect('/')	




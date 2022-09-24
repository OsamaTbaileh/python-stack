from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return render (request,"dojo_survey.html")

def create_user(request):
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    gender = request.POST['flexRadioDefault']
    comment = request.POST['comment']
    context = {
        "name_on_template" : name,
        "location_on_template" : location,
        "language_on_template" : language,
        "gender_on_template" : gender,
        "comment_on_template" :comment
    }
    return render (request, "result.html", context)


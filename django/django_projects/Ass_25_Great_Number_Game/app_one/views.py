from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import random

def root(request):
    if 'random_number' not in request.session:
        request.session['random_number'] = random.randint(0,101)
        print (request.session['random_number'])

    if 'color' in request.session:
        del request.session['color']
    if 'dimension' in request.session:
        del request.session['dimension']
    if 'ok' in request.session:
        del request.session['ok']
    return render(request, "great_number_game.html")

def guess_method(request):
    if 'answer' not in request.session:
        request.session['answer'] = "" 
    if 'color' not in request.session:
        request.session['color'] = "" 
    if 'dimension' not in request.session:
        request.session['dimension'] = "300px"



    if int(request.POST['number']) == (request.session['random_number']):
        request.session['ok'] = "ok"
        request.session['answer'] = "was the number"
        request.session['color'] = "green"

    if int(request.POST['number']) > (request.session['random_number']):
        request.session['answer'] = "Too high"
        request.session['color'] = "red"

    if int(request.POST['number']) < (request.session['random_number']):
        request.session['answer'] = "Too low"
        request.session['color'] = "red"

    return render(request, "great_number_game.html")

def play_again_method(request):
    del request.session['random_number']
    return redirect('/')

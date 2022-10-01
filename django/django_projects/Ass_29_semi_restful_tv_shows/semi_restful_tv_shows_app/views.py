from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Show


def root(request):
    return redirect('/shows')


def view_all_shows(request):
    context = {
        "all_the_shows" : Show.objects.all()
    }
    return render(request, "all_shows.html", context)


def add_new_show(request):    
    return render(request, "add_new_show.html")


def create_new_show(request):   
    new_show = Show.objects.create(title = request.POST['title'], 
        network = request.POST['network'], 
        release_date = request.POST['release_date'], 
        description = request.POST['description'])
    return redirect ('/shows/'+ str(new_show.id))


def view_the_show(request, show_id):
    the_show = Show.objects.get(id = show_id)
    context = {
        "the_show_template" : the_show
    }
    return render(request, "tv_show.html", context)


def go_to_edit_the_show(request, show_id):
    the_show = Show.objects.get(id = show_id)
    context = {
        "the_show_template" : the_show
    } 
    return render(request, "edit_show.html", context)


def update_the_show(request, show_id):
    the_show = Show.objects.get(id=show_id)
    the_show.title = request.POST['title']
    the_show.network = request.POST['network']
    the_show.release_date = request.POST['release_date']
    the_show.description = request.POST['description']
    the_show.save()
    return redirect('/shows/' + str(show_id))


def delete_the_show(request, show_id):
    the_show = Show.objects.get(id=show_id)
    the_show.delete()
    return redirect ('/shows')


def go_back_to_shows(request):
    return redirect('/shows')
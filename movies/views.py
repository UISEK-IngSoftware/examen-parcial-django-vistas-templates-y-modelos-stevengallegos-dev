from django.shortcuts import render
from django.template import loader
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request,'index.html', {
        'movies': movies
        })

def movie_details(request, movie_id):
    movie = Movie.objects.get(id = movie_id)
    return render(request, 'movie_details.html', {
        'movie': movie
    })
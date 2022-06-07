from django.shortcuts import render
from .request import * 


# Create your views here.
def home(request):
    popular_movies = get_movies('popular')

    return render(request,'home.html',{"popular_movies":popular_movies})

def description(request,movie_id):
    one_movie = get_single_movie(movie_id)
    movie = get_single_movie(movie_id)
    youtube_id = get_youtube(movie['title'])
    youtube_url = f'https://www.youtube.com/embed/{youtube_id}?autoplay=1&muted=0'
    return render(request, 'details.html', {'one_movie':one_movie, 'youtube_url':youtube_url})

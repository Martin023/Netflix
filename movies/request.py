import requests
from decouple import config

def get_movies(category):
    BASE_URL= f'https://api.themoviedb.org/3/movie/{category}?api_key={config("API_KEY")}'
    response= requests.get(BASE_URL)
    movielists= response.json()
    movie_results =[]
    for movie in movielists['results']:
        if movie ['poster_path'] is not None:
            movie_results.append(movie) 
    return movie_results

def get_single_movie(movie_id):
    BASE_URL= f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={config("API_KEY")}'
    return requests.get(BASE_URL).json()


def get_youtube(movie_title):
    search_query = movie_title.replace(' ', '+')
    BASE_URL= f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={search_query}&key={config("YOUTUBE_API_KEY")}'
    response = requests.get(BASE_URL)
    youtube_id = response.json()['items'][0]['id']['videoId']
    return youtube_id
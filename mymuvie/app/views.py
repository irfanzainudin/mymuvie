import requests
from django.shortcuts import render

from .models import Movie


# http://www.omdbapi.com/?apikey=7cdadab5

def index(request):
    movie_list = Movie.objects.get_queryset()
    context = {
        "movie_list": movie_list
	}
    return render(request, "app/index.html", context)

# {'Title': 'Hidden', 'Year': '2015', 'Rated': 'R', 'Released': '15 Sep 2015', 'Runtime': '84 min', 'Genre': 'Horror, Sci-Fi, Thriller', 'Director': 'Matt Duffer, Ross Duffer', 'Writer': 'Matt Duffer, Ross Duffer', 'Actors': 'Alexander Skarsgård, Andrea Riseborough, Emily Alyn Lind', 'Plot': 'A family takes refuge in a bomb shelter to avoid a dangerous outbreak.', 'Language': 'English', 'Country': 'United States', 'Awards': 'N/A', 'Poster': 'https://m.media-amazon.com/images/M/MV5BM2Q2ZGQyOTAtMWYzYi00YzdiLWJlOGUtMmMyZWExMzc4Nzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '6.4/10'}, {'Source': 'Rotten Tomatoes', 'Value': '80%'}], 'Metascore': 'N/A', 'imdbRating': '6.4', 'imdbVotes': '24,662', 'imdbID': 'tt2131532', 'Type': 'movie', 'DVD': '06 Oct 2015', 'BoxOffice': 'N/A', 'Production': 'N/A', 'Website': 'N/A', 'Response': 'True'}
def search(request):
    r = requests.get(url="http://www.omdbapi.com/?apikey=7cdadab5&t=" + request.POST["m_title"])
    title = r.json()["Title"]
    year = r.json()["Year"]
    rated = r.json()["Rated"]
    released = r.json()["Released"]
    runtime = r.json()["Runtime"]
    genre = r.json()["Genre"]
    director = r.json()["Director"]
    writer = r.json()["Writer"]
    actors = r.json()["Actors"]
    plot = r.json()["Plot"]
    language = r.json()["Language"]
    awards = r.json()["Awards"]
    poster = r.json()["Poster"]
    ratings = str(r.json()["Ratings"])
    metascore = r.json()["Metascore"]
    imdb_rating = r.json()["imdbRating"]
    imdb_votes = r.json()["imdbVotes"]
    imdb_id = r.json()["imdbID"]
    c_type = r.json()["Type"]
    dvd = r.json()["DVD"]
    box_office = r.json()["BoxOffice"]
    production = r.json()["Production"]
    website = r.json()["Website"]
    search_result = [title, year]
    # search_result = [
    #     title,
    #     year,
    #     rated,
    #     released,
    #     runtime,
    #     genre,
    #     director,
    #     writer,
    #     actors,
    #     plot,
    #     language,
    #     awards,
    #     poster,
    #     ratings,
    #     metascore,
    #     imdb_rating,
    #     imdb_votes,
    #     imdb_id,
    #     c_type,
    #     dvd,
    #     box_office,
    #     production,
    #     website
    # ]
    context = {
        "search_result": search_result
	}
    return render(request, "app/search.html", context)
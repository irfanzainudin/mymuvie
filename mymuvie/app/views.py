import requests, datetime
from django.shortcuts import get_object_or_404, render

from .models import Movie


# http://www.omdbapi.com/?apikey=7cdadab5

def index(request):
    movie_list = Movie.objects.get_queryset()
    context = {
        "movie_list": movie_list
	}
    return render(request, "app/home.html", context)

# Movie
# {'Title': 'Hidden', 'Year': '2015', 'Rated': 'R', 'Released': '15 Sep 2015', 'Runtime': '84 min', 'Genre': 'Horror, Sci-Fi, Thriller', 'Director': 'Matt Duffer, Ross Duffer', 'Writer': 'Matt Duffer, Ross Duffer', 'Actors': 'Alexander Skarsgård, Andrea Riseborough, Emily Alyn Lind', 'Plot': 'A family takes refuge in a bomb shelter to avoid a dangerous outbreak.', 'Language': 'English', 'Country': 'United States', 'Awards': 'N/A', 'Poster': 'https://m.media-amazon.com/images/M/MV5BM2Q2ZGQyOTAtMWYzYi00YzdiLWJlOGUtMmMyZWExMzc4Nzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '6.4/10'}, {'Source': 'Rotten Tomatoes', 'Value': '80%'}], 'Metascore': 'N/A', 'imdbRating': '6.4', 'imdbVotes': '24,662', 'imdbID': 'tt2131532', 'Type': 'movie', 'DVD': '06 Oct 2015', 'BoxOffice': 'N/A', 'Production': 'N/A', 'Website': 'N/A', 'Response': 'True'}

# Series
# {'Title': 'The Resident', 'Year': '2018–2023', 'Rated': 'TV-14', 'Released': '21 Jan 2018', 'Runtime': '60 min', 'Genre': 'Drama', 'Director': 'N/A', 'Writer': 'Amy Holden Jones, Hayley Schore, Roshan Sethi', 'Actors': 'Matt Czuchry, Manish Dayal, Bruce Greenwood', 'Plot': 'A group of doctors at Chastain Memorial Hospital face personal and professional challenges on a daily basis.', 'Language': 'English', 'Country': 'United States', 'Awards': '1 win & 2 nominations', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTQ0MWEzZmEtYmViYS00Yjk3LTk0NTYtOWFiMGQzYmM3MzI5XkEyXkFqcGdeQXVyMTEwMTQ4MzU5._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.8/10'}], 'Metascore': 'N/A', 'imdbRating': '7.8', 'imdbVotes': '30,191', 'imdbID': 'tt6483832', 'Type': 'series', 'totalSeasons': '6', 'Response': 'True'}
def search(request):
    m_title = request.POST["m_title"]
    m_year = request.POST["m_year"] if request.POST["m_year"] else ""
    url = "http://www.omdbapi.com/?apikey=7cdadab5&t=" + m_title + "&y=" + m_year
    r = requests.get(url=url)
    # print(r.json())
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
    country = r.json()["Country"]
    awards = r.json()["Awards"]
    poster = r.json()["Poster"]
    ratings = str(r.json()["Ratings"])
    metascore = r.json()["Metascore"]
    imdb_rating = r.json()["imdbRating"]
    imdb_votes = r.json()["imdbVotes"]
    imdb_id = r.json()["imdbID"]
    c_type = r.json()["Type"]
    dvd = r.json()["DVD"] if r.json()["DVD"] else ""
    box_office = r.json()["BoxOffice"]
    production = r.json()["Production"]
    website = r.json()["Website"]
    search_result = [(
        title,
        year,
        rated,
        released,
        runtime,
        genre,
        director,
        writer,
        actors,
        plot,
        language,
        awards,
        poster,
        ratings,
        metascore,
        imdb_rating,
        imdb_votes,
        imdb_id,
        c_type,
        dvd,
        box_office,
        production,
        website
    )]
    movie_list = Movie.objects.get_queryset()
    context = {
        "movie_list": movie_list,
        "search_result": search_result
	}
    return render(request, "app/search.html", context)

def save(request):
    m_title = request.POST["item"].split('/')[0]
    m_year = request.POST["item"].split('/')[1]
    url = "http://www.omdbapi.com/?apikey=7cdadab5&t=" + m_title + "&y=" + m_year
    r = requests.get(url=url)
    title = r.json()["Title"]
    year = r.json()["Year"]
    # rated = r.json()["Rated"]
    # released = r.json()["Released"]
    # runtime = r.json()["Runtime"]
    # genre = r.json()["Genre"]
    # director = r.json()["Director"]
    # writer = r.json()["Writer"]
    # actors = r.json()["Actors"]
    # plot = r.json()["Plot"]
    # language = r.json()["Language"]
    # country = r.json()["Country"]
    # awards = r.json()["Awards"]
    # poster = r.json()["Poster"]
    # ratings = str(r.json()["Ratings"])
    # metascore = r.json()["Metascore"]
    # imdb_rating = r.json()["imdbRating"]
    # imdb_votes = r.json()["imdbVotes"]
    # imdb_id = r.json()["imdbID"]
    # c_type = r.json()["Type"]
    # dvd = r.json()["DVD"]
    # box_office = r.json()["BoxOffice"]
    # production = r.json()["Production"]
    # website = r.json()["Website"]
    selected_movie = Movie.objects.create()
    selected_movie.title = title
    selected_movie.year = year
    selected_movie.save()
    movie_list = Movie.objects.get_queryset()
    context = {
        "movie_list": movie_list
	}
    return render(request, "app/save.html", context)
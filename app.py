
from flask import Flask, redirect, render_template, request, abort, url_for
from src.repositories.movie_repository import MovieRepository, movie_repository_singleton
from src.models.movie import Movie

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    your_list = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, your_list = your_list)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3

    
        #store whatever the user searched for in the title
    title = request.args.get('searchMov', "-2")

            #if they did search for something get the movie
    movie = movie_repository_singleton.get_movie_by_title(title)
    #if nothing was put into the search bar create a fake movie that notifies the program that nothing was serached for
    if title =="" or title == "-2":
        movie = Movie("-1", "-1", -1)
    
        
#code I wrote end here

    return render_template('search_movies.html', search_active=True, movie = movie, title = title)
#

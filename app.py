from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2 Jeremy Abel
    title = request.form.get('title', None)
    director = request.form.get('director', None)
    rating = request.form.get('rating', 0)

    # Input verification 
    if (title==None or director==None or rating<1 or rating>5):
        # Creates a new form 
        return redirect('/movies/new')
    else:
        # Adds the movie review to the list of reviews 
        movie_repository_singleton.create_movie(title, director, rating)
        # After creating the movie in the database, we redirect to the list all movies page
        return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)

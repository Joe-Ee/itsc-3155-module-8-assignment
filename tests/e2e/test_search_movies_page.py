# TODO: Feature 3
import pytest
from app import app
from flask.testing import FlaskClient
from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton

def test_get_movie_by_title(test_app: FlaskClient):
    #test for nothing. User just clicks enter immedietly
    response = test_app.get('/movies/search?searchMov=')
    response_data = response.data

    assert b'<p>Type in a movie title to get its rating<p>' in response_data
    
    #test for a movie that is not in the database
    response = test_app.get('/movies/search?searchMov=cars')
    response_data = response.data

    assert b'<p>That movie is not in our database, please try another one</p>' in response_data

    #nothing is put in
    response = test_app.get('/movies/search?searchMov')
    response_data = response.data
    assert b'<p>Type in a movie title to get its rating<p>' in response_data

    #test case where they search for a movie taht is in the repository and works 
    movie = movie_repository_singleton.create_movie('Star Wars', 'George Lucas', 5)

    response = test_app.get('/movies/search?searchMov=Star Wars')
    response_data = response.data

    assert b'<td >Star Wars</td>' in response_data
    assert b'<td>5</td>' in response_data

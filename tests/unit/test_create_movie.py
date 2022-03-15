# TODO: Feature 2 || Jeremy Abel
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

def test_create_movie():
    testMovie = movie_repository_singleton.create_movie('Star Wars', 'George Lucas', 5)
    
    assert type(testMovie) == Movie
    assert testMovie.title == 'Star Wars'
    assert testMovie.director == 'George Lucas'
    assert testMovie.rating == 5
    
    


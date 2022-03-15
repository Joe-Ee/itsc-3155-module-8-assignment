from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton

def test_get_movie_by_title():
    #create movies and add them to the singleton
    movie = movie_repository_singleton.create_movie('Star Wars', 'George Lucas', 5)
    shrek = movie_repository_singleton.create_movie("shrek", "mr.shrek", 5)
    dogs = Movie("dogs", "mr.director", 3)
    default = movie_repository_singleton.create_movie("-1", "-1", -1)
    
    movie_repository_singleton.create_movie("dogs", "mr.director", 3)

    #test to see if the movies are in the list properly
    assert movie_repository_singleton.get_movie_by_title('Star Wars').title == movie.title
    assert movie_repository_singleton.get_movie_by_title("shrek") == shrek
    assert movie_repository_singleton.get_movie_by_title("notInHere") == None
    assert movie_repository_singleton.get_movie_by_title("-1") == default
    assert movie_repository_singleton.get_movie_by_title("dogs").title == dogs.title
    assert movie_repository_singleton.get_movie_by_title("") == None





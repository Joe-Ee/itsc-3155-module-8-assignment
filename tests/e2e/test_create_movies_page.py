# TODO: Feature 2 || Jeremy Abel 
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movies_page(test_app: FlaskClient):
    # default case
    response = test_app.post('/movies', data=dict(
        title = 'Pulp Fiction',
        director ='Quentin Tarantino',
        rate = 5
    ), follow_redirects= True )
    assert response.status_code == 200
    
    # empty response case 
    response = test_app.post('/movies', data=dict(
        title = '',
        director ='',
        rate = 0
    ), follow_redirects= True )
    assert response.status_code == 200
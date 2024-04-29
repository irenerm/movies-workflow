"""
Este módulo contiene pruebas unitarias para verificar la funcionalidad asociada con
la gestión de películas en la aplicación. Esto incluye la creación de nuevas películas,
la verificación de películas existentes, y el listado de todas las películas.
"""

import pytest
from movies.movie import Movie
from movies.movie_commands import CreateMovieCommand, ListMovies

@pytest.fixture(autouse=True)
def setup_database():
    """Prepara y limpia la base de datos antes y después de cada test."""
    Movie.create_table()
    yield
    Movie.delete_rows()

def test_create_movie():
    """Test para verificar la creación de una nueva película."""
    cmd = CreateMovieCommand(title="Avatar", duration=178, category="Action")
    movie = cmd.execute()
    db_movie = Movie.get_by_id(movie.id)
    assert db_movie is not None
    assert db_movie.id == movie.id
    assert db_movie.title == movie.title
    assert db_movie.duration == movie.duration
    assert db_movie.category == movie.category

def test_create_movie_already_exists():
    """Test para verificar que la película ya existente no se duplica."""
    Movie(title="Avatar", duration=178, category="Action").save()
    cmd = CreateMovieCommand(title="Avatar", duration=178, category="Action")
    movie = cmd.execute()
    db_movie = Movie.get_by_id(movie.id)
    assert db_movie is not None
    assert db_movie.id == movie.id

def test_list_movies():
    """Test para verificar que la lista de películas se recupera correctamente."""
    Movie(title="Avatar", duration=178, category="Action").save()
    Movie(title="Spider-Man 3", duration=156, category="Action").save()
    query = ListMovies()
    movies = query.execute()
    assert len(movies) == 2

"""
Este módulo contiene la definición de las rutas del API para la aplicación Flask,
manejando la creación, recuperación y listado de películas.
"""

from flask import Flask, jsonify, request
from movies.movie_commands import CreateMovieCommand, GetMovieById, ListMovies

app = Flask(__name__)


@app.route("/create-movie/", methods=["POST"])
def create_movie():
    """
    Crea una nueva película basada en los datos JSON proporcionados y devuelve la película creada.
    """
    cmd = CreateMovieCommand(**request.json)
    movie = cmd.execute()
    return jsonify(movie.dict())


@app.route("/movie/<movie_id>/", methods=["GET"])
def get_movie(movie_id):
    """
    Obtiene una película por su ID y devuelve los detalles de la película.
    """
    query = GetMovieById(id=movie_id)
    movie = query.execute()
    return jsonify(movie.dict())


@app.route("/movie-list/", methods=["GET"])
def list_movies():
    """
    Lista todas las películas disponibles y devuelve una lista de películas.
    """
    query = ListMovies()
    movies = query.execute()
    return jsonify([movie.dict() for movie in movies])


if __name__ == "__main__":
    app.run(debug=True)

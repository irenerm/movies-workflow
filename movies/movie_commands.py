"""
Este módulo contiene comandos que operan sobre la entidad Movie, facilitando la creación,
listado y recuperación de instancias de películas a través de una API.
"""

from typing import List
from pydantic import BaseModel, Field
from movies.movie import Movie


class GetMovieById(BaseModel):
    """
    Comando para obtener una película por su identificador único.

    Attributes:
        id (str): El identificador único de la película, requerido para la búsqueda.
    """

    id: str = Field(..., description="The ID of the movie")

    def execute(self) -> Movie:
        """
        Ejecuta la operación de búsqueda de una película utilizando su ID.

        Returns:
            Movie: La instancia de la película encontrada o None si no existe.
        """
        return Movie.get_by_id(self.id)


class CreateMovieCommand(BaseModel):
    """
    Comando para crear una nueva película si no existe.

    Attributes:
        title (str): El título de la película.
        duration (int): La duración de la película en minutos.
        category (str): La categoría de la película.
    """

    title: str
    duration: int
    category: str

    def execute(self) -> Movie:
        """
        Ejecuta el comando para crear una nueva película.

        Returns:
            Movie: La película creada o encontrada.
        """
        movie = Movie.get_by_title(self.title)
        if movie is None:
            movie = Movie(
                title=self.title, duration=self.duration, category=self.category
            ).save()
        return movie


class ListMovies(BaseModel):
    """
    Comando para listar todas las películas disponibles.
    """

    def execute(self) -> List[Movie]:
        """
        Ejecuta el comando para listar todas las películas disponibles.

        Returns:
            List[Movie]: Lista de películas.
        """
        return Movie.list()

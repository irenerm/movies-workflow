"""
Este módulo contiene comandos que operan sobre la entidad Movie, facilitando la creación,
listado y recuperación de instancias de películas a través de una API.
"""
"""
Este módulo contiene comandos que operan sobre la entidad Movie, facilitando la creación,
listado y recuperación de instancias de películas a través de una API.
"""

from typing import List
from pydantic import BaseModel
from movies.movie import Movie


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

    """
    Ejecuta el comando para crear una nueva película o devolver una existente basada en el título.
        
    Returns:
        Movie: La película creada o encontrada.
    """
    def execute(self) -> Movie:
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
        movies = Movie.list()
        return movies


class GetMovieById(BaseModel):
    """
    Comando para obtener una película por su identificador.
    
    Attributes:
        id (str): El identificador único de la película.
    """
    id: str

    def execute(self) -> Movie:
        """
        Ejecuta el comando para obtener una película basada en su ID.
        
        Returns:
            Movie: La película obtenida.
        """
        movie = Movie.get_by_id(self.id)
        return movie

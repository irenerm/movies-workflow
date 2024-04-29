"""
Este módulo define la clase Movie y sus operaciones de base de datos asociadas.
"""

import os
import sqlite3
import uuid
from typing import List
from pydantic import BaseModel, Field


class Movie(BaseModel):
    """
    Representa una película con operaciones para guardar y recuperar desde la base de datos.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    duration: int
    category: str

    @classmethod
    def get_by_id(cls, movie_id: str) -> "Movie":
        """Recupera una película por su ID desde la base de datos."""
        movie = None
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM movies WHERE id=?", (movie_id,))

        record = cur.fetchone()
        if record is not None:
            movie = cls(**record)
        con.close()
        return movie

    @staticmethod
    def create_table():
        """Creación de tabla."""
        pass

    @staticmethod
    def delete_rows():
        """Eliminación de filas."""
        pass

    @classmethod
    def get_by_title(cls, title: str) -> "Movie":
        """Recupera una película por su título desde la base de datos."""
        movie = None
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM movies WHERE title = ?", (title,))

        record = cur.fetchone()
        if record is not None:
            movie = cls(**record)
        con.close()
        return movie

    @classmethod
    def list(cls) -> List["Movie"]:
        """Lista todas las películas disponibles en la base de datos."""
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM movies")

        records = cur.fetchall()
        movies = [cls(**record) for record in records]
        con.close()
        return movies

    def save(self) -> "Movie":
        """Guarda la película en la base de datos."""
        with sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db")) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO movies (id, title, duration, category) VALUES(?, ?, ?, ?)",
                (self.id, self.title, self.duration, self.category),
            )
            con.commit()
        return self

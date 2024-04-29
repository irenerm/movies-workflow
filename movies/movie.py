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

    @classmethod
    def get_by_id(cls, movie_id: str) -> "Movie":
        """
        Recupera una película por su ID desde la base de datos.

        Args:
            movie_id (str): El identificador único de la película.

        Returns:
            Movie: La instancia de la película si se encuentra.
        """
        with sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db")) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
            record = cur.fetchone()
            return cls(**record) if record else None

    @staticmethod
    def create_table():
        """
        Crea la tabla de películas en la base de datos si no existe.
        """
        with sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db")) as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXISTS movies (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    duration INTEGER,
                    category TEXT
                )
            """
            )

    @staticmethod
    def delete_rows():
        """
        Elimina todas las filas de la tabla de películas para limpiar los datos.
        """
        with sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db")) as con:
            con.execute("DELETE FROM movies")

    @classmethod
    def list(cls) -> List["Movie"]:
        """
        Devuelve una lista de todas las películas disponibles en la base de datos.

        Returns:
            List[Movie]: Una lista de instancias de películas.
        """
        with sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db")) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM movies")
            records = cur.fetchall()
            return [cls(**record) for record in records]

    def save(self) -> "Movie":
        """
        Guarda la película en la base de datos.

        Returns:
            Movie: La instancia de la película guardada.
        """
        with sqlite3.connect(os.getenv("DATABASE_NAME", "movies.db")) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO movies (id, title, duration, category) VALUES (?, ?, ?, ?)",
                (self.id, self.title, self.duration, self.category),
            )
            con.commit()
        return self

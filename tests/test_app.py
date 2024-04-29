"""Módulo de pruebas para verificar la funcionalidad de la aplicación web."""

import json
import pathlib
import pytest
from jsonschema import validate, RefResolver
from web_app import app
from movies.movie import Movie

@pytest.fixture
def test_client():
    """Configura el cliente de prueba para la aplicación Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def validate_payload(payload, schema_name):
    """Valida un payload según el esquema JSON especificado."""
    schemas_dir = str(pathlib.Path(__file__).parent.absolute() / "schemas")
    schema_path = pathlib.Path(f"{schemas_dir}/{schema_name}")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validate(
        payload,
        schema,
        resolver=RefResolver("file://" + str(schema_path.absolute()), schema)
    )

def test_create_movie(test_client):
    """Prueba la creación de una película mediante la API."""
    data = {
        "title": "Avatar",
        "duration": 178,
        "category": "Action"
    }
    response = test_client.post(
        "/create-movie/",
        data=json.dumps(data),
        content_type="application/json",
    )
    validate_payload(response.json, "Movie.json")

def test_get_movie(test_client):
    """Prueba la obtención de detalles de una película específica por ID."""
    movie = Movie(title="Avatar", duration=178, category="Action").save()
    response = test_client.get(f"/movie/{movie.id}/", content_type="application/json")
    validate_payload(response.json, "Movie.json")

def test_list_movies(test_client):
    """Prueba la recuperación de una lista de películas."""
    Movie(title="Avatar", duration=178, category="Action").save()
    response = test_client.get("/movie-list/", content_type="application/json")
    validate_payload(response.json, "MovieList.json")

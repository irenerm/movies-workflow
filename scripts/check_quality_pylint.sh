#!/bin/bash

# Umbral mínimo de calificación para pylint
MIN_SCORE=7.0

# Ejecuta pylint solo en los archivos Python dentro de la carpeta 'movies'
# y almacena el resultado
PYLINT_OUTPUT=$(find movies -name "*.py" -exec pylint --fail-under=$MIN_SCORE {} +)
RESULT=$?

# Verifica el resultado de pylint
if [ $RESULT -eq 0 ]; then
    echo "Pylint pasó con una calificación igual o superior a $MIN_SCORE"
    exit 0  # Exit code para indicar éxito
else
    echo "Pylint falló con una calificación menor a $MIN_SCORE"
    echo "$PYLINT_OUTPUT"
    exit 1  # Exit code para indicar fallo
fi

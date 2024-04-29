#!/bin/bash

# Umbral mínimo de calificación para pylint
MIN_SCORE=7.0

# Ejecuta pylint en todos los archivos Python y almacena el resultado
PYLINT_OUTPUT=$(find . -name "*.py" -exec pylint --fail-under=$MIN_SCORE {} +)
RESULT=$?

# Verifica el resultado de pylint
if [ $RESULT -eq 0 ]; then
    echo "Pylint pasó con una calificación igual o superior a $MIN_SCORE"
else
    echo "Pylint falló con una calificación menor a $MIN_SCORE"
    echo "$PYLINT_OUTPUT"
    exit 1
fi

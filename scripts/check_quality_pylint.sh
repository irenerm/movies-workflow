#!/bin/bash

# Run Pylint on all Python files
find . -name "*.py" -exec pylint {} +

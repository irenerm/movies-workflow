#!/bin/bash

# Run pytest with coverage
pytest --cov=movies --cov-report=term-missing

# Check if the coverage is less than 90%
coverage=$(pytest --cov=movies --cov-report=term | tail -n 1 | awk '{print $4}' | sed 's/%//')
required_coverage=90

if (( $(echo "$coverage < $required_coverage" | bc -l) )); then
    echo "Test coverage $coverage% is less than required $required_coverage%"
    exit 1
fi

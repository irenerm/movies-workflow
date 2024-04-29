#!/bin/bash

# Run pytest with coverage and capture the output
output=$(pytest --cov=movies --cov-report=term)
echo "$output"

# Extract the total coverage percentage using grep and awk
coverage=$(echo "$output" | grep 'TOTAL' | awk '{print $4}' | sed 's/%//')

# Define the required coverage level
required_coverage=90

# Compare the coverage result with the required coverage
if (( $(echo "$coverage < $required_coverage" | bc -l) )); then
    echo "Test coverage ${coverage}% is less than required ${required_coverage}%."
    exit 1
else
    echo "Test coverage ${coverage}% meets or exceeds the required ${required_coverage}%."
    exit 0
fi

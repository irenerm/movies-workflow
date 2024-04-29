#!/bin/bash

# Set the PYTHONPATH to include the current directory to ensure that local modules are found
export PYTHONPATH=$(pwd):$PYTHONPATH

# Change directory to the root of the project
cd $(dirname "$0")/..

# Run pytest on the tests directory
pytest tests/

# Check the exit status of pytest and exit accordingly
if [ $? -eq 0 ]; then
    echo "Tests passed successfully."
    exit 0
else
    echo "Tests failed. Check the output above for errors."
    exit 1
fi

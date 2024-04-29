#!/bin/bash

# Format all Python files and check for changes
black --check .

if [ $? -ne 0 ]; then
    echo "Code format issues found."
    exit 1
fi

#!/bin/bash

# Format all Python files and check for changes using Black
black --check .

# Check the exit status of the last command (black --check .)
if [ $? -ne 0 ]; then
    echo "Code format issues found. Please run 'black .' to fix them."
    exit 1
else
    echo "All files are correctly formatted."
    exit 0
fi

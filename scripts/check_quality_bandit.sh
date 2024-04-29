#!/bin/bash

# Run Bandit security analysis on all Python files, ignoring B101 (assert_used)
bandit -r . -s B101
result=$?

# Check the result of Bandit
if [ $result -eq 0 ]; then
    echo "Bandit security analysis completed successfully with no issues."
    exit 0
else
    echo "Bandit security analysis found issues that need to be addressed."
    exit 1
fi

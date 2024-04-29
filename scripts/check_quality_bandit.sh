#!/bin/bash

# Run Bandit security analysis on all Python files, ignoring B101 (assert_used)
bandit -r . -s B101

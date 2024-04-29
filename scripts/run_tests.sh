#!/bin/bash
export PYTHONPATH=$(pwd):$PYTHONPATH
cd $(dirname "$0")/..
pytest tests/

#!/bin/bash
LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
# PYTHONPATH=/lib/

python3 ./parser/parser.py

exec "$@"

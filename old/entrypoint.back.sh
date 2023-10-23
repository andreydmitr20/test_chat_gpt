#!/bin/bash
LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8
# PYTHONPATH=/lib/

cd back
python3 m migrate
cd ..

uwsgi --ini uwsgi.ini

exec "$@"

#!/bin/bash
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

TIMEOUT=120

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 \
--timeout $TIMEOUT \
--log-level=debug \
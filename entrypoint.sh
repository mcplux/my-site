#! /usr/bin/env bash

PATH="/app/.venv/bin:$PATH"

echo "Making migrations..."
python manage.py migrate

echo "Collecting statics"
python manage.py collectstatic --no-input

echo "Running server..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 1

#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate
python manage.py seed_db
# python manage.py collectstatic --noinput

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
# gunicorn djblogger.wsgi:application --bind 0.0.0.0:8000
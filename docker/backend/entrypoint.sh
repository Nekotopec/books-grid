#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py docker_init_admin
python manage.py setup_test_data
exec "$@"
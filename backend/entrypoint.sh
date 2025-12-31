#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --no-input

echo "Creating superuser if it doesn't exist..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'karafi.work@gmail.com', 'test-admin')
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
END

echo "Starting server..."
# Using gunicorn for production is recommended, but user Dockerfile uses runserver
# For Cloud Run, we should listen on the $PORT environment variable
exec python manage.py runserver 0.0.0.0:${PORT:-8000}

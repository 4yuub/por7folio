#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --no-input

echo "Creating superuser if it doesn't exist..."
python manage.py shell << END
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
password = os.getenv('ADMIN_PASSWORD', 'admin')
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser '{username}' already exists.")
END

echo "Starting server..."
# Using gunicorn for production is recommended, but user Dockerfile uses runserver
# For Cloud Run, we should listen on the $PORT environment variable
exec python manage.py runserver 0.0.0.0:${PORT:-8000}

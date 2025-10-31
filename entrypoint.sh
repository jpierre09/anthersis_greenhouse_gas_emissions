#!/bin/bash
set -e

sleep 5
python manage.py migrate --noinput

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
username = "${SUPERUSER_USERNAME}"
email = "${SUPERUSER_EMAIL}"
password = "${SUPERUSER_PASSWORD}"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
EOF


python manage.py runserver 0.0.0.0:8000

web: gunicorn muhammad_second_version.wsgi --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py collecstatic --noinput
release: python manage.py migrate --noinput
FROM python:3.9.13-buster
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=connectword.settings
ENV DJANGO_SECRET_KEY = "django-insecure-r9btm6ct*+b@pc=&rw$=pa*(#g5+1!3mmmvww(=($$7+^e8m47"
ENV DJANGO_DEBUG = False
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

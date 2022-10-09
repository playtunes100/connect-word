connectenv\scripts\activate
docker run --name redis-test -d -p 6379:6379 redis
py manage.py runserver
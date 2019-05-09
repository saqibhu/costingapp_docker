#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    #while ! nc -z $SQL_HOST $SQL_PORT; do
    #  sleep 0.1
    #done

    echo "PostgreSQL started"
fi

#clear the database each time the container is run
#python manage.py flush --no-input

python manage.py migrate

exec "$@"

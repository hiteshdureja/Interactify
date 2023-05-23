#!/bin/bash
set -e

echo "${0}: Connecting to database."

((count = 1000))                           # Maximum number to try.
while [[ $count -ne 0 ]] ; do
    ping -c 1 backend-db                    # Try once.
    rc=$?
    if [[ $rc -eq 0 ]] ; then
        echo "Connected to database.."
        break
    else
        sleep 1                          # Minimise network storm.
    fi
    ((count = count - 1))                # So we don't go forever.
done

# Database is now available, proceed with the rest of the script
echo "Database is ready. Running migrations"
python manage.py makemigrations --merge
python manage.py migrate --noinput

echo "Completed migrations. Collecting static files.."
python manage.py collectstatic --no-input

echo "Static files collected. Creating log directory if not exists..."
DIR="/var/log/gunicorn"
if [ -d "$DIR" ]; then
  echo "Log directory already exists at ${DIR}..."
else
  mkdir $DIR
  echo "Log directory created..."
fi

echo "Starting gunicorn server..."

gunicorn interactify.asgi:application \
  --timeout 60 --bind 0.0.0.0:80 --workers 3 \
  --worker-class uvicorn.workers.UvicornWorker \
  --access-logfile /var/log/gunicorn/gunicorn-access.log \
  --error-logfile /var/log/gunicorn/gunicorn-error.log

#gunicorn interactify.asgi:application \
#    --config ./gunicorn/config.py \
#    --access-logfile /var/log/gunicorn/gunicorn-access.log \
#    --error-logfile /var/log/gunicorn/gunicorn-error.log

echo "Server started at port 80..."

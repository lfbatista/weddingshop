#!/bin/sh

python manage.py flush --no-input
python manage.py migrate --run-syncdb
# import products.json to db
(echo "import import_data"; echo "import_data.import_data()") | python manage.py shell

exec "$@"

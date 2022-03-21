#!/bin/bash
# this script is to build the venv fast and make migrations
# give the permission before use
# run the virtualenv before run this script
# chmod 755 script.sh

rm mysite/socialdistribution/migrations/0001_initial.py
pip install -r requirements.txt
wait
cd mysite
wait
python manage.py makemigrations
wait
python manage.py migrate
wait
python manage.py createsuperuser
# wait
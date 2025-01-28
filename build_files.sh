#!/bin/bash
echo "Collecting static files"
python3 manage.py collectstatic --noinput

echo "Creating static files directory"
mkdir -p staticfiles

echo "Copying static files"
cp -r static staticfiles

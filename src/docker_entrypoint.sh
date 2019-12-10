#!/bin/sh
mkdir -p /app/logs/
touch /app/logs/error.log
touch /app/logs/access.log

exec gunicorn -c app_config.py webhook:app
